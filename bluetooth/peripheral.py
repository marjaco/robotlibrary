# Version 2.0.1
import bluetooth
from robotlibrary.bluetooth.advertising import advertising_payload
from robotlibrary.bluetooth.ble_flags import *
from robotlibrary.bluetooth.ble_services_definitions import ROBOT_SERVICE, ROBOT_UUID, MOTOR_RX_UUID, MOTOR_TX_UUID

from robotlibrary.bluetooth.parser import decode_motor

class BLEPeripheral:
    def __init__(self, name: str, add_robot_stuff=False):
        self.ble = bluetooth.BLE()
        self._ble_irq_dict = {}
        self._handles = {}
        self.ble.active(True)
        self.ble.irq(self._irq)
        self._connections = set()
        self._read_callbacks = {}
        self._payload = advertising_payload(name=name, services=[ROBOT_UUID])
        if add_robot_stuff:
            self._handles[ROBOT_UUID] = {}
            #[robot_handles] = self.ble.gatts_register_services((ROBOT_SERVICE, ))
            [robot_handles] = self.ble.gatts_register_services((ROBOT_SERVICE,))
            self._handles[ROBOT_UUID][MOTOR_RX_UUID] = robot_handles[0]
            self._handles[ROBOT_UUID][MOTOR_TX_UUID] = robot_handles[1]
            self.register_irq(IRQ_CENTRAL_CONNECT, self._handle_connect)
            self.register_irq(IRQ_CENTRAL_DISCONNECT, self._handle_disconnect)
            self.register_irq(IRQ_GATTS_WRITE, self._handle_read)

    def register_irq(self, event, func):
        self._ble_irq_dict[event] = func

    def _irq(self, event, data):
        if event in self._ble_irq_dict:
            self._ble_irq_dict[event](data)

    def _handle_connect(self, data):
        conn_handle, _, _ = data
        print("New connection", conn_handle)
        self._connections.add(conn_handle)

    def _handle_disconnect(self, data):
        conn_handle, _, _ = data
        print("Disconnected", conn_handle)
        self._connections.remove(conn_handle)
        # Start advertising again to allow for a new connection.
        self.advertise()

    def _handle_read(self, data):
        conn_handle, value_handle = data
        val = self.ble.gatts_read(value_handle)
        #print(f"{value_handle} sent: {val}")
        
        for service in self._handles:
            for char in self._handles[service]:

                if self._handles[service][char] == value_handle and self._read_callbacks[char] is not None:
                    #print(self._read_callbacks[char], "val:",decode_motor(val))
                    self._read_callbacks[char](val)

    def send(self, service_uuid, char_uuid, data):
        if service_uuid not in self._handles or char_uuid not in self._handles[service_uuid]:
            return
        for conn_handle in self._connections:
            self.ble.gatts_notify(conn_handle, self._handles[service_uuid][char_uuid], data)

    def is_connected(self):
        return len(self._connections) > 0

    def advertise(self, interval_us=500000):
        print("Starting advertising")
        self.ble.gap_advertise(interval_us, adv_data=self._payload)

    def register_read_callback(self, uuid, callback):
        self._read_callbacks[uuid] = callback

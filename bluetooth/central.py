# Version 1.91
from robotlibrary.bluetooth.ble_flags import *
from robotlibrary.bluetooth.ble_services_definitions import ROBOT_UUID, MOTOR_RX_UUID, MOTOR_TX_UUID
from robotlibrary.bluetooth.advertising import decode_services, decode_field
import bluetooth


class BLECentral:
    def __init__(self, to_connect_name: str, add_robot_stuff=False):
        self._to_connect_name = to_connect_name
        self.ble = bluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self._irq)
        self._irq_dict = {}
        self._handles = {}
        self._connections = set()
        self._read_callbacks = {}
        self._read_cb = None
        self._service_to_scan = []
        if add_robot_stuff:
            self._is_connected = False
            self.register_irq(IRQ_SCAN_RESULT, self._handle_scan)
            self.register_irq(IRQ_PERIPHERAL_CONNECT, self._handle_connect)
            self.register_irq(IRQ_PERIPHERAL_DISCONNECT, self._handle_disconnect)
            self.register_irq(IRQ_GATTC_SERVICE_RESULT, self._handle_services)
            self.register_irq(IRQ_GATTC_SERVICE_DONE, self._on_service_discovery_complete)
            self.register_irq(IRQ_GATTC_CHARACTERISTIC_RESULT, self._handle_characteristics)
            self.register_irq(IRQ_GATTC_NOTIFY, self._handle_read)

    def _handle_scan(self, data):
        addr_type, addr, adv_type, rssi, adv_data = data
        print("Found Peripheral:", addr_type, bytes(addr), decode_field(adv_data, ADV_TYPE_NAME))
        device_name = [bytes(i).decode() for i in decode_field(adv_data, ADV_TYPE_NAME)]
        device_uuid = decode_services(adv_data)
        if adv_type in [ADV_IND, ADV_DIRECT_IND] and ROBOT_UUID in device_uuid and self._to_connect_name in device_name:
            self.ble.gap_scan(None)
            print("Found Candidate:", addr_type, addr, decode_field(adv_data, ADV_TYPE_NAME))
            self.ble.gap_connect(addr_type, addr)

    def _handle_connect(self, data):
        conn_handle, addr_type, addr = data
        print("connected to:", addr_type, addr)
        self._connections.add(conn_handle)
        self.ble.gattc_discover_services(conn_handle)

    def _handle_disconnect(self, data):
        conn_handle, _, _ = data
        self._connections.remove(conn_handle)
        self._is_connected = False
        print(conn_handle, "disconnected. Restarted scanner")
        self.scan()

    def _handle_services(self, data):
        conn_handle, start_handle, end_handle, uuid = data
        print("service", data)
        if uuid == ROBOT_UUID:
            self._handles[ROBOT_UUID] = {}
            self._service_to_scan.append((start_handle, end_handle))

    def _on_service_discovery_complete(self, data):
        conn_handle, _ = data
        for (start_handle, end_handle) in self._service_to_scan:
            self.ble.gattc_discover_characteristics(conn_handle, start_handle, end_handle)

        self._service_to_scan = []
        self._is_connected = True

    def _handle_characteristics(self, data):
        conn_handle, _, value_handle, properties, uuid = data
        if uuid == MOTOR_RX_UUID:
            self._handles[ROBOT_UUID][MOTOR_RX_UUID] = value_handle
        if uuid == MOTOR_TX_UUID:
            self._handles[ROBOT_UUID][MOTOR_TX_UUID] = value_handle

    def _handle_read(self, data):
        _, value_handle, notify_data = data
        for service in self._handles:
            for char in self._handles[service]:
                if value_handle == self._handles[service][char] and self._read_callbacks[char] is not None:
                    self._read_callbacks[char](notify_data)

    def _irq(self, event: int, data):
        if event in self._irq_dict:
            self._irq_dict[event](data)

    def register_irq(self, event: int, func):
        self._irq_dict[event] = func

    def scan(self):
        self.ble.gap_scan(2000, 30000, 30000)

    def register_read_callback(self, uuid, callback):
        self._read_callbacks[uuid] = callback

    def send(self, service_uuid, char_uuid, data):
        for conn_handle in self._connections:
            self.ble.gattc_write(conn_handle, self._handles[service_uuid][char_uuid], data)

    def is_connected(self):
        return self._is_connected


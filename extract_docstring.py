import ast,glob
from os import walk

def extract_docstrings(filename):
    s = ""
    with open(filename, "r") as f:
        module = ast.parse(f.read())
    for node in ast.walk(module):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            if ast.get_docstring(node) is not None:
                s += f"## {getattr(node, 'name', 'Module')} \n"
                s += str((ast.get_docstring(node)))
                s += "\n\n"
    return s

for py in glob.glob("*.py"):
    doc = extract_docstrings(py)
    if doc:
        with open(f"docs/{py}.md", "w") as f:
            f.write(f"# Documentation for {py} \n\n")
            f.write(doc)


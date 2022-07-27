from cx_Freeze import setup, Executable

base = None

executables = [Executable("clicker.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': ["idna", "time", "threading", "pynput", "pynput.keyboard", "pynput.mouse"],
    },
}

setup(
    name="clicker",
    options=options,
    version="0.1",
    description='Just Clickin.',
    executables=executables
)
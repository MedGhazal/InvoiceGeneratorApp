from setuptools import setup

APP = ["Invoices.py"]
DATA_FILES = [
    "gui.py",
    "La Mome_infos.txt",
    "Marina_infos.txt",
    "script_methods.py",
    "tex_files.py",
    "logo.png",
]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)

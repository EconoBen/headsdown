from setuptools import setup
import subprocess

## ensure developer tools are installed

# if xcode exists move on, else install
result = subprocess.check_output(["xcode-select --version"],shell=True, text=True)
if "version" not in result:
    subprocess.check_output(["xcode-select --install"],shell=True)

## run setup

APP = ['headsdown.py']
DATA_FILES = ['block_sites.csv']
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'images/icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps']
)
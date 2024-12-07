# -*- mode: python ; coding: utf-8 -*-

import os
import sys

# Get the path to the main directory
main_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Include all files in the main directory
datas = [(os.path.join(main_dir, f), '.') for f in os.listdir(main_dir) if os.path.isfile(os.path.join(main_dir, f))]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['pyperclip', 'cryptography', 'cryptography.hazmat.primitives', 'cryptography.hazmat.backends','cryptography.fernet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    distpath='D:\\Python IDE + Projects\\dist',  # Specify your desired output folder here
)
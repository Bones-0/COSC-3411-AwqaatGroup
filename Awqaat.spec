# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
from pathlib import Path
import kivy

# Correct paths inside your venv
KIVY_PATH = Path(kivy.__file__).resolve().parent
GEOPY_PATH = "/home/hassan/Documents/PythonProjects/TruePrayer/.venv/lib/python3.11/site-packages/geopy"

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],

    datas=[
        ('UserInterface/main.kv', 'UserInterface'),
        ('images/*', 'images'),
        ('sounds/*', 'sounds'),
        (str(KIVY_PATH / "core" / "window" / "window_x11.py"), "kivy/core/window"),
    ]


    hiddenimports=[
        'kivy.core.window.window_x11',
        'kivy.core.window',
        'geopy',
        'geopy.geocoders',
        'geopy.adapters',
        'geopy.point',
        'geocoder',
        'requests',
    ]


    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Awqaat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
)

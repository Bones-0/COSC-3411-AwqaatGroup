# Awqaat.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('UserInterface/main.kv', 'UserInterface'),
        ('images', 'images'),
        ('sounds', 'sounds'),
    ],
    hiddenimports=[
        'geopy',
        'geopy.geocoders',
        'geopy.adapters',
        'geopy.point',
        'requests',
    ],
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    a.scripts,
    name='Awqaat',
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    a.pure,
    a.zipfiles,
    name='Awqaat'
)

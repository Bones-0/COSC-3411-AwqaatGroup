# Awqaat.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('UserInterface', 'UserInterface'),  # Include entire folder
        ('images', 'images'),
        ('sounds', 'sounds'),
    ],
    hiddenimports=[
        'kivy.core.window.window_sdl2',  # ← Add this!
        'kivy.core.image.img_sdl2',      # ← Add this!
        'kivy.core.audio.audio_sdl2',    # ← Add this! 

        'geopy',
        'geopy.geocoders',
        'geopy.adapters',
        'geopy.point',
        'requests',
    ],
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],  # ← Change: empty list instead of including everything
    exclude_binaries=True,  # ← Add this line
    name='Awqaat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# Then ADD this COLLECT section at the end (if it doesn't exist):
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Awqaat',
)
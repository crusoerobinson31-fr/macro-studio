# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules("macro_app")

a = Analysis(
    ["macro_app/main.py"],
    pathex=["."],
    hiddenimports=hiddenimports,
)

pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name="MacroStudio",
    console=False,
)

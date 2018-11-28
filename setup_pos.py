from setuptools import setup
import py2exe
import os
Mydata_files = [('', ['logo.ico'])]
packs = []
setup(
 	data_files=Mydata_files,
  options = {
    'py2exe' : {
        'compressed': 1,
        'dll_excludes':["phonon_ds9d4.dll","phonon_ds94.dll"],
        'optimize': 2,
        'packages':packs,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        }
        },
windows = [{
    "script": "main_app.py",
    "icon_resources": [(1, "logo.ico")],
    "dest_base": "QServer"

}],
  zipfile=r"lib\shardlib",
)

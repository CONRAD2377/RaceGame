import sys
from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(
	name="A bit Racey",
	options={"build_exe": {"packages":["pygame"],
						   "include_files":["car2.png", "crashsound.wav", "jazz.wav"]}},
	executables = executables
	)
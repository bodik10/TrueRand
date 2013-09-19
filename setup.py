# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys

from cx_Freeze import setup, Executable

base = "Win32GUI"

buildOptions = dict(
        compressed = True,
        includes = ["atexit"],
        include_files = ["coins", "TrueRand.exe.manifest"], # manifest - USELESS!!!
        packages = ["modules"],
        path = sys.path)

setup(
        name = "TrueRandom",
        version = "1.0",
        author = "Bohdan Fedys",
        description = "True Random Generator Client",
        options = dict(build_exe = buildOptions),
        executables = [Executable(
            "TrueRand.py",
            base = base,
            icon = 'pics\\icon.ico',
            copyDependentFiles = True,
            shortcutName = "True Random Generator",
            shortcutDir = "ProgramMenuFolder"
        )]
)


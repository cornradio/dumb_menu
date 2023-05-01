import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '1.0.7'
DESCRIPTION = 'A light weight command line menu that supports Windows, MacOS, and Linux'
LONG_DESCRIPTION = 'A light weight command line menu. Supporting Windows, MacOS, and Linux OS. It has support for hotkeys'

# Setting up
setup(
    name="dumb_menu",
    version=VERSION,
    author="clever chen",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'getch; platform_system=="Unix"',
        'getch; platform_system=="MacOS"',
        'msvcrt; platform_system=="Windows"',
        'getch; platform_system=="Linux"'
    ],
    keywords=['python', 'menu', 'dumb_menu', 'windows', 'mac', 'linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Linux :: Linux"
    ]
)
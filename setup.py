from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A simple python OpenGL library'
LONG_DESCRIPTION = 'Create 2d or 3d graphics with pyogl'

# Setting up
setup(
    name="pyogl",
    version=VERSION,
    author="TechPenguineer",
    author_email="<techpenguineer@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyqtgraph'],
    keywords=['python', 'picture', 'opengl', 'rendering', 'graphic'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
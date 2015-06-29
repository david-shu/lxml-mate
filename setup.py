
import sys


try:
    from setuptools import setup
except ImportError:
    if sys.version_info > (3,):
        raise RuntimeError("python3 support requires setuptools")
    from distutils.core import setup


info = {}
src = open("lxmlmate.py")
lines = []
for ln in src:
    lines.append(ln)
    if "__version__" in ln:
        for ln in src:
            if "__version__" not in ln:
                break
            lines.append(ln)
        break
exec("".join(lines),info)


with open( 'README.rst' ) as f:
    info['__doc__'] = f.read()
    

NAME = "lxmlmate"
VERSION = info["__version__"]
DESCRIPTION = "The simplest Object-XML mapper for Python. Lite for lxml."
LONG_DESC = info["__doc__"]
AUTHOR = "David Shu"
AUTHOR_EMAIL = "david.shu@126.com"
URL="https://github.com/david-shu/lxml-mate"
LICENSE = "MIT"
KEYWORDS = "xml lxml"
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: Markup",
    "Topic :: Text Processing :: Markup :: XML",
]


setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      long_description=LONG_DESC,
      license=LICENSE,
      keywords=KEYWORDS,
      #packages=["lxml-lite"],
      classifiers=CLASSIFIERS,
      py_modules=['lxmlmate','example'],
      requires=['lxml'],
      data_files=['README.rst']
     )

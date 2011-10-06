import sys
import os
from distutils.core import setup

from eqentia_client.client import __version__

setup(name = "eqentia_client",
      version = __version__,
      description = "A small library that provides an interface wrapper to Eqentia Rest Api",
      author = "Morgan Craft <http://www.morgancraft.com>",
      author_email = 'mgan59@gmail.com',
      license = 'MIT',
      packages = ['eqentia_client'])

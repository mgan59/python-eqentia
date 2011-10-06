import sys
import os
from distutils.core import setup

from eqentia_client.client import __version__

setup(name = "python-eqentia",
      version = __version__,
      description = "A small library that provides an interface wrapper to Eqentia Rest Api",
      author = "Morgan Craft <http://www.morgancraft.com>",
      author_email = 'mgan59@gmail.com',
      license = 'MIT',
      packages = ['eqentia_client'],
      classifiers=['Development Status :: 4 - Beta',
                         'Environment :: Web Environment',
                         'Intended Audience :: Developers',
                         'License :: OSI Approved :: MIT License',
                         'Operating System :: OS Independent',
                         'Programming Language :: Python',
                         'Topic :: Blogging'],
            )

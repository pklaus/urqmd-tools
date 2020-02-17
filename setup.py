# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

try:
    import pypandoc
    LDESC = open('README.md', 'r').read()
    LDESC = pypandoc.convert(LDESC, 'rst', format='md')
except (ImportError, IOError, RuntimeError) as e:
    print("Could not create long description:")
    print(str(e))
    LDESC = ''

setup(name='urqmd-tools',
      version = '0.9.dev0',
      description = 'Python tools that facilitate working with UrQMD',
      long_description = LDESC,
      author = 'Philipp Klaus',
      author_email = 'klaus@physik.uni-frankfurt.de',
      url = 'https://github.com/pklaus/python-urqmd-tools',
      license = 'GPL',
      packages = find_packages(),
      entry_points = {
          'console_scripts': [
              'urqmd-tools.pids = urqmd_tools.pids:main',
              'urqmd-tools.parser.f14 = urqmd_tools.parser.f14:main',
          ],
      },
      include_package_data = False,
      zip_safe = True,
      platforms = 'any',
      install_requires = [
          'attrs',
      ],
      extras_require = {
      },
      keywords = 'UrQMD Python Physics Heavy-Ion-Collisions Transport Model',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Visualization',
      ]
)

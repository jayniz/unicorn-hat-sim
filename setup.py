from setuptools import setup, find_packages
from codecs import open
from os import path
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst').replace("\r","")
except(IOError, ImportError):
    long_description = open('README.md').read().replace("\r","")

setup(
  name = 'unicorn-hat-sim',
  packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
  version = '1.0.0',
  description = 'Unicorn HAT (HD) simulator',
  long_description = long_description,
  author = 'Jannis Hermanns',
  author_email = 'jannis@gmail.com',
  url = 'https://github.com/jayniz/unicorn-hat-sim', 
  download_url = 'https://github.com/jayniz/unicorn-hat-sim/archive/1.0.2.tar.gz',
  keywords = ['raspberrypi', 'unicorn', 'hat', 'led', 'simulator'],
  license = 'MIT',
  classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3'
  ],
  install_requires=['pygame'],

)
from setuptools import setup, find_packages
from codecs import open
from os import path
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst').replace("\r", "")
except(IOError, ImportError):
    long_description = open('README.md').read().replace("\r", "")

setup(
    name='unicorn-hat-sim',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    version='1.0.0',
    description='Unicorn HAT (HD) simulator - Originally by Jannis Hermanns <jannis@gmail.com>',
    long_description=long_description,
    author='Mark Pitman',
    author_email='mark.pitman@gmail.com',
    url='https://github.com/mapitman/unicorn-hat-sim',
    download_url='https://github.com/mapitman/unicorn-hat-sim/archive/1.0.0.tar.gz',
    keywords=['raspberrypi', 'unicorn', 'hat', 'led', 'simulator'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    install_requires=['pygame'],
)

'''
    A convert TART JSON data into a measurement set.
    Author: Tim Molteno, tim@elec.ac.nz
    Copyright (c) 2019-2024.

    License. GPLv3.
'''
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='tart2ms',
    version='0.6.0b4',
    description='Convert TART observation data to Measurement Sets',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='http://github.com/tmolteno/tart2ms',
    author='Tim Molteno',
    author_email='tim@elec.ac.nz',
    license='GPLv3',
    install_requires=['dask-ms<=0.2.10',
                    'dask<=2023.5.0',
                    'numba<=0.55.1',
                    'python-casacore',
                    'tart',
                    'tart_tools',
                    'astropy',
                    'numpy',
                    'h5py',
                    'progress',
                    'requests',
                    'pandas',
                    'scipy'],
    test_suite='nose.collector',
    tests_require=['nose'],
    extras_require={
        "predict": ["codex-africanus<=0.3.4"],
    },
    packages=['tart2ms'],
    include_package_data=True,
    scripts=['bin/tart2ms'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
        "Topic :: Communications :: Ham Radio",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Intended Audience :: Science/Research"])

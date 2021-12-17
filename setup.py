from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import setup

description = 'Tools for Starlette'
THIS_DIR = Path(__file__).resolve().parent
try:
    long_description = THIS_DIR.joinpath('README.md').read_text()
except FileNotFoundError:
    long_description = description

# avoid loading the package before requirements are installed:
version = SourceFileLoader('version', 'asgard/version.py').load_module()

setup(
    name='asgard',
    version=str(version.VERSION),
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X',
        'Topic :: Internet',
    ],
    author='Denis Eliseev',
    author_email='d.a.eliseev@gmail.com',
    url='https://github.com/deliseev/asgard',
    license='MIT',
    packages=['asgard'],
    entry_points="""
        [console_scripts]
        asgard=asgard.main:cli
    """,
    python_requires='>=3.8',
    zip_safe=True,
    install_requires=[
        'uvicorn>=0.16.0',
    ],
    extras_require={
        'extra': [
        ],
    },
)

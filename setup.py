from setuptools import setup, find_packages

NAME = 'coloratura'
VERSION = '0.9.3'
DESCRIPTION = '🦜Awesome cprint() function to colored terminal text. Supported full RGB!'
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Environment :: Plugins',
]

setup(
    name=NAME,
    version=VERSION,
    author='pyblog.pl',
    author_email='rewolucjazywieniowa@gmail.com',
    description=DESCRIPTION,
    long_description=open('DESCRIPTION.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DawidKos/Coloratura',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords=['color', 'colored', 'colour', 'terminal', 'text', 'ansi', 'colorama', 'hue'],
    classifiers=CLASSIFIERS
)

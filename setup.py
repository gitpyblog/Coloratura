from setuptools import setup

NAME = 'coloratura'


classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',
    'License :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Environment :: Console'
]

setup(
    name=NAME,
    version='0.9.0',
    description='Awesome cprint() function to colored terminal text. Supported full RGB!',
    long_description=open('README.md').read(),
    keywords='color colour terminal text ansi windows colorama hue',
    url='https://github.com/DawidKos/Coloratura',
    author='pyblog.pl',
    author_email='rewolucjazywieniowa@gmail.com',
    license='MIT',
    classifiers=classifiers,
)

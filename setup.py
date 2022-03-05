from setuptools import setup

NAME = 'coloratura'


classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Environment :: Console',
    'Topic :: Colored terminal text',
]

setup(
    name=NAME,
    version='0.9.13',
    description='Awesome cprint() function to colored terminal text. Supported full RGB!',
    long_description=open('DESCRIPTION.md').read(),
    long_description_content_type='text/markdown',
    keywords='color colored colour terminal text ansi windows colorama hue',
    url='https://github.com/DawidKos/Coloratura',
    author='pyblog.pl',
    author_email='rewolucjazywieniowa@gmail.com',
    license='MIT',
    packages=[NAME],
    classifiers=classifiers,
)

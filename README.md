![Latest version](https://img.shields.io/pypi/v/coloratura?color=%23f6d155&label=version&style=flat-square)

# 🐦Coloratura

##### Awsome **cprint()** function to colored terminal text. Supported full RGB! 😍

## Installation

You can install coloratura with **pip** as follows:

```
pip install coloratura
```

## Usage

First of all, get the basic cprint functions and selected color palettes:

```python
from coloratura import cprint, Pantone, Bit4
```

Printing colored text is incredibly ea``sy:

```python
cprint('This text is in the CLASSIC BLUE color from the Pantone palette', color=Pantone.CLASSIC_BLUE)
```

**Easy right?**
But what if you want to print text with a colored background?

```python
cprint('This is great!', color=Pantone.EMERALD, bg=Pantone.ULTIMATE_GRAY)
```

You can also add styles to the font:

```python
cprint('This string is italic and green', color=Bit4.GREEN, styles=['italic'])
```

You can mix multiple text styles

```python
cprint('This string is italic and bold', styles=['italic', 'bold'])
```

## Colors and styles

### List of all styles

> bold, italic, underline, strong-underline, crossed-out, framed

**Remember:** Styles can be mixed together by including them in the list of strings

### List of all colors from the pantone palette:

> ![pantone](https://img.shields.io/badge/-VERY__PERI-6868ac?style=flat-square&label=2022)
> ![pantone](https://img.shields.io/badge/-ILLUMINATING-f5df4d?style=flat-square&label=2021)
> ![pantone](https://img.shields.io/badge/-ULTIMATE__GRAY-97999b?style=flat-square&label=2021)
> ![pantone](https://img.shields.io/badge/-CLASSIC__BLUE-0f4c81?style=flat-square&label=2020)
> ![pantone](https://img.shields.io/badge/-LIVING__CORAL-ff6f61?style=flat-square&label=2019)
> ![pantone](https://img.shields.io/badge/-ULTRA__VIOLET-5f4b8b?style=flat-square&label=2018)
> ![pantone](https://img.shields.io/badge/-GREENERY-88b04b?style=flat-square&label=2017)
> ![pantone](https://img.shields.io/badge/-ROSE__QUARTZ-f7cac9?style=flat-square&label=2016)
> ![pantone](https://img.shields.io/badge/-SERENITY-92a8d1?style=flat-square&label=2016)
> ![pantone](https://img.shields.io/badge/-MARSALA-955251?style=flat-square&label=2015)
> ![pantone](https://img.shields.io/badge/-RADIANT__ORCHID-b565a1?style=flat-square&label=2014)
> ![pantone](https://img.shields.io/badge/-TURQUOISE-45b5aa?style=flat-square&label=2010)
> ![pantone](https://img.shields.io/badge/-EMERALD-009b77?style=flat-square&label=2013)
> ![pantone](https://img.shields.io/badge/-TANGERINE__TANGO-e34f33?style=flat-square&label=2012)
> ![pantone](https://img.shields.io/badge/-HONEYSUCKLE-d85a7b?style=flat-square&label=2011)

### List of all colors from the 4bit palette:

> ![Bit4](https://img.shields.io/badge/-BLACK-0c0c0c?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-RED-aa0000?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-GREEN-00aa00?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-YELLOW-aa5500?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BLUE-0000aa?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-MAGENTA-aa00aa?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-CYAN-00aaaa?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-WHITE-f0f0f0?style=flat-square)
>
> ![Bit4](https://img.shields.io/badge/-BRIGHT__BLACK-555555?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__RED-ff5555?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__GREEN-55ff55?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__YELLOW-ffff55?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__BLUE-5555ff?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__MAGENTA-ff55ff?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__CYAN-55ffff?style=flat-square)
> ![Bit4](https://img.shields.io/badge/-BRIGHT__WHITE-fafafa?style=flat-square)

### List of all colors from the Material palette:

![material.jpg](./assets/material.jpg)

### List of all colors from the Flat palette:

![flat.jpg](./assets/flat.jpg)

### List of all colors from the Social palette:

![social.jpg](./assets/social.jpg)

**..pssst!**
Using .palette()  you can check all the colors!

```python
# example
Material.palette()
```

**Too little? 🤔**

With the Color class you can define your own colors in the full RGB spectrum 🤯

Look how simple it is:

```python
CUSTOM_COLOR = Color('rgb', 191, 25, 50)
```

> ![custom](https://img.shields.io/badge/-CUSTOM__COLOR-bf1932?style=flat-square)

### *..and this is just the beginning of this great library!* 💚

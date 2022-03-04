from Coloratura import Color


class Reset:
    COLORS = '\033[39m'
    BG = '\033[49m'
    ALL = '\033[0m'


class Pantone:
    """Pantone colors"""
    ILLUMINATING = Color('rgb', 245, 233, 77)  # 2021 - Color of the year
    ULTIMATE_GRAY = Color('rgb', 147, 149, 151)  # 2021 - Color of the year
    CLASSIC_BLUE = Color('rgb', 15, 76, 169)  # 2020 - Color of the year
    LIVING_CORAL = Color('rgb', 255, 11, 97)  # 2019 - Color of the year
    ULTRA_VIOLET = Color('rgb', 95, 75, 139)  # 2018 - Color of the year
    GREENERY = Color('rgb', 136, 176, 75)  # 2017 - Color of the year
    ROSE_QUARTZ = Color('rgb', 248, 205, 205)  # 2016 - Color of the year
    SERENITY = Color('rgb', 147, 169, 209)  # 2016 - Color of the year
    MARSALA = Color('rgb', 151, 90, 88)  # 2015 - Color of the year
    RADIANT_ORCHID = Color('rgb', 176, 103, 161)  # 2014 - Color of the year
    EMERALD = Color('rgb', 0, 153, 123)  # 2013 - Color of the year
    TANGERINE_TANGO = Color('rgb', 221, 65, 36)  # 2012 - Color of the year
    HONEYSUCKLE = Color('rgb', 216, 90, 123)  # 2011 - Color of the year
    TURQUOISE = Color('rgb', 96, 181, 170)  # 2010 - Color of the year


class Bit4:
    """4 BIT colors"""
    BLACK = Color('bit4', 30)
    RED = Color('bit4', 31)
    GREEN = Color('bit4', 32)
    YELLOW = Color('bit4', 33)
    BLUE = Color('bit4', 34)
    MAGENTA = Color('bit4', 35)
    CYAN = Color('bit4', 36)
    WHITE = Color('bit4', 37)
    BRIGHT_BLACK = Color('bit4', 90)
    BRIGHT_RED = Color('bit4', 91)
    BRIGHT_GREEN = Color('bit4', 92)
    BRIGHT_YELLOW = Color('bit4', 93)
    BRIGHT_BLUE = Color('bit4', 94)
    BRIGHT_MAGENTA = Color('bit4', 95)
    BRIGHT_CYAN = Color('bit4', 96)
    BRIGHT_WHITE = Color('bit4', 97)

from random import choice


class Color:
    def __init__(self, color_space, *args):
        self.color_space = str(color_space).lower()
        self.color = args

    def __str__(self):
        if self.color_space == 'rgb':
            r = self.color[0]
            g = self.color[1]
            b = self.color[2]
            return f'{r};{g};{b}'
        else:
            raise NameError('Kolor błędnie zdefiniowany')


class Pantone:
    # Colors of the year
    ILLUMINATING = Color('rgb', 245, 233, 77)  # 2021
    ULTIMATE_GRAY = Color('rgb', 147, 149, 151)  # 2021
    CLASSIC_BLUE = Color('rgb', 15, 76, 169)  # 2020
    LIVING_CORAL = Color('rgb', 255, 11, 97)  # 2019
    ULTRA_VIOLET = Color('rgb', 95, 75, 139)  # 2018
    GREENERY = Color('rgb', 136, 176, 75)  # 2017
    ROSE_QUARTZ = Color('rgb', 248, 205, 205)  # 2016
    SERENITY = Color('rgb', 147, 169, 209)  # 2016
    MARSALA = Color('rgb', 151, 90, 88)  # 2015
    RADIANT_ORCHID = Color('rgb', 176, 103, 161)  # 2014
    EMERALD = Color('rgb', 0, 153, 123)  # 2013
    TANGERINE_TANGO = Color('rgb', 221, 65, 36)  # 2012
    HONEYSUCKLE = Color('rgb', 216, 90, 123)  # 2011
    TURQUOISE = Color('rgb', 96, 181, 170)  # 2010


RES_C = '\033[39m'
RES_BG = '\033[49m'
RESET_ALL = '\033[0m'


def cprint(*text, sep='', end='\n', color=None, bg=None, styles=None):
    new_text = sep.join(text)

    if color is not None:
        new_text = f'\033[38;2;{color}m{new_text}'

    if bg is not None:
        new_text = f'\033[48;2;{bg}m{new_text}'

    if type(styles) is list and styles is not None:
        for style in styles:
            if 'bold' == style:
                new_text = '\033[1m' + new_text
            if 'italic' == style:
                new_text = '\033[3m' + new_text
            if 'underline' == style:
                new_text = '\033[4m' + new_text
            if 'strong-underline' == style:
                new_text = '\033[21m' + new_text
            if 'crossed-out' == style:
                new_text = '\033[9m' + new_text
            if 'framed' == style:
                new_text = '\033[51m' + new_text

    return print(new_text, RESET_ALL, sep=sep, end=end)


cprint('Ala ma kota', color=choice([Pantone.EMERALD, Pantone.LIVING_CORAL, Pantone.ROSE_QUARTZ]))

cprint('Ala ma kota')
cprint('Ala ma kota', styles=['italic'])
cprint('Ala ma kota', styles=['bold'])
cprint('Ala ma kota', styles=['underline'])
cprint('Ala ma kota', styles=['strong-underline'])
cprint('Ala ma kota', styles=['crossed-out'])
cprint('Ala ma kota', styles=['framed'])
cprint('Ala ma kota', styles=['italic', 'bold', 'strong-underline', 'crossed-out'])


# for i in range(110):
#     # print(f'\033[{i}m test{RESET_ALL} {i}')
#     cprint(f'\033[{i}m', 'teścik', RESET_ALL, f' {i}', color=Pantone.LIVING_CORAL)

# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.CLASSIC_BLUE)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ROSE_QUARTZ)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ULTRA_VIOLET)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.MARSALA)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.EMERALD)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ILLUMINATING)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.LIVING_CORAL)
# cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ULTIMATE_GRAY)

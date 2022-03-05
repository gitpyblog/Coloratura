from coloratura import cprint, Pantone, Bit4


def test_styles():
    cprint('Ala ma kota')
    cprint('Ala ma kota', styles=['italic'])
    cprint('Ala ma kota', styles=['bold'])
    cprint('Ala ma kota', styles=['underline'])
    cprint('Ala ma kota', styles=['strong-underline'])
    cprint('Ala ma kota', styles=['crossed-out'])
    cprint('Ala ma kota', styles=['framed'])
    cprint('Ala ma kota', styles=['italic', 'bold', 'strong-underline', 'crossed-out'])
    print('\n')


def test_font():
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.CLASSIC_BLUE)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ROSE_QUARTZ)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ULTRA_VIOLET)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.MARSALA)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.EMERALD)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ILLUMINATING)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.LIVING_CORAL)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.ULTIMATE_GRAY)
    print('\n')


def test_bg():
    cprint(f'Ala ma kota.', 'Kot ma Alę!', bg=Pantone.ULTIMATE_GRAY)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', bg=Pantone.HONEYSUCKLE)
    cprint(f'Ala ma kota.', 'Kot ma Alę!', color=Pantone.CLASSIC_BLUE, bg=Pantone.ROSE_QUARTZ)
    print('\n')


def test_bit4():
    cprint('Bit4 font', color=Bit4.BLACK)
    cprint('Bit4 font', color=Bit4.WHITE)
    cprint('Bit4 font', color=Bit4.RED)
    cprint('Bit4 font', color=Bit4.GREEN)
    cprint('Bit4 font', color=Bit4.YELLOW)
    cprint('Bit4 font', color=Bit4.BLUE)
    cprint('Bit4 font', color=Bit4.MAGENTA)
    cprint('Bit4 font', color=Bit4.CYAN)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_BLACK)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_WHITE)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_RED)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_GREEN)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_YELLOW)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_BLUE)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_MAGENTA)
    cprint('Bit4 font bright', color=Bit4.BRIGHT_CYAN)
    print('\n')


def test_bg_bit4():
    cprint('Bit4 background', color=Bit4.YELLOW, bg=Bit4.BLACK)
    cprint('Bit4 background', bg=Bit4.WHITE)
    cprint('Bit4 background', bg=Bit4.RED)
    cprint('Bit4 background', bg=Bit4.GREEN)
    cprint('Bit4 background', bg=Bit4.YELLOW)
    cprint('Bit4 background', bg=Bit4.BLUE)
    cprint('Bit4 background', bg=Bit4.MAGENTA)
    cprint('Bit4 background', bg=Bit4.CYAN)

    cprint('BIT4 background bright', color=Bit4.BRIGHT_YELLOW, bg=Bit4.BRIGHT_BLACK)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_WHITE)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_RED)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_GREEN)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_YELLOW)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_BLUE)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_MAGENTA)
    cprint('BIT4 background bright', bg=Bit4.BRIGHT_CYAN)
    print('\n')


def generate_bit4():
    for i in range(30, 37):
        print(f'\033[{i}m Bit4 - Ala ma kota. Kot ma Alę!\033[0m')
    print('')
    for i in range(90, 97):
        print(f'\033[{i}m Bit4 - Ala ma kota. Kot ma Alę!\033[0m')


def generate_bg_bit4():
    for i in range(40, 47):
        print(f'\033[{i}m Bit4 - Ala ma kota. Kot ma Alę!\033[0m')
    print('')
    for i in range(100, 107):
        print(f'\033[{i}m Bit4 - Ala ma kota. Kot ma Alę!\033[0m')


test_styles()
test_font()
test_bg()
test_bit4()
test_bg_bit4()

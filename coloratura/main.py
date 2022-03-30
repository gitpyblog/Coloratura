from typing import Union


class Color:
    FONT = '\033[39m'
    BG = '\033[49m'
    RESET = '\033[0m'

    def __init__(self, color_space: Union[str, None], *args: any):
        """
        With this class you can create your own custom colors.

        Example:
            black_rgb = Color('rgb' , 0, 0, 0)
        Args:
            color_space: color space. Currently, supported rgb
            args: Color values
        """
        self.color_space = str(color_space).lower()
        self.color = args

    def __str__(self):
        if self.color_space == 'rgb':
            return f'\033[38;2;{self.color[0]};{self.color[1]};{self.color[2]}m'
        elif self.color_space == 'bit4':
            return f'\033[{self.color[0]}m'


def cprint(*text, color: Color = None, bg: Color = None, styles: list = None, sep=' ', end='\n') -> print:
    """
    Function that returns a colored string.

    Example:
        cprint(value, ..., color=BLUE, bg=GRAY, styles=['bold', 'italic'])

    Args:
        text: String to format
        color: Color of the text
        bg: Background color
        styles: List of styles to apply to the text
        sep: Separator between the arguments
        end: End parameter defines what character is printed at the end of the string, defaults to new line character.

    Returns:
        print() with a color, background color, and styles.
    """
    update_string = sep.join([str(elem) for elem in text])

    if color:
        if color.color_space == 'rgb':
            update_string = f'\033[38;2;{color.color[0]};{color.color[1]};{color.color[2]}m{update_string}'
        elif color.color_space == 'bit4':
            update_string = f'\033[{color.color[0]}m{update_string}'

    if bg:
        if bg.color_space == 'rgb':
            update_string = f'\033[48;2;{bg.color[0]};{bg.color[1]};{bg.color[2]}m{update_string}'
        elif bg.color_space == 'bit4':
            update_string = f'\033[{bg.color[0]}m{update_string}'

    if styles:
        decorations = {
            'bold': '\033[1m',
            'italic': '\033[3m',
            'underline': '\033[4m',
            'strong-underline': '\033[21m',
            'crossed-out': '\033[9m',
            'framed': '\033[51m'
        }
        # for style in styles:
        #     if style in decorations:
        #         update_string = f'{decorations[style]}{update_string}'
        update_string = ''.join([f'{decorations[style]}' if style in decorations else '' for style in styles]) + update_string

    return print(f'{update_string}\033[0m', sep=sep, end=end)

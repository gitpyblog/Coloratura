class Color:
    def __init__(self, color_space: str | None, *args: any):
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


def cprint(*text, color: Color = None, bg: Color = None, styles: list = None, sep='', end='\n') -> print:
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
    update_string = sep.join(text)

    if color is not None:
        if color.color_space == 'rgb':
            update_string = f'\033[38;2;{color.color[0]};{color.color[1]};{color.color[2]}m{update_string}'
        elif color.color_space == 'bit4':
            update_string = f'\033[{color.color[0]}m{update_string}'

    if bg is not None:
        if bg.color_space == 'rgb':
            update_string = f'\033[48;2;{bg.color[0]};{bg.color[1]};{bg.color[2]}m{update_string}'
        elif bg.color_space == 'bit4':
            update_string = f'\033[{bg.color[0] + 10}m{update_string}'

    if type(styles) is list and styles is not None:
        for style in styles:
            if 'bold' == style:
                update_string = '\033[1m' + update_string
            if 'italic' == style:
                update_string = '\033[3m' + update_string
            if 'underline' == style:
                update_string = '\033[4m' + update_string
            if 'strong-underline' == style:
                update_string = '\033[21m' + update_string
            if 'crossed-out' == style:
                update_string = '\033[9m' + update_string
            if 'framed' == style:
                update_string = '\033[51m' + update_string

    return print(update_string, '\033[0m', sep=sep, end=end)

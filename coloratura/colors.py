from coloratura import Color, cprint


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


class Material:
    """Material UI colors"""
    RED_50 = Color('rgb', 255, 235, 238)
    RED_100 = Color('rgb', 255, 205, 210)
    RED_200 = Color('rgb', 239, 154, 154)
    RED_300 = Color('rgb', 229, 115, 115)
    RED_400 = Color('rgb', 239, 83, 80)
    RED_500 = Color('rgb', 244, 67, 54)
    RED_600 = Color('rgb', 229, 57, 53)
    RED_700 = Color('rgb', 211, 47, 47)
    RED_800 = Color('rgb', 198, 40, 40)
    RED_900 = Color('rgb', 183, 28, 28)
    RED_A100 = Color('rgb', 255, 138, 128)
    RED_A200 = Color('rgb', 255, 82, 82)
    RED_A400 = Color('rgb', 255, 23, 68)
    RED_A700 = Color('rgb', 213, 0, 0)

    PINK_50 = Color('rgb', 252, 228, 236)
    PINK_100 = Color('rgb', 248, 187, 208)
    PINK_200 = Color('rgb', 244, 143, 177)
    PINK_300 = Color('rgb', 240, 98, 146)
    PINK_400 = Color('rgb', 236, 64, 122)
    PINK_500 = Color('rgb', 233, 30, 99)
    PINK_600 = Color('rgb', 216, 27, 96)
    PINK_700 = Color('rgb', 194, 24, 91)
    PINK_800 = Color('rgb', 173, 20, 87)
    PINK_900 = Color('rgb', 136, 14, 79)
    PINK_A100 = Color('rgb', 255, 128, 171)
    PINK_A200 = Color('rgb', 255, 64, 129)
    PINK_A400 = Color('rgb', 245, 0, 87)
    PINK_A700 = Color('rgb', 197, 17, 98)

    PURPLE_50 = Color('rgb', 243, 229, 245)
    PURPLE_100 = Color('rgb', 225, 190, 231)
    PURPLE_200 = Color('rgb', 206, 147, 216)
    PURPLE_300 = Color('rgb', 186, 104, 200)
    PURPLE_400 = Color('rgb', 171, 71, 188)
    PURPLE_500 = Color('rgb', 156, 39, 176)
    PURPLE_600 = Color('rgb', 142, 36, 170)
    PURPLE_700 = Color('rgb', 123, 31, 162)
    PURPLE_800 = Color('rgb', 106, 27, 154)
    PURPLE_900 = Color('rgb', 74, 20, 140)
    PURPLE_A100 = Color('rgb', 234, 128, 252)
    PURPLE_A200 = Color('rgb', 224, 64, 251)
    PURPLE_A400 = Color('rgb', 213, 0, 249)
    PURPLE_A700 = Color('rgb', 170, 0, 255)

    DEEP_PURPLE_50 = Color('rgb', 237, 231, 246)
    DEEP_PURPLE_100 = Color('rgb', 179, 157, 219)
    DEEP_PURPLE_200 = Color('rgb', 149, 117, 205)
    DEEP_PURPLE_300 = Color('rgb', 149, 117, 205)
    DEEP_PURPLE_400 = Color('rgb', 126, 87, 194)
    DEEP_PURPLE_500 = Color('rgb', 103, 58, 183)
    DEEP_PURPLE_600 = Color('rgb', 94, 53, 177)
    DEEP_PURPLE_700 = Color('rgb', 81, 45, 168)
    DEEP_PURPLE_800 = Color('rgb', 69, 39, 160)
    DEEP_PURPLE_900 = Color('rgb', 49, 27, 146)
    DEEP_PURPLE_A100 = Color('rgb', 179, 136, 255)
    DEEP_PURPLE_A200 = Color('rgb', 124, 77, 255)
    DEEP_PURPLE_A400 = Color('rgb', 101, 31, 255)
    DEEP_PURPLE_A700 = Color('rgb', 98, 0, 234)

    INDIGO_50 = Color('rgb', 232, 234, 246)
    INDIGO_100 = Color('rgb', 197, 202, 233)
    INDIGO_200 = Color('rgb', 159, 168, 218)
    INDIGO_300 = Color('rgb', 121, 134, 203)
    INDIGO_400 = Color('rgb', 92, 107, 192)
    INDIGO_500 = Color('rgb', 63, 81, 181)
    INDIGO_600 = Color('rgb', 57, 73, 171)
    INDIGO_700 = Color('rgb', 48, 63, 159)
    INDIGO_800 = Color('rgb', 40, 53, 147)
    INDIGO_900 = Color('rgb', 26, 35, 126)
    INDIGO_A100 = Color('rgb', 140, 158, 255)
    INDIGO_A200 = Color('rgb', 83, 109, 254)
    INDIGO_A400 = Color('rgb', 61, 90, 254)
    INDIGO_A700 = Color('rgb', 48, 79, 254)

    BLUE_50 = Color('rgb', 227, 242, 253)
    BLUE_100 = Color('rgb', 187, 222, 251)
    BLUE_200 = Color('rgb', 144, 202, 249)
    BLUE_300 = Color('rgb', 100, 181, 246)
    BLUE_400 = Color('rgb', 66, 165, 245)
    BLUE_500 = Color('rgb', 33, 150, 243)
    BLUE_600 = Color('rgb', 30, 136, 229)
    BLUE_700 = Color('rgb', 25, 118, 210)
    BLUE_800 = Color('rgb', 21, 101, 192)
    BLUE_900 = Color('rgb', 13, 71, 161)
    BLUE_A100 = Color('rgb', 130, 177, 255)
    BLUE_A200 = Color('rgb', 68, 138, 255)
    BLUE_A400 = Color('rgb', 41, 121, 255)
    BLUE_A700 = Color('rgb', 41, 98, 255)

    LIGHT_BLUE_50 = Color('rgb', 225, 245, 254)
    LIGHT_BLUE_100 = Color('rgb', 179, 229, 252)
    LIGHT_BLUE_200 = Color('rgb', 129, 212, 250)
    LIGHT_BLUE_300 = Color('rgb', 79, 195, 247)
    LIGHT_BLUE_400 = Color('rgb', 41, 182, 246)
    LIGHT_BLUE_500 = Color('rgb', 3, 169, 244)
    LIGHT_BLUE_600 = Color('rgb', 3, 155, 229)
    LIGHT_BLUE_700 = Color('rgb', 2, 136, 209)
    LIGHT_BLUE_800 = Color('rgb', 2, 119, 189)
    LIGHT_BLUE_900 = Color('rgb', 1, 87, 155)
    LIGHT_BLUE_A100 = Color('rgb', 128, 216, 255)
    LIGHT_BLUE_A200 = Color('rgb', 64, 196, 255)
    LIGHT_BLUE_A400 = Color('rgb', 0, 176, 255)
    LIGHT_BLUE_A700 = Color('rgb', 0, 145, 234)

    CYAN_50 = Color('rgb', 224, 247, 250)
    CYAN_100 = Color('rgb', 178, 235, 242)
    CYAN_200 = Color('rgb', 128, 222, 234)
    CYAN_300 = Color('rgb', 77, 208, 225)
    CYAN_400 = Color('rgb', 38, 198, 218)
    CYAN_500 = Color('rgb', 0, 188, 212)
    CYAN_600 = Color('rgb', 0, 172, 193)
    CYAN_700 = Color('rgb', 0, 151, 167)
    CYAN_800 = Color('rgb', 0, 131, 143)
    CYAN_900 = Color('rgb', 0, 96, 100)
    CYAN_A100 = Color('rgb', 132, 255, 255)
    CYAN_A200 = Color('rgb', 24, 255, 255)
    CYAN_A400 = Color('rgb', 0, 229, 255)
    CYAN_A700 = Color('rgb', 0, 184, 212)

    TEAL_50 = Color('rgb', 224, 242, 241)
    TEAL_100 = Color('rgb', 178, 223, 219)
    TEAL_200 = Color('rgb', 128, 203, 196)
    TEAL_300 = Color('rgb', 77, 182, 172)
    TEAL_400 = Color('rgb', 38, 166, 154)
    TEAL_500 = Color('rgb', 0, 150, 136)
    TEAL_600 = Color('rgb', 0, 137, 123)
    TEAL_700 = Color('rgb', 0, 121, 107)
    TEAL_800 = Color('rgb', 0, 105, 92)
    TEAL_900 = Color('rgb', 0, 77, 64)
    TEAL_A100 = Color('rgb', 167, 255, 235)
    TEAL_A200 = Color('rgb', 100, 255, 218)
    TEAL_A400 = Color('rgb', 29, 233, 182)
    TEAL_A700 = Color('rgb', 0, 191, 165)

    GREEN_50 = Color('rgb', 232, 245, 233)
    GREEN_100 = Color('rgb', 200, 230, 201)
    GREEN_200 = Color('rgb', 165, 214, 167)
    GREEN_300 = Color('rgb', 129, 199, 132)
    GREEN_400 = Color('rgb', 102, 187, 106)
    GREEN_500 = Color('rgb', 102, 187, 106)
    GREEN_600 = Color('rgb', 67, 160, 71)
    GREEN_700 = Color('rgb', 56, 142, 60)
    GREEN_800 = Color('rgb', 46, 125, 50)
    GREEN_900 = Color('rgb', 27, 94, 32)
    GREEN_A100 = Color('rgb', 185, 246, 202)
    GREEN_A200 = Color('rgb', 105, 240, 174)
    GREEN_A400 = Color('rgb', 0, 230, 118)
    GREEN_A700 = Color('rgb', 0, 200, 83)

    LIGHT_GREEN_50 = Color('rgb', 241, 248, 233)
    LIGHT_GREEN_100 = Color('rgb', 220, 237, 200)
    LIGHT_GREEN_200 = Color('rgb', 197, 225, 165)
    LIGHT_GREEN_300 = Color('rgb', 174, 213, 129)
    LIGHT_GREEN_400 = Color('rgb', 156, 204, 101)
    LIGHT_GREEN_500 = Color('rgb', 139, 195, 74)
    LIGHT_GREEN_600 = Color('rgb', 124, 179, 66)
    LIGHT_GREEN_700 = Color('rgb', 104, 159, 56)
    LIGHT_GREEN_800 = Color('rgb', 85, 139, 47)
    LIGHT_GREEN_900 = Color('rgb', 51, 105, 30)
    LIGHT_GREEN_A100 = Color('rgb', 204, 255, 144)
    LIGHT_GREEN_A200 = Color('rgb', 178, 255, 89)
    LIGHT_GREEN_A400 = Color('rgb', 118, 255, 3)
    LIGHT_GREEN_A700 = Color('rgb', 100, 221, 23)

    LIME_50 = Color('rgb', 249, 251, 231)
    LIME_100 = Color('rgb', 240, 244, 195)
    LIME_200 = Color('rgb', 230, 238, 156)
    LIME_300 = Color('rgb', 220, 231, 117)
    LIME_400 = Color('rgb', 212, 225, 87)
    LIME_500 = Color('rgb', 205, 220, 57)
    LIME_600 = Color('rgb', 192, 202, 51)
    LIME_700 = Color('rgb', 175, 180, 43)
    LIME_800 = Color('rgb', 158, 157, 36)
    LIME_900 = Color('rgb', 130, 119, 23)
    LIME_A100 = Color('rgb', 244, 255, 129)
    LIME_A200 = Color('rgb', 238, 255, 65)
    LIME_A400 = Color('rgb', 198, 255, 0)
    LIME_A700 = Color('rgb', 174, 234, 0)

    YELLOW_50 = Color('rgb', 255, 253, 231)
    YELLOW_100 = Color('rgb', 255, 249, 196)
    YELLOW_200 = Color('rgb', 255, 245, 157)
    YELLOW_300 = Color('rgb', 255, 241, 118)
    YELLOW_400 = Color('rgb', 255, 238, 88)
    YELLOW_500 = Color('rgb', 255, 235, 59)
    YELLOW_600 = Color('rgb', 253, 216, 53)
    YELLOW_700 = Color('rgb', 251, 192, 45)
    YELLOW_800 = Color('rgb', 249, 168, 37)
    YELLOW_900 = Color('rgb', 245, 127, 23)
    YELLOW_A100 = Color('rgb', 255, 255, 141)
    YELLOW_A200 = Color('rgb', 255, 255, 0)
    YELLOW_A400 = Color('rgb', 255, 234, 0)
    YELLOW_A700 = Color('rgb', 255, 214, 0)

    AMBER_50 = Color('rgb', 255, 248, 225)
    AMBER_100 = Color('rgb', 255, 236, 179)
    AMBER_200 = Color('rgb', 255, 224, 130)
    AMBER_300 = Color('rgb', 255, 213, 79)
    AMBER_400 = Color('rgb', 255, 202, 40)
    AMBER_500 = Color('rgb', 255, 193, 7)
    AMBER_600 = Color('rgb', 255, 179, 0)
    AMBER_700 = Color('rgb', 255, 160, 0)
    AMBER_800 = Color('rgb', 255, 143, 0)
    AMBER_900 = Color('rgb', 255, 111, 0)
    AMBER_A100 = Color('rgb', 255, 229, 127)
    AMBER_A200 = Color('rgb', 255, 215, 64)
    AMBER_A400 = Color('rgb', 255, 196, 0)
    AMBER_A700 = Color('rgb', 255, 171, 0)

    ORANGE_50 = Color('rgb', 255, 243, 224)
    ORANGE_100 = Color('rgb', 255, 224, 178)
    ORANGE_200 = Color('rgb', 255, 204, 128)
    ORANGE_300 = Color('rgb', 255, 183, 77)
    ORANGE_400 = Color('rgb', 255, 167, 38)
    ORANGE_500 = Color('rgb', 255, 152, 0)
    ORANGE_600 = Color('rgb', 251, 140, 0)
    ORANGE_700 = Color('rgb', 245, 124, 0)
    ORANGE_800 = Color('rgb', 239, 108, 0)
    ORANGE_900 = Color('rgb', 230, 81, 0)
    ORANGE_A100 = Color('rgb', 255, 209, 128)
    ORANGE_A200 = Color('rgb', 255, 171, 64)
    ORANGE_A400 = Color('rgb', 255, 145, 0)
    ORANGE_A700 = Color('rgb', 255, 109, 0)

    DEEP_ORANGE_50 = Color('rgb', 251, 233, 231)
    DEEP_ORANGE_100 = Color('rgb', 255, 204, 188)
    DEEP_ORANGE_200 = Color('rgb', 255, 171, 145)
    DEEP_ORANGE_300 = Color('rgb', 255, 138, 101)
    DEEP_ORANGE_400 = Color('rgb', 255, 112, 67)
    DEEP_ORANGE_500 = Color('rgb', 255, 87, 34)
    DEEP_ORANGE_600 = Color('rgb', 244, 81, 30)
    DEEP_ORANGE_700 = Color('rgb', 230, 74, 25)
    DEEP_ORANGE_800 = Color('rgb', 216, 67, 21)
    DEEP_ORANGE_900 = Color('rgb', 191, 54, 12)
    DEEP_ORANGE_A100 = Color('rgb', 255, 158, 128)
    DEEP_ORANGE_A200 = Color('rgb', 255, 110, 64)
    DEEP_ORANGE_A400 = Color('rgb', 255, 61, 0)
    DEEP_ORANGE_A700 = Color('rgb', 221, 44, 0)

    BROWN_50 = Color('rgb', 239, 235, 233)
    BROWN_100 = Color('rgb', 215, 204, 200)
    BROWN_200 = Color('rgb', 188, 170, 164)
    BROWN_300 = Color('rgb', 161, 136, 127)
    BROWN_400 = Color('rgb', 141, 110, 99)
    BROWN_500 = Color('rgb', 121, 85, 72)
    BROWN_600 = Color('rgb', 109, 76, 65)
    BROWN_700 = Color('rgb', 93, 64, 55)
    BROWN_800 = Color('rgb', 78, 52, 46)
    BROWN_900 = Color('rgb', 62, 39, 35)

    GREY_50 = Color('rgb', 250, 250, 250)
    GREY_100 = Color('rgb', 245, 245, 245)
    GREY_200 = Color('rgb', 238, 238, 238)
    GREY_300 = Color('rgb', 224, 224, 224)
    GREY_400 = Color('rgb', 189, 189, 189)
    GREY_500 = Color('rgb', 158, 158, 158)
    GREY_600 = Color('rgb', 117, 117, 117)
    GREY_700 = Color('rgb', 97, 97, 97)
    GREY_800 = Color('rgb', 66, 66, 66)
    GREY_900 = Color('rgb', 33, 33, 33)

    BLUE_GREY_50 = Color('rgb', 236, 239, 241)
    BLUE_GREY_100 = Color('rgb', 207, 216, 220)
    BLUE_GREY_200 = Color('rgb', 176, 190, 197)
    BLUE_GREY_300 = Color('rgb', 144, 164, 174)
    BLUE_GREY_400 = Color('rgb', 120, 144, 156)
    BLUE_GREY_500 = Color('rgb', 96, 125, 139)
    BLUE_GREY_600 = Color('rgb', 84, 110, 122)
    BLUE_GREY_700 = Color('rgb', 69, 90, 100)
    BLUE_GREY_800 = Color('rgb', 55, 71, 79)
    BLUE_GREY_900 = Color('rgb', 38, 50, 56)

    @staticmethod
    def palette():
        width = 8
        color_names = 'RED', 'PINK', 'PURPLE', 'DEEP_PURPLE', 'INDIGO', 'BLUE', 'LIGHT_BLUE', 'CYAN', 'TEAL', 'GREEN', \
                      'LIGHT_GREEN', 'LIME', 'YELLOW', 'AMBER', 'ORANGE', 'DEEP_ORANGE', 'BROWN', 'GREY', 'BLUE_GREY'

        color_codes = 100, 200, 300, 400, 500, 600, 700, 800, 900, 'A100', 'A200', 'A400', 'A700'

        def color_name():
            line_label_first = list()
            line_label_second = list()

            for color in color_names:
                if '_' in color:
                    color = color.split('_')
                    line_label_first.append(color[0].ljust(width).lower())
                    line_label_second.append(color[1].ljust(width).lower())
                else:
                    line_label_first.append(''.ljust(width).lower())
                    line_label_second.append(color.ljust(width).lower())

            print(''.ljust(width), ''.join(line_label_first))
            print(''.ljust(width), ''.join(line_label_second))

        color_name()

        def color_code(code, a=False):
            color_list = color_names
            if a is True:
                color_list = color_list[:-3]

            cprint(f'{code} '.rjust(width), end='')
            for color in color_list:
                cprint(''.center(width), bg=getattr(Material, f'{color}_{code}'), end='')
            print('')

        for c in color_codes:
            if str(c).startswith('A'):
                color_code(c, a=True)
            else:
                color_code(c)


class Social:
    """Popular social media colors"""
    FACEBOOK = Color('rgb', 24, 119, 242)
    DROPBOX = Color('rgb', 0, 97, 255)
    TUMBLR = Color('rgb', 52, 70, 93)
    QUORA = Color('rgb', 185, 43, 39)
    SOUNDCLOUD = Color('rgb', 255, 51, 0)
    LINE = Color('rgb', 0, 195, 0)
    DRIBBBLE = Color('rgb', 234, 76, 137)
    MESSENGER = Color('rgb', 0, 153, 255)
    WORDPRESS = Color('rgb', 33, 117, 155)
    YAHOO = Color('rgb', 65, 0, 147)
    YELP = Color('rgb', 175, 6, 6)
    BLOGGER = Color('rgb', 245, 125, 0)
    MEDIUM = Color('rgb', 2, 184, 117)
    FLICKR = Color('rgb', 255, 0, 132)
    TWITTER = Color('rgb', 29, 161, 242)
    VIMEO = Color('rgb', 26, 183, 234)
    PINTEREST = Color('rgb', 189, 8, 28)
    WEIBO = Color('rgb', 223, 32, 41)
    SNAPCHAT = Color('rgb', 255, 252, 0)
    VINE = Color('rgb', 0, 180, 137)
    FOURSQUARE = Color('rgb', 249, 72, 119)
    LINKEDIN = Color('rgb', 10, 102, 194)
    SLIDESHARE = Color('rgb', 0, 119, 181)
    YOUTUBE = Color('rgb', 205, 32, 31)
    PRODUCTHUNT = Color('rgb', 218, 85, 47)
    WHATSAPP = Color('rgb', 37, 211, 102)
    SLACK = Color('rgb', 58, 175, 133)
    TIKTOK = Color('rgb', 238, 29, 81)
    SKYPE = Color('rgb', 0, 175, 240)
    VK = Color('rgb', 76, 117, 163)
    REDDIT = Color('rgb', 255, 87, 0)
    HACKERNEWS = Color('rgb', 255, 102, 0)
    WECHAT = Color('rgb', 9, 184, 62)
    INSTAGRAM = Color('rgb', 228, 64, 95)
    BEHANCE = Color('rgb', 19, 20, 24)

    @staticmethod
    def palette():
        return ' '.join([i for i in Social.__dict__.keys()][2:-3])

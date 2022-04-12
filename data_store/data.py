""" Test data for yandex speller api tests """


class Url:
    # url data
    URL = 'https://speller.yandex.net/services/spellservice.json/'
    CHECK_TEXT = URL + 'checkText'
    CHECK_TEXTS = URL + 'checkTexts'


class RequestData:
    """ Request data """
    # options
    OPTION_2 = "2"
    OPTION_4 = "4"
    OPTION_8 = "8"
    OPTION_512 = "512"
    # languages
    RU = "ru"
    EN = "en"
    UK = "uk"
    # valid data
    VALID_RU_WORD = 'слово'
    VALID_EN_WORD = 'word'
    VALID_UK_WORD = 'мова'
    # invalid data
    INVALID_UK_WORD = 'моваа'
    INVALID_RU_WORD = 'словоо'
    INVALID_EN_WORD = 'wordd'
    # digits
    BELOW_ZERO = -45
    ZERO = 0
    ABOVE_ZERO = 55
    BIG = 183546
    # word with digit
    WORD_WITH_DIGIT = "wor4d"
    # CAPITAL
    VALID_CAPITAL = "Москва"
    INVALID_CAPITAL = "москва"


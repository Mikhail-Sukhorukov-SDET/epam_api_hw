""" Test data for yandex speller api tests """


class Url():
    # url data
    URL = 'https://speller.yandex.net/services/spellservice.json'
    TEXT = 'checkText'
    TEXTS = 'checkTexts'


class RequestData():
    # request data
    VALID_RU_WORD = 'слово'
    INVALID_RU_WORD = 'словоо'
    VALID_EN_WORD = 'word'
    INVALID_EN_WORD = 'wordd'
    VALID_UK_WORD = 'мова'
    INVALID_UK_WORD = 'моваа'
    BELOW_ZERO = -45
    ZERO = 0
    ABOVE_ZERO = 55
    BIG = 183546

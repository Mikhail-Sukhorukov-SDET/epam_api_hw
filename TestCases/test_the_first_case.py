import json
import jsonpath
import pytest
import os
import requests

URL = 'https://speller.yandex.net/services/spellservice.json'
TEXT = 'checkText'
TEXTS = 'checkTexts'
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


# run with: pytest -n3 -m "invalid"
@pytest.mark.invalid
class TestInvalidWords():
    """ Check invalid words - word must be corrected in response """

    @pytest.mark.parametrize("invalid_word, valid_word", (
            [INVALID_EN_WORD, VALID_EN_WORD], [INVALID_RU_WORD, VALID_RU_WORD], [INVALID_UK_WORD, VALID_UK_WORD]),
                             ids=["en", "ru", "uk"])
    def test_invalid_word(self, invalid_word, valid_word):
        json_data = {'text': invalid_word}
        response = requests.get(os.path.join(URL, TEXT), params=json_data)
        response_json = json.loads(response.text)
        word = jsonpath.jsonpath(response_json[0], 'word')
        s = jsonpath.jsonpath(response_json[0], 's')
        assert json_data['text'] == word[0]
        assert valid_word in s[0]


# run with: pytest -n3 -m "valid"
@pytest.mark.valid
class TestValidWords():
    """ Check valid words - must be empty response """

    @pytest.mark.parametrize("valid_word", (VALID_EN_WORD, VALID_RU_WORD, VALID_UK_WORD),
                             ids=["en", "ru", "uk"])
    def test_valid_word(self, valid_word):
        json_data = {'text': valid_word}
        response = requests.get(os.path.join(URL, TEXT), params=json_data)
        assert response.text == "[]"


# run with: pytest -n4 -m "digits"
@pytest.mark.digits
class TestDigits():
    """ Check that digits is not acceptable """

    @pytest.mark.parametrize("digit", (BELOW_ZERO, ZERO, ABOVE_ZERO, BIG),
                             ids=["below zero", "zero", "above zero", "big"])
    def test_valid_word(self, digit):
        json_data = {'text': digit}
        response = requests.get(os.path.join(URL, TEXT), params=json_data)
        assert response.text == "[]"

# run with: pytest -n9 -m "filtration"
@pytest.mark.filtration
class TestLanguages():
    """ By default settings, ru and en languages are turned on """
    @pytest.mark.filtration_ru
    class TestLanguageRu():
        """ Check filtration by ru language """

        def test_filtration_by_ru_language_ru_word(self):
            json_data = {'text': INVALID_RU_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_RU_WORD in s[0]

        def test_filtration_by_ru_language_uk_word(self):
            json_data = {'text': INVALID_UK_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            assert response.text == "[]"

        def test_filtration_by_ru_language_en_word(self):
            json_data = {'text': INVALID_EN_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_EN_WORD in s[0]

    @pytest.mark.filtration_en
    class TestLanguageEn():
        """ Check filtration by en language """

        def test_filtration_by_en_language_ru_word(self):
            json_data = {'text': INVALID_RU_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_RU_WORD in s[0]

        def test_filtration_by_en_language_uk_word(self):
            json_data = {'text': INVALID_UK_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            assert response.text == "[]"

        def test_filtration_by_en_language_en_word(self):
            json_data = {'text': INVALID_EN_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_EN_WORD in s[0]

    @pytest.mark.filtration_uk
    class TestLanguageUk():
        """ Check filtration by uk language """

        def test_filtration_by_uk_language_ru_word(self):
            json_data = {'text': INVALID_RU_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_RU_WORD in s[0]

        def test_filtration_by_uk_language_uk_word(self):
            json_data = {'text': INVALID_UK_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_UK_WORD in s[0]

        def test_filtration_by_uk_language_en_word(self):
            json_data = {'text': INVALID_EN_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(URL, TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert VALID_EN_WORD in s[0]

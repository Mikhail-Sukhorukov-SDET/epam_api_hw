import json
import jsonpath
import pytest
import os
import requests
from data_store.data import Url as url
from data_store.data import RequestData as data

# run with: pytest -n3 -m "invalid"
@pytest.mark.invalid
class TestInvalidWords():
    """ Check invalid words - word must be corrected in response """

    @pytest.mark.parametrize("invalid_word, valid_word", (
            [data.INVALID_EN_WORD, data.VALID_EN_WORD],
            [data.INVALID_RU_WORD, data.VALID_RU_WORD],
            [data.INVALID_UK_WORD, data.VALID_UK_WORD]),
                             ids=["en", "ru", "uk"])
    def test_invalid_word(self, invalid_word, valid_word):
        json_data = {'text': invalid_word}
        response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
        response_json = json.loads(response.text)
        word = jsonpath.jsonpath(response_json[0], 'word')
        s = jsonpath.jsonpath(response_json[0], 's')
        assert json_data['text'] == word[0]
        assert valid_word in s[0]


# run with: pytest -n3 -m "valid"
@pytest.mark.valid
class TestValidWords():
    """ Check valid words - must be empty response """

    @pytest.mark.parametrize("valid_word", (
            data.VALID_EN_WORD, data.VALID_RU_WORD, data.VALID_UK_WORD),
                             ids=["en", "ru", "uk"])
    def test_valid_word(self, valid_word):
        json_data = {'text': valid_word}
        response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
        assert response.text == "[]"


# run with: pytest -n4 -m "digits"
@pytest.mark.digits
class TestDigits():
    """ Check that digits is not acceptable """

    @pytest.mark.parametrize("digit", (
            data.BELOW_ZERO, data.ZERO, data.ABOVE_ZERO,
            data.BIG),
                             ids=["below zero", "zero", "above zero", "big"])
    def test_valid_word(self, digit):
        json_data = {'text': digit}
        response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
        assert response.text == "[]"


# run with: pytest -n9 -m "filtration"
@pytest.mark.filtration
class TestLanguages():
    """ By default settings, ru and en languages are turned on """

    @pytest.mark.filtration_ru
    class TestLanguageRu():
        """ Check filtration by ru language """

        def test_filtration_by_ru_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]

        def test_filtration_by_ru_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            assert response.text == "[]"

        def test_filtration_by_ru_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'ru'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]

    @pytest.mark.filtration_en
    class TestLanguageEn():
        """ Check filtration by en language """

        def test_filtration_by_en_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]

        def test_filtration_by_en_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            assert response.text == "[]"

        def test_filtration_by_en_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'en'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]

    @pytest.mark.filtration_uk
    class TestLanguageUk():
        """ Check filtration by uk language """

        def test_filtration_by_uk_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]

        def test_filtration_by_uk_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_UK_WORD in s[0]

        def test_filtration_by_uk_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'uk'}
            response = requests.get(os.path.join(url.URL, url.TEXT), params=json_data)
            response_json = json.loads(response.text)
            word = jsonpath.jsonpath(response_json[0], 'word')
            s = jsonpath.jsonpath(response_json[0], 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]

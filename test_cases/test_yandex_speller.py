import json
import jsonpath
import pytest
import requests
from data_store.data import Url as url
from data_store.data import RequestData as data

# all tests run with: pytest -n5


def get_json_object(response_text, json_part="", index=0):
    """ Check response.text - if it doesn't contain any content return True,
    if it contain any content return part of json object """
    if response_text == "[]":
        return True
    response_json = json.loads(response_text)
    return jsonpath.jsonpath(response_json[index], json_part)


def request(type, url, json_data):
    """ Return response of created request """
    if type == "" or url == "" or json_data == "":
        return
    response = None
    if type == "get":
        response = requests.get(url, params=json_data)
    elif type == "post":
        response = requests.post(url, params=json_data)
    elif type == "put":
        response = requests.put(url, params=json_data)
    elif type == "delete":
        response = requests.delete(url, params=json_data)
    return response


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
        response = request("get", url.URL, json_data)
        word = get_json_object(response.text, 'word')
        s = get_json_object(response.text, 's')
        assert json_data['text'] == word[0]
        assert valid_word in s[0]
        assert response.status_code == 200


# run with: pytest -n3 -m "valid"
@pytest.mark.valid
class TestValidWords():
    """ Check valid words - must be empty response """

    @pytest.mark.parametrize("valid_word", (
            data.VALID_EN_WORD, data.VALID_RU_WORD, data.VALID_UK_WORD),
                             ids=["en", "ru", "uk"])
    def test_valid_word(self, valid_word):
        json_data = {'text': valid_word}
        response = request("get", url.URL, json_data)
        assert get_json_object(response.text)
        assert response.status_code == 200


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
        response = request("get", url.URL, json_data)
        assert get_json_object(response.text)
        assert response.status_code == 200


# run with: pytest -n9 -m "filtration"
@pytest.mark.filtration
class TestLanguages():
    """ By default settings, ru and en languages are turned on """

    # run with: pytest -n3 -m "filtration_ru"
    @pytest.mark.filtration_ru
    class TestLanguageRu():
        """ Check filtration by ru language """

        def test_filtration_by_ru_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'ru'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]
            assert response.status_code == 200

        def test_filtration_by_ru_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'ru'}
            response = request("get", url.URL, json_data)
            assert get_json_object(response.text)
            assert response.status_code == 200

        def test_filtration_by_ru_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'ru'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]
            assert response.status_code == 200

    # run with: pytest -n3 -m "filtration_en"
    @pytest.mark.filtration_en
    class TestLanguageEn():
        """ Check filtration by en language """

        def test_filtration_by_en_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'en'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]
            assert response.status_code == 200

        def test_filtration_by_en_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'en'}
            response = request("get", url.URL, json_data)
            assert get_json_object(response.text)
            assert response.status_code == 200

        def test_filtration_by_en_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'en'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]
            assert response.status_code == 200

    # run with: pytest -n3 -m "filtration_uk"
    @pytest.mark.filtration_uk
    class TestLanguageUk():
        """ Check filtration by uk language """

        def test_filtration_by_uk_language_ru_word(self):
            json_data = {'text': data.INVALID_RU_WORD, 'lang': 'uk'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_RU_WORD in s[0]
            assert response.status_code == 200

        def test_filtration_by_uk_language_uk_word(self):
            json_data = {'text': data.INVALID_UK_WORD, 'lang': 'uk'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_UK_WORD in s[0]
            assert response.status_code == 200

        def test_filtration_by_uk_language_en_word(self):
            json_data = {'text': data.INVALID_EN_WORD, 'lang': 'uk'}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]
            assert response.status_code == 200

    # run with: pytest -n2 -m "word_with_digit"
    @pytest.mark.word_with_digit
    class TestWordWithDigit():
        """ Check that option 2 filtrate words with digits """

        def test_word_with_digit_without_opiton_2(self):
            json_data = {'text': "wor4d"}
            response = request("get", url.URL, json_data)
            word = get_json_object(response.text, 'word')
            s = get_json_object(response.text, 's')
            assert json_data['text'] == word[0]
            assert data.VALID_EN_WORD in s[0]
            assert response.status_code == 200

        def test_word_with_digit_with_opiton_2(self):
            json_data = {'text': 'wor4d', 'options': '2'}
            response = request("get", url.URL, json_data)
            assert get_json_object(response.text)
            assert response.status_code == 200



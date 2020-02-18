import json
import jsonpath
import pytest
import os
import requests

URL = 'https://speller.yandex.net/services/spellservice.json'
TEXT = 'checkText'
TEXTS = 'checkTexts'

# run with: pytest -n3 -m "invalid"
@pytest.mark.invalid
class TestInvalidWords():
    """ Check invalid words - word must be corrected in response """
    @pytest.mark.parametrize("invalid_word, valid_word", (["wordd", "word"], ["словоо", "слово"], ["моваа", "мова"]),
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
    @pytest.mark.parametrize("valid_word", ("word", "слово", "мова"),
                             ids=["en", "ru", "uk"])
    def test_valid_word(self, valid_word):
        json_data = {'text': valid_word}
        response = requests.get(os.path.join(URL, TEXT), params=json_data)
        assert response.text == "[]"

# run with: pytest -n4 -m "digits"
@pytest.mark.digits
class TestDigits():
    """ Check that digits is not acceptable """

    @pytest.mark.parametrize("digit", (-5, 0, 33, 15895),
                             ids=["below zero", "zero", "not bid", "big"])
    def test_valid_word(self, digit):
        json_data = {'text': digit}
        response = requests.get(os.path.join(URL, TEXT), params=json_data)
        assert response.text == "[]"


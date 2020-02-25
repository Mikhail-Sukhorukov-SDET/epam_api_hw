import requests
import json
import jsonpath
from DataStore.data import Url as url


class YandexSpellerApi:
    REQUEST_TEXT = "text"
    REQUEST_OPTIONS = "options"
    REQUEST_LANG = "lang"

    def create_json_for_request(self, content, options="0", lang=""):
        json_object = {YandexSpellerApi.REQUEST_TEXT: content, YandexSpellerApi.REQUEST_OPTIONS: options,
                       YandexSpellerApi.REQUEST_LANG: lang}
        return json_object

    def check_text(self, json_object):
        response = requests.get(url.CHECK_TEXT, params=json_object)
        return response

    def check_texts(self, content, options="0", lang=""):
        json_object = self.create_json_for_request(content, options, lang)
        response = requests.get(url.CHECK_TEXTS, params=json_object)
        return response

    def check_response(self, response_text, content="", assert_data="", index=0):
        if response_text == "[]":
            assert assert_data == response_text
        else:
            response_json = json.loads(response_text)
            response = jsonpath.jsonpath(response_json[index], content)
            assert assert_data in response[0]

    def check_status_code(self, status_code, assert_data=200):
        assert status_code == assert_data

    def reading_csv_file(self):
        ddt_file = open('data.csv', 'r')
        lines = ddt_file.readlines()
        invalid_words = []
        valid_words = []
        for line in lines:
            invalid_word = line.split(',')[0]
            valid_word = line.split(',')[1]
            invalid_words.append(invalid_word)
            if "\n" in valid_word:
                valid_word = valid_word[:-1]
            valid_words.append(valid_word)
        words = {"valid": valid_words,
                 "invalid": invalid_words}
        return words

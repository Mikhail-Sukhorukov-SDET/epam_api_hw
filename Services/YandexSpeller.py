import requests
import json
import jsonpath
from DataStore.data import Url as url


class YandexSpellerApi:
    def check_text(self, content, options="0", lang=""):
        json_object = {"text": content, "options": options, "lang": lang}
        response = requests.get(url.CHECK_TEXT, params=json_object)
        return response

    def check_texts(self, content, options="0", lang=""):
        json_object = {"text": content, "options": options, "lang": lang}
        response = requests.get(url.CHECK_TEXTS, params=json_object)
        return response

    def check_response(self, response_text, content="", assert_data="", index=0):
        if response_text == "[]":
            assert assert_data == response_text
        else:
            response_json = json.loads(response_text)
            response = jsonpath.jsonpath(response_json[index], content)
            assert assert_data == response[0] or assert_data in response[0]

    def check_status_code(self, status_code, assert_data=200):
        assert status_code == assert_data

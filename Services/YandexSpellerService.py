import requests
from DataStore.data import Url as url
from Services.BaseServices import BaseServices


class YandexSpellerApi(BaseServices):
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





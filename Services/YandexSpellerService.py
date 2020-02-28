import requests
from DataStore.data import Url as url
from Services.BaseService import BaseService


class YandexSpellerApi(BaseService):

    def __init__(self):
        super().__init__()
        self.request_text = "text"
        self.request_lang = "lang"
        self.request_options = "options"

    def create_json_for_request(self, content, options="0", lang=""):
        json_object = {self.request_text: content, self.request_lang: lang, self.request_options: options}
        return json_object

    def check_text(self, json_object):
        response = requests.get(url.CHECK_TEXT, params=json_object)
        return response

    def check_texts(self, content, options="0", lang=""):
        json_object = self.create_json_for_request(content, options, lang)
        response = requests.get(url.CHECK_TEXTS, params=json_object)
        return response





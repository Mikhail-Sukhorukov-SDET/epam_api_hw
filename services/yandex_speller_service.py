import requests
from data_store.data import Url
from services.base_service import BaseService


class YandexSpellerApi(BaseService):

    def __init__(self):
        super().__init__()
        self.request_text = "text"
        self.request_lang = "lang"
        self.request_options = "options"

    def create_json_for_request(self, content, options="0", lang=""):
        return {self.request_text: content, self.request_lang: lang, self.request_options: options}

    @staticmethod
    def check_text(json_object):
        return requests.get(Url.CHECK_TEXT, params=json_object)

    def check_texts(self, content, options="0", lang=""):
        json_object = self.create_json_for_request(content, options, lang)
        return requests.get(Url.CHECK_TEXTS, params=json_object)





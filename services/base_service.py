""" Page with common methods for all services  """
import json
import jsonpath
from logging import getLogger
import os


logger = getLogger()


class BaseService:

    def __init__(self):
        self.data_file_name = "data.csv"

    @staticmethod
    def check_response(response_text, content="", assert_data="", index=0):
        if response_text == "[]":
            assert assert_data == response_text
        else:
            response_json = json.loads(response_text)
            response = jsonpath.jsonpath(response_json[index], content)
            assert assert_data in response[0]

    @staticmethod
    def check_status_code(status_code, assert_data=200):
        assert status_code == assert_data

    def reading_csv_file(self):
        logger.info(os.path.abspath(__file__))
        with open(self.data_file_name) as csv:
            invalid_words = []
            valid_words = []
            for line in csv.readlines():
                invalid_word, valid_word = line.strip().split(',')
                invalid_words.append(invalid_word)
                valid_words.append(valid_word)
        return {"valid": valid_words, "invalid": invalid_words}

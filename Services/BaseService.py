""" Page with common methods for all services  """
import json
import jsonpath


class BaseService():
    DATA_FILE_NAME = "data.csv"
    KEY_VALID = "valid"
    KEY_INVALID = "invalid"

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
        ddt_file = open(BaseService.DATA_FILE_NAME, 'r')
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
        words = {BaseService.KEY_VALID: valid_words,
                 BaseService.KEY_INVALID: invalid_words}
        return words

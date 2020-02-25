import pytest
from DataStore.data import RequestData as data
from Services.YandexSpeller import YandexSpellerApi


# run with: pytest -n3 -m "invalid"
@pytest.mark.invalid
class TestInvalidWords:
    """ Check invalid words - word must be corrected in response """

    @pytest.mark.parametrize("invalid_word, valid_word", (
            [data.INVALID_EN_WORD, data.VALID_EN_WORD],
            [data.INVALID_RU_WORD, data.VALID_RU_WORD],
            [data.INVALID_UK_WORD, data.VALID_UK_WORD]),
                             ids=["en", "ru", "uk"])
    def test_invalid_word(self, invalid_word, valid_word):
        speller = YandexSpellerApi()
        json_object = speller.create_json_for_request(content=invalid_word)
        response = speller.check_text(json_object)
        speller.check_response(response.text, 'word', invalid_word)
        speller.check_response(response.text, 's', valid_word)
        speller.check_status_code(response.status_code)


# run with: pytest -n3 -m "valid"
@pytest.mark.valid
class TestValidWords():
    """ Check valid words - must be empty response """

    @pytest.mark.parametrize("valid_word", (
            data.VALID_EN_WORD, data.VALID_RU_WORD, data.VALID_UK_WORD),
                             ids=["en", "ru", "uk"])
    def test_valid_word(self, valid_word):
        speller = YandexSpellerApi()
        json_object = speller.create_json_for_request(content=valid_word)
        response = speller.check_text(json_object)
        speller.check_response(response.text, assert_data="[]")
        speller.check_status_code(response.status_code)


# run with: pytest -n4 -m "digits"
@pytest.mark.digits
class TestDigits():
    """ Check that digits is not acceptable """

    @pytest.mark.parametrize("digit", (
            data.BELOW_ZERO, data.ZERO, data.ABOVE_ZERO, data.BIG), ids=["below zero", "zero", "above zero", "big"])
    def test_digits(self, digit):
        speller = YandexSpellerApi()
        json_object = speller.create_json_for_request(content=digit)
        response = speller.check_text(json_object)
        speller.check_response(response.text, assert_data="[]")
        speller.check_status_code(response.status_code)


# run with: pytest -n9 -m "filtration"
@pytest.mark.filtration
class TestLanguages():
    """ By default settings, ru and en languages are turned on """

    # run with: pytest -n3 -m "filtration_ru"
    @pytest.mark.filtration_ru
    class TestLanguageRu():
        """ Check filtration by ru language """

        def test_filtration_by_ru_language_ru_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_RU_WORD, lang=data.RU)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_RU_WORD)
            speller.check_response(response.text, 's', data.VALID_RU_WORD)
            speller.check_status_code(response.status_code)

        def test_filtration_by_ru_language_uk_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_UK_WORD, lang=data.RU)
            response = speller.check_text(json_object)
            speller.check_response(response.text, assert_data="[]")
            speller.check_status_code(response.status_code)

        def test_filtration_by_ru_language_en_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_EN_WORD, lang=data.RU)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_EN_WORD)
            speller.check_response(response.text, 's', data.VALID_EN_WORD)
            speller.check_status_code(response.status_code)

    # run with: pytest -n3 -m "filtration_en"
    @pytest.mark.filtration_en
    class TestLanguageEn():
        """ Check filtration by en language """

        def test_filtration_by_en_language_ru_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_RU_WORD, lang=data.EN)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_RU_WORD)
            speller.check_response(response.text, 's', data.VALID_RU_WORD)
            speller.check_status_code(response.status_code)

        def test_filtration_by_en_language_uk_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_UK_WORD, lang=data.EN)
            response = speller.check_text(json_object)
            speller.check_response(response.text, assert_data="[]")
            speller.check_status_code(response.status_code)

        def test_filtration_by_en_language_en_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_EN_WORD, lang=data.EN)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_EN_WORD)
            speller.check_response(response.text, 's', data.VALID_EN_WORD)
            speller.check_status_code(response.status_code)

    # run with: pytest -n3 -m "filtration_uk"
    @pytest.mark.filtration_uk
    class TestLanguageUk():
        """ Check filtration by uk language """

        def test_filtration_by_uk_language_ru_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_RU_WORD, lang=data.UK)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_RU_WORD)
            speller.check_response(response.text, 's', data.VALID_RU_WORD)
            speller.check_status_code(response.status_code)

        def test_filtration_by_uk_language_uk_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_UK_WORD, lang=data.UK)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_UK_WORD)
            speller.check_response(response.text, 's', data.VALID_UK_WORD)
            speller.check_status_code(response.status_code)

        def test_filtration_by_uk_language_en_word(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.INVALID_EN_WORD, lang=data.UK)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.INVALID_EN_WORD)
            speller.check_response(response.text, 's', data.VALID_EN_WORD)
            speller.check_status_code(response.status_code)

    # run with: pytest -n2 -m "word_with_digit"
    @pytest.mark.word_with_digit
    class TestWordWithDigit():
        """ Check that option 2 filtrate words with digits """

        def test_word_with_digit_without_opiton_2(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.WORD_WITH_DIGIT)
            response = speller.check_text(json_object)
            speller.check_response(response.text, 'word', data.WORD_WITH_DIGIT)
            speller.check_response(response.text, 's', data.VALID_EN_WORD)
            speller.check_status_code(response.status_code)

        def test_word_with_digit_with_opiton_2(self):
            speller = YandexSpellerApi()
            json_object = speller.create_json_for_request(content=data.WORD_WITH_DIGIT, options=data.OPTION_2)
            response = speller.check_text(json_object)
            speller.check_response(response.text, assert_data="[]")
            speller.check_status_code(response.status_code)

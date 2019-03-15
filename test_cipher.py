import pytest

from cipher import encrypt, decrypt, break_the_code

words = {'ala': 'ala', 'masz': 'masz', 'kot': 'kot', 'studenckie': 'studenckie', 'koło': 'koło', 'naukowe': 'naukowe'}


@pytest.mark.parametrize(
    "plaintext, shift, expected_result",
    [
        ("alu, masz kota?", 3, "dox, pdvc nrwd?"),
        ("studenckie kolo naukowe.", 18, "klmvwfucaw cgdg fsmcgow."),
    ],
)
def test_encrypt(plaintext, shift, expected_result):
    assert encrypt(plaintext, shift) == expected_result


@pytest.mark.parametrize(
    "plaintext, shift, expected_result",
    [
        ("dox, pdvc nrwd?", 3, "alu, masz kota?"),
        ("klmvwfucaw cgdg fsmcgow.", 18, "studenckie kolo naukowe."),
    ],
)
def test_decrypt(plaintext, shift, expected_result):
    assert decrypt(plaintext, shift) == expected_result


@pytest.mark.parametrize(
    "plaintext, expected_result, possibility",
    [
        ("dox, pdvc nrwd?", "alu, masz kota?", 33.33),
        ("klmvwfucaw cgdg fsmcgow.", "studenckie kolo naukowe.", 66.67),
    ],
)
def test_break(plaintext, expected_result, possibility):
    assert (
            break_the_code(plaintext, words)
            == f"Most possible match: {expected_result} - possibility = {possibility}%"
    )

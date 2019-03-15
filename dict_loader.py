import time

DICT_WITH_WORDS = {}


def load_words():
    """Loads words from slowa.txt."""
    try:
        with open("slowa.txt", "r") as f:
            for line in f:
                DICT_WITH_WORDS[line.rstrip().lower()] = line.rstrip().lower()
    except FileNotFoundError:
        print("Please make sure that slowa.txt file is in working directory.")
        pass


def load_words_with_varieties():
    """Loads words from odm.txt."""
    try:
        with open("odm.txt", "r") as f:
            for line in f:
                for word in line.split(","):
                    DICT_WITH_WORDS[word.rstrip().lower()] = word.rstrip().lower()
    except FileNotFoundError:
        print("Please make sure that odm.txt file is in working directory.")
        pass


def loader() -> dict:
    """
    Loads polish words from files to DICT_WITH_WORDS.

    Words will be used in cipher.break_the_code function to break cipher and show most possible match.
    :return: DICT_WITH_WORDS
    :rtype: dict
    """
    time_start = time.time()
    print("Loading words, please standby...")
    load_words()
    load_words_with_varieties()
    print(f"{len(DICT_WITH_WORDS.keys())} words loaded")
    time_end = time.time()
    print(f"Execution time: {round(time_end - time_start, 2)} seconds")
    return DICT_WITH_WORDS


if __name__ == "__main__":
    loader()

from win10toast import ToastNotifier
import more_itertools
import requests
import random
import time


def list_of_word():
    # list of words from api
    word_list = list(requests.get("https://www.mit.edu/~ecprice/wordlist.10000"))
    words = list()
    # Converting The Nested list to a Single list
    for i in word_list:
        n = str(i).split("\\n")
        n.remove(n[0])
        words.append(n)
    word = list(more_itertools.collapse(words))
    return word


def Translate():
    word_list = list_of_word()

    word = random.choice(word_list).strip("'")

    meaning = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    m = meaning.json()

    mean = m[0]["meanings"][0]["definitions"][0]["definition"]
    return word, mean


def notification():
    n = ToastNotifier()
    word, mean = Translate()
    while True:
        n.show_toast(
            "Time to larn!!",
            f"{word} : {mean}",
            duration=5,
            icon_path="alarm_alert_attention_bell_clock_notification_ring_icon_123203.ico",
        )
        time.sleep(60 * 60)


def main():
    notification()

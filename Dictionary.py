import json
from difflib import get_close_matches
import time

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes, or N if No: " % get_close_matches(w, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return 'The word does not exist. Please re-check it'
        else:
            return "We didn't understand your querry."
    else:
        return "The word does not exist. Please re-check it"


while True:
    word = input('If you want to stop the programm, write "exit"\nEnter word: ')
    if word == 'exit':
        break
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    time.sleep(0.3)

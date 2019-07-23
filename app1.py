import json
import difflib

from difflib import get_close_matches

data=json.load(open("dictionary.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s.If yes enter Y and If No enter N.:"%get_close_matches(word,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=='N':
            return "The word does not exist.Please double check it."
        else:
            return("We cannot understand your request")
    else:
        return"The word does not exit.Please double check it"

word=input("Enter the word:")

output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Type Y if yes and N if no: " % get_close_matches(word, data.keys(), cutoff=0.8)[
                0])
        if yn == "Y".lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N".lower():
            return "the word dosen't exist. please double check it."
        else:
            return "We didn't understand your entry. "
    else:
        return "The word Doesn't exist. Please double check it."


word = input("Enter A Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

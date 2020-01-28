import json
from difflib import get_close_matches

# from difflib import SequenceMatcher for finding possibilities in [0,1]

data = json.load(open("data.json"))

def translate(w):
    """ Give the meaning or explanations of the asked word

        The asked word will be Capitalize or translate to all Upper case if
        required to get the best possible match.

        This also use get_close_matches to give word that is the most close
        to the asked one, if that is not find in the dictionary.
    """
        
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input('Did you mean "%s" instead? Enter Y if yes or N if no: ' % get_close_matches(w,data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn.lower() == 'n':
            return "The word doesn't exists. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exists. Please double check it."


word = input("Enter word: ")
output = translate(word.lower())

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

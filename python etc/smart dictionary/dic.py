import json
from difflib import get_close_matches

data = json.load(open("data.json")) #data.json have all the data

def translate(word):
    word = word.lower()
    if word in data:
        return data[word] #return list with definitions
    elif word.title() in data: #if a word starts with capital letter
        return data[word.title()]
    elif word.upper() in data: #for acronyms, like USA
        return data[word.upper()]
    elif get_close_matches(word, data.keys()):
        return get_close_matches(word,data.keys())[0] #return string, get the top 1 match
    return "Error:" #string error

def get_definition():
    word = input("Write a word:")
    result = translate(word)
    if type(result) == list:
        return(format_definition(result))   
    else: #is string
        if "Error:" in result:
            return result
        else:
            yn = input("Did you mean %s? Enter Y if yes, or N if no: " %result)
            if yn.lower() == "y":
                return(format_definition(translate(result))) 
            else:
                return "Error: Word do not exist"

def format_definition(list):
    response = "Definition:\n"
    for item in list:
        response+= "- "+ str(item)+"\n"
    return response

print(get_definition())
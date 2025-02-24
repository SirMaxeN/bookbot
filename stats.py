def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for c in text.lower():
        if c in characters:
            characters[c] +=1
        else:
            characters[c] = 1
    return characters

def sort_key(dict):
    return dict["value"]

def single_key(dict):
    return {dict["name"]:dict["value"]}

def sort_dictionary(dict):
    output = []
    for key in dict:
        output.append({"name":key, "value":dict[key]})

    output.sort(reverse=True,key=sort_key)

    output = list(map(single_key, output))

    return output


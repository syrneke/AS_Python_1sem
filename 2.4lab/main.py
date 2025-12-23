#вар9

#а
def capitalize_words(text, separator=" "):
    words = text.split(separator)
    result = ""
    for word in words:
        result = result + word.capitalize() + separator
    return result[:-1] 

#б
def filter_elements(list1, list2, filter_function=None):
    result = []
    all_items = list1 + list2
    if filter_function is None:
        return all_items
    for item in all_items:
        if filter_function(item):
            result.append(item)
    return result

#в
def merge_dictionaries(*dicts): 
    result = {}
    for d in dicts:  
        for key in d:
            result[key] = d[key] 
    return result

#г
def unique_keys(*dicts):  
    result = {}
    counts = {}
    for d in dicts:
        for key in d:
            counts[key] = counts.get(key, 0) + 1
    for d in dicts:
        for key, value in d.items():
            if counts[key] == 1:
                result[key] = value
    return result

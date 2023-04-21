import re

def passwordchecker(password):

    uppercase_regex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
    lowercase_regex = re.compile(r'[abcdefghijklmnopqrstuvwxyz]')
    number_regex = re.compile(r'\d')
    special_regex = re.compile(r'\W')
    uppercase_check = uppercase_regex.search(password)
    lowercase_check = lowercase_regex.search(password)
    number_check = number_regex.search(password)
    special_check = special_regex.search(password)
    strong = ''
    if (uppercase_check == None) == True | (lowercase_check == None) == True | (number_check == None) == True | (
            special_check == None) == True:
        strong = 0
    elif len(password) < 8:
        strong = 0
    else:
        strong = 1
    return strong
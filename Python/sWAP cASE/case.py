def swap_case(s):
    new_string = ""
    for i in s:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string


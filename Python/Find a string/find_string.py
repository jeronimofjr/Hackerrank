def count_substring(string, sub_string):
    count = 0
    size_sub_string = len(sub_string)
    for  i in range(0, len(string)-size_sub_string+1):
        if sub_string == string[i:i + size_sub_string]:
             count += 1
    return count

string = input()
print(any([i.isalnum() for i in string]))
print(any([i.isalpha() for i in string]))
print(any([i.isdigit() for i in string]))
print(any([i.islower() for i in string]))
print(any([i.isupper() for i in string]))

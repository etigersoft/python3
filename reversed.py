word = str(input("Enter word to reverse: "))

# for a string using reversed function
print("Reversed function:")
print(list(reversed(word)))

# using a custom function
def reverse_string(word):
    out=""
    for i in range(len(word)):
        print(i)
        out += word[len(word) - i-1]
    return out

print("Custom function:") 
print(reverse_string(word))

# using a custom function from Platzy slices course 
# https://platzi.com/clases/1937-python/29638-trabajando-con-texto-slices/
def reverse_string_easy(word):
    return word[::-1]

print("Custom function easy:") 
print(reverse_string_easy(word))
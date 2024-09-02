def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower(): # convert to lower case to ignore case sensitivity
        if char in vowels:
            count += 1
    return count

# example
result = count_vowels("code challange")
print(result)

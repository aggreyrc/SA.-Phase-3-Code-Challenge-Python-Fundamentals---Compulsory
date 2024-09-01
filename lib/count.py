def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
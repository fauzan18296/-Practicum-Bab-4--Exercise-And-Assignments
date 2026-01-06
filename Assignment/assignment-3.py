def most_frequent_character(text, max_char = None, max_count = 0):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] > max_count:
            max_count = frequency[char]
            max_char = char

    return max_char, max_count


text = input("Masukkan kalimat: ")

character, count = most_frequent_character(text)
print(f"Karakter terbanyak: '{character}' muncul {count} kali")

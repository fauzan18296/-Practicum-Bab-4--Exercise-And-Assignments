check_palindrome = lambda text: text.replace(" ", "").lower()  if text == text[::-1] else "bukan Palindrom"

text1 = input("Masukkan teks pertama: ")
text2 = input("Masukkan teks kedua: ")

print(f'"{text1}" adalah Palindrom') if check_palindrome(text1) else print(f'"{text1}" bukan Palindrom')

print(f'"{text2}" adalah Palindrom') if check_palindrome(text2) else print(f'"{text2}" bukan Palindrom')
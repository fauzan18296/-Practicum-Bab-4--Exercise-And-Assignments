count_character = lambda text: len(text.strip().split())

letter = input("Masukkan sebuah kalimat: ")

amount = count_character(letter)
print("Jumlah kata:", amount)
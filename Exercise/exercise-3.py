SYMBOLS = '{}()[].,:;+-*/&|<>=~!?'
letter = input("Masukan pesan: ")
sentence = ""
for element in letter:
          if element not in SYMBOLS:
                    sentence += element
print(sentence)
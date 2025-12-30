letter = input("Masukan pesannya: ")
found_char_num = ""
for found_number in letter:
          if found_number.isdigit():
                    found_char_num += found_number
found_result = int(found_char_num)
print(found_char_num)
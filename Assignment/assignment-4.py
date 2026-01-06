remove_line = int(input("Masukkan nomor baris yang ingin dihapus: "))

with open("data.txt", "r") as file:
    line = file.readlines()

with open("data.txt", "w") as file:
    for i in range(len(line)):
        if i != remove_line - 1:
            file.write(line[i])

print(f"Baris ke-{remove_line} berhasil dihapus.")
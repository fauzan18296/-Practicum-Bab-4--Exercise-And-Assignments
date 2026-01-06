import csv

boundary_value = int(input("Masukkan batas nilai: "))

with open("nilai.csv", newline="") as file:
    reader = csv.DictReader(file)

    print("Mahasiswa dengan nilai di atas", boundary_value, ":")

    for row in reader:
        if int(row["Nilai"]) > boundary_value:
            print(row["Nama"])

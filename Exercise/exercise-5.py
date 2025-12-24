import datetime as dt
date = dt.datetime.now()
with open("datenotes.txt", "a") as file:
          file.write(f"{date.strftime("%d-%m-%Y, %H:%M:%S")}\n")
          print("Waktu dan tanggal telah berhasil dibuat pada file datenotes!!")
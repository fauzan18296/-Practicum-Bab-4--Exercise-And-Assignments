filenames = ["file1.txt", "file2.txt"]
with open("gabungan.txt", "w") as outfile:
          for filename in filenames:
                    with open(filename) as infile:
                              for letter in infile:
                                        if outfile.write(letter):
                                                  print("File gabungan telah berhasil di buat!!")
filenames = ["file1.txt", "file2.txt"]
with open("gabungan.txt", "w") as outfile:
          for filename in filenames:
                    with open(filename) as infile:
                              for letter in infile:
                                        outfile.write(letter)
                                        print("File gabungan.txt telah berhasil di buat!!")
class FileReader:
    def __init__(self, dir):
        self.direction = dir

    def read(self):
        try:
            file = open(self.direction, "r")
            print(file.read())
        except:
            print("")

    def write(self, text):
        file = open(self.direction, "a")
        file.write("\n" + text)
        file.close()

    def count(self):
        file = open(self.direction, "r")
        line_count = 0
        word_count = 0
        for line in file:
            line = line.strip("\n")
            words = line.split()
            line_count += 1
            word_count += len(words)
        file.close()
        print("Number of lines:" + str(line_count - 1))
        print("Number of words:", word_count)

    def __add__(self, other):
        with open(self.direction) as file1:
            data = file1.read()
        with open(other) as file2:
            data2 = file2.read()
        data += "\n"
        data += data2

        with open(self.direction, "w") as fp:
            fp.write(data)

    def __str__(self):
        return self.direction


dir1 = "file.txt"
dir2 = "file2.txt"

file = FileReader(dir1)
file2 = FileReader(dir2)
file.write("Hello World")
file.read()
file.count()

file2.write("Hello MAYAMI")
file2.read()
file2.count()

file.__add__(file2.__str__())
file.read()
file.count()

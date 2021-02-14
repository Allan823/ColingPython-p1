import collections
import re
 
def main():
    filename1 = input("Введите имя текстового документа: ")
    filename2 = input("Введите имя результирующего файла: ")
    filename3 = input("Введите имя результирующего файла для именованных сущностей: ")
    with open(filename1) as fin, open(filename2, "w") as fout1, open(filename3, "w") as fout2:
        words = re.split(r"\W+", fin.read())
        counter = collections.Counter(words)
        print("Ключевые слова документа:", counter.most_common(5))
 
        for word in words:
            if not word.istitle():
                print(word, file = fout1)
            else:
                print(word, file = fout2)
 
if __name__ == "__main__":
    main()

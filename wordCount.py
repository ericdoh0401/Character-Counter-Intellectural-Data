# 한국어와 중국어 글짜 카운터

import os

# 파일이 들어가있는 폴더의 디렉토리
DIRECTORY = "c:/Users/16266/Desktop/temporary"

class krnWordCnt:
    def __init__(self):
        self.data = ""
        self.total = 0

    def memoryStorage(self, directory):
        with open(directory, 'r', encoding = 'utf-8') as file:
            for line in file.readlines():
                self.data += line.strip()
    
    def memoryCleaning(self):
        counter = 0
        for ch in self.data:
            holder = ord(ch)
            if holder >= 11810 and holder < 65279:
                counter += 1
        self.total += counter
        return str(counter)
    
    def dataCleaning(self):
        self.data = ""
    
    def ret_total(self):
        return str(self.total)


test1 = krnWordCnt()
list = os.listdir(DIRECTORY)
memory = []
for file in list:
    file_dir = os.path.join(DIRECTORY, file)
    test1.memoryStorage(file_dir)
    wordCnt = test1.memoryCleaning()
    memory.append([file, wordCnt])
    test1.dataCleaning()

# 나온 데이타값을 저장할 텍스트파일명
with open("data_storage3.txt", 'w') as file:
    for f, wc in memory:
        file.write("filename: {} \t # of unique characters: {} \n".format(f, wc))
    file.write("total # of unique characters: {}".format(test1.ret_total()))
# 介绍(Introduce)
这是一个python库。它是用来简化代码的。库中的代码十分工整。
This is a python lib.It is used to simplify the code.The code for the lib is neat.

## 安装 (Installation)
您应该使用“pip install PythonK”来下载这个库。
You should use: "pip install PythonK" to installation this lib.

## 使用示例(Usage examples)
#import libs
from PythonK import PK

#test json
json = {
    "data" : [
        1,
        2
    ]
}
#test csv
csv = [
    "1 11",
    "2 22"
]

#read file
print(PK.file.Read(r"D:\PK\text_test.txt", "UTF-8"))
#read json file
print(PK.file.json.Read(r"D:\PK\json_test.json"))
#read csv file
print(PK.file.csv.Read(r"D:\PK\csv_test.csv"))
#read csv file dict
print(PK.file.csv.Read(r"D:\PK\csv_test.csv", True))
#read bin file
print(PK.file.bin.Read(r"D:\PK\bin_test.bin"))
#file path
print(PK.file.Path())
#string to binary
print(PK.string.toBinary("NAK"))
#string to hexadecimal
print(PK.string.toHexadecimal("NAK"))
#binary to string
print(PK.binary.toString("010011100100000101001011"))
#binary to hexadecimal
print(PK.binary.toHexadecimal("010011100100000101001011"))
#hexadecimal to string
print(PK.hexadecimal.toString("4e414b"))
#hexadecimal to binary
print(PK.hexadecimal.toBinary("4e414b"))
#write file
PK.file.Write(r"D:\PK\text_test.txt", "1\n2\n3\n4\n5", "UTF-8", PK.type.COVER())
#write json file
PK.file.json.Write(r"D:\PK\json_test.json", json)
#write csv file
PK.file.csv.Write(r"D:\PK\csv_test.csv", csv)
#write bin file
PK.file.bin.Write(r"D:\PK\bin_test.bin", b"\x00\xFF\x10")
#create hash table
hash = PK.hash.hashtable()
#add hash value
hash.AddHashValue("S NAK E", "2025")
#detect hash value
print(hash.Detect("S NAK E", "2025"))
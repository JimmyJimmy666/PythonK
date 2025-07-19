import json
import pathlib
import inspect
import csv
import time
import urllib
import urllib.request

class PK():
    class type():
        def COVER():
            return "w"
        def JOIN():
            return "a"

    class file():
        class json():
            @staticmethod
            def Read(path):
                with open(path, "r", encoding="UTF-8") as f:
                    return json.load(f)
            @staticmethod
            def Write(path, jsonf):
                with open(path, "w", encoding="UTF-8") as f:
                    json.dump(jsonf, f, ensure_ascii=False, indent=4)

        class csv():
            @staticmethod
            def Read(path, dict=False):
                if dict == False:
                    with open(path, "r", encoding="UTF-8") as f:
                        return list(csv.reader(f))
                elif dict == True:
                    with open(path, "r", encoding="UTF-8") as f:
                        return list(csv.DictReader(f))
            @staticmethod
            def Write(path, csvf):
                with open(path, "w", newline="", encoding="UTF-8") as f:
                    csv.writer(f).writerows([[line] for line in csvf])

        class bin():
            @staticmethod
            def Read(path):
                with open(path, "rb") as f:
                    return f.read()
            @staticmethod
            def Write(path, text=""):
                with open(path, "wb") as f:
                    f.write(text)
                
        @staticmethod
        def Read(path, format="UTF-8"):
            with open(path, "r", encoding=format) as f:
                return f.read()
        @staticmethod
        def Write(path, text="", format="UTF-8", type="w"):
            with open(path, type, encoding=format) as f:
                f.write(text)
        @staticmethod
        def getPath():
            return pathlib.Path(inspect.stack()[1].filename).parent.resolve()
        
    class string():
        @staticmethod
        def toBinary(string):
            return "".join(format(ord(char), '08b') for char in string)
        @staticmethod
        def toHexadecimal(string):
            return string.encode('UTF-8').hex()
        
    class binary():
        @staticmethod
        def toString(string):
            return "".join([chr(int(string[i:i+8], 2)) for i in range(0, len(string), 8)])
        @staticmethod
        def toHexadecimal(string):
            return "".join([chr(int(string[i:i+8], 2)) for i in range(0, len(string), 8)]).encode('UTF-8').hex()
        
    class hexadecimal():
        @staticmethod
        def toString(string):
            return bytes.fromhex(string).decode('utf-8')
        @staticmethod
        def toBinary(string):
            return "".join(format(ord(char), '08b') for char in bytes.fromhex(string).decode('utf-8'))
        
    class time():
        @staticmethod
        def Get():
            return time.time()
        
    class hash():
        @staticmethod
        def CreateHashTable():
            return PK.hash.hashtable()
        class hashtable(dict):
            def AddHashValue(self, key, value):
                self[key] = PK.string.toHexadecimal(value)
            def Detect(self, key, value):
                return self[key] == PK.string.toHexadecimal(value)

    class url():
        @staticmethod
        def getUrl(url):
            return urllib.request.urlopen(url).read().decode("UTF-8")

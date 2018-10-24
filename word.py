import re
from collections import Counter

def many_words(file):
    with open(file,"r") as f:
        word=re.findall(r"[a-zA-Z]+",f.read())
        # 获取数量前3多的元素
        # Counter(word).most_common(3)
        for k, v in Counter(word).items():
            print("%s : %s"%(k,v))

if __name__=="__main__":
    many_words("word.txt")
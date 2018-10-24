"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
xxxx-xxxx-xxxx-xxxx
"""
import random,string
# 大小写字母 + 数字
CHAR=string.ascii_letters+string.digits
# 生成单个激活码
def single_code(length):
    code=""
    for x in range(length):
        i=random.randint(0,len(CHAR)-1)
        code+=CHAR[i]
    return "-".join(code[i:i+4] for i in range(0,len(code),4))
# 激活码长度 与 数量
def many_codes(length,num):
    codelist=[]
    count=0
    while True:
        code=single_code(length)
        # 去重复
        if code in codelist:
            count=count
        else:
            codelist.append(code)
            count+=1
        if count==num:
            break
    with open("codes.txt","w") as f:
        for x in codelist:
            f.write(x+"\n")


if __name__=="__main__":
    many_codes(16,200)
        

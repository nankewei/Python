"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
xxxx-xxxx-xxxx-xxxx
保存到 MySQL 关系型数据库中
"""
import random, string, mysql.connector
# 大小写字母 + 数字
CHAR = string.ascii_letters + string.digits


# 生成单个激活码
def single_code(length):
    code = ""
    for x in range(length):
        i = random.randint(0, len(CHAR) - 1)
        code += CHAR[i]
    return "-".join(code[i:i + 4] for i in range(0, len(code), 4))


# 激活码长度 与 数量
def many_codes(length, num):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="study",
        user="root",
        password="113470",
        charset="utf8",
        # 启动缓冲
        buffered=True)
    cursor = conn.cursor()
    sql = "select * from test"
    codelist = cursor.execute(sql)
    count = 0
    while True:
        code = single_code(length)
        # 去重复
        if codelist != None and code in codelist:
            count = count
        else:
            sql = "insert into test(code) values(%s)"
            # 以元组形式传递
            cursor.execute(sql, (code, ))
            count += 1
        if count == num:
            break
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    many_codes(16, 200)

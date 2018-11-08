'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os

def how_many_lines(path="."):
    blank_lines, code_lines, comment_lines, total_lines = 0, 0, 0, 0
    for x in os.listdir(path):
        x = os.path.join(path, x)
        if os.path.isdir(x):
            how_many_lines(x)
        if os.path.isfile(x) and os.path.splitext(x)[1] == ".py":
            with open(x, "r", encoding="utf-8") as f:
                print(x)
                while True:
                    line = f.readline()
                    total_lines += 1
                    if not line:
                        break
                    elif line.strip().startswith("#"):
                        comment_lines += 1
                    elif line.strip().startswith("'''") or line.strip().startswith('"""'):
                        comment_lines += 1
                        # 如果 '''  or """ 数量为 1 则 则表示注释分多行， 否则注释为一行（一对三引号在同一行）
                        if line.count("'''") == 1 or line.count('"""') == 1:
                            # 读取下一行
                            while True:
                                line = f.readline()
                                total_lines += 1
                                comment_lines += 1
                                if "'''" in line or '"""' in line:
                                    break
                    elif line.strip():
                        code_lines += 1
                    else:
                        blank_lines += 1
                # while 会读取到代码总行数的下一行，所以要减 1
                print('the number of totalines is : ' + str(total_lines - 1))
                print('the number of comments is : ' + str(comment_lines))
                print('the number of codelines is : ' + str(code_lines))
                print('the number of blanklines is : ' + str(blank_lines))
                blank_lines, code_lines, comment_lines, total_lines = 0, 0, 0, 0


if __name__ == "__main__":
    how_many_lines()

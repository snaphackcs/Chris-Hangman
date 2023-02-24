

import re

file = input("输入字典文件名称：")
while True:
    try:
        fp = open(file, 'r', encoding='utf-8')
        print("文件打开成功ヾ(≧▽≦*)o\n\n===================================")
        break
    except Exception as e:
        print("文件打开失败：{}".format(e))
        file = input("输入字典文件名称：")

while True:
    try:
        vocab_len = int(input("输入单词长度："))
    except Exception as e:
        print("输入错误：{}".format(e))
        continue

    pattern_list = ['.'] * vocab_len
    while True:
        print("\n现在知道的字母：{}".format(''.join(pattern_list).replace('.', '_')))
        char_add = input("输入猜中的字母：")
        while len(char_add) != 1:
            print("只要一个字母就够啦(￣_￣|||)")
            char_add = input("输入猜中的字母：")

        while True:
            try:
                idx_add = input("输入这个单词在字典文件中的位置：").split(' ')
                for idx in range(len(idx_add)):
                    if int(idx_add[idx]) <= vocab_len:
                        idx_add[idx] = int(idx_add[idx])-1
                    else:
                        idx_add.clear()
                        break
                
                if input("确定替换吗？(。・ω・。)[y?]: ").lower() != 'y':
                    idx_add.clear()
                if len(idx_add) == 0:
                    continue
                for i in idx_add:
                    pattern_list[i] = char_add
                print("好耶！一个单词猜中了！ヾ(≧▽≦*)o\n\n===================================")
                break
            except Exception as e:
                print("输入错误：{}\n\n===================================".format(e))
        pattern = re.compile(''.join(pattern_list))

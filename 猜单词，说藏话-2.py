

import re


def foo(pattern):
    def bar(s):
        if re.match(pattern, s):
            return True
        return False
    return bar


file = input("输入字典文件名称：")
while True:
    try:
        fp = open(file, 'r', encoding='utf-8')
        print("文件打开成功ヾ(≧▽≦*)o\n\n===================================")
        break
    except Exception as e:
        print("文件打开失败：{}".format(e))
        file = input("输入字典文件名称：")
lst = fp.readlines()

while True:
    try:
        vocab_len = int(input("输入单词长度："))
    except Exception as e:
        print("输入错误：{}".format(e))
        continue

    pattern_list = ['[a-z]'] * vocab_len
    while True:
        print("\n现在知道的字母：{}".format(
            ''.join(['_' if i == '[a-z]' else i for i in pattern_list])))
        char_add = input("输入猜中的字母：").lower()
        while len(char_add) != 1 and not char_add.isalpha():
            print("只要一个字母就够啦(￣_￣|||)")
            char_add = input("输入猜中的字母：").lower()

        while True:
            try:
                idx_add = input("输入这个单词在字典文件中的位置：").split(' ')
                new_idx = []
                for idx in idx_add:
                    idx = int(idx)
                    if idx > vocab_len:
                        print("单词没有这么长哦：{} (。・ω・。)".format(vocab_len))
                        new_idx.clear()
                        break
                    elif idx < 0:
                        print("索引不能是负数啦：{} (￣_￣|||)".format(vocab_len))
                        new_idx.clear()
                        break
                    new_idx.append(idx-1)

                if len(idx_add) == 0:
                    print("不替换啦，索引位置不对")
                    continue

                if input("确定替换吗？(。・ω・。)[y?]: ").lower() != 'y':
                    new_idx.clear()
                if len(idx_add) == 0:
                    print("不替换啦，")
                    continue
                for i in new_idx:
                    pattern_list[i] = char_add

                print("好耶！一个字母猜中了！ヾ(≧▽≦*)o\n\n===================================")
                break
            except Exception as e:
                print("输入错误：{}\n\n===================================".format(e))
                continue

        pat = str(''.join(pattern_list))
        pattern = re.compile(pat+r"\s")
        regex = foo(pattern)
        print("找到了这些单词")
        for i in filter(regex, lst):
            print(f"- {i}", end='')

        if pat.isalpha():
            print("答案是：{}".format(pat))
            break

    if input("继续吗？").lower() != 'y':
        break

# Day_03_01_file.py
# 폴더 : Data

def read_1(filename):
    f = open(filename, 'r', encoding='utf-8')

    lines = f.readlines()
    # print(lines)

    # for line in lines:
    #     # print(line, end='')
    #     print(line.strip())

    # strip : 문자열 양 끝에 있는 공백들 제거
    f.close()
    return ''.join(lines)

def read_2(filename):
    f = open(filename, 'r', encoding='utf-8')

    while True:
        line = f.readline()
        # if len(line) == 0:
        if not line:
            break
        print(line.strip())

    f.close()

def read_3(filename):
    f = open(filename, 'r', encoding='utf-8')

    for line in f:
        print(line.strip())

    f.close()

def read_4(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # print(line.strip())
            lines.append(line.strip())

        # f.close()
    return lines

# 경로(path) : 상대경로, 절대경로
# filename = './Data/poem.txt'
# filename = '../snu/Data/poem.txt'
filename = 'Data/poem.txt'
# lines = read_4(filename)
# print(lines)

# text_all = read_1(filename)
# print(text_all)

def write():
    f = open('Data/write.txt', 'w', encoding='utf-8')
    f.write('hello\n')
    f.write('python' + '\n')
    f.write('welcome')
    f.write('\n')
    f.close()

write()

# strip 사용법
# temp = '\t\t\n\n  apple koong  \n\n\t\t'
# print('[{}]'.format(temp))
# temp = temp.strip()
# print('[{}]'.format(temp))

# split, join 사용법
# a = 'AA,BB,CC'
# b = a.split(',')
# print(b)
# c = ''.join(b)
# print(c)
# d = ':'.join(b)
# print(d)




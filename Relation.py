# 获得元素集合，列表类型
X = input('请输入元素集合，以“,”分割: ').split(',')
if X == ['']:
    print('ERROR！元素集合为空！')
    exit(1)
    pass
x = []
chars = []
for i in range(26):
    chars.append(chr(ord('a') + i))
    chars.append(chr(ord('A') + i))
    pass
# 标记是否为字母集合
flag = 1
for i in X:
    if i in chars:
        x.append(i)
        flag = 0
    else:
        x.append(eval(i))
    pass
X = x

# 获得关系集合，列表类型，类表中每一个为元组类型
R = input('请输入关系集合，以“ ”分割，形如（X,Y）: ').split(' ')
if R == ['']:
    print('ERROR！关系集合为空！')
    exit(1)
    pass
r = []
for i in R:
    if flag == 1:
        r.append(eval(i))
    else:
        # 当为字母集合时，特殊处理
        r.append((i[1], i[3]))
    pass
R = r

print(X)
print(R)

# 生成关系矩阵
T = []
for i in range(len(X)):
    T.append([])
    for j in range(len(X)):
        if (X[i], X[j]) in R:
            T[i].append(1)
        else:
            T[i].append(0)
        pass
    pass

for i in range(len(X)):
    for j in range(len(X)):
        print(T[i][j], end='')
        pass
    print()
    pass


# 判断自反性
flag_0 = 1
for i in range(len(X)):
    for j in range(len(X)):
        if i == j:
            if T[i][j] == 0:
                flag_0 = 0
                break
        pass
    pass
if flag_0 == 1:
    print('具有自反性')

# 判断反自反性
flag_1 = 1
for i in range(len(X)):
    for j in range(len(X)):
        if i == j:
            if T[i][j] == 1:
                flag_1 = 0
                break
        pass
    pass
if flag_1 == 1:
    print('具有反自反性')

# 当两种都不是时
if flag_0 == 0 and flag_1 == 0:
    print('既不具有自反性，也不具有反自反性')


# 判断关系矩阵是否全零
flag_T = 1
for i in range(len(X)):
    for j in range(len(X)):
        if T[i][j] == 1:
            flag_T = 0
            break
        pass
    pass

# 判断对称性
flag_0 = 1
for i in range(len(X)):
    for j in range(len(X)):
        if i != j:
            if T[i][j] != T[j][i]:
                flag_0 = 0
                break
        pass
    pass
if flag_T == 0 and flag_0 == 1:
    print('具有对称性')

# 判断反对称性
flag_1 = 1
for i in range(len(X)):
    for j in range(len(X)):
        if i != j:
            if T[i][j] == T[j][i]:
                flag_1 = 0
                break
        pass
    pass
if flag_T == 0 and flag_1 == 1:
    print('具有反对称性')

# 当两种都不是时
if flag_T == 0 and flag_0 ==0 and flag_1 == 0:
    print('既不具有对称性，也不具有反对称性')
# 当关系矩阵全零时
if flag_T ==1:
    print('既有对称性，也有反对称性')


# 判断是否具有传递性
flag = 1
for i in range(len(X)):
    for j in range(len(X)):
        for k in range(len(X)):
            if flag == 1:
                if (X[i], X[j]) in R and (X[j], X[k]) in R:
                    if (X[i], X[k]) in R:
                        flag = 1
                    else:
                        flag = 0
                        break
                else:
                    flag = 1
            pass
        pass
    pass
if flag == 1:
    print('具有传递性')
else:
    print('不具有传递性')

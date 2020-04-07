zushu = int(input("请输入组数："))

s = 0
for i in range(zushu):
    hangshu = int(input("请输入行数："))
    for j in range(hangshu):
        coor = [int(i) for i in input().strip().split()]
        s+=(coor[2]-coor[0]+1)*(coor[3]-coor[1]+1)
        coor = []
    print(s)
    s = 0


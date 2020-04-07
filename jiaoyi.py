zushu = int(input("请输入组数："))

group = []
total = 0
for i in range(zushu):
    coor = [int(x) for x in input("请输入交易后第i个朋友的硬币数：").strip().split()]
    group.append(coor)

for j in range(zushu):
    hang = group[j]
    total = sum(hang)
    if total%5 == 0 and total!=0:
        print(int(total/5))
    else:
        print(-1)
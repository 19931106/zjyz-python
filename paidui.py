zushu = int(input("zushu"))

group = []
for i in range(zushu):
    coor = [int(x) for x in input("rgbshu").strip().split()]
    group.append(coor)

for j in range(zushu):
    rgb_coor = group[j]
    rgb_coor.sort()
    if (rgb_coor[0]+rgb_coor[1])*2 < rgb_coor[2]:
        res = rgb_coor[0] + rgb_coor[1]
    else:
        res = sum(rgb_coor)//3
    print(res)


from decimal import *

n = list(map(Decimal, input().split()))
# ex) 0, 0, 0, 1, 1, 0 -> 차례로 A, B, C의 좌표

def dist(a, b): # 두 점 사이의 거리
    return ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])).sqrt()

a, b, c = (n[0], n[1]), (n[2], n[3]), (n[4], n[5])
l1, l2, l3 = dist(b, c), dist(a, c), dist(a, b)

if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]): # 기울기가 동일/평행사변형이 될 수 없다
    print(-1)

else:
    l_list = [l1, l2, l3]
    print((max(l_list) - min(l_list)) * 2)
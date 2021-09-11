n = str(input())

index = len(n) // 2

n1 = n[:index]
n2 = n[-index:]

sum1 = 0
sum2 = 0
for i in range(index):
    sum1 += int(n1[i])
    sum2 += int(n2[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

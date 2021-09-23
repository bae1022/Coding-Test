s = input().split('-')
minus_n = []

for i in range(len(s)):

    n = s[i].split('+')

    n_result = 0
    for j in range(len(n)):
        n_result += int(n[j])

    minus_n.append(n_result)

result = int(minus_n[0])
for i in range(1, len(minus_n)):
    result -= minus_n[i]

print(result)
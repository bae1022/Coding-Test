n = int(input()) # n개의 수로 이루어짐
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

max_num = -1000000001
min_num = 1000000001

def dfs(num, cnt, add, sub, mul, div):
    global max_num
    global min_num

    if cnt == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if add > 0:
        dfs(num + nums[cnt], cnt + 1, add - 1, sub, mul, div)

    if sub > 0:
        dfs(num - nums[cnt], cnt + 1, add, sub - 1, mul, div)

    if mul > 0:
        dfs(num * nums[cnt], cnt + 1, add, sub, mul - 1, div)

    if div > 0:
        if num < 0 and nums[cnt] > 0: # 음수를 양수로 나눌 때:
            temp = -num // nums[cnt]

            dfs(-temp, cnt + 1, add, sub, mul, div - 1)

        else:
            dfs(num // nums[cnt], cnt + 1, add, sub, mul, div - 1)


dfs(nums[0], 1, operators[0], operators[1], operators[2], operators[3])

print(max_num)
print(min_num)
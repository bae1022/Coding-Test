s = str(input())
t = str(input())

s_len = len(s)
t_len = len(t)

s_temp = s * t_len
t_temp = t * s_len

if s_temp == t_temp:
    print(1)
else:
    print(0)
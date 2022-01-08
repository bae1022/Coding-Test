keyboard = {'q': [0, 0],
            'w': [0, 1],
            'e': [0, 2],
            'r': [0, 3],
            't': [0, 4],
            'y': [0, 5],
            'u': [0, 6],
            'i': [0, 7],
            'o': [0, 8],
            'p': [0, 9],
            'a': [1, 0],
            's': [1, 1],
            'd': [1, 2],
            'f': [1, 3],
            'g': [1, 4],
            'h': [1, 5],
            'j': [1, 6],
            'k': [1, 7],
            'l': [1, 8],
            'z': [2, 0],
            'x': [2, 1],
            'c': [2, 2],
            'v': [2, 3],
            'b': [2, 4],
            'n': [2, 5],
            'm': [2, 6],
            }

answer = 0
sl, sr = map(str, input().split())

left_x = keyboard[sl][0]
left_y = keyboard[sl][1]
right_x = keyboard[sr][0]
right_y = keyboard[sr][1]

s = str(input())

for i in range(len(s)):
    key = keyboard[s[i]]

    key_x = key[0]
    key_y = key[1]

    if (key_x == 0 and 0 <= key_y <= 4) or (key_x == 1 and 0 <= key_y <= 4) or (key_x == 2 and 0 <= key_y <= 3):
        answer += (abs(left_x - key_x) + abs(left_y - key_y))

        left_x = key_x
        left_y = key_y

    else:
        answer += (abs(right_x - key_x) + abs(right_y - key_y))

        right_x = key_x
        right_y = key_y

    answer += 1

print(answer)
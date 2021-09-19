s = input()
s_cnt = [0 for _ in range(26)] # 알파벳의 개수 만큼

for i in s:
    s_cnt[ord(i) - 65] += 1 # ord() 는 아스키코드로 변환하는 함수

n = 0
odd_word = ''
word = ''
for i in range(26):
    if s_cnt[i] % 2 == 1: # 홀수개인 알파벳의 개수를 셈
        n += 1
        odd_word += chr(i + 65) # 홀수개인 알파벳을 저장

    word += chr(i + 65) * (s_cnt[i] // 2)

if n > 1:
    print("I'm Sorry Hansoo")
else:
    print(word + odd_word + word[::-1]) #word[::-1]: 배열을 역순으로 출력하는 방법 중 하나
def solution(phone_book):

    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        t = len(str(phone_book[i]))
        if str(phone_book[i]) == str(phone_book[i + 1])[0:t]:
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["1234", "1235", "567"]))
print(solution(["934793", "34", "44", "9347"]))
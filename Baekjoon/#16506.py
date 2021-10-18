n = int(input())

def binary(n, leng):
    nums = []
    answer = ''

    while n != 0:
        a = n % 2
        n = n // 2
        nums.append(a)

    for i in range(-1, -len(nums) - 1, -1):
        answer += str(nums[i])

    cnt = 0
    if len(answer) < leng:
        cnt = leng - len(answer)

        answer = '0' * cnt + answer

    return answer

for _ in range(n):
    answer = ''

    n1, n2, n3, n4 = map(str, input().split()) # opcode rD rA rB 또는 opcode rD rA #C

    rD = binary(int(n2), 3)
    rA = binary(int(n3), 3)
    rB = binary(int(n4), 3)
    rC = binary(int(n4), 4)

    if n1 == 'ADD' or n1 == 'ADDC':
        opcode = '0000'
        answer += opcode

        if n1 == 'ADD':
            op_type = 0

        elif n1 == 'ADDC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'SUB' or n1 == 'SUBC':
        opcode = '0001'

        answer += opcode

        if n1 == 'SUB':
            op_type = 0

        elif n1 == 'SUBC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'MOV' or n1 == 'MOVC':
        opcode = '0010'

        answer += opcode

        if n1 == 'MOV':
            op_type = 0

        elif n1 == 'MOVC':
            op_type = 1

        answer += str(op_type) + '0' + rD + '000'

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'AND' or n1 == 'ANDC':
        opcode = '0011'

        answer += opcode

        if n1 == 'AND':
            op_type = 0

        elif n1 == 'ANDC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'OR' or n1 == 'ORC':
        opcode = '0100'

        answer += opcode

        if n1 == 'OR':
            op_type = 0

        elif n1 == 'ORC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'NOT':
        opcode = '0101'

        answer += opcode

        op_type = 0

        answer += str(op_type) + '0' + rD + '000'

        answer += rB + '0'

    elif n1 == 'MULT' or n1 == 'MULTC':
        opcode = '0110'

        answer += opcode

        if n1 == 'MULT':
            op_type = 0

        elif n1 == 'MULTC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'LSFTL' or n1 == 'LSFTLC':
        opcode = '0111'

        answer += opcode

        if n1 == 'LSFTL':
            op_type = 0

        elif n1 == 'LSFTLC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'LSFTR' or n1 == 'LSFTRC':
        opcode = '1000'

        answer += opcode

        if n1 == 'LSFTR':
            op_type = 0

        elif n1 == 'LSFTRC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'ASFTR' or n1 == 'ASFTRC':
        opcode = '1001'

        answer += opcode

        if n1 == 'ASFTR':
            op_type = 0

        elif n1 == 'ASFTRC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'RL' or n1 == 'RLC':
        opcode = '1010'

        answer += opcode

        if n1 == 'RL':
            op_type = 0

        elif n1 == 'RLC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    elif n1 == 'RR' or n1 == 'RRC':
        opcode = '1011'

        answer += opcode

        if n1 == 'RR':
            op_type = 0

        elif n1 == 'RRC':
            op_type = 1

        answer += str(op_type) + '0' + rD + rA

        if op_type == 0:
            answer += rB + '0'

        elif op_type == 1:
            answer += rC

    print(answer)
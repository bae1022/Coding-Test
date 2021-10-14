def solution(enroll, referral, seller, amount):
    #enroll: 각 판매원의 이름
    # referral: 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름 배열
    # seller: 판매량 집계 데이터의 판매원 이름
    # amount: 판매량 집계 데이터의 판매 수량

    answer = [0] * len(enroll)
    graph_dict = dict(zip(enroll, range(len(enroll))))

    print(graph_dict)

    for i in range(len(seller)):
        man = seller[i]
        price = amount[i] * 100

        while True:
            node_num = graph_dict[man]
            div = price // 10
            answer[node_num] += price - div

            price = div
            man = referral[node_num]

            if man == "-": # 부모 노드가 없는 상태
                break
            if div == 0:
                break

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))


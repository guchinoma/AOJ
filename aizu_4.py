N = input()
a = []
answer_list = []

for i in range(N):
    a.append(map(int, raw_input().strip().split()))

for j in range(len(a)):
    number_1 = a[j][0]
    number_2 = a[j][1]
    number_3 = a[j][2]

    number_1_mul = number_1 ** 2
    number_2_mul = number_2 ** 2
    number_3_mul = number_3 ** 2

    if number_1_mul == number_2_mul + number_3_mul:
        print("YES")
    if number_2_mul == number_3_mul + number_1_mul:
        print("YES")
    if number_3_mul == number_1_mul + number_2_mul:
        print("YES")

    else:
        print("NO")
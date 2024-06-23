
N = int(input())


medidas = list(map(int, input().split()))


encontrou_queda = False
for i in range(1, N):
    if medidas[i] < medidas[i - 1]:
        print(i + 1)
        encontrou_queda = True
        break


if not encontrou_queda:
    print(0)


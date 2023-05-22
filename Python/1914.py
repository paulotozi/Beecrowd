N = int(input())

for _ in range(N):

    nomes = input().split()
    nums = input().split()

    soma = int(nums[0]) + int(nums[1])

    if(soma % 2 == 0):

        idx = nomes.index("PAR")

        print(nomes[idx - 1])

    elif(soma % 2 != 0):

        idx = nomes.index("IMPAR")

        print(nomes[idx - 1])
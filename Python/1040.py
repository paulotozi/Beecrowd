N = input().split(" ")
n1, n2, n3, n4 = N
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((2 * n1) + (3 * n2) + (4 * n3) + (n4)) / 10

print("Media: {}".format("{:.1f}".format(media)))

if(media >= 7.0):

    print("Aluno aprovado.")

elif(media >= 5.0 and media <= 6.9):

    print("Aluno em exame.")
    not_ex = float(input())
    print("Nota do exame: {}".format("{:.1f}".format(not_ex)))

    med_final = (media + not_ex) / 2

    if(med_final >= 5):

        print("Aluno aprovado.")
        print("Media final: {}".format("{:.1f}".format(med_final)))

    elif(med_final < 5):

        print("Aluno reprovado.")

elif(media < 7):

    print("Aluno reprovado.")

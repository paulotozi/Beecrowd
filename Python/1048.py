S = float(input())

if(S <= 400):

    new_S = S * 0.15
    print("Novo salario: {:.2f}".format(S + new_S))
    print("Reajuste ganho: {:.2f}".format(new_S))
    print("Em percentual: 15 %")

if(S > 400 and S <= 800):

    new_S = S * 0.12
    print("Novo salario: {:.2f}".format(S + new_S))
    print("Reajuste ganho: {:.2f}".format(new_S))
    print("Em percentual: 12 %")

if(S > 800 and S <= 1200):

    new_S = S * 0.10
    print("Novo salario: {:.2f}".format(S + new_S))
    print("Reajuste ganho: {:.2f}".format(new_S))
    print("Em percentual: 10 %")

if(S > 1200 and S <= 2000):

    new_S = S * 0.07
    print("Novo salario: {:.2f}".format(S + new_S))
    print("Reajuste ganho: {:.2f}".format(new_S))
    print("Em percentual: 7 %")

if(S > 2000):

    new_S = S * 0.04
    print("Novo salario: {:.2f}".format(S + new_S))
    print("Reajuste ganho: {:.2f}".format(new_S))
    print("Em percentual: 4 %")
def faktorial(n):
    vysledok = 1
    for i in range(2, n + 1):
        vysledok *= i
    return vysledok

pokus = faktorial(10)
print(pokus)


def kombCislo(n,k):
    return faktorial(n) // (faktorial(k) * faktorial(n - k))

cislo = kombCislo(n=10, k=2)
print(cislo)


def PaStroj(velkost):
    for riadok in range(velkost):
        for cislo in range(0, riadok + 1):
            print(kombCislo(riadok, cislo), end=" ")
        print()

PaStroj(5)

from listaPrimos import NmrPrimos, NaoPrimo, PrimosEPalindromo, NaoPalindromo

a = NmrPrimos()
b = NaoPrimo()
c = PrimosEPalindromo()
d = NaoPalindromo()


def primo(numero: str):
    listaDePrimos = a.getList()
    listaDeNaoPrimos = b.getList()

    if str(numero) in listaDePrimos:
        return True

    if str(numero) in listaDeNaoPrimos:
        return False
    numero = int(numero)
    if numero > 1:

        for i in range(2, numero):

            if (numero % i) == 0:
                b.addToList(str(numero))
                return False
            # else:
            #     primo(i)
        else:
            a.addToList(str(numero))
            return True

    else:
        return False


# def palindromo(numero: int, digitos: int):
def palindromo(numero: str):
    listaDePalindromos = c.getList()
    listaDeNaoPalindromos = d.getList()
    # nmrAux = str(numero)
    # qtdNmr = len(nmrAux)
    nmrPalindromo = None
    # while qtdNmr >= digitos:
    # print(len(str(numero)))
    # if len(str(numero)) == 8:
    #     print(numero)
    if str(numero) in listaDeNaoPalindromos:
        d.addToList(numero)
    elif str(numero) in listaDePalindromos and primo(numero):
        nmrPalindromo = numero

    # elif primo(numero):
    elif int(numero) == int(str(numero)[::-1]):

        # if numero == int(str(numero)[::-1]):
        if primo(numero):
            c.addToList(numero)
            nmrPalindromo = numero
        else:
            ...
    else:
        d.addToList(numero)

    return nmrPalindromo

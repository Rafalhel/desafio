import csv


class NmrPrimos:
    def __init__(self):
        self.nome = 'primos.csv'
        self.lista = []
        self.primos = []
        self.nmr = None

    def getList(self):
        try:
            with open(self.nome, 'r') as arq:
                reader = csv.reader(arq)
                lista = []
                for i in reader:
                    # print(i[0])
                    lista.append(i[0])
                self.lista = lista
        except FileNotFoundError:
            ...
            # print(f'Arquivo {self.nome.replace(".csv", "")} não encontrado!')
        return self.lista

    def addToList(self, nmr: str):
        self.nmr = nmr
        a = self.getList()
        if str(self.nmr) not in a:
            self.lista.append(str(self.nmr))
            with open(self.nome, 'w') as arq:
                writer = csv.writer(arq, lineterminator='\r')
                # self.lista.sort()
                for i in self.lista:
                    i = str(i)
                    writer.writerow([i])
            # print(f'Arquivo {self.nome.replace(".csv", "")} atualizado!')


class NaoPrimo(NmrPrimos):
    def __init__(self):
        super().__init__()
        self.nome = 'naoPrimos.csv'
        self.lista = []
        self.primos = []


class NaoPalindromo(NmrPrimos):
    def __init__(self):
        super().__init__()
        self.nome = 'naoPalindromo.csv'
        self.lista = []
        self.primos = []


class PrimosEPalindromo(NmrPrimos):
    def __init__(self):
        super().__init__()
        self.nome = 'primosEPalindromo.csv'
        self.lista = []
        self.primos = []

    # def addToList(self, nmr: int):
    #     self.nmr = nmr
    #     a = self.getList()
    #     if str(self.nmr) not in a:
    #         self.lista.append(str(self.nmr))
    #         with open(self.nome, 'w') as arq:
    #             writer = csv.writer(arq, lineterminator='\r')
    #             self.lista.sort()
    #             for i in self.lista:
    #                 i = str(i)
    #                 writer.writerow([i])
    #         try:
    #             notificacao().notificar('Palindromo', f'Palindromo encontrado: {self.nmr}')
    #         except Exception as e:
    #             print(f'Notificação deu erro {e}')
    #         print(f'Arquivo {self.nome.replace(".csv", "")} atualizado!')

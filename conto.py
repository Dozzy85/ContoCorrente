class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.saldo = importo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.saldo)


c1 = ContoCorrente("Alessandro", "10", 2000)
c2 = ContoCorrente("Susanna", "20", 5000)

c1.descrizione()
c2.descrizione()

c1.deposita(500)
c1.descrizione()

c2.preleva(200)
c2.descrizione()
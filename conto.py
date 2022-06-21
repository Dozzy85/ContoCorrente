#La classe Conto è una super classe
class Conto:
    def __init__(self, nome, conto):
        self.nome=nome
        self.conto=conto

#Classe ContoCorrente è una sotto classe della classe Conto
class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome,conto)
        self.__saldo = importo

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    #property per la lettura del dato reso "privato" tramite le __
    @property
    def saldo(self):
        print("Sono dentro getter")
        return self.__saldo

    # property per la scrittura del dato reso "privato" tramite le __
    @saldo.setter
    def saldo(self,importo):
        print("Sono dentro setter")
        self.preleva(self.__saldo)
        self.deposita(importo)

#Classe per avere dei metodi che possa essere invocato direttamente nelle classi senza invocare istanze
class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente,destinazione,importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


c1=ContoCorrente("Alessandro","10",2000)
c2=ContoCorrente("Susanna","20",5000)
c1.descrizione()
c2.descrizione()

GestoreContiCorrenti.bonifico(c1,c2,500)
c1.descrizione()
c2.descrizione()

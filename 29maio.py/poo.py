class Anny:
    def __init__(self, estudando=False, dormindo=False, maquiando=False, comendo=False):
        self.estudando = estudando
        self.dormindo = dormindo
        self.maquiando = maquiando
        self.comendo = comendo

    def estudar(self):
        self.estudando = True
        self.dormindo = False
        self.maquiando = False
        self.comendo = False
        print("Anny está estudando. Legal!")

    def dormir(self):
        self.estudando = False
        self.dormindo = True
        self.maquiando = False
        self.comendo = False
        print("Anny está dormindo. Zzzzzz...")

    def maquiar(self):
        self.estudando = False
        self.dormindo = False
        self.maquiando = True
        self.comendo = False
        print("Anny está se maquiando, ficou linda!")

    def comer(self):
        if self.dormindo:
            print("Anny não pode comer enquanto dorme!")
        else:
            self.comendo = True
            self.estudando = False
            self.maquiando = False
            print("Anny está comendo. Muito saboroso!")

    def status(self):
        status = {
            "estudando": self.estudando,
            "dormindo": self.dormindo,
            "maquiando": self.maquiando,
            "comendo": self.comendo
        }
        for atividade, estado in status.items():
            print(f"Anny está {atividade}: {estado}")

# Exemplo de uso:
anny = Anny()
anny.status()
anny.estudar()
anny.status()
anny.dormir()
anny.status()
anny.maquiar()
anny.status()
anny.comer()
anny.status()

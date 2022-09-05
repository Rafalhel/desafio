from win10toast import ToastNotifier

class notificacao:
    def __init__(self):
        self.toast = ToastNotifier()
    def notificar(self, titulo: str, mensagem: str):
        self.toast.show_toast(titulo, mensagem,  duration=20)
'217468389'
'883163882'
'git remote add origin https://github.com/Rafalhel/desafio'
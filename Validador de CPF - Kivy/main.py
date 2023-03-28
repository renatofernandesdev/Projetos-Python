# Desenvolvido por Renato Fernandes (renatofernandes.dev@gmail.com)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from collections import Counter

KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "Validador de CPF"
    Image:
        id: dice_state
        size_hint_y: 0.7
        size_hint_x: 0.7
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        source: "img\cpf.jpg"
    MDRaisedButton:
        text: "Validar"
        id: 'roll_button'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_release: app.validar()
    MDTextField:
        id: text_cpf
        hint_text: "CPF com 11 Dígitos"
        max_text_length: 11
        helper_text: "Insira o CPF"
        helper_text_mode: "persistent"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint_x: .4
    MDLabel:
        id: resultadopos
        text: ""
        pos_hint: {"center_y": 0.10}
        theme_text_color: "Custom"
        text_color: 0/255, 206/255, 5/255, 1
        halign: "center"
        font_style: "H4"
        bold: True
    MDLabel:
        id: resultadoneg
        text: ""
        pos_hint: {"center_y": 0.10}
        theme_text_color: "Error"
        halign: "center"
        font_style: "H4"
    MDLabel:
        id: resultadoinvalido
        text: ""
        pos_hint: {"center_y": 0.10}
        theme_text_color: "Custom"
        text_color: 0, 0, 2, 2
        halign: "center"
        font_style: "H4"
    MDLabel:
        id: dev
        text: "Developed by: Renato Fernandes"
        pos_hint: {"center_y": 0.03}
        theme_text_color: "Custom"
        text_color: 0, 0, 2, 2
        halign: "right"
'''

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)
    
    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def validar(self):
        cpf = self.kvs.ids.text_cpf.text
        if (cpf.isdigit() is False) or len(cpf) != 11: # Confere se a pessoa digitou 11 números.
            self.kvs.ids.resultadopos.text = ("")
            self.kvs.ids.resultadoneg.text = ("")
            self.kvs.ids.resultadoinvalido.text = ("Insira somente 11 números.")
        else:
            cpflist = list(cpf)
            icpflist = []
            validacao = 0
            validacao2 = 0
            count = [10, 9, 8, 7, 6, 5, 4, 3, 2]
            count2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

            #CRIA UMA LISTA DO CPF STRING PARA UMA LISTA DE INTEIROS
            for icpf in cpflist:
                icpflist.append(int(icpf))

            primeiravalidacao = icpflist[9] # Seta a chave da primeira validação com o 10º dígito do CPF.
            segundavalidacao = icpflist[10] # Seta a chave da primeira validação com o 11º dígito do CPF.

            #PRIMEIRA VALIDACAO
            validacao = [x*y for x,y in zip(count,icpflist)] # Multiplica as listas count * icountcpf.
            validacao = sum(validacao) # Soma os valores da lista validacao e retorna um valor inteiro.
            validacao = ( validacao * 10 ) % 11 # Resto da divisão ( Validação ).

            #SEGUNDA VALIDACAO
            validacao2 = [x*y for x,y in zip(count2,icpflist)] # Multiplica as listas count2 * icountcpf.
            validacao2 = sum(validacao2) # Soma os valores da lista validacao e retorna um valor inteiro.
            validacao2 = ( validacao2 * 10 ) % 11 # Resto da divisão ( validação ).

            #CASO RESTO DA VALIDAÇÃO SEJA 10 TROCAR PARA 0
            if validacao == 10:
                validacao = primeiravalidacao
            if validacao2 == 10:
                validacao2 = segundavalidacao

            #CONFERINDO SE ENTROU COM NUMEROS IGUAIS
            def todos_iguais(icpflist):
                c = Counter(icpflist)
                quantidade = list(c.values())[0]
                return quantidade == len(icpflist)

            #FINALIZACAO
            if todos_iguais(icpflist) == True:
                self.kvs.ids.resultadoinvalido.text = ("")
                self.kvs.ids.resultadopos.text = ("")
                self.kvs.ids.resultadoneg.text = ("CPF INVÁLIDO")
            else:
                if (validacao == primeiravalidacao and validacao2 == segundavalidacao):
                    self.kvs.ids.resultadoinvalido.text = ("")
                    self.kvs.ids.resultadoneg.text = ("")
                    self.kvs.ids.resultadopos.text = ("CPF VÁLIDO")              
                else:
                    self.kvs.ids.resultadoinvalido.text = ("")
                    self.kvs.ids.resultadopos.text = ("")
                    self.kvs.ids.resultadoneg.text = ("CPF INVÁLIDO")

ma = MainApp()
ma.run()
import fuzzy
import PySimpleGUI as sg

class Tela:
    vacantArray = []
    def __init__(self):
        layout = [
            [sg.Text('-------------------- Cadastro de Vaga --------------------------')],
            [sg.Text('Nome da vaga:', size=(25,0)), sg.Input(key='vacant_name',size=(10,0))],
            [sg.Text('Raciocínio lógico:', size=(25,0)), sg.Input(key='vacant_raisonnement',size=(10,0))],
            [sg.Text('Vigor físico:', size=(25,0)), sg.Input(key='vacant_physique',size=(10,0))],
            [sg.Text('Relacionamento com público:', size=(25,0)), sg.Input(key='vacant_public',size=(10,0))],
            [sg.Button('CadastrarVaga', size=(25,0))],
            [sg.Text('----------------------------------------------------------------')],
            [sg.Text('------------------ Formulário Candidato ------------------------')],
            [sg.Text('Raciocínio lógico:', size=(25,0)), sg.Input(key='vacant_raisonnement_form',size=(10,0))],
            [sg.Text('Vigor físico:', size=(25,0)), sg.Input(key='vacant_physique_form',size=(10,0))],
            [sg.Text('Relacionamento com público:', size=(25,0)), sg.Input(key='vacant_public_form',size=(10,0))],
            [sg.Button('Recomendar', size=(25,0))],
            [sg.Text('----------------------------------------------------------------')],
            [sg.Text('-------------------- Vagas cadastradas -------------------------')],
            [sg.Multiline(size=(30, 5), key='textbox')],
        ]

        self.window = sg.Window("fuzzy").layout(layout)

    def display(self):
        while True:
            self.button, self.values= self.window.Read()
            if self.button == sg.WIN_CLOSED:
               break
            if self.button == 'CadastrarVaga':
                vacant_name = str(self.values['vacant_name'])
                vacant_raisonnement = int(self.values['vacant_raisonnement'])
                vacant_physique = int(self.values['vacant_physique'])
                vacant_public = int(self.values['vacant_public'])
                Tela.vacantArray.append({ vacant_name ,vacant_raisonnement,vacant_physique,vacant_public})
                self.window['textbox'].update('Vaga : {name} | R : {vacant_raisonnement} | V : {vacant_physique}| P: {vacant_public}'.format(
                    name=vacant_name, 
                    vacant_raisonnement=vacant_raisonnement,
                    vacant_physique=vacant_physique,
                    vacant_public=vacant_public) + '\n', append=True)
            if self.button == 'Recomendar':
                vacant_raisonnement_form = int(self.values['vacant_raisonnement_form'])
                vacant_physique_form = int(self.values['vacant_physique_form'])
                vacant_public_form = int(self.values['vacant_public_form'])
                fuzzy.fuzzy(Tela.vacantArray,vacant_raisonnement_form,vacant_physique_form,vacant_public_form)

if __name__ == '__main__':        
    tela = Tela()
    tela.display()




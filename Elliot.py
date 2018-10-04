from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter

class Minhalogica(LogicAdapter):
    def __init__(self,  **kwargs):
        super(Minhalogica, self).__init__(**kwargs)
    def can_process(self, statement):
        return True

    def process(self, statement):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)
        # For this example, we will just return the input as output
        selected_statement = statement
        selected_statement.confidence = confidence
        return selected_statement



conversa0= ['oi', 'olá', 'tudo bem', 'sim e você?', 'Estou bem', 'que bom', 'qual seu nome', 'Elliot', 'você conhece o Mr. Robôt', 'O que você quer com ele ele não é confiavel' 'tchau']
bot = ChatBot(
    "Chippy", storage_adapter='chatterbot.storage.SQLStorageAdapter',
     logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'],
     database='./database.sqlite3')


bot.set_trainer(ListTrainer)
bot.train(conversa0)

chamar = input('Inicializar:  ')

while chamar == 'Elliot':
    quest = input('Você: ')
    resposta = bot.get_response(quest)

    if float(resposta.confidence) > 0.7:

        print('Elliot: ', resposta)


    elif quest == 'fechar':
        break

    else:
        print('Aprendendo...')

while chamar == 'Mr Robot':
    print("Scripts Desponivel: ", "Arping.txt", "-", "AtaqueMitm.txt", "-", "MonitorARP.txt", "-", "SMTPHACKING.txt", "-", "WebCrawler")
    quest2 = input('Digite Script com a extenção .txt: ')
    resposta = bot.get_response(quest2)
    if True:
        data = open(quest2, 'r')
        for line in data:
            print(line)
        data.close()
        break
    elif quest2 == '':
         break



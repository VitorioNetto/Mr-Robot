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


bot = ChatBot("Chippy", logic_adapters=["chatterbot.logic.BestMatch"])

conversa0= ['oi', 'olá', 'tudo bem', 'sim', 'tchau']
bot.set_trainer(ListTrainer)
bot.train(conversa0)

chamar = input('Inicializar:  ')

while chamar == 'Elliot':
#while True: #quest != 'tchau.':
    print("############################################################################################")
    quest = input('Você: ')

    resposta = bot.get_response(quest)
    if float(resposta.confidence) > 0.6:

        print('Elliot: ', resposta)


    elif quest == 'tchau':
         break
    else:

            resposta == quest
            print('Elliot: ', resposta)


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



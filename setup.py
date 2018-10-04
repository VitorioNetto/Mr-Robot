from distutils.core import setup
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter

include_files = ['database.sqlite3', 'Arping.txt', 'AtaqueMitm.txt', 'MonitorARP.txt', 'SMTPHACKING.txt', 'WebCrawler.txt']
setup(
    name='MR. Robot',
    version='0.1',
    licença = ' CIA ',
    install_requires = ['chatterbot'],
    url='hhtps://www.virtualinteligencia.com.br/cia',
    author='Vitorio Netto',
    author_email='nanointeligencia.cop@gmail.com',
    description='Simula o hacker Elliot e sua personalidade Mr robot',
    data_files = include_files,
    py_modules=['Elliot'],
    script=['Elliot'],

)

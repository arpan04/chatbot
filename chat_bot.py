from chatterbot import ChatBot  ## importing chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer  ##importing trainer from chatterbot library

import os

bot = ChatBot('jerry')    ##creating bot
trainer= ChatterBotCorpusTrainer(bot)

corpus_path="C:/Users/Arpan Pandey/english/"  ## defining the path to where the corpus data is stored in my pc

for files in os.listdir(corpus_path):
	trainer.train(corpus_path + files)   ##training the bot on corpus_data


while True:
	message =input('You: ')
	if message.strip() != 'bye':
		reply=bot.get_response(message)
		print('jerry :',reply)
	if message.strip() =="bye":
		print('jerry: Adios')
		break

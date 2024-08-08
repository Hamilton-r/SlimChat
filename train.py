from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')
lyrics = "/Users/rhamilton/Documents/lyrics/EMINEM/combined.txt"
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
trainer = ListTrainer(chatbot)
trainer.train(lyrics)
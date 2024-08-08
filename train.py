from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')
lyrics = "enter opath to .txt file containing lyrics you defined earlier"
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
trainer = ListTrainer(chatbot)
trainer.train(lyrics)

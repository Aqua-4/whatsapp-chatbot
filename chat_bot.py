# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:58:38 2019

@author: Parashar
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#import logging
from whatsapp_list import train_list


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
# logging.basicConfig(level=logging.ERROR)

chatbot = ChatBot('WhatsApp Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)


# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
# trainer2 = ListTrainer(chatbot)
# trainer2.train(train_list())

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:32:55 2019

@author: Parashar
"""

# Steps
"""
export whatsApp chato to text
change the variable and point to the file,
returns chatbot training type list
"""


def train_list():

    f_name = "WhatsApp Chat with Hrishikesh Dhatrak"
    to = "Hrishikesh Dhatrak: "
    me = "😈Parashar😇: "

    op = []
    f_ip = open("{}.txt".format(f_name), "r", encoding="utf8")
    for line in f_ip:
        res = line.split(to)[-1] if (to in line) else line.split(me)[-1]
        op.append(res[:-1])
    return op

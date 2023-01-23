import os
import re
import sys
import logging
from io import IOBase
import openai
from contextlib import redirect_stdout
import requests
from bs4 import BeautifulSoup
import datetime

me = "Ruben"
now = datetime.datetime.now()
openai.api_key = "PLACE YOUR API KEY HERE"



class Tee(IOBase):
    def __init__(self, file1, file2=sys.stdout):
        self.file1 = file1
        self.file2 = file2

    def write(self, data):
        self.file1.write(data)
        self.file2.write(data)





def chat_welcome():
    print(f"VOICE:\n\nHi {me}, I see you're feeling lonely again and you want to talk to somebody. Have you checked your phone for an open conversation yet? ")
    input1 = input()
    print(f"ME:\n\n{input1}")
    if input1 == "no":
        print("VOICE:\n\nPlease check your phone first. Maybe there's somebody who wants to talk to you.")
    elif input1 == "yes":
        print("VOICE:\n\nI'm sorry to hear that your feeling lonely. Before we talk, do you want me to record everything and send it to your Diary?")
        input1 = input()
        print(f"ME:\n\n{input1}")
        if input1 == "no":
            print("VOICE:\n\nOkay")
            status = 0
            chat()
        if input1 == "yes":
            print("VOICE:\n\nOk, I'll do that")
            status = 1
            chat()

def chat():
    active = True
    while active:
        input1 = input("Write something...\n")
        print(f"ME:\n\n{input1}")
        if "goodnight" in input1:
            print(f"VOICE:\n\nHave a good night {me}")
        else:
            yes



sys.stdout = Tee(open(f"C:/Users/user/OneDrive/Desktop/tagebuch/{now.date()}.txt", "w"))
chat_welcome()
sys.stdout.flush()
sys.stdout.close()





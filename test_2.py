# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:12:51 2020

@author: ANISH

"""
import speech_recognition as sr
import pyttsx3
import psycopg2
import eel

from gtts       import gTTS
from nltk       import word_tokenize
from functions  import *

x = 5
inp_yes = 'yes'
inp_no = 'no'
stop_words = ['i','want','to','order','and','some','would',\
    'like','go','visit','view']

eel.init('web')

# engine = pyttsx3.init('sapi5') 
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', voices[1].id)
# #inp0 = myCommand("Anythong else") 
    
#########ONLY FOR TESTING!######
##########SAME AS THE TRY BLOCK AFTER THIS######################
@eel.expose
def tryblock():
    conn,cur = db_connect()
    eel.left_printer("Do you know exactly what you want to buy?")
    speak("Do u know exactly what u want to buy ?")
    inp0 = inp_no
    #inp0 = myCommand("Do u know exactly what u want to buy ?")
    eel.right_printer(inp0.capitalize())

    if inp0 == inp_yes:
        known_item(conn,cur)
        
    else : 
        unknown_item(conn,cur)

###########DELETE ME^###########
################################
            
            
try:
    conn = psycopg2.connect(database="IVR_POS", user="postgres", password="hi", host="127.0.0.1", port="5432")

    
    n=4
    cur = conn.cursor()
    #speak("Do u know exactly what u want to buy ?")
    #inp0 = myCommand("Do u know exactly what u want to buy ?")

    speak("        Do u want a completely voice based system?")

    inp0 = inp_no
    # myCommand("Do u want a completely voice based system?")
    print(inp0)

    if inp0 == inp_yes:

        speak("Do u know exactly what u want to buy ?")
        #inp0 = myCommand("Do u know exactly what u want to buy ?")
        inp0 = inp_no
        print(inp0)
 
        complete_voice(cur,conn,inp0)
        

    else :
        eel.start('index.html', size=(540, 960))
    
        # inp0 = 'no'
        # #if inp0 = 'yes':
        # user_buy=[]
        # if inp0 == 'yes':
            
        #     item_printer(cur)
        #     speak("Choose an item please")
        #     inp = myCommand("Item name")
        #     inp = "britannia,milk,bread"
        #     user_buy.append(db_searcher(inp,cur,2))
        #     print(user_buy)

        # else : 
        #     parent_category_selector(cur)
        #     speak("Please Select a category from these")
            
        #     #inp1 = myCommand("Which category")
        #     inp1='bakery'
        #     print(inp1)
        #     stopword_remover(inp1)
            
        #     child_category_selector(cur,inp1.capitalize())
        #     speak("Please Select a sub category from these")
            
        #     #inp2 = myCommand("Which sub_category")
        #     inp2="bread"
        #     print(inp2)
        #     stopword_remover(inp2)
        #     item_selector(cur,inp2.capitalize())
            
        #     #inp3 = myCommand("Which item ?")
        #     inp3 = 'britannia milk bread'
        #     print(inp3)
        #     inp3 = word_tokenize(inp3)

        #     #stopword_remover(inp3)
        #     user_buy.append((db_searcher(inp3,cur,4)))
        #     print(user_buy)

    
    # for i in range(n):
    #     inp1 = input("Category") 
    #     inp2 = input("Sub_cat")
    #     inp3 = input("item")
    #     inp4 = int(input())
        
    #     user_buy.append(combiner(cur,inp1,inp2,inp3,inp4))
    #     print(user_buy)
    
    
except psycopg2.Error as e:
    print("I am unable to connect to the database")
    print (e)
    print (e.pgcode)
    print (e.pgerror)
    #print (traceback.format_exc())

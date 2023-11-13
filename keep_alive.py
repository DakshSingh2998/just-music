from flask import Flask
from threading import Thread
#Daksh

app=Flask('')
@app.route('/')
def home():
  return "I am Alive!!"

def run():
  app.run(host='0.0.0.0',port=8079)

def keep_alive():
  t=Thread(target=run)
  t.start()

import json

def save_user(data):
    with open("data/user.json","w")as f:
        json.dump(data,f,indent=4)

def save_transactions(transactions):
    with open("data/transactions.json","w") as f:
             json.dump(transactions,f,indent=4)

def load_user():
     with open("data/user.json","r")as f:
          return json.load(f) 
               
def load_transactions():
     with open("data/transactions.json","r")as f:
          return json.load(f)           

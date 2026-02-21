import json
import bank
import storage

from security import hash_Pin,verify_Pin

tries = 3
while tries > 0:
                     
 stored_hash = hash_Pin("2614")

 user_pin = input("Enter your PIN 🪪 :")

 if verify_Pin(user_pin,stored_hash):
    print(" Access Granted 🔓")
    break
                
 else:
    tries -=1
    print(f"Wrong PIN : Attempts {tries} left")
       
if tries == 0:
    print("Your Account has LOCKED")
    exit()


while True:
  with open("data/transactions.json","r") as f:
     transactions = json.load(f)
     
  
  with open("data/user.json","r") as f:
      data = json.load(f)
 
  user_account = input("Check Balance:1 🏛️\nWithdraw:2💸\nDeposit:3💸\nExit:4🏃\nTransaction-History:5\nChoice Option ⚙️:")

  if user_account == "1":
    with open("data/user.json","r") as f:
      data = json.load(f)
      print(f">>Balance:{data["Balance"]}<<\n")

   
  elif user_account == "2":
     amount = int(input("Amount to Withdraw 💵:")) 

     transactions = storage.load_transactions()

     data,new_transactions= bank.Withdraw(data,amount)

     if new_transactions:
      transactions.append(new_transactions)
       
     storage.save_user(data)
     storage.save_transactions(transactions)

  elif user_account == "3":
     amount = int(input("Amount to Deposit 💵:")) 

     transactions = storage.load_transactions()

     data,new_transactions= bank.Deposit(data,amount)

     if transactions:
      transactions.append(new_transactions)
     
     storage.save_user(data)
     storage.save_transactions(transactions)

 
  elif user_account == "4":
     print("Thanks For Using Our ATM 💵💰💳") 
     break

  elif user_account == "5":
     with open("data/transactions.json","r") as f:
        transactions = json.load(f)
        print(transactions)          




          
  


          


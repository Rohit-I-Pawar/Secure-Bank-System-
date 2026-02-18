import json

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
       
    with open("data/user.json","r") as f:
     data = json.load(f)
    if data["PIN"] == "":
     new_PIN = input("Enter new PIN:")
     data["PIN"] = hash_Pin(new_PIN)
        
     
     with open("data/user.json","w")as f:
        json.dump(data,f)

        print("PIN set SuccessFully") 
    
if tries == 0:
    print("Your Account has LOCKED")
    exit()


while True:
 user_account = input("Check Balance:1 🏛️\nWithdraw:2💸\nDeposit:3💸\nExit:4🏃\nChoice Option ⚙️:")

 if user_account == "1":
    with open("data/user.json","r") as f:
      data = json.load(f)
      print(f">>Balance:{data["Balance"]}<<\n")

 elif user_account == "2":
     amount = int(input("Amount to Withdraw 💵:")) 
     if amount <= 0:
      print("❌ Invaild amount ❌")

     elif amount <= data["Balance"]: 
      data["Balance"] -= amount

      print("Withdraw Successfully ✅")
      print(f"Current Balance :{data["Balance"]}")

     else:
        print("Insufficient Balance 💰")
         

     with open("data/user.json","w") as f:
            json.dump(data,f)
          
                  
 elif user_account == "3":
    amount = int(input("Amount to Deposit 💵:")) 
    data["Balance"] += amount

    print("Deposit Successfully ✅")
    print(f"Current Balance:{data["Balance"]}")

    with open("data/user.json","w") as f:
            json.dump(data,f)
         
 elif user_account == "4":
     print("Thanks For Using Our ATM 💵💰💳")      
     break

          
  


          

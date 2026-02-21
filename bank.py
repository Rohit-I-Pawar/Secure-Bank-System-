def Withdraw(data,amount):
    if amount <= 0:
      print("❌ Invaild amount ❌")
      
    elif amount <= data["Balance"]: 
      data["Balance"] -= amount
      print("Withdraw Successfully ✅")
      print(f"Current Balance :{data["Balance"]}")

      new_transaction = {
             "type": "Withdraw",
             "amount":amount 
      }
      
    return data,new_transaction
      


def Deposit(data,amount):
      data["Balance"] += amount
      print("Deposit Successfully ✅")
      print(f"Current Balance :{data["Balance"]}")
      new_transactions = {
             "type": "Deposit",
             "amount":amount 
      }
      return data,new_transactions



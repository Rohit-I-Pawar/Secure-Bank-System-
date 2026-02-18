import hashlib

def hash_Pin(pin):
 return hashlib.sha256(pin.encode()).hexdigest()

def verify_Pin(pin,stored_hash):
 
 user_hash = hash_Pin(pin)

 return user_hash == stored_hash
    
 

 
 




  
 

  












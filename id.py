import hashlib

def generate_unique_id(username, aadhar_number, pan_number, dob):

    name_part = username[:4].upper() 
    aadhar_part = aadhar_number[-4:]   
    pan_part = pan_number[3:6].upper() 
    dob_part = dob[-4:]               

   
    data_to_hash = f"{name_part}{aadhar_part}{pan_part}{dob_part}"

    unique_id = hashlib.sha256(data_to_hash.encode()).hexdigest()[:10].upper()
    unique_id_full = hashlib.sha256(data_to_hash.encode()).hexdigest()
    print("Hashed data is :", unique_id_full)

    return unique_id
    

username = input("enter name:")
aadhar_number = input("enter aadhar")  
pan_number = input("pan no") 
dob = input("enter dob")

generated_id = generate_unique_id(username, aadhar_number, pan_number, dob)
print("Generated Unique ID:", generated_id)


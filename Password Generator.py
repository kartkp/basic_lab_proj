#password generater_kartk
import random
import string

def gen_pass(length):

    char = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(char) for i in range(length))
    
    return password
password = gen_pass (12)
print("Your generated password is:", password)

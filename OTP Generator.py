#otp generator_kartk
import random
otp_length = int(input("Length of the otp digit you want??: "))

otp_characters = "0123456789"
otp = ""
for i in range(otp_length):
    otp += random.choice(otp_characters)


print("Your 4-digit OTP is:", otp)

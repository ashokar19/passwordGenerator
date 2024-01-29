import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = "12345678910"
special = "!@#$%^&*()-+=?\/"

while(True):
    def pass_details():
        chars = ""
        restriction_lower = input("You want your password to contain lower case characters?")
        restriction_upper = input("You want your password to contain upper case characters?")
        restriction_number = input("You want your password to contain numeric characters?")
        restriction_special = input("You want your password to contain special characters?")
        #if resctriction_lower matches one of the values in the collection right of "in"
        if restriction_lower in ["yes", "Yes", "YES", "y", "Y"]:
            chars = chars + lower
        else:
            chars = chars
        if restriction_upper in ["yes", "Yes", "YES", "y", "Y"]:
            chars = chars + upper
        else:
            chars = chars
        if restriction_number in ["yes", "Yes", "YES", "y", "Y"]:
            chars = chars + number
        else:
            chars = chars
        if restriction_special in ["yes", "Yes", "YES", "y", "Y"]:
            chars = chars + special
        else:
            chars = chars
            
        
        pass_length = int(input("How long do you want your password"))
        pass_count = int(input("How many passwords do you want to generate"))
        
        for i in range(0, pass_count):
            #resets password to print out
            password = ""
            for i in range(0, pass_length):
                #takes random char from chars
                pass_char = random.choice(chars)
                #adds that random char in this iteration to password
                password = password + pass_char
            #prints password for ith iteration of pass_count
            print("Password: " + password)
        
    pass_details()
    
    go_again = input("Do you wanna continue making passwords? (answer 'y' or 'n')")
    if go_again == "y":
        print("")
        #passes to next while loop iteration
        pass
    elif go_again == "n":
        break
        
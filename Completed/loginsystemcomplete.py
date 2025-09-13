print("==============================================")
print("---<| dear customers please enter your gmail |>---".upper())
print("==============================================")
# Start with an empty email
gmail = ""

# This loop checks for a valid email structure
while True:
    # Ask for input
    gmail = str(input()).lower().strip()
    
    # Check if it has @ and .com in the right order
    if "@" not in gmail or ".com" not in gmail:
        print("Email must contain @ and end with .com")
    else:
        # Split the email into parts around the @
        parts = gmail.split("@")
        if len(parts) != 2:  # Should have exactly 2 parts: before@ and after@
            print("Invalid email format")
        elif len(parts[0]) == 0:  # Check if nothing before @
            print("Email must have something before the @")
        elif not parts[1].endswith(".com"):  # Check if part after @ ends with .com
            print("Email must end with .com after the @")
        else:
            # If all checks pass, break out of the loop
            break
print("===========================")
password=4090     
if(gmail):
    print("----gmail entered----".upper())
else:
    print("enter gmail".upper())

if(gmail.lower()=="sarimgamerop@gmail.com"):
    password = 5678
if(gmail.lower()=="hijabfatima@gmail.com"):
    password = 3452
    
print("===========================")

attemptsout = " You are out of attempts "
loginsuccess = "Login Succesful"
attemptstring = "Password Not Correct Try Again"

# ATTEMPT 1
print("----ENTER YOUR PASSWORD----".upper())
inputpassword = int(input())

if (inputpassword == password):
    print(loginsuccess)
else:
    print(attemptstring)
    # ATTEMPT 2 - ONLY HAPPENS IF ATTEMPT 1 FAILED
    print("----ENTER YOUR PASSWORD----".upper())
    secondattempt = int(input())
    
    if (secondattempt == password):
        print(loginsuccess)
    else:
        print(attemptstring) # FIXED: from attemptstring to attempt_string
        # ATTEMPT 3 - ONLY HAPPENS IF ATTEMPT 2 FAILED
        print("----ENTER YOUR PASSWORD----".upper())
        thirdattempt = int(input())
        
        if (thirdattempt == password):
            print(loginsuccess)
        else:
            print(attemptstring) # FIXED: from attemptstring to attempt_string
            # ATTEMPT 4 - ONLY HAPPENS IF ATTEMPT 3 FAILED
            print("----ENTER YOUR PASSWORD----".upper())
            lastattempt = int(input())
            
            if (lastattempt == password):
                print(loginsuccess) # FIXED: from loginsuccess to login_success
            else:
                # FINALLY, IF ALL ATTEMPTS FAIL, PRINT THIS
                print(attemptsout.upper())


programkillingprevention = str(input())
if(programkillingprevention=="close"):
    print ("Closing Now")
if(programkillingprevention=="retry"):
    print("sorry this is in development type close to end the program".upper())
secprotection = str(input())
if(secprotection=="close"):
    print("DONE")
   
print("===================")



    

def main():
    
    # get score from user
    score = int(input("Enter your Score: "))
    # to know if they have extracurricular or not
    # 
    extracurricular = int(input("If you have extracurricular press 1 else press 0 : "))
    
    # extracurricular logic
    
    if extracurricular == 1:
        extracurricular == True
    else:
        extracurricular == False
    
    # let's get to the logic
    # check more on this in the ReadMe file
    
    if score >= 90:
        print("Accepted")
    elif score >= 75 and extracurricular:
        print("Accepted")
    else:
        print("rejected")
    
main()
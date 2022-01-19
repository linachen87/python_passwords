import csv
def getdata():
    file = list(csv.reader(open("user.csv")))
    tmp = []
    for line in file:
        tmp.append(line)
    
    return tmp

def create_userID(tmp):
    
    
    nameagain = True
    while nameagain == True:
        new_userID = input("Please enter your new user ID: ")
        row=0
        inlist = False
        for x in tmp:
            if new_userID == tmp[row][0]:
                print("The user already exist,please enter again")
                inlist = True
            row = row + 1
        if inlist == False:
            print("Great, this user ID works")
            nameagain = False
    return new_userID


def create_password():
    goodpassword = False
    specialcharacters = ['!','@','#','$','%','^','&','*']
    nubercharacter = ['0','1','2','3','4','5','6','7','8','9']
    while goodpassword == False:
        newpassword = input("Enter your new password: ")
        score = 0
        issc = False
        isnc = False
        isuc = False
        islc = False
        if len(newpassword) >= 8:
            score = score + 1
            print("length equal or biger than 8")
        for x in newpassword:
            if x.isupper():
                isuc = True
                print("Have uper case")
            if x.islower():
                islc = True
                print("Have lower case")
            if x in specialcharacters:
                issc = True
                print("Have special character")
            if x in nubercharacter:
                isnc = True
                print("Have number character")
        if isuc == True:
            score = score + 1
        if islc == True:
            score = score + 1
        if issc == True:
            score = score + 1
        if isnc == True:
            score = score + 1
        print("Your new password score is ",score)
        if score ==1 or score == 2:
            print("Weak password , please reenter a new password")
        if score == 3 or score == 4:
            print("This password could be improved")
            retry = input("Would you like to improve your password,y/n :")
            retry = retry.lower()
            if retry == 'y':
                continue
            else:
                print("OK")
                goodpassword = True
                return newpassword
        if score == 5:
            print("Strong password!")
            goodpassword = True
            return newpassword
def add_to_csv(userID, password):
    newrecord = userID+","+password+"\n"
    file = open("user.csv","a")
    file.write(newrecord)
    file.close()

def find_userID(tmp):
    asknameagain = True
    userID = ""
    while asknameagain == True:
        searchID = input("User ID that you'd like to find:")
        row = 0
        inlist = False
        for x in tmp:
            if searchID == tmp[row][0]:
                inlist = True
                print("Search ID in the list")
            row = row + 1
        if inlist == True:
            userID = searchID
            asknameagain = False
        else:
            print("Searched ID is not in the list")
    return userID
                
    
def change_password(tmp,userID):
    password = create_password()
    row = 0
    for x in tmp:
        if userID == tmp[row][0]:
            tmp[row][1]=password
        row = row + 1
    
    file = open("user.csv","w")
    line = 0

    for y in tmp:
        newrecord = tmp[line][0] + ","+tmp[line][1]+"\n"
        file.write(newrecord)
        line = line + 1
    file.close

def display_all_userID():
    tmp = getdata()
    row = 0
    for x in tmp:
        print(tmp[row][0])
        row = row + 1
         

def main():
    tmp = getdata()
    tryagain = True
    while tryagain == True:
        print("1) Create a new user ID")
        print("2) Change a password")
        print("3) Display all the user IDS")
        print("4) Quit")
        print()
        selection = int(input("Enter your selection: "))

        if selection == 1:
            userid = create_userID(tmp)
            password = create_password()
            add_to_csv(userid,password)
            print("your new user ID and password has been added to the csv file")
        elif selection == 2:
            userID = find_userID(tmp)
            change_password(tmp,userID)
            print("You password has been sucefully changed")
        elif selection == 3:
            print("Here are all the users ID")
            display_all_userID()
            print()
        elif selection == 4:
            print("Bye!")
            tryagain = False
        else:
            print("Wrong selection, please try again")
        
main()


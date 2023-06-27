# Important Steps Before you start
# In the current directory you will see a file called 'instagram_users.txt'
# Download or copy its contents and put it somewhere on your computer.
# Go to line 37 of this file and replace the text with the path of the instagram_users.txt file on your computer.
# Failure to do so will mean the program won't run as intended.
# Godspeed

# Create a class InstaUsers which has a constructor with *private* variables name, username, followers.
# Create getter and setter methods for each param
class InstaUser:
    def __init__(self, name, username, followers):
        self.__name = name
        self.__username = username
        self.__followers = followers

    def getName(self):
        return self.__name

    def getUsername(self):
        return self.__username

    def getFollowers(self):
        return self.__followers

    def setName(self, name):
        self.__name = name

    def setUsername(self, username):
        self.__username = username

    def setFollowers(self, followers):
        self.__followers = followers


# In the main program create a variable named path and store the path of the file instagram_users.txt on your computer

path = 'C:\\Users\\PRETTY\\Desktop\\Projects\\Python\\instagram_users.txt'

# In the main program declare an array called InstaUsersArray that can store 6 slots of data of type InstaUsers

InstaUsersArray = []


# Create a function called read() that reads the contents of the text file, maps each set of values to an InstaUser
# and appends it into the array InstaUsersArray at the correct slot/free slot
# Make use of exception handling
def read():
    global path, InstaUsersArray
    try:
        file = open(path, 'r')
        Users = 0
        for _ in file:
            Users += 1
        file.close()
        file = open(path, 'r')
        for i in range(int(Users / 3)):
            InstaUsersArray.append(InstaUser(file.readline().strip(), file.readline().strip(),
                                             int(file.readline().strip())))
        file.close()

    except IOError:
        # If the file does not exist stop the program

        print("File not found")
        exit(0)
        

read()


# Input a new user named "Robert Dowser" with username robby and followers 69 and add to the list
newName = input('Enter name: ')
newUsername = input('Enter username: ')
newFollowers = input('Enter followers: ')

# Create a new instance of InstaUser
newInstaUser = InstaUser(newName, newUsername, newFollowers)

# Whoops, we made a mistake use a setter method to change the username from robby to robert.
newInstaUser.setUsername('robert')

# Add to the array at the next free slot
InstaUsersArray.append(newInstaUser)

# Write vales to new textfile called instagram_usersV2

arr = []

for item in InstaUsersArray:
    arr.append(item.getName())
    arr.append(item.getUsername())
    arr.append(item.getFollowers())

# Define a path for where you want to create store the new instagram_users2.
path2 = 'instagram_users2.txt'

file2 = open(path2, 'w')
for line in arr:
    file2.write(str(line) + '\n')

file2.close()

# Expected result from the text file instagram_users2 is:
# JOHN
# john.doe
# 306
# BOB
# bobbylee
# 130
# REX
# rex_boy
# 407
# TOM
# drthomascook
# 3760
# ZIGGY
# ziggler
# 59
# ROBERT
# robert
# 69

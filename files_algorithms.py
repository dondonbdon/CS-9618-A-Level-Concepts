# Create a file named instagram_users in the res folder like so
path = 'instagram_users.txt'
TextForInstagramUsers = ['JOHN', 'john.doe', '306', 'BOB', 'bobbylee', '130', 'REX', 'rex_boy',
                         '407', 'TOM', 'drthomascook', '3760', 'ZIGGY', 'ziggler', '59']


# Populate the array with the values in the array named TextForInstagramUsers
file2 = open(path, 'w')
for line in TextForInstagramUsers:
    file2.write(str(line) + '\n')


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
        for _ in range(int(Users / 3)):
            InstaUsersArray.append(InstaUser(file.readline().strip(), file.readline().strip(),
                                             int(file.readline().strip())))
        file.close()

    except IOError:
        print("File not found")


read()


# Input a new user named "ROBERT" with username robby and followers 69 and add to the list
newName = input('Enter name: ')
newUsername = input('Enter username: ')
newFollowers = input('Enter followers: ')

# Create a new instance of InstaUser
newInstaUser = InstaUser(newName, newUsername, newFollowers)

# Whoops, we made a mistake use a setter method to change the username from robby to robman101.
newInstaUser.setUsername('robman')

# Add to the array at the next free slot
InstaUsersArray.append(newInstaUser)

# Write vales to new textfile called instagram_users2

arr = []

for item in InstaUsersArray:
    arr.append(item.getName())
    arr.append(item.getUsername())
    arr.append(item.getFollowers())

path2 = 'instagram_users2.txt'

file2 = open(path2, 'w')
for line in arr:
    file2.write(str(line) + '\n')

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
# Robert Dowser
# robman
# 69

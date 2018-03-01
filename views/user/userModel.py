######################################
#            USER CLASS
######################################

USERS=[] #global variable for users.

class User():
    """this class indicates the user
    functions include createUser,checkBusinessExists"""
    
    def __init__(self, userId, userName, email, password):
        # initialise the variables for this class here
        self.username = userName
        self.email=email
        self.password = password
        self.userId = userId
        self.userList =[]
        self.result=None

    def createUser(self, userId, username, email, password):
        """this function is for creating a new user. the fuction returns a boolean true if a user has been
        successfully registered and false if otherwise."""
        oldUsersListLength = len(self.userList) # lets store the length of userList before appending a new user.
        print(self.userList != None)
        if self.userList:
            for user in self.userList:
                for vals in user.values():
                    if userId not in vals:
                        #create the list below with precise indexing as illustrated below
                        # { userId:[[0] = username, [1] = email, [2] = password] }
                        self.userList.append({userId:[username, email, password]})
                        if len(self.userList) > oldUsersListLength:
                            return True #'user added' # user was created successfully.
                        else:
                            return False # user was not created.
                    else:
                        self.userList.append({userId:[username, email, password]})
                        return True
        else:
            self.userList.append({userId:[username, email, password]})
            return True

    def checkUsernameExists(self, username):
        """helper function to check whether username Exists before registering a new user. this function returns
        a boolean true if the username already exists and false if the username is not yet used."""        
        #lets loop through this global userList and append all usernames to list availUsernames
        availUsernames=[]        
        # result = None
        if USERS:
            for items in USERS:
                for values in items.values():
                    availUsernames.append(values[0]) #index zero holds our usernames by default.
                    if username not in availUsernames:
                        return False #false will mean they dont exist
                    else:
                        return True # this will mean they exist
        else:            
            print(availUsernames)
            return False                  
        

    def getUserdetails(self, userId):
        """this function is resposible for getting the details for the userId passed
        function returns a list of details for that userId."""
        pass
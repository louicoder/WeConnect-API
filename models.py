
USERS=[]
BUSINESSES=[]
REVIEWS=[]
#this is the business class handling all business logic

######################################
#           BUSINESS CLASS
######################################

class Business():
    """class that handles bussiness logic ie. create business,view own businesses,view all businesses,
    delete a business and update business the functions in this class include
    createBusiness, checkBusinessExists, updateBusiness, deleteBusiness, getOwnBusinesses, getAllBusinesses"""
    
    def __init__(self, busId, userId, busName, busLocation, busCategory, busDescription):
        # initialise the variables here. business id,user id, business name, business location,
        #  business category,business description.
        self.busId=busId
        self.userId=userId
        self.busName = busName
        self.busLocation=busLocation
        self.busCategory=busCategory
        self.busDescription = busDescription
        self.businessList = []

    def createBusiness(self, busId, userId, busName, busLocation, busCategory, busDescription):
        """function for creating a new business. funtion returns a boolean true if a business has been created and false 
        if business is not created."""
        #global businessList
        result = None
        oldBizListLength = len(self.businessList) # length of busines ltist before manipulation.
        #create the list below with precise indexing as illustrated below
        # [0] = userId, [1] = busName, [2] = busLocation, [3] = busCategory, [4] = busDescription
        self.businessList.append({busId:[userId, busName, busLocation, busCategory, busDescription]})
        
        if len(self.businessList) > oldBizListLength:
            result = True #incase creating a business is successful return true.
        else:
            result = False #incase creating a business failes return False.
        
        return result


    def checkBusinessExists(self, busId):
        """function to check whether a business Exists or not. function return a boolean true if business exists and
        false if it does not exist."""
        if self.businessList:
            print('here')
            for bus in self.businessList:
                if busId in bus.keys():
                    # result = True #business id /key exists
                    return True
                else:
                    # result = False#busId doesnt exist
                    return False
        else:
            result = False
        

    def updateBusiness(self, busId, userId, busName, busLocation, busCategory, busDescription):
        """this function is for updating business details. function returns a boolean true is business was updated 
        and false for otherwise"""        
        oldList=[] #this will hold the old details of the business
        newList=[] #this will hold the new details of the business
        if self.businessList:
            for xt in self.businessList:
                for key, val in xt.items():
                    if key == busId:
                        oldList.append([x for x in val]) #oldlist going to be used for comparison
                        xt[key]=[busId, userId, busName, busLocation, busCategory, busDescription]
                        newList.append([x for x in xt[key]]) #new list going to be used for comparison
                        if oldList[0] == newList[0] and oldList[1] == newList[1] and oldList[2] == newList[2] and oldList[3] == newList[3] and oldList[4] == newList[4]:
                            return False
                        else:
                            return True
        else:
            return False
    
    def deleteBusiness(self, busId):
        """this fuinction is responsible for deleting a business"""
        pass


    def getOwnBusinesses(self, userId):
        """function checks for a peron's own created businesses. function returns 
        a list of businesses attached to the passed userId"""        
        foundrows=[] #we will store our found records in this list
        #result = False
        if self.businessList:
            for x in self.businessList:
                for val in x.values():
                    if val[0] == userId:
                        foundrows.append(x)                        
            return foundrows
        else:
            return ''
        
    def getAllBusinesses(self):
        """this function return all businesses that ar available. 
        the function returns a list of all businesses registered."""
        foundBusinesses = []
        if len(self.businessList) > 0: # make sure atleast there are some records
            for x in self.businessList: # x represents each individual business
                foundBusinesses.append(x)
        return foundBusinesses


#  this is the review class handling all the reviews logic

######################################
#           REVIEWS CLASS
######################################

class Reviews():
    """class that handles all the reviews logic functions in this class include
     create review,retrieve business reviews."""    

    def __init__(self, reviewId, userId, busId, username, review):
        """lets initialise the variables for this class here."""
        self.reviewId = reviewId
        self.userId= userId
        self.busId = busId
        self.username= username
        self.review = review
        self.reviewList = []

    
    def createNewReview(self, reviewId, userId, busId, username, review):
        """function to create a new review. function return a boolean whether review was created or not"""
        #global reviewList
        result = False
        oldListLength = len(self.reviewList)
        #create the list below with precise indexing as illustrated below
        # [ [0] = userId, [1] = busId, [2] = username, [3] = review ]
        self.reviewList.append({reviewId:[userId, busId, username, review]})
        #lets chek the length of list before and after appending the review
        print('here')
        if len(self.reviewList) > oldListLength:
            # print('here')
            result = True #this means the list has changed
        else:
            result = False #this means the list hasn't changed

        return result

    def getBizReviews(self, busId):
        """this function returns reviews that belong to a particular business passed as the argument busId.
        functions returns a list of reviews attached to that business through the busId"""
        
        foundReviews = []
        # loop through the list to see which reviews have the passed userId as their 3rd index value
        for x in self.reviewList:
            for y in x.values():
                if y[2] == 1:
                    foundReviews.append(y)
        
        return foundReviews


######################################
#            USER CLASS
######################################

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
    

       



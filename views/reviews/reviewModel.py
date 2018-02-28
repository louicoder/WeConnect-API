REVIEWS=[]

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
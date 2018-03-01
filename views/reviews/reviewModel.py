from ..business.views import BUSINESSES
REVIEWS=[]


#  this is the review class handling all the reviews logic

######################################
#           REVIEWS CLASS
######################################

class Reviews():
    """class that handles all the reviews logic functions in this class include
     create review,retrieve business reviews."""    

    def __init__(self, reviewId, busId, review):
        """lets initialise the variables for this class here."""
        self.reviewId = reviewId
        self.busId = busId
        self.review = review

    
    def createNewReview(self, reviewId, busId, review):
        """function to create a new review. function return a boolean whether review was created or not"""
        global REVIEWS
        result = False
        oldListLength = len(REVIEWS)        
        REVIEWS.append({reviewId:[busId, review]})
        #lets chek the length of list before and after appending the review
        if len(REVIEWS) > oldListLength:
            result = True #this means the list has changed
        else:
            result = False #this means the list hasn't changed

        return result

    def getBizReviews(self, busId):
        """this function returns reviews that belong to a particular business passed as the argument busId.
        functions returns a list of reviews attached to that business through the busId"""
        global REVIEWS
        foundReviews = []
        # loop through the list to see which reviews have the passed userId as their 3rd index value
        for x in REVIEWS:
            for y in x.values():
                if y[2] == 1:
                    foundReviews.append(y)
        
        return foundReviews

    def getAllReviews(self):
        """function returns all reviews on all businesses"""
        global REVIEWS

        if not REVIEWS:
            return None
        else:
            return REVIEWS
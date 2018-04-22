from ..business.views import BUSINESSES
from ..business.views import Business
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

    @staticmethod
    def createNewReview(reviewId, busId, review):
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

    @staticmethod
    def get_business_reviews(busId):
        """this function returns reviews that belong to a particular business passed as the argument busId.
        functions returns a list of reviews attached to that business through the busId"""
        global REVIEWS
        busId = busId
        foundReviews =[]
        # res = Business.get_one_business(busId)
        # print(res)        
        
        if REVIEWS:
            for x in REVIEWS:
                for k, v in x.items():
                    if v[0] == busId:
                        foundReviews.append(v)
       
        return foundReviews

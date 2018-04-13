from flask import jsonify
#this is the business class handling all business logic

######################################
#           BUSINESS CLASS
######################################

# BUSINESSES=[{'busId':12, 'busName':'forklift', 'busLocation':'bwaise', 'busCategory':'medical', 'busDescription':'only business in town'}]
BUSINESSES=[]

class Business():
    """class that handles bussiness logic ie. create business,view own businesses,view all businesses,
    delete a business and update business the functions in this class include
    createBusiness, checkBusinessExists, updateBusiness, deleteBusiness, getOwnBusinesses, getAllBusinesses"""
    
    def __init__(self, busId, busName, userId, busLocation, busCategory, busDescription):
        # initialise the variables here. business id,user id, business name, business location,
        #  business category,business description.
        self.busId=busId
        self.busName = busName
        self.userId = userId
        self.busLocation=busLocation
        self.busCategory=busCategory
        self.busDescription = busDescription
        self.businessList = []

    def createBusiness(self, busId, busName, userId, busLocation, busCategory, busDescription):
        """function for creating a new business. funtion returns a boolean true if a business has been created and false 
        if business is not created."""
        global BUSINESSES
        result = False
        oldBizListLength = len(BUSINESSES) # length of busines ltist before manipulation.
        #create the list below with precise indexing as illustrated below
        # [0] = userId, [1] = busName, [2] = busLocation, [3] = busCategory, [4] = busDescription
        BUSINESSES.append({busId:[busName, userId, busLocation, busCategory, busDescription]})
        
        if len(BUSINESSES) > oldBizListLength:
            result = True #incase creating a business is successful return true.
        else:
            result = False #incase creating a business failes return False.        
        return result

    @staticmethod
    def checkBusinessExists(busId):
        """function to check whether a business Exists or not. function return a boolean true if business exists and
        false if it does not exist."""
        index = None
        global BUSINESSES
        if BUSINESSES:
            for x, y in enumerate(BUSINESSES, 0):
                for key, val in y.items():
                    if key == busId:
                        index = x
                        return index
        else:
            return index
        
    @staticmethod
    def updateBusiness(busId):
        """this function is for updating business details. function returns a index to update"""   
        index = None
        global BUSINESSES
        biz = []
        if BUSINESSES:
            for x, y in enumerate(BUSINESSES, 0):
                for key, val in y.items():
                    if key == busId:
                        index = x
                        biz.append([index,val])
                        # BUSINESSES[index]={busId:[busName, busLocation, busCategory, busDescription]}
                        return biz
        else:
            return biz
    
    @staticmethod
    def deleteBusiness(busId):
        """this fuinction is responsible for deleting a business"""
        global BUSINESSES
        index = None
        if BUSINESSES:
            for x, y in enumerate(BUSINESSES, 0):
                for key, val in y.items():
                    if key == busId:
                        index = x
                        return index
        else:
            return index

    # @staticmethod
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
        global BUSINESSES
        if BUSINESSES:
            return BUSINESSES
        else:
            return None

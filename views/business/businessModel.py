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
    
    def __init__(self, busId, busName, busLocation, busCategory, busDescription):
        # initialise the variables here. business id,user id, business name, business location,
        #  business category,business description.
        self.busId=busId
        self.busName = busName
        self.busLocation=busLocation
        self.busCategory=busCategory
        self.busDescription = busDescription
        self.businessList = []

    def createBusiness(self, Id, busName, busLocation, busCategory, busDescription):
        """function for creating a new business. funtion returns a boolean true if a business has been created and false 
        if business is not created."""
        global BUSINESSES
        result = None
        oldBizListLength = len(BUSINESSES) # length of busines ltist before manipulation.
        #create the list below with precise indexing as illustrated below
        # [0] = userId, [1] = busName, [2] = busLocation, [3] = busCategory, [4] = busDescription
        BUSINESSES.append({Id:[busName, busLocation, busCategory, busDescription]})
        
        if len(BUSINESSES) > oldBizListLength:
            result = True #incase creating a business is successful return true.
        else:
            result = False #incase creating a business failes return False.
        
        return result


    def checkBusinessExists(self, Id):
        """function to check whether a business Exists or not. function return a boolean true if business exists and
        false if it does not exist."""
        global BUSINESSES
        resultList=[]
        if BUSINESSES:            
            for bus in BUSINESSES:
                for biz in bus:
                    if bus['id'] == Id:
                        print('in here')
                        resultList.append([bus['busId'], bus['busName'], bus['busLocation'], bus['busCategory'], bus['busDescription']])
                        return resultList
                    else:
                    # result = False#busId doesnt exist
                        return None
        else:
            return None
        

    def updateBusiness(self, busId, busName, busLocation, busCategory, busDescription):
        """this function is for updating business details. function returns a boolean true is business was updated 
        and false for otherwise"""        
        if BUSINESSES:
            for xt in BUSINESSES:
                for key in xt:
                    if key == busId:
                        # xt['Id']=busId
                        xt[0]= busName
                        xt[1] = busLocation
                        xt[2]= busCategory
                        xt[3]= busDescription   
                        return True
                    else:
                        return False
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
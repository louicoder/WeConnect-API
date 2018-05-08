# Businesses=[
#         {
#             "de07ac48-b074-4d01-9217-0c23cde503d8": [
#                 "business1",
#                 "773458ufdssdfs908098sdf",
#                 "kampala",
#                 "somecategory",
#                 "some description for the business"
#             ]
#         },
#         {
#             "de07ac48-b074-0494-9217-0c23cde503d8": [
#                 "business",
#                 "773458ufdssdfs908098sdf",
#                 "kampala",
#                 "somecategory",
#                 "some description for the business"
#             ]
#         }
#     ]

# ls=[]
# id="de07ac48-b074-4d01-9217-0c23cde503d8"
# for x in Businesses:
#     for k, v in x.items():
#         if id == k:
#             ls.append(v[0])

# print(ls)

###################################################
# test two
###################################################


USERS= [
        {
            "email": "louis@email.com",
            "password": "pbkdf2:sha256:50000$6oef1KX6$fad611ebd0b8b664949c813c325fb86645825c0d9a686aa67fee55530867f996",
            "userid": "6d0f008d-d40c-493c-b4f8-d72a68aa1710",
            "username": "louis"
        }
    ]

for x in USERS:
    for k, v in x.items():
        if k == 'username':
            if v == 'louis':
                x['password'] = 'password'
                print('yes')

print(USERS)
            
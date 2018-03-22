 
BUSINESSES=[{'busId':[12, 'forklift', 27347836284, 'bwaise', 'medical', 'only business in town']}]

busId = 12
ls ={}
for x, y in enumerate(BUSINESSES, 0):
    for key, val in y.items():
        if val[0] == 12:
            index = x
            ls.update({'index':index, 'values': val})

# print(ls)

x = {'99b2deee-8b48-444a-84c9-3be1b03fede6': ['business', '773458ufdssdfs908098sdf', 'kampala', 'technology', 'a tech business']}
# print(BUSINESSES[0])

for k, v in x.items():
    print(v[0])

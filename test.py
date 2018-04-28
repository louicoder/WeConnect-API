mail = 'louis@mail.com'
x = [mail]

x = [x for x in mail]
if '.' not in x:
    print('not')
else:
    print('yes')
'''
lab5 if statement
'''

#3.1

alien_color = 'red'

if alien_color =='green':
    print('you just earned 5 points')
    
    
#3.2

alien_color = 'yellow'

if alien_color == 'green' :
    print('you just earned 10 points')
    
else:
     print('you just earned 10 points')
    
#3.3

favorite_fruit = ('grapes','bananas','watermelon')

if 'grapes' in favorite_fruit:
    print('you really like grapes')
if 'watermelon' in favorite_fruit:
    print('you really like watermelon')
if "mango" in favorite_fruit:
    print ('you really like mango')
    
#3.4
age = 14
#if age < 10:
#    print('you are a kid')
#elif age <20:
#    print('you are a teenager')
#else:
#    print('you are an adult')
#    if age >65:
#print('you are an elder')

if age >=20:
    print('you are an adult')
    if age >65:
        print('you are an elder')
elif age > 10:
    print('you are a teenager')
else:
    print('you are a kid')
    
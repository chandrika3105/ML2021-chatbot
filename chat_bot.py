'''
   ******************************************************************************************
   *   1. This is a program for chatbot.                                                    *
   *   2. Name of the chatbot is Jacob.                                                     *
   *   3. This chatbot gives information about different Fruits.                            *
   *   4. Information includes different typs of vitamins in them.                          *
   *   5. You can get every Fruit information (A-Z)                                         *
   ******************************************************************************************
'''

import random
import datetime as dt
def greet():
    greetings = ['Holaaa..!! I m Jacob...! I m here to help you.. in knowing the vitamins which are rich in fruits!,By the way may i know your name please..! : ',
                'Hey! hello I m Jacob !! You can get help from me in getting information about vitamins which are present in fruits and in which countries the fruits are highly available, May i know your good name? : ']
    return random.choice(greetings)


def welcome(name):
    time = dt.datetime.now().hour
    if time<12:
        return 'Good Morning '+name+' !! Have a very great day!'
    elif time>=12 and time<16:
        return 'Wishning you a Good Afternoon filled with relaxation '+name+' !! '
    elif time>=16 and time<22:
        return 'A very pleasant evening '+name+' !!'
    else:
        return 'Ohhh!! its too late ,'+name+' However i ll help you!'

def opts():
    fruits = ['Apple','Apricot','Avocado','Banana','Blackberry','Canteloupe','Cherry','Custardapple','Dates','Durian','Figs','Grapefruit','Grapes','Guava','Gooseberry','Jackfruit','Kiwi','Kumquat','Lemon','Lime','Lychees','Mandarins','Mango','Mangosteen','Nectarine','Oranges','Passionfruit','Papaya','Peaches','Pear','Persimmons','Pineapple','Plums','Pomegranate','Pomelo','Rambutans','Sapodillas','Starapple','Strawberry','Tamarillos','Watermelon']
    vitamins = ['C','A,C','B3,C','B6,C','C','A,C','A','B6','B COMPLEX','C','A,K','C','C,K','C','C,A','B,C','C,E','C','C','B6,C','C','C','C','C','A,C','C','C,A','C,A','E,K','C','C','C','C','B,C,K','C','C','A,C,B6','C,B5','C','A,C,B1,B2,B3,B6','A,B6,C']
    print('Enter the name of the Fruit,to get details : ')
    print('The fruits are : ')
    list_frutis(fruits)
    print('\n--OR--\n')
    print("Enter 0 to end the chat!!\n")
    x = input()
    print()
    y = x.capitalize()
    while y!='0':
        if y in fruits:
            if y[-1]=='s':
                print('1.'+y+' have vitamins '+vitamins[fruits.index(y)])
                print()
                print('2.'+y+' are good for health')
            else:
                print('1.'+y+' has vitamins '+vitamins[fruits.index(y)])
                print()
                print('2. '+y+' is good for health')
            countries(fruits.index(y))
        else:
            print("!!Enter a valid fruit name!!!!! \n")
            print()
        opts()
    else:
        print("Have a great day ! Chat once again ,,BYE!BYE!")
        print()
        quit()

def countries(x):
    country = ['India,Vietnam,China','Turkey,Iran','Mexico,Peru','India,China','Turkey,Afghanisthan','China,Turkey','Iran,USA','Indonesia','Egypt,SaudiArabia','Thailand,Malasia','India,Japan,China','US','Italy','India','Indonesia,Phillipines','Bangladesh,India','Italy','US,china','India,Mexico','China,US,India','China','Italy,Spain','India,China,Thailand','Thailand','China,Spain','Brazil,Mexico','Phillipines','India,Brazil','China,Spain','China,Italy','China,Korea,Japan','Costa Rica,Phillipines','China,Romania','India,Iran','China,Thailand','Indonesia,Phillipines','Mexico,Venezuela','America,Australia','China,US','Equador,Colombia,Peru','China,Turkey']
    print('\n3. The production of your required fruit is mostly takes place in the countries : ',country[x]+'\n')  
def list_frutis(x):
    print(x)

def bot_Jacob():
    print(greet())
    print()
    name = input()
    print()
    print(welcome(name))
    print()
    opts()
print()
print("\t\t\t---------WELCOME TO MY CHATBOT----------")
print()
bot_Jacob()





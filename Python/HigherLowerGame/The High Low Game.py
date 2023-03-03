import random
from Game_data import data
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)


"""


def setter(data: list):#Selecting random data from List containing dictionary
    var={}
    var=random.choice(data)
    return var

def printa(var,A):#print function to print the details
 print(f'"{A}": Name-> {var["name"]}, Description-> {var["description"]},{var["country"]}\n\n')

def swapa():#for each correct answer to change the data of var_A and var_B
   global var_a
   global var_b
   var_a=var_b
   var_b=setter(data)
   if var_a== var_b:
    var_b=setter(data)

def compare(var_a,var_b,user):#To compare two variables and return if they got right or wrong answer
   global score
   if var_a['follower_count']>var_b['follower_count']and user=="a":#comparing variable and answer
      print("you got it right dear\n")
      print(f"number of followers {var_a['follower_count']}mn")
      print(f"number of followers {var_b['follower_count']}mn")
      score+=1#increasing score
      swapa()#now bcz this will occur only if user is right we have to pass new values so we will use swap function
      print(f"your score is {score}\n\n")
      game()
   elif var_a['follower_count']<var_b['follower_count']and user=="b":
      print("you got it right dear\n")
      print(f"number of followers {var_a['follower_count']}")
      print(f"number of followers {var_b['follower_count']}")
      score+=1
      swapa()
      print(f"your score is {score}\n\n")
      game()
   else:
      print("sorry, you failed\n")#here user got the wrong answer
      print(f"your score is {score}\n\n")
      if input("do you want to continue ").lower()=="y":#if user wants then continue else end the game
         game()
      else:
         return 0

score=0
var_a=setter(data)#setting data for first time
var_b=setter(data)
if var_a== var_b:#if computer selects the same value for both the variable
   var_b=setter(data)

def game():
    A="A"
    B="B"
    printa(var_a,A)
    print(vs)
    printa(var_b,B)
    user=input("whom of them have more followers ").lower()
    compare(var_a,var_b,user)

game()
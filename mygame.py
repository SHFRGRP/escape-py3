# -*- coding: #windows-1251 -*-

#by AxReal (Alexey Axenov) https://www.sololearn.com/Profile/5698359/?ref=app

#This code use inputs!

#To successful run this code, you should run it in Python IDLE (windows), with 'python code.py' (unix) or with QPython3 (Android, in Google Play)

#or you can run this code time-by-time and add new inputs to new run



'''
Changelog:
v1.0:
First Version...
v1.1:
Improved scenes
Added thrid scene
Added examine action
More improves!!!

???????
This is a powerful console quest, and you can't win in first time ;)
Try it out!

You can run this code time-by-time and add new inputs to new run
???????


'''
class Coin:
  def __init__(self, price, year):
    self.price = price
    self.year = year


version = "1.1"
scene = 1
is_coin_found = False
coin = Coin("5?", 1987)


print("Welcome to Can You Escape v" + version)
is_playing = True
msg = "Input: "


def start():
    global msg
    print(
        '''
        You woke up in a dark room. You're trying to remember something, but a headache and a vague way of thinking hinder you.
        You go up and see the door ahead of you. You can go ahead, or stay here (go/stay). So You can examine current room by 'examine' action without arguments or examine things that you find.
        '''
        )
    msg = "Your action: "
    

def get_input():
    print()
    command = input(msg).split()
    print()
    if len(command) >= 1:
        verb_word = command [0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
            if len(command) >= 2:
                noun_word = command [1]
                verb(noun_word)
            else:
                verb()
        else:
            print ("Action to {} does not exist".format(verb_word))
    
        
    else:
        print("You typed empty line!")


def game_over():
    global is_playing
    is_playing = False
    print("You LOSE!")


def game_win():
    global is_playing
    is_playing = False
    print("You WIN!")


def right():
  if scene == 2:
    print("You have opened right door...")
    print("Oh... NO! This man was evil! He killed you with knife!\nYou Dead!")
    game_over()
  else:
    print('Right? What means right?')


def left():
  global scene
  if scene == 2:
    scene += 1
    print("You have opened left door...")
    print("You entered new room... But it have only one locked door! This door with code lock. You should provide 4-digits number. Faster! Footsteps hears clother... You have 3 tries.")
    tries = 0
    while is_playing:
     if tries <= 2:
      code = input("\nProvide code: ")
      if code == str(coin.year):
        finalgood()
      # is_playing = False
        break
      else:
        print('\nWrong!!!\n')
        tries += 1
     else:
       finalbad()
      # is_playing = False
    
   # game_win()
  else:
    print('You watch left and see... wall ahead...')


def go():
  global scene
  if scene == 1:
    global msg
    scene += 1
    print('You entered the room.')
    print('''You have saw two doors. Wait... You hear someone\'s foot steps from right door... ''' )
    print("Go right: right, Go left: left.")
    msg = "Where will you go: "
   # del verb_dict["stay"]
  #  del verb_dict["go"]
  else:
   print('Not now, bro)')

def stay():
  if scene == 1:
    print('You stayed here. But...')
    print('You started to choke... the light slowly begins to fade... the last thing you heard is someone\'s evil laugh...')
    print("You dead...")
    game_over()
  else:
    print('Not now, bro)')
    
def examine(thing='room'):
  global is_coin_found
  if thing == 'room':
   if scene == 1:
     print('\nYou see empty room with one unlocked door... Wait! You found the coin! '+coin.price+', huh:)\n')
     is_coin_found = True
   elif scene == 2:
     print('\nYou see room with two doors: left and right. You hear footsteps from right door. Choose faster!\n')
   elif scene == 3:
     print("\nYou entered the empty room with locked door. Door\'s lock have code number with 4 digits. You hear footsteps from back door. Provide code faster, you have 3 tries!\n")
    
  elif thing == 'coin':
   if is_coin_found:
    print('\nIt\'s a '+coin.price+' coin, '+str(coin.year)+' year.\n')
   else:
    print('\nYou don\'t have coins.\n')
  else:
    print('You can\'t examine '+thing)


def finalgood():
  print("Back door opened, but you managed to open the door and run away from here. You ran for a long time, there was a forest around. But after 3 hours of running you ran out into the village and found out that you were in another state:)")
  game_win()
  
def finalbad():
  print("Back door opened... Man entered the room and... killed you with knife!\nYou Dead!")
  game_over()

verb_dict = {

"stay":stay,
"go":go,
"right":right,
"left":left,
"examine":examine

}

start()

while is_playing:
    get_input()


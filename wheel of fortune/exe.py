#import
from computer import computer
from human_player import player,human_player
from movies import movies
import random
import sys
import time

#functions
def equal(a,b):
    if a==b:
        return True

def winnings(q,a):
        if q in movie_name:
            if q in "aeiou":
                a.add_prize_money(-100)
            print(a.get_move(movie_name,guessed)[0])
            l=random.choice(available_prize_money)
            print(f'{a.name} got {l}')
            a.add_prize_money(l)
            t=random.choice(available_prizes)
            print(f'{a.name} won {t}')
            if t=="bankrupt":
                a.bankrupt()
            else:
                a.add_prizes(t)
        else:
            print("better luck next time")


def human_move():
    for a in human:
        print(f'{a.name}:')
        print(a.get_move(movie_name,guessed)[0])
        print(a)
        while True:
            q=a.get_move_human()
            if (a.prize_money < 100 and q in "aeiou") or q in guessed:
                pass
            else:
                break;
        if q =="pass" or q in guessed:
            continue;
        elif q=="exit":
            sys.exit(0)
        guessed.append(q)
        winnings(q,a)
        print(a,"\n")
        if equal(movie_name,a.get_move(movie_name,guessed)[1]):
            print(f'\n{a.name} won:')
            for i in a.prizes:
                print(i)
            break;
        time.sleep(1)

def computer_move():
    for a in computer_player:
        print(f'computer {a.name}:')
        q=a.get_move_computer(movie_name,guessed,difficulty)
        if  q=="pass":
            continue
        print(f'{a.name} choose {q}')
        guessed.append(q)
        winnings(q,a)
        print(a,"\n")
        if equal(movie_name,a.get_move(movie_name,guessed)[1]):
            break;
        time.sleep(1)
        
#declared    
available_prizes=["bankrupt","cushion","bedsheet","fountain pen",
                  "blank cd","trip to paris","iphone X",
                  "amazon $100 voucher","an egg","a tomato"]
available_prize_money=[0,75,50,75,100,100,50,50,50,50,25]
movie_name=movies()
number_player=int(input("enter number of players:"))
number_computer=int(input("enter computer players:"))
if number_computer >0:
    difficulty=int(input("set difficulty:"))
human=[]
guessed=[]
computer_player=[]

#made objects
for i in range(number_player):
    a=input(f'enter player {i+1} name:')
    human.append(human_player(a))
    harry=human_player(a)
for i in range(number_computer):
    computer_player.append(computer(str(i+1)))

#game start
while(True):
    #humans
    human_move()

    if equal(movie_name,harry.get_move(movie_name,guessed)[1]):
        break;

    #computer players
    if number_computer >0:
        computer_move()

    if equal(movie_name,harry.get_move(movie_name,guessed)[1]):
        print("You lose")
        break;
                
        
    

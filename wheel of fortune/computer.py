import random
vowels="aeiou"
letters="thsnrdlymwfgcbpkvjqxz"
frequency="eothasinrdluymwfgcbpkvjqxz"
from human_player import player

class computer(player):
    def __init__(s,name):
        player.__init__(s,name)
    def set_difficulty(s,difficulty):
        a=random.randint(1,10)
        if a<=difficulty:
            return 'difficult'
        else:
            return 'easy'
    def possible_guessed(s,guessed,difficulty):
        a=computer.set_difficulty(s,difficulty)
        if a=='difficult':
            l=[i for i in frequency if i not in guessed]
            for i in l:
                if i in vowels and s.prize_money<100:
                    continue
                else:
                    return i
        else:
            if int(s.prize_money)<100:
                s=letters
            else:
                s=letters+vowels
            p=random.choice(s)
            return p
    def get_move_computer(s,total,guessed,difficulty):
        a=computer.possible_guessed(s,guessed,difficulty)
        if a is None or a in guessed:
            return "pass"
        else:
            return a
            

class player():
    def  __init__(s,name):
        s.name=name
        s.prize_money=0
        s.prizes=[]
    def add_prize_money(s,value):
        s.prize_money+=value
    def bankrupt(s):
        s.prize_money=0
    def add_prizes(s,value):
        s.prizes.append(value)
    def __str__(s):
        return f'{s.name} has ${s.prize_money}'
    def get_move(s,total,guessed):
        q=""
        for a in total:
            if a==" ":
                q+=" "
            elif a in guessed:
                q=q+a
            else:
                q+="_"
        return (f'guessed:{guessed}\nstring:{q}',q)
class human_player(player):
    def __init__(s,name):
        player.__init__(s,name)
    def get_move_human(s):
        q=input("\nenter 'pass','exit',or a letter:")
        return q

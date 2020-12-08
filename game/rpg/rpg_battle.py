import random
from colors import *
class options:
    def __init__(self,hp,mp,atk,defence,magic,items):
        self.hp=hp
        self.mp=mp
        self.max_mp=mp
        self.max_hp=hp
        self.magic=magic
        self.defence=defence
        self.atk=atk
        self.items=items
        self.actions=["attack" , "magic" , "items"]
    def generate_damage(self):
        al=self.atk-10
        ah=self.atk+10
        return random.randrange(al,ah)
    def generate_defence(self):
        al=self.defence-5
        ah=self.defence+5
        return random.randrange(al,ah)
    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
    def get_hp(self):
        return self.hp
    def get_mp(self):
        return self.mp
    def generate_magic_damage(self,i):
        ml=self.magic[i]["dmg"]-5
        mh=self.magic[i]["dmg"]+5
        return random.randrange(ml,mh)
    def reduce_mp(self,i):
        try:
            self.mp-=self.magic[i]["cost"]
        except:
            self.mp-=i
        return self.mp
    def choose_action(self):
        i=1
        print(color("You choose:-",fg="red",style="bold"))
        for items in self.actions:
            print(i,":",items)
            i+=1
    def get_action_name(self,i):
        return self.actions[i]
    def choose_magic(self):
        k=1
        print(color("Magics",fg="blue",style="bold"))
        for magics in self.magic:
            print(k,":",magics["name"],
                  "(cost:",magics["cost"],",type:",magics["type"],")")
            k+=1
    def choose_items(self):
        k=1
        print(color("Items",fg="blue",style="bold"))
        for item in self.items:
            print(k,":",item["name"],
                  "(quantity:",item["quantity"],",type:",item["type"],",points:",item["points"],")")
            k+=1
    def reduce_quan(self,i):
        self.items[i]["quantity"]-=1     
    def magic_pro(self,i,p):
            return self.magic[i][p]
    def len_magic(self):
            return len(self.magic)
    def len_item(self):
            return len(self.items)
    def item_pro(self,i,p):
            return self.items[i][p]
    def stats(self,n):
        print("  hp=",self.hp)
        print(" __________")
        print("|",end="")
        a=self.hp/self.max_hp*10
        if n=="h":
            t="indianred"
            y="skyblue"
        elif n=="v":
            t="rosybrown"
            y="moccasin"
        else:
            t="gold"
            y="tan"
        if(n=="h" and a<=1):
            t="silver"
        for i in range(0,10):
            if(a>i):
                print(color("█",fg=t),end="")
            else:
                print(" ",end="")
        print("|")
        print(" ‾‾‾‾‾‾‾‾‾‾")
        print(" mp=",self.mp)
        print(" _____")
        print("|",end="")
        a=self.mp/self.max_mp*5
        for i in range(0,5):
            if(a>i):
                print(color("█",fg=y),end="")
            else:
                print(" ",end="")
        print("|")
        print(" ‾‾‾‾‾")
        

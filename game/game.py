from rpg.rpg_battle import options
from copy import deepcopy
from colors import *
from PIL import Image
import random
import time
def choose_enemy(enemy):  
    k=1
    print("choose enemy")
    for i in enemy:
        print(k,":",i["name"])
        k+=1

magic=[{"name":"earth", "cost":110, "dmg":370,"type":"black"},
       {"name":"fire",  "cost":100, "dmg":305,"type":"black"},
       {"name":"water", "cost":130, "dmg":400,"type":"black"},
       {"name":"cura", "cost":110, "dmg":570,"type":"white"},
       {"name":"cure", "cost":120, "dmg":700,"type":"white"},
       {"name":"curaga", "cost":150, "dmg":900,"type":"white"}]
enemy_magic=[{"name":"black", "cost":110, "dmg":309,"type":"black"},
             {"name":"blacker", "cost":120, "dmg":340,"type":"black"}]
villain_magic=[{"name":"black", "cost":110, "dmg":370,"type":"black"},
               {"name":"blacker", "cost":120, "dmg":350,"type":"black"},
               {"name":"dark", "cost":130, "dmg":400,"type":"black"}]
items=[{"name":"grenade","quantity":5,"type":"dmg","points":500},
       {"name":"heal portion","quantity":5,"type":"hp","points":2000},
       {"name":"exilir","quantity":5,"type":"mp","points":300}]
enemy_items=[{"name":"grenade","quantity":3,"type":"dmg","points":500}]
villain_items=[{"name":"heal portion","quantity":1,"type":"hp","points":2000},
               {"name":"exilir","quantity":1,"type":"mp","points":300},
               {"name":"grenade","quantity":5,"type":"dmg","points":500},
               {"name":"misser","quantity":3,"type":"special","points":10}]
hero=options(3154,503,133,43,magic,items)
run=True
z=0
l=0
w=0
v=0
while run:
    if(z==0) and z==l:
        print("Wave 1")
        enemy_items1=deepcopy(enemy_items)
        enemy=[{"name":"enemy","power":options(323,153,60,25,enemy_magic,enemy_items1)}]
        z+=1
    elif(z==1) and z==l:
        print("Wave 2")
        enemy_items1=deepcopy(enemy_items)
        enemy_items2=deepcopy(enemy_items)
        enemy=[{"name":"enemy1","power":options(523,163,76,30,enemy_magic,enemy_items1)},
               {"name":"enemy2","power":options(423,150,74,25,enemy_magic,enemy_items2)}]
        z+=1
    elif(z==2) and z==l:
        print("Wave 3")
        enemy_items1=deepcopy(enemy_items)
        enemy_items2=deepcopy(enemy_items)
        enemy_items3=deepcopy(enemy_items)
        enemy=[{"name":"enemy1","power":options(523,193,73,40,enemy_magic,enemy_items1)},
              {"name":"enemy2","power":options(623,243,60,30,enemy_magic,enemy_items2)},
              {"name":"enemy3","power":options(358,103,100,35,enemy_magic,enemy_items3)}]
        z+=1
    elif(z==3) and z==l:
        print("Final Wave")
        enemy_items1=deepcopy(enemy_items)
        enemy_items2=deepcopy(enemy_items)
        enemy_items3=deepcopy(enemy_items)
        enemy=[{"name":"enemy1","power":options(683,203,90,45,enemy_magic,enemy_items1)},
               {"name":"enemy2","power":options(563,183,80,50,enemy_magic,enemy_items2)},
               {"name":"enemy3","power":options(703,253,112,55,enemy_magic,enemy_items3)},
               {"name":"qwerty","power":options(5000,603,150,95,villain_magic,villain_items)}]
        z+=1
    print("hero:")
    hero.stats("h")
    for i in enemy:
        print(i["name"],":")
        if i["name"]=="qwerty":
            i["power"].stats("v")
        else:
            i["power"].stats("e")  
    hero.choose_action()
    i=input()
    if(i=="00"):
        break
    try:
        print("You choose",color(hero.get_action_name(int(i)-1),fg="orange"))
        if i=="1":
            dmg=hero.generate_damage()
            choose_enemy(enemy)
            o=int(input())-1
            if(o>len(enemy)-1):
                print("INVALID")
                time.sleep(3)
                continue;
            qq=enemy[o]["power"].generate_defence()
            if qq>dmg:
                qq=0
            enemy[o]["power"].take_damage(dmg-qq)
            print("You attacked for",color(dmg,fg="orangered"),"damage points.It dealt",dmg-qq,"points")
        if(i=="2"):
            hero.choose_magic()
            k=int(input())-1
            if(k>len(magic)-1):
                print("INVALID")
                time.sleep(3)
                continue;
            print("You choose",color(magic[k]["name"],fg="orange"))
            if(hero.get_mp()<magic[k]["cost"]):
                print(color(("less mp"),fg="mediumorchid"))
                time.sleep(3)
                continue;
            hero.reduce_mp(k)
            print("current mp: ",color(hero.get_mp(),fg="brown"))
            dmg=hero.generate_magic_damage(k)
            if(magic[k]["type"]=="black"):
                choose_enemy(enemy)
                o=int(input())-1
                if(o>len(enemy)-1):
                    print("INVALID")
                    time.sleep(3)
                    continue;
                qq=enemy[o]["power"].generate_defence()
                if qq>dmg:
                    qq=0
                enemy[o]["power"].take_damage(dmg-qq)
                print(magic[k]["name"],"deal",color(dmg-qq,fg="orangered"),"damage points.")
            else:
                hero.take_damage(-dmg)
                print(magic[k]["name"],"heals for",color(dmg,fg="orange"),"points.")
        if(i=="3"):
            hero.choose_items()
            i=int(input())-1
            if(i>len(items)-1):
                print("INVALID")
                time.sleep(3)
                continue;
            print("You choose",color(items[i]["name"],fg="orange"))
            hero.reduce_quan(i)
            if(items[i]["quantity"]<0):
                items[i]["quantity"]=0
                print(color(("no item left"),fg="mediumorchid"))
                time.sleep(3)
                continue;
            dmg=items[i]["points"]
            if(items[i]["type"]=="dmg"):
                choose_enemy(enemy)
                o=int(input())-1
                try:
                    qq=enemy[o]["power"].generate_defence()
                except:
                    print("INVALID")
                    time.sleep(3)
                    continue;
                if(qq>dmg):
                    qq=0
                enemy[o]["power"].take_damage(dmg-qq)
                print(items[i]["name"],"deal",color(dmg-qq,fg="orangered"),"damage points.")
            elif(items[i]["type"]=="hp"):
                hero.take_damage(-dmg)
                print(items[i]["name"],"heals for",color(dmg,fg="orange"),"points")
            elif(items[i]["type"]=="mp"):
                hero.reduce_mp(-dmg)
                print(items[i]["name"],"gave",color(dmg,fg="orange"),"magic points.")
    except:
        print("INVALID")
        time.sleep(3)
        continue;
    print("hero:")
    hero.stats("h")
    for i in enemy:
        print(i["name"],":")
        if i["name"]=="qwerty":
            i["power"].stats("v")
        else:
            i["power"].stats("e")   
    time.sleep(1)
    n=[]
    for i in enemy:
        if i["power"].get_hp()==0: 
            n.append(i)
            print("You defeted",color(i["name"],fg="blue"))
    for i in n:
        enemy.remove(i)        
    del(n[::])
    if v==0:
        w=0
    while(w <len(enemy)):
        i=enemy[w]
        r=random.randint(0, 2)
        time.sleep(0.5)
        if v==5:
            v=0
            continue
        elif(v>0):
            v+=1
        if i["name"]=="qwerty" and i["power"].get_hp()<500:
            q=0
            dmg=villain_items[q]["points"]
            i["power"].take_damage(-dmg)
            i["power"].reduce_quan(q)
            w=w+1
            print(i["name"],"choose",i["power"].item_pro(q,"name"))
        elif i["name"]=="qwerty" and i["power"].get_mp()<60:
            q=1
            dmg=villain_items[q]["points"]
            i["power"].reduce_mp(-dmg)
            i["power"].reduce_quan(q)
            w+=1
            print(i["name"],"choose",i["power"].item_pro(q,"name"))
        elif(r==0):
            dmg=i["power"].generate_damage()
            qq=hero.generate_defence()
            if(qq>dmg):
                qq=0
            hero.take_damage(dmg-qq)
            w+=1
            print(i["name"],"attacked for",color(dmg,fg="indianred"),"damage points. It dealt",dmg-qq,"points")
        elif(r==1):
            q=random.randint(0,i["power"].len_magic()-1)
            if(i["power"].get_mp()<i["power"].magic_pro(q,"cost")):
                continue;
            i["power"].reduce_mp(i["power"].magic_pro(q,"cost"))
            dmg=i["power"].generate_magic_damage(q)
            qq=hero.generate_defence()
            if qq>dmg:
                qq=0
            hero.take_damage(dmg-qq)
            w+=1
            print(i["name"],"choose",i["power"].magic_pro(q,"name"),"magic.It dealt",dmg-qq,"dmg points")
        elif(r==2):
            q=random.randint(0,i["power"].len_item()-1)
            if(i["name"]=="qwerty"):
                if(v==0):
                    q=random.randint(2, 3)
                else:
                    q=2
            if(i["power"].item_pro(q,"quantity")<=0):
                continue;
            else:
                i["power"].reduce_quan(q)
            dmg=i["power"].item_pro(q,"points")
            if(i["power"].item_pro(q,"type")=="dmg"):
                qq=hero.generate_defence()
                if qq>dmg:
                    qq=0
                hero.take_damage(dmg-qq)
                print(i["name"],"choose",i["power"].item_pro(q,"name"),".It dealt",dmg-qq,"dmg points")
            elif(i["power"].item_pro(q,"type")=="special"):
                v=v+1
                print(i["name"],"choose",i["power"].item_pro(q,"name"),"You will miss 3 turns.")  
            if(v==0):
                w=w+1
    time.sleep(3)
    if len(enemy)==0:
        l+=1
        if(l==4):
            print("you win the game")
            break;
    if(hero.get_hp()==0):
        my=Image.open("cry1.png")
        my.show()
        print("You lose")
        break;   
'''
print(color('my string', fg='cyan'))
print(color('some text', fg='violet', bg='yellow', style='bold'))
'''

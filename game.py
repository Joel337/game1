#Recreated RPG challenge for nephews and neices
#JDT, joelsemail@gmail.com
import random, sys, copy, base64, os

class Character:
    name = "the girl has no name"
    health = 1
    attack = 1
    dodge = 0
    special = 0
    h_potion = 2
    grenade = 2
    challenge = 0
    def __init__(self, name = name, health = health, attack = attack, challenge = challenge):
        self.name = name
        self.health = health
        self.attack = attack
        self.challenge = challenge

#Create enemies
ghost = Character(name = "ghost", health = 100, attack = 200, challenge = 2)
goblin = Character(name = "goblin", health = 50, attack = 50, challenge = 1)
spider = Character(name = "poisonous spider", health = 50, attack = 100, challenge = 1)
orc = Character(name = "smelly orc", health = 300, attack = 100, challenge = 2)
raven = Character(name = "ravenous raven", health = 50, attack = 50, challenge = 1)
giant = Character(name = "giant", health = 800, attack = 250, challenge = 3)
wizard = Character(name ="wizard", health = 400, attack = 500, challenge = 4)
lion = Character(name = "lion", health = 400, attack = 400, challenge = 3)
robot = Character(name = "giant robot", health = 800, attack = 600, challenge = 5)
dragon = Character(name = "red dragon", health = 700, attack = 800, challenge = 5)
dragon2 = Character(name = "golden dragon", health = 999, attack = 999, challenge = 7)
shark = Character(name = "flying shark", health = 400, attack = 999, challenge = 6)
moon = Character(name= "Malevolent moon", health = 5000, attack = 0, challenge = 0)

#get enemies per level based on level difficulty. return array of enemies. 
def get_enemies(difficulty):
    enemies=[]
    potential_enemies=[ghost, goblin, spider, orc, raven, giant, wizard, lion, robot, dragon, dragon2, shark]
    while difficulty > 0:
        check_enemy = random.choice(potential_enemies)
        if difficulty - check_enemy.challenge >= 0:
            difficulty=(difficulty - check_enemy.challenge)
            enemies.append(check_enemy)
    room = copy.deepcopy(enemies)
    return room

#start game menu
def start_menu():
    menu_in = input("What would you like to do?\n 1) New Game \n 2) Load Game \n 3) Quit\n")
    menu_in = int(menu_in)
    if (menu_in == 1):
        start_select()
    elif (menu_in == 2):
        load()
    elif (menu_in == 3):
        sys.exit()
    else:
        print("You've entered an invalid option: " + str(menu_in))
        start_menu()

#starting game text
def game_start(level, character):
    print("You have chosen " + character.name + " to fight through a dungeon of dangerous monsters!\n")
    print("You will now start at the first level.  You can save your progress at the end of each level by pressing save.\n")
    print("Copy the code it gives you to another file.  You'll need it... \nBecause all eventually fall!\n")
    if character.name == "Uncle Joel":
        print("Or, at least you would if you weren't playing as me! But that's ok, everything is allowed in this game.\n")
    print("""The goal is to get as far as you can because the game is simply too hard!
Though now that I think about it, I did put this together in a hurry. There are some inintentional mistakes that could *SAVE* you.
But I don't think you'll find those...
Were you to somehow beat level 10, which you won't, it will give you a code to send me.
But it's not going to happen, because you would have to be a sneaky genius to get that far!
    """)
    game(level, character)

#character selection
def start_select():
    def char_select():
        print("Who will you select as your champion? Beware, you must fight a great many monsters!\n\n press 'i' for more information or")
        print("make your selection below: \n 1) Phinneas\n 2) Cole\n 3) Stella\n 4) Silas")
        select_in = input()
        if (select_in == 'i' or select_in == "I"):
            print("""
       Phinneas is the toughest of the bunch! He has the most health and can survive the toughest monsters.  He can also regenerate health!

       Cole doesn't have as much health as Phinneas, and doesn't attack as strongly as Stella, but he's good at both. Plus, he's a nina and
       can dodge enemy attacks!

       Stella would be vulnerable to enemy monsters. . . if she wasn't so quick at attacking them and destroying them with a single blow.
       In fact, Stella is a wizard of great renown--just wait until she starts calling down meteors! She is also nimble, and can dodge a bit!

       Silas is the youngest of the champtions, but that doesn't mean he's the weakest.  He can make make objects come alive to protect him 
       or defeat his enemies!
            """)
            char_select()
        elif select_in == 'j':
                player.name="Uncle Joel"
                player.health=999
                player.attack=999
                player.dodge=5
                player.special=5
                game_start(1, player)
        else:
            select_in = int(select_in)
            if select_in == 1:
                player.name="Phinneas"
                player.health=800
                player.attack=200
                player.dodge=0
                player.special=1
            if select_in == 2:
                player.name="Cole"
                player.health=500
                player.attack=400
                player.dodge=3
                player.special=1
            if select_in == 3:
                player.name="Stella"
                player.health=300
                player.attack=700
                player.dodge=1
                player.special=1
            if select_in == 4:
                player.name="Silas"
                player.health=400
                player.attack=200
                player.dodge=0
                player.special=4
            #else:
                #print("Your selection was invalid")
            game_start(1, player)

    char_select()

#generate an encoded savefile. We obfuscate the level--we will mod 16 on load.
def save(level, character):
    mod_level = level*16+level
    save_string="level:"
    save_string+=(str(mod_level)+";")
    save_string+="name:"+ character.name + ";"
    save_string+="health:"+ str(character.health) + ";"
    save_string+="attack:"+ str(character.attack) + ";"
    save_string+="dodge:"+ str(character.dodge) + ";"
    save_string+="special:"+ str(character.special) + ";"
    save_string = save_string.encode("utf-8")
    encoded=base64.b64encode(save_string)
    print("Your save code is: " + str(encoded) + "\nOnly copy the characters between the quotation marks (\').\n")

#load gamefile
def load():
    encoded=input("Enter your save code: ")
    plain=str(base64.b64decode(encoded))
    plain=str(base64.b64decode(encoded))
    #print(plain)
    info = plain.split(";")
    info[0] = info[0].replace("b'level:","")
    info[1] = info[1].replace("name:","")
    info[2] = info[2].replace("health:","")
    info[3] = info[3].replace("attack:","")
    info[4] = info[4].replace("dodge:","")
    info[5] = info[5].replace("special:","")
    
    #level is saved as a multiple of 16 + value, so mod 16 to get it back
    level = (int(info[0]))%16
    name = info[1]
    health = info[2]
    attack = info[3]
    dodge = info[4]
    special = info[5]
    
    player.name = name
    player.health = health
    player.attack = attack
    player.dodge = dodge
    player.special = special
    
    #if the save file puts them past max level, send them to the win screen.
    if level > 10:
        won(player)

    game(level, player)

def get_item(item, character):
    selection = item%10
    weapons = ["Wand of fire", "Sword of the sun", "Greatsword of Gondor", "Elegant quarterstaff", "Glistening rapier", "Damascus steel scimitar"]
    armor = ["Mithril vest", "Engraved platemail", "Spiked Helmet", "Greek Aspis", "Kite Shield"]

    if selection <=3:
        damage_bonus = (random.randint(10,20))*10
        print("You received a " + random.choice(weapons) + " that gives you " + str(damage_bonus) + " extra attack power!")
        character.attack+=damage_bonus
    elif selection <=7:
        health_bonus = (random.randint(10,20))*10
        print("You received a " + random.choice(armor) + " that gives you " + str(health_bonus) + " extra health!")
        character.health+=health_bonus
    elif selection == 8:
        print("You found a piece of ninja armor, increasing your ability to dodge!")
        character.dodge+=1
    elif selection == 9:
        print("You found a tome of inspiration, giving you the ability to use your special power one more time!")
        character.special+=1

#Core function for each room
def game(level, character):
    os.system('cls||clear')
    enemies = get_enemies(level+(level//2))
    turn = 1
    moon = Character(name="Malevolent moon", health = 5000, attack = 0, challenge = 0)

    if (level <10):
        print("***You enter room " + str(level) + "***\n\n")
    if (level==10):
        
        enemies.append(moon)
        print("""
You enter the final room and discover it is not much of a room at all. It has no ceiling!
Then you hear it... the moon! The moon is angry with you. You have been killing its moon creatures!

'You cannot stop me' whispers the moon in your head.  'In time, I shall succeed.  Observe.'

You feel your time is limited before the moon defeats you. And to make things worse, the moon
summons monsters.  You have a feeling these will not be the last either...
""")
        

    while len(enemies)!=0:
        if (moon in enemies):
            if moon.health > 0:
                potential_summon=[giant, wizard, lion, robot, dragon, dragon2, shark]
                summon = random.choice(potential_summon)
                enemies.append(summon)
                print("The moon summons a " +  summon.name + "!")
                              
            else:
                won(character)
        print("You see:\n")
        for enemy in enemies:
            print("a " + enemy.name + ",    health: " + str(enemy.health) + "   attack: " + str(enemy.attack))
        print("\nYour have: " + str(character.health)+ " health, " + str(character.attack) + " attack, " + str(character.h_potion) + " health potions, " 
                + str(character.grenade) + " grenades, and " + str(character.special) + " uses of your special ability.\nWhat would you like to do?\n ") 
        g_in = input("1) attack, 2) use health potion, 3) use grenade, 4) use special ability\n")
        g_in = int(g_in)
        if g_in == 1:
            print("Who do you want to attack?")
            i = 1
            for enemy in enemies:
                print(str(i) + ") " +enemy.name + "\n")
                i+=1
            attack = input()
            attack = int(attack)
            print("You attack the " + enemies[attack-1].name + " for " + str(character.attack) + " damage!\n")
            if enemies[attack-1].health > character.attack:
                enemies[attack-1].health = (enemies[attack-1].health - character.attack)
            else:
                print("Your attack killed the " + enemies[attack-1].name + "!\n")
                if enemies[attack-1].name=="Malevolent moon":
                    won(character)
                del enemies[attack-1]
        if g_in == 2:
            if character.h_potion != 0:
                print("You use a health potion and gain 300 health!\n")
                character.health+=300
                character.h_potion -= 1
            else:
                print("You reach down for a health potion, but there isn't one! What a waste!")
        if g_in == 3:
            if character.grenade != 0:
                print("You throw a grenade and deal 150 damage to all the enemies!")
                i = 0
                while i < len(enemies):
                    enemies[i].health = enemies[i].health-150
                    i+=1
                i = 0
                while i < len(enemies):
                    if enemies[i].health <= 0:
                        if enemies[i].name=="Malevolent moon":
                             won(character)
                        del enemies[i]
                    i+=1
                character.grenade -= 1
            else: 
                print("You reach down for a grenade, but there isn't one! What a waste!")
        if g_in == 4:
            if character.special != 0:
                if character.name == "Phinneas":
                    print("You focus and start to grow! Your health triples!")
                    character.health = character.health*3
                    character.special = character.special - 1
                if character.name == "Cole":
                    print("You reflect on your ninja training. Time slows down. You begin to dodge with ease!")
                    character.dodge = 4
                    character.special = character.special - 1
                if character.name == "Stella":
                    print("You concentrate and call on meteors to fall on your enemies! They deal 800 damage to every monster!")
                    i = 0
                    while i < len(enemies):
                        enemies[i].health = enemies[i].health-150
                        i+=1
                    i = 0
                    while i < len(enemies):
                        if enemies[i].health <= 0:
                             if enemies[i].name=="Malevolent moon":
                                won(character)
                             del enemies[i]
                        i+=1
                    character.special = character.special - 1
                if character.name == "Silas":
                    print("You look around and find objects to animate! Toys, walls, trees, they all come to your aid!")
                    flip = random.randint(0,1)
                    if flip==0:
                        print("The objects form a living barrier in front of you, sentient chairs float poised to block enemy swords!\nYou gain 500 health!")
                        character.health+=500
                    if flip==1:
                        e_select = random.randint(0, (len(enemies)-1))
                        print("They rush one of your enemies, dealing 1000 damange to the " + enemies[e_select].name)
                        enemies[e_select].health-=1000
                        if enemies[e_select].health<=0:
                            if enemies[e_select].name=="Malevolent moon":
                                won(character)
                            del enemies[e_select]
                    character.special = character.special - 1
                if character.name == "Uncle Joel":
                    character.health+=500
                    character.attack+=500
                    character.dodge+=1
                    character.special = character.special - 1

        #enemies left alive attack attack
        for enemy in enemies:
            if enemy.health <= 0:
                enemies.remove(enemy)
            print(enemy.name + " attacks you for " + str(enemy.attack) + " damage!\n")
            dodge = random.randint(0, 9)
            if dodge>character.dodge:
                character.health = (character.health - enemy.attack)
            else:
                print("You dodge its attack!\n")
        if character.health <=0:
            print("You have been slain. Game over.  Press 'q' to quit.")
            q = input()
            if q == 'q':
                exit()

    print("You have slain all the monsters in this room! Good job! You gain some health\n")
    character.health+=100
    item = input("As a reward a traveling merchant offers you a surprise item. Pick a number: ")
    get_item(int(item)+level, character)

    end_room = input("Would you like to:\n 1) continue without saving, 2) save and quit, 3) save and continue?")
    end_room=int(end_room)
    if end_room == 1:
        game(level+1, character)
    if end_room == 2:
        save(level+1, character)
        i=input("press any key to quit")
        exit()
    if end_room == 3:
        save(level+1, character)
        i=input("press any key to continue")
        game(level+1, character)

 
def won(character):
    victory_flag="ZmxhZz17Zm9sbG93X3RoZV93aGl0ZV9yYWJiaXR9"
    plain_flag=str(base64.b64decode(victory_flag))
    print("You," + character.name + " have done it!  You have bested the monsters and emerged victorious!\n")
    print("The code to send is: " + plain_flag)

def test(player):
    player.name = "test"
    player.attack = 10000
    player.health = 50000
    player.dodge = 5

    game(10, player)

#run things
player = Character()   
print("HELLO WINSLOW CHILDREN\n")
start_menu()


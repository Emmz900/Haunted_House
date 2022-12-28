from room import Room
from item import Item, Open_Item
from character import Character, Enemy
from rpginfo import RPGInfo

# rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
servers_room = Room("Servers Room")

# descriptions
kitchen.set_description("It is dark and musty, "
                        "the room is still littered with plates and bowls now covered in cobwebs.")
ballroom.set_description("The space feels large and empty. "
                         "Although leaves and dirt now layer the floor it was clearly very grand and ornate"
                         " in it's day."
                         " Dust sheets cover piles of furniture and the walls are still full of "
                         "exquisite decorations.")
dining_hall.set_description("The large mahogany dining table fills the center of the room. "
                            "Nothing but bones and crumbs remain from the last feast that was served here.")
servers_room.set_description("This is a small cramped space, "
                             "you have to weave carefully between the stacked tables to get through.")
# links
kitchen.link_room(ballroom, "south")
kitchen.link_room(servers_room, "west")
ballroom.link_room(dining_hall, "west")
ballroom.link_room(kitchen, "north")
dining_hall.link_room(servers_room, "north")
dining_hall.link_room(ballroom, "east")
servers_room.link_room(kitchen, "east")
servers_room.link_room(dining_hall, "south")

# characters
fenris = Enemy("Fenris", "He is a shaggy dark werewolf pacing the far end of the room. "
                         "He seems to tolerate your presence, for now.")
fenris.set_conversation("Grrrr....you don't belong here....")
fenris.set_weakness("gun")
fenris.set_hug("His fur looks so soft and cozy but he growls menacingly as you approach, "
               "seems he doesn't want a hug...")
#fenris.set_dead("The werewolf's body lays at the edge of the room where you slayed him.")

creepers = Enemy("Creepers", "He is a slow moving zombie. "
                             "You can easily stay out of reach as you walk around the room"
                             " with the dining table between you.")
creepers.set_conversation("Ugghh.....brains.....yum....")
creepers.set_weakness("pan")
creepers.set_hug("Hugging a zombie who wants to eat your brains seem like a bad idea!")
#creepers.set_dead("Creepers is laying on the floor, "
                  #"it is unclear whether you have simply knocked him out or if he's really dead.")

count_doom = Enemy("Count Doom", "He is a deathly white vampire asleep in his coffin.")
count_doom.set_conversation("Why have you woken me from my slumber? Have you come to offer yourself as my feast? MMMM!")
count_doom.set_weakness("sharpened pole")
count_doom.set_hug("No way are you putting your neck that close to those fangs.....")
#count_doom.set_dead("There is a pile of dust on the floor that used to be Count Doom.")

jane = Character("Jane", "She is a sad, ill looking, ghost still dressed in her maids outfit.")
jane.set_conversation("A visitor! How splendid! "
                      "If you want to explore this place please be careful of the monsters, "
                      "they each only have one vulnerability so you'll need the right tools to fight them. "
                      "Some rooms have multiple secrets to discover.")
jane.set_hug("Hugging a ghost is tricky but she throws her spectral arms around you and grins. "
             "You feel shivers embrace your body but she looks so happy!")

mr_mouse = Character("Mr Mouse", "He is a very respectable looking little mouse!")
mr_mouse.set_conversation("Hem hem. I am Mr Mouse at your service kind person. "
                          "I do hope you've brought me some cheese? No? Well, good day to you then!")
mr_mouse.set_hug("He looks at you curiously then scampers into your arms and curls up next to your warm body heat, "
                 "awww!")

# place in room
ballroom.set_character(fenris)
dining_hall.set_character(creepers)
kitchen.set_character(jane)
servers_room.set_character(mr_mouse)

# items (name, description, room?)
fists = Item("fists")
fists.set_description("They are your hands....")

pan = Item("pan")
pan.set_description("It is a heavy well worn frying pan that would be perfect for knocking someone out with.")
kitchen.set_item(pan)

brick = Item("brick")
brick.set_description("It is solid and heavy, could be good for throwing if you have the strength?")
ballroom.set_item(brick)

dagger = Item("dagger")
dagger.set_description("It is small and ivory and still looks to be in perfect condition.")

cheese = Item("cube of cheese")
cheese.set_description("The small cube of cheese has been well preserved in the cabinet drawer.")

gun = Item("gun")
gun.set_description("It is a small pistol loaded with a silver bullet.")

sharpened_pole = Item("sharpened pole")
sharpened_pole.set_description("That is better, the end is now a sharpened point.")

silver_key = Item("silver key")
silver_key.set_description("It looks too small to be for a door. What else could it open?")

# open_items (name, description, set interaction, set key, set portable, link)
pole = Open_Item("pole")
pole.set_description("It is large and wooden. The original use is unclear but the ends are rounded. "
                     "Perhaps there is something to sharpen it with lying around?")
pole.set_interaction("You carefully sharpen one end of the pole with the dagger.")
pole.set_key(dagger)
pole.set_portable(True)
pole.link_items(sharpened_pole)
servers_room.set_open_item(pole)

coffin = Open_Item("coffin")
coffin.set_description("In the corner there is a perfectly clean black coffin with gold engravings.")
coffin.set_interaction("You carefully lift the heavy lid on the coffin to reveal it's contents. You see ")
coffin.set_key(None)
coffin.set_portable(False)
ballroom.set_open_item(coffin)
coffin.link_items(count_doom)

cabinet = Open_Item("cabinet")
cabinet.set_description("It is very large and wooden with carvings and paintings inlaid"
                        " and many drawers and cupboards.")
cabinet.set_interaction("You search through the doors and cupboards that you can open.")
cabinet.set_key(None)
cabinet.set_portable(False)
cabinet.link_items(cheese)
dining_hall.set_open_item(cabinet)

locked_box = Open_Item("locked box")
locked_box.set_description("When you blow away the dust intricate carvings are revealed of what looks like "
                           "a wolf's head. The box is locked firmly shut.")
locked_box.set_interaction("The key fits perfectly. You unlock the box and carefully open the lid.")
locked_box.set_key(silver_key)
locked_box.link_items(gun)
locked_box.set_portable(False)
kitchen.set_open_item(locked_box)

# if given cheese, give silver key. if dead give dagger
mr_mouse.set_loot(silver_key)
creepers.set_loot(dagger)

# item combat
pan.set_win("You bash creepers over the head with the pan and he falls to the ground. That was easy!")
pan.set_lose("You lunge forward with the pan but it's quickly knocked out of your hands. You're in trouble now")
brick.set_lose("You toss the brick at the enemy and miss. That was embarrassing.")
brick.set_win("You toss the brick and somehow hit! That's not supposed to happen.")
gun.set_win("You aim across the room and pierce the wolf's heart with the silver bullet. He collapses.")
gun.set_lose("You aim the gun and fire. Your aim is true but it seems they are immune to bullets! "
             "They are coming for you now!")
pole.set_lose("You try to bash them with the blunt pole, they snap it in half and throw it to the floor. "
              "Now you're in trouble.")
pole.set_win("You magically knock them out with the old pole, how on earth did you manage that?")
sharpened_pole.set_win("You lunge forward and pierce Count Doom's heart with the wooden stake. He crumbles instantly")
sharpened_pole.set_lose("You try to stab them with the pole, they snap it in half and throw it to the floor. "
                        "Now you're in trouble.")
dagger.set_lose("You try to slash at them with the dagger but you just can't get close enough. "
                "They lunge forward.")
cheese.set_lose("You throw the cheese, they look at you curiously. That didn't achieve anything!")
silver_key.set_lose("You throw the key in their direction, it bounces back onto the floor achieving nothing.")
fists.set_lose("You run towards them and start punching with your fists. They fight back.")


# methods
def check_bag(thing):
    key_1 = str(thing)
    present = False
    for i in inventory:
        if i == key_1:
            present = True
        else:
            pass
    return present


def add_to_bag(thing):
    thing = thing.get_name()
    inventory.append(thing)
    print("You place the " + thing + " in your bag. "
                                     "To see you bag or interact further type 'i' or 'inventory at any time.")

# allow movement
current_room = kitchen

# statements
dead = False
finished = False
new_room = True

# inventory
inventory = ["fists"]
Item.bag["fists"] = fists

# Introduction
haunted_house = RPGInfo("The Haunted House")
print("---------------------------------------")
haunted_house.welcome()
RPGInfo.info()
print("")
print("You have been travelling through the dark woods for many hours... ")
print("When you stumble upon an old abandoned mansion. You step through the old servants door into the first room.")
print("Good luck and beware!")

#BODY OF THE GAME
while not dead and not finished:
    # tells you where you are
    if new_room:
        print("")
        current_room.get_details()
        print("What would you like to do?")
        print("You can move on to a new room (direction), "
              "investigate this room ('search'), or talk or fight with any inhabitants ('talk'/'fight')")
    else:
        print("You can move (direction), 'search', 'talk', 'fight', 'inventory'/'i' or "
              "'describe' for a reminder of your surroundings.")

    # user inputs option
    command = input("> ")
    command_fixed = command.lower()
    inhabitant = current_room.get_character()

    # movement
    if command_fixed in ["north", "south", "east", "west"]:
        current_room = current_room.move(command_fixed)
        new_room = True  # would be better only if moving actually changes room....

    # search and interact
    elif command_fixed == "search" or command_fixed == "investigate":
        new_room = False
        thing = current_room.get_item()
        open_thing = current_room.get_open_item()

        # if there is a normal item
        if thing is not None:
            print("You search the room for something useful or interesting.")
            thing.describe()
            add_to_bag(thing)
            current_room.set_item(None)

        # if there is an interactive item
        elif open_thing is not None:
            print("You search the room for something useful or interesting.")
            open_thing.describe()
            if inhabitant == fenris and open_thing == coffin:
                print("The werewolf is standing in the way of getting any closer to the coffin. "
                      "You will need to get him out of the way first.")

            # if it doesn't need a key to open it, open
            elif open_thing.get_key() is None:
                action = input("Would you like to investigate further? ")
                if action == "yes":
                    new = open_thing.open()
                    if new == count_doom:
                        current_room.set_character(count_doom)
                    else:
                        add_to_bag(new)
                    current_room.set_open_item(None)
                else:
                    pass

            # else if it does need a key....(elif open_thing.get_key() is not None)
            else:
                key_1 = open_thing.get_key()

                # if the item can be picked up choose, otherwise interact
                if open_thing.portable:
                    resp = input("Would you like to pick this item up ('pick') or interact further 'interact': ")
                    if resp == "pick" or resp == "pick up":
                        add_to_bag(open_thing)
                        current_room.set_open_item(None)
                    elif resp == "interact":
                        pass
                    else:
                        print("That's not an option.")
                else:
                    resp = "interact"

                if resp == "interact":
                    print("Inventory: {}".format(", ".join(inventory)))
                    attempt = True
                    while attempt:
                        interact = input("Which item from your inventory would you like to use to interact further "
                                         "(type 'end' to go back to the room for now)?: ")
                        # can this be changed the second time it runs on an object to include end instructions?
                        if check_bag(interact) or interact == "end" or interact == "no":
                            key = Item.get_item(interact)
                            if interact == "end" or interact == "no":
                                attempt = False
                                if open_thing.portable:
                                    add_to_bag(open_thing)
                                    current_room.set_open_item(None)
                                else:
                                    pass
                            elif open_thing.open_with_key(key):
                                attempt = False
                                current_room.set_open_item(None)
                                new_item = open_thing.get_linked_item()
                                add_to_bag(new_item)
                            else:
                                attempt = True
                        else:
                            print("You do not have that item.")
                else:
                    pass

        else:
            print("You search through the cobwebs and dirt but find nothing.")

    # talk to inhabitants
    elif command_fixed == "talk":
        new_room = False
        if inhabitant == mr_mouse and check_bag("cube of cheese"):
            print("[Mr Mouse says]: Hem hem. I am Mr Mouse at your service kind person. "
                  "I do hope you've brought me some cheese?")
            print("You pull the cube of cheese out of your bag and hold it out for him. "
                  "He quickly snatches it out of your hands and smells it deeply.")
            inventory.remove("cube of cheese")
            print("[Mr Mouse says]: Mmmmm! It is exquisite! Thank you dear friend. "
                  "Here in return have this key I found.")
            silver_key.describe()
            add_to_bag(silver_key)
            mr_mouse.set_conversation("Thank you for this cheese. I will savour it for as long as possible.")
        elif inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one here to talk to. You hum a little tune to yourself")

    # hug inhabitants
    elif command_fixed == "hug":
        new_room = False
        if inhabitant is not None:
            inhabitant.hug()
        else:
            print("You are all alone, you hug yourself tightly and feel a little better.")

    # fight with an enemy!
    elif command_fixed == "fight" and isinstance(inhabitant, Enemy):
        new_room = False
        if inhabitant is not None:
            if len(inventory) > 1:
                print("You have collected: {}".format(", ".join(inventory)))
                #could add option so they can back out after seeing inventory?
                print("What will you fight with?")
                weapon = input("> ")
                battle = False
                for i in inventory:
                    if i == weapon:
                        battle = True
                    else:
                        pass
                if battle:
                    print("You fight " + inhabitant.get_name() + " with your " + weapon)
                    if weapon == "cheese" or weapon == "brick" or weapon == "silver key":
                        weapon = Item.get_item(weapon)
                        print(weapon.get_lose())
                        if current_room.get_item() is None:
                            inventory.remove(weapon.get_name())
                            current_room.set_item(weapon)
                        else:
                            print("You sheepishly pick up the " + weapon.get_name() + " and put it back in your bag.")
                    elif inhabitant.fight(weapon):
                        weapon = Item.get_item(weapon)
                        weapon.win_fight()
                        loot = inhabitant.give_loot()
                        current_room.set_character(None)
                        if loot is not None:
                            print("Something falls from his pocket. You look closer.")
                            loot.describe()
                            add_to_bag(loot)
                        else:
                            pass
                        # can i add dead characters on the floor? turn them into items or in the room description?
                    else:
                        weapon = Item.get_item(weapon)
                        weapon.lose_fight()
                        print("The world fades to black....it is over.")
                        dead = True
                else:
                    print("You do not have that object. Choose an object from your inventory.")
            else:
                print("You have not collected any items. You will fight with your fists!")
                fists.get_lose()
                print("You have died. Press play to try again.")
                dead = True
        else:
            print(
                "There's no one to fight here. You jab your fists in the air and kick your legs anyway: 'hyah, hyah!'")
        if Enemy.number_of_enemies == 0:
            finished = True
        else:
            finished = False

    # try to fight with a friendly character
    elif command_fixed == "fight" and isinstance(inhabitant, Character):
        new_room = False
        inhabitant.fight("fists")

    # try to fight in an empty room
    elif command_fixed == "fight" and current_room.get_character() is None:
        new_room = False
        print("There's no one to fight here. You jab your fists in the air and kick your legs anyway: 'hyah, hyah!'")

    # check inventory
    elif command_fixed == "i" or command_fixed == "inventory":
        new_room = False
        print("Inventory: {}".format(", ".join(inventory)))
        item1 = input("Would you like to investigate any of these items further? Type an item name or 'no': ")
        if item1 == "no":
            print("You close your bag and go back to the room")
        else:
            if check_bag(item1):
                #print("You pick up the " + item1)
                item1 = Item.get_item(item1)
                print(item1.get_name() + ": " + item1.get_description())
                attempt = True
                while attempt:
                    item2 = input("Choose an object to combine with this or type 'end' to go back: ")
                    if check_bag(item2):
                        item2 = Item.get_item(item2)
                        if item1.test_key(item2.get_name()):
                            item1.open_with_key(item2.get_name())
                            inventory.remove("pole")
                            add_to_bag(sharpened_pole)
                            attempt = False
                        elif item2.test_key(item1.get_name()):
                            item2.open_with_key(item1.get_name())
                            inventory.remove("pole")
                            add_to_bag(sharpened_pole)
                            attempt = False
                        elif item2 == "end":
                            attempt = False
                        else:
                            item1.open_with_key(item2.get_name())
                    elif item2 == "end":
                        attempt = False
                    else:
                        print("You do not have that item")
            else:
                print("You do not have that item.")

    #describe the room again
    elif command_fixed == "describe":
        new_room = False
        current_room.get_details()

    #any other input doesn't work
    else:
        new_room = False
        print("You can't do that.")

#Once all the monsters have been slain finish the game
if finished:
    print("")
    print("Well done, you have defeated all the monsters in the haunted house! You are awesome!")
    print("I hope you had fun :)")
    print("")

print("")
RPGInfo.author = "Emma Menzies"
RPGInfo.credits()

# vampire drop key to upstairs?
# house plan? Populate with items and monsters as you go?

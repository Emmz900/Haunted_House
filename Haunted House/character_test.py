from room import Room
from item import Item, Open_Item
from character import Character, Enemy
from rpginfo import RPGInfo

start = Room("start")
current_room = start

inventory = ["fists", "bowl"]

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Uuuuggghhhh. Muuust eat braaainsss!")
dave.set_weakness("cheese")

count_doom = Enemy("Count Doom", "He is a deathly white vampire")
count_doom.set_conversation("Why have you woken me from my slumber? Have you come to offer yourself as my feast? MMMM!")
count_doom.set_weakness("sharpened pole")
count_doom.set_hug("No way are you putting your neck that close to those fangs.....")

bowl = Item("Bowl")
bowl.set_description("A round implement for holding food.")

coffin = Open_Item("coffin")
coffin.set_description("In the corner there is a perfectly clean black coffin with gold engravings.")
coffin.set_interaction("You carefully lift the heavy lid on the coffin to reveal it's contents. You see ")
coffin.set_key(None)
coffin.set_portable(False)
start.set_open_item(coffin)
coffin.link_items(count_doom)

dave.set_loot(bowl)

print(*inventory, sep=', ')
print("Inventory: {}".format(", ".join(inventory)))
#bowl.describe()
#print(bowl)
#thing = Item.get_item("spoon")
#print(thing)
#thing.describe()
#print(Item.get_item('Bowl'))
#print(Item.bag)

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

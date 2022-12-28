got_pole = False
got_dagger = False
for item in inventory:
    if item == "pole":
        got_pole = True
    elif item == "dagger":
        got_dagger = True
    else:
        pass
if got_pole and got_dagger:
    resp = input("Would you like to investigate any of these items further? ")
    if resp == "yes":  # give descriptions? let you choose anything in inventory
        print("You pick up the pole and look at it carefully. "
              "There must be a way to make this useful somehow....")
        poss = True
        while poss:
            action = input("Which item would you like to combine with the pole? "
                           "(Type 'leave' to give up for now) ")  # make this a separate method in main!?
            if action == "dagger":
                pole.get_interaction()
                thing3 = pole.get_linked_item()
                thing3.describe()
                inventory.append(thing3.get_name())
                print("You place the item in your bag. To see your bag type 'i' or 'inventory at any time.")
                current_room.set_item2(None)
                inventory.remove("pole")
                poss = False
                got_pole = False
            elif action == "leave":
                poss = False
            else:
                print("You bash the items together unsuccessfully. Why would you do that?")

# if the item cannot be picked up
                else:
                    print("Inventory: {}".format(", ".join(inventory)))
                    attempt = True
                    while attempt:
                        interact = input("Which item from your inventory would you like to use to interact further "
                                         "(type 'end' to go back to the room for now)?: ")
                        if check_bag(interact) or interact == "end" or interact == "no":
                            key = Item.get_item(interact)
                            if interact == "end" or interact == "no":
                                attempt = False
                            elif open_thing.open_with_key(key):
                                attempt = False
                                current_room.set_open_item(None)
                                new_item = open_thing.get_linked_item()
                                add_to_bag(new_item)
                            else:
                                pass
                                #print("That doesn't seem to work, maybe another object would be better?")
                        else:
                            print("You do not have that item.")

class Character():

    number_of_characters = 0

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.hug_response = None
        self.loot = None
        self.fave = None
        self.living = True
        Character.number_of_characters = Character.number_of_characters + 1

    # Describe this character
    def describe(self):
        print(self.name + " wanders the room. " + self.description)

    def get_name(self):
        return self.name

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_loot(self, loot):
        self.loot = loot

    def give_loot(self):
        return self.loot

    def get_living(self):
        return self.living

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you. How rude!")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you. Instead they seem to want a hug....?")
        return True

    #hug the character
    def set_hug(self, hug_response):
        self.hug_response = hug_response

    def get_hug(self):
        return self.hug_response

    def hug(self):
        if self.hug_response is not None:
            print(self.hug_response)
        else:
            print("They don't seem to want a hug.")


class Enemy(Character):

    number_of_enemies = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.living = True
        #self.dead_description = None
        Enemy.number_of_enemies = Enemy.number_of_enemies + 1

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def set_living(self, living):
        self.living = living

    #def set_dead(self, dead_description):
        #self.dead_description = dead_description

    def get_dead(self):
        return self.dead_description

    def fight(self, combat_item):
        if combat_item == self.weakness:
            self.living = False
            Enemy.number_of_enemies = Enemy.number_of_enemies - 1
            return True
        else:
            return False

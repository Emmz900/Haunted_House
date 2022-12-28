class Item():

    number_of_items = 0
    bag = {}

    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.key = None
        self.win = None
        self.lose = None
        Item.number_of_items = Item.number_of_items + 1

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def set_win(self, item_win):
        self.win = item_win

    def get_win(self):
        return self.win

    def set_lose(self, item_lose):
        self.lose = item_lose

    def get_lose(self):
        return self.lose

    def win_fight(self):
        print(self.get_win())

    def lose_fight(self):
        print(self.get_lose())

    def test_key(self, key):
        return False

    def describe(self):
        print("You find a " + self.get_name().upper() + ". " + self.get_description())
        Item.bag[self.get_name()] = self

    def open_with_key(self, key):
        print("You bash the items together unsuccessfully.")

    @staticmethod
    def get_item(name):
        for i in Item.bag:
            if i == name:
                return Item.bag[i]
            else:
                pass


class Open_Item(Item):

    def __init__(self, item_name):
        super().__init__(item_name)
        self.interaction = None
        self.linked_item = None
        self.key = None
        self.portable = None

    def set_interaction(self, item_interaction):
        self.interaction = item_interaction

    def get_interaction(self):
        return self.interaction

    def get_portable(self):
        return self.portable

    def set_portable(self, portable):
        self.portable = portable

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def link_items(self, item_to_link):
        self.linked_item = item_to_link

    def get_linked_item(self):
        return self.linked_item

    def test_key(self, key):
        if key == self.key:
            return True
        else:
            return False

    def open(self):
        self.get_interaction()
        new = self.get_linked_item()
        new.describe()
        Item.bag[new.get_name()] = new
        return new

    def open_with_key(self, key):
        if key == self.key:
            self.get_interaction()
            new = self.get_linked_item()
            new.describe()
            Item.bag[new.get_name()] = new
            return True
        else:
            print("You bash the items together unsuccessfully.")

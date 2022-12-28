class Room():

    number_of_rooms = 0
    from character import Character, Enemy

    def __init__(self, room_name):
        """

        :param room_name: The name of the room must be given when creating an instance of the Room class
        """
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.item2 = None
        Room.number_of_rooms = Room.number_of_rooms + 1

    def get_description(self):
        """
        Returns a string containing the description of the room

        :return: str - room description
        """
        return self.description

    def set_description(self, room_description):
        """
        Sets the description of a room

        :param room_description: str
        """
        self.description = room_description

    def set_name(self, room_name):
        """
        Set room name

        :param room_name: str
        """
        self.name = room_name

    def get_name(self):
        """

        :return: str - the room name
        """
        return self.name

    def set_character(self, character):
        """
        Put a character into the room

        :param character: class character instance
        """
        self.character = character

    def get_character(self):
        """
        Return the character that is in the room

        :return: class character instance
        """
        return self.character

    def set_item(self, item):
        """
        Put an item in the room

        :param item: class item instance
        :return:
        """
        self.item = item

    def get_item(self):
        """
        Return the item that was set in the room

        :return: class item instance
        """
        return self.item

    def set_open_item(self, item):
        """
        Put an interactable item in the room

        :param item: Open_item from class Item
        """
        self.item2 = item

    def get_open_item(self):
        """
        Return any interactable items from the room

        :return: Open_item instance from class Item
        """
        return self.item2

    def describe(self):
        """
        Print the description of the room.

        :return: printed string of the room description
        """
        print(self.description)

    def link_room(self, room_to_link, direction):
        """
        Link a room to the current one in a particular cardinal direction

        :param room_to_link: 
        :param direction:
        :return:
        """
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("You are in the " + self.get_name() + ".")
        print(self.description)
        inhabitant = self.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

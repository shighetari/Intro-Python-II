# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        return f'\n Current room:\n {self.name}\n Area description:\n {self.description} \n items in the room: {[(i.name, i.description) for i in self.item]} \n'

    def print_items(self):
        print([i.name for i in self.item])

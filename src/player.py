# Write a class to hold player information, e.g. what room they are in
# currently.
# from adv import player
from item import Item


class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self.inventory = []

    def __str__(self):
        return f'location: {self.location}, name: {self.name}, Current Inventory: {self.inventory}, Inventory: {[i.name for i in self.inventory]} '

    def print_inventory(self, player_name):
        print([item.name for item in self.inventory])

    def move(self, direction, player):
        # movement
        if direction == 'n' and hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
            print('testing north')
            print(player.location)

        elif direction == 'e' and hasattr(player.location, 'e_to'):
            print('testing east')
            player.location = player.location.e_to
            print(player.location)

        elif direction == 's' and hasattr(player.location, 's_to'):
            print('testing south')
            player.location = player.location.s_to
            print(player.location)

        elif direction == 'w' and hasattr(player.location, 'w_to'):
            print('testing west')
            player.location = player.location.w_to
            print(player.location)

        else:
            print('You find your self at a dead end, try another direction!')

    def get(self, command, player):
        if command[0] == 'get' or command[0] == 'take':
            found = False
            print('testing get in player.py')
            if len(command) > 1:
                for item in player.location.item:
                    if command[1] == item.name.lower():
                        found = True
                        # Python list method pop() removes
                        # and returns last object or obj from the list.
                        # .pop() last element .pop(0) first element
                        player.inventory.append(item)
                        Item.take_item(self, player)
                        player.print_inventory(self)
                        player.location.item.remove(item)
                        break
                if not found:
                    print(
                        f'There is no such thing as {command} around here...')
            else:
                print('what do you want exactly?')

    # def drop(self, command, player):
    #     have = False
    #     for item in self.inventory:
    #         if command[1]

    def drop(self, command, player):
        if command[0] == 'drop' or command[0] == 'remove':
            dropped = False
            print('testing drop method in player.py')
        
        
            for item in player.inventory:
                if command[1] == item.name.lower():
                    dropped = True
                    player.inventory.remove(item)
                    player.location.item.append(item)
                    Item.on_drop(self, player)
                    player.print_inventory(self)
                    break

            if not dropped:
                    print(
                        f'You do not have {command} in your inventory')
        else:
                print('what do you want exactly?')







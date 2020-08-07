class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}\n'.format(self=self)

    def take_item(self, player):

        print(f'You pick up a {player.location.item[0]} ')

    def on_drop(self, player):
        print(f'You drop the {self.name}')

    

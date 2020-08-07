from room import Room
from player import Player
from colors import Color
from item import Item
# Declare all the rooms

# Items
item = {
    'gun':  Item("Gun", "use this only when you have no alternative choice!"),
    'dung':  Item("Dung", "It's really just a weaponized bag of poop"),
    'bat':  Item("Bat", "Swing at your foes!"),
    'helmet':  Item("Helmet", "it's old and muddy!"),
    'gems':  Item("Gems", "Wow! A sneak peek for what lay ahead?")
}
room = {
    'outside':  Room("🌑 Outside Cave Entrance 🌑",
                     "⬆️  North of you, the cave mount beckons", [item['gun']]),

    'foyer':    Room("🏨 Foyer 🏨", """Dim light filters in from the south ⬇️. Dusty
passages run north ⬆️  and east ➡️.""", [item['dung']]),

    'overlook': Room("⛰️ Grand Overlook ⛰️", """A steep cliff appears before you, falling
into the darkness. Ahead to the north ⬆️ , a light flickers in
the distance, but there is no way across the chasm.↪️""", [item['bat']]),

    'narrow':   Room("🛣️ Narrow Passage 🛣️", """The narrow passage bends here from west ⬅️
to north ⬆️. The smell of gold permeates the air. 🔝""", [item['gems']]),

    'treasure': Room("👑 Treasure Chamber 👑", """🎆🎇🙌🎉🎈🥂 \n You've found the long-lost treasure chamber! \n🥂 🎈🎉🙌🎇🎆 \n Sadly, it has already been completely emptied by earlier adventurers.\n The only exit is to the south. ⬇️🔚""", [item['helmet']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print(f"\n 👋🧞 Hey there stranger! My name is Geni Boebeani \n I'm here to guide you on this adventure game I suppose...")
print(f" Well I guess you can start off by telling me your name? After all I am going to be serving you 🙄 \n")

# print('\033[1m' + 'This is my text string.' + '\033[0m') tried to get bold text to work via classes and then this directly lol.
player_name = input("Enter your player name here: ")
player = Player(room["outside"], player_name)
print(f"\nWelcome to this weird game I'm working on {player_name}!")
print(
    f"Here is a quick summary of where you currently are:\n {player.location}")
# print(f"testing room item:\n {player.location.item}")


# print(player)

# Write a loop that:
while True:
    # print(player_name)

    command = input(
        f"🧞 \nWhat do you want to do, {player_name}?\n Enter your command here:").lower().split()
    # print(player.location)

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    

    # if len(command) == 1:
    #     command = command[0]
        # print("You wish to:", command)

    if command[0] == "q":
        print("You pressed Q to quit! Cya later mate")
        break

    # if command in ['s', 'n', 'w', 'e']:
    #     print(' 🏃 You chose to wonder off! Let us see where your adventures take you! 🌇 ')
    #     player.move(command[0])
    if command[0] == 'n':
        print('You choose to move north!')
        player.move(command[0], player)
        # player = Player(room["foyer"], player_name)
        # print(player)

    if command[0] == 's':
        print('You choose to move south!')
        player.move(command[0], player)

    if command[0] == 'e':
        print('You choose to move east!')
        player.move(command[0], player)

    if command[0] == 'w':
        print('You choose to move west!')
        player.move(command[0], player)

    # if len(command) > 1:g
    #     print('\n INPUT ERROR: Please enter a valid command.\n A command uses only 1 string input.\n example: enter in q to quit the game or n, w, s, e \n North ⬆️  West ⬅️  South ⬇️  East ➡️ \n')
    if command[0] == 'get' or command[0] == 'take':
        print('testing GET')
        player.get(command, player)
    if command[0] == 'drop' or command[0] == 'remove':
        print('testing DROP')
        player.drop(command, player)

import random, time, sys


name = input('A whimsical journey awaits you, enter your name to get started! ')
print(f"Hello {name}! Welcome to Dreamer's Dilemma; before the game begins, you'll play a quick tutorial.")
inventory = []

def follow_the_voice():
    """Function for the storyline when the player chooses to follow the voice."""
    print("You walk towards the voice...")
    time.sleep(2)
    print("The haunting voice compels you, you follow the echo.")
    time.sleep(2)
    print("It has you in a trance. You can only obey.")
    time.sleep(3)
    print('You reach a forest.')
    time.sleep(2)
    print(f"{name}, I know you're near, {name}, come here my dear.")
    time.sleep(3)
    print("The voice is clearer than ever. You follow its sound closely.")
    time.sleep(2)
    print('You finally see the source of the voice.')
    time.sleep(2)
    print('A frail old lady sits near a large pine tree.')
    time.sleep(2)
    print('She turns to face you..')
    time.sleep(1)
    print('"You\'re not from around here.. I can sense it."')
    time.sleep(2)
    print('"Come close my dear, I won\'t bite, I\'ll send you home" ')
    time.sleep(3)
    print('After some hesitation you approach her...')
    time.sleep(3)
    print('"Free you that I can do, but do it for free I cannot"')
    time.sleep(3)
    print('You start to look to see if you have anything to offer..')
    time.sleep(1)

    # Check inventory for valuable items
    if 'warm jacket' in inventory or 'rope' in inventory:
        print("You remember you do have an item worth something.. ")
        time.sleep(0.5)
        print("You offer it to the old lady without a hitch...")
        time.sleep(1)
        print("Thank you my dear, Now close your eyes, it'll be over soon..")
        time.sleep(3)
        print('You wake up suddenly, feeling comfortable.')
        time.sleep(1)
        print("You're safe in your bed, you have successfully returned home. Ending 6/6 discovered! ")
        time.sleep(1)
        sys.exit()
    else:
        print("You quickly realise you have nothing to offer.")
        time.sleep(0.5)
        print("You relay the message to the old lady..")
        time.sleep(1)
        print('She looks at you with a sharp look,"That\'s okay my dear.." ')
        time.sleep(1)
        print('"Just shut your eyes for me.. you\'ll leave this place soon"')
        time.sleep(3)
        print(f'... You awake in a dark, dim room. You faintly hear "{name}, {name}" calling on loop in the background.')
        time.sleep(2)
        print('You inspect the room further, you notice two possible exits.')
        time.sleep(1)
        print("You're back at the beginning, she's cursed you into an infinite loop!!! Ending 5/6 discovered! ")
        time.sleep(1)
        sys.exit()

def merchant_encounter():
    """Function for the merchant encounter."""
    print("As you continue to walk, you encounter a merchant.")
    time.sleep(0.5)
    print('They offer you a deal, "One Gold for your strong rope?",')
    merchant = input("Do you accept the trade? \033[3mYes\033[0m or \033[3mNo\033[0m ")

    if merchant.lower() == 'yes' and 'rope' in inventory:
        print("You accept the trade, you no longer have rope.")
        inventory.remove('rope')
        inventory.append('gold coin')
        print('Your inventory has been updated.')
        print(inventory)
    elif merchant.lower() == 'no':
        print("You decline the trade, you keep your rope.")
    else:
        print("You don't have the rope to trade.")

def snowy_town_scene():
    """Function for the snowy town scene."""
    print('You keep on moving. Soon you start feeling a cold breeze.')
    time.sleep(0.5)
    print("This doesn't seem right.. you find yourself approaching a snowy town.")
    snow = input("Do you go \033[3minto\033[0m or \033[3maround\033[0m the town? ")

    if snow == 'into':
        print("You walk into town.")
        time.sleep(1)
        print('You encounter a shop.')

        if 'gold coin' in inventory:
            print("You buy yourself a warm jacket to stay warm.")
            inventory.remove('gold coin')
            inventory.append('warm jacket')
        else:
            print('You regret not trading for a gold coin earlier.')
            time.sleep(2)

        print("The eerie feeling of the town gives you no comfort.")
        print("You decide to head in the direction of the earlier voice.")
        follow_the_voice()  # Continues with the voice function

    elif snow == 'around':
        # Ditch life/death situation if going around the town
        print('You walk around town avoiding its buildings.')
        time.sleep(1)
        print('You stomp through the snow.')
        time.sleep(0.5)
        print("You aren't paying attention to where you're going.")
        time.sleep(1)
        print("THUD!")
        time.sleep(1)
        print("You have fallen into a ditch. It's cold and you don't have much time")

        # Check for rope to escape the ditch
        if 'rope' in inventory:
            print("You're grateful that you kept the rope, you haul yourself out.")
            time.sleep(1)
            print("You look down, considering if the rope is worth taking with you.")
            inventory.remove('rope')

            rope_choice = input("Do you risk taking the rope out with you? \033[3mYes\033[0m or \033[3mNo\033[0m? ")

            if rope_choice.lower() == 'yes' and random.choice([True, False]):
                print("Luck is on your side! You manage to keep the rope.")
                inventory.append('rope')
            else:
                print("Unfortunately, the rope slips from your grasp and is lost.")
            print("Confused on what else to do, you start heading in the direction of the voice.")
            follow_the_voice()
        else:
            print("You don't have a rope to escape.")
            print("With no way to get out, you accept your fate.")
            time.sleep(2)
            print('You succumb to the elements... Ending 4/6 discovered!')
            time.sleep(1)
            sys.exit()


# Tutorial
question = input("If you'd like to skip the tutorial type \033[3mA\033[0m, otherwise type any other letter: ")
if question.lower() == 'a':
    pass
else:
    print('Welcome to the Tutorial!')
    time.sleep(1)
    print("Through this game you'll be asked to make different decisions.")
    time.sleep(1)
    print("It's important that your answer is one of the two options supplied.")
    time.sleep(1)
    print("There will always only be two options, and they'll be italicised for your understanding.")
    time.sleep(1)
    tutorial = input("Here's an example. Choose \033[3mone\033[0m or \033[3mtwo\033[0m. ")
    time.sleep(0.5)

    if tutorial == 'one':
        print("You chose 1, you've made your first decision.")
    elif tutorial == 'two':
        print("You chose 2, you've made your first decision.")
    else:
        print("Uh Oh, that's not quite right, please only choose from the available options")

    time.sleep(2)
    print("Also during the game, you have the opportunity to collect items to add to your inventory.")
    tutoriallist = []
    print(tutoriallist)
    print("As you can see nothing is currently there.")
    time.sleep(2)
    print('As you progress through the game your inventory will change, such as if you pick up an item.')
    time.sleep(1)
    print("For example let's say you pick up a ball.")
    tutoriallist.append("ball")
    print(tutoriallist)
    time.sleep(2)
    print('The item is now in your inventory. If you give away the ball..')
    time.sleep(2)
    tutoriallist.remove("ball")
    print(tutoriallist)
    print('You no longer have it in your inventory.')
    time.sleep(2)
    print("That's the basics. Enjoy the game!!")
    time.sleep(3)

# Start of the game
print("It's a crisp Autumn morning; the sun shines through red and golden leaves.")
time.sleep(1)
start = input(
    "The coziness lulls you back to bed, do you \033[3mresist\033[0m the heaviness of your tired eyes, or \033[3mgive in\033[0m to its pleas? ")

if start.lower() == 'give in':
    print("You give into the comfort promised by sleep, little do you know comfort is far from what you'll receive...")
    time.sleep(2)
    print(f'... You awake in a dark, dim room. You faintly hear "{name}, {name}" calling on loop in the background.')
    time.sleep(2)
    print('You inspect the room further, you notice two possible exits.')
    time.sleep(1)
    print('A door on the left with loud noises, and a door on the right with eerie silence')
    time.sleep(1)
    beginning = input("Do you take the \033[3mleft\033[0m or the \033[3mright\033[0m door? ")

    if beginning == 'left':
        print("You go through the left door...you feel harsh rain coming down.")
        print("Over the sound of the rain, you observe your surroundings, you're in a rainforest.")
        time.sleep(0.5)
        print("Through the rain, you see a cave and a wooden shelter.")
        rainforest = input("Do you run into the \033[3mcave\033[0m or under the \033[3mwooden shelter\033[0m? ")

        if rainforest == 'cave':
            print("You run into the cave seeking cover, a large growl startles you from behind.")
            time.sleep(0.5)
            print("A large jaguar pounces on you. You have become his lunch. Ending 2/6 discovered!")
            time.sleep(1)
            sys.exit()

        elif rainforest == 'wooden shelter':
            print("You run under the shelter. You discover rope.")
            time.sleep(1)
            rope_choice_r = input('Do you take the rope? \033[3myes\033[0m or \033[3mno\033[0m? ')

            if rope_choice_r == 'yes':
                print('You take the rope for safe keeping')
                inventory.append('rope')

            elif rope_choice_r == 'no':
                print("You leave the rope behind..")

            # Voice option
            time.sleep(2)
            print(f"With the rain now cleared. You can hear a voice echoing your name; '{name}, {name}..' ")
            voice = input("Do you walk \033[3mtowards\033[0m or \033[3maway\033[0m from the voice? ")

            if voice == 'away':
                print("You decide to walk away from the voice...")
                time.sleep(1)
                merchant_encounter()
                snowy_town_scene()
            elif voice == 'towards':
                follow_the_voice()

    elif beginning == 'right':
        time.sleep(1)
        print("You go through the right door...you feel intense heat.")
        time.sleep(1)
        print("With warm sand under your feet, it hits you, you're in a desert.")
        time.sleep(1)
        print("The intense silence has you studying your environment.")
        time.sleep(2)
        print("You spot sandprints in the sand.")
        sandprints = input("Do you run follow the prints \033[3myes\033[0m or \033[3mno\033[0m? ")

        if sandprints == 'yes':
            print("You start following the sandprints...")
            time.sleep(1)
            print("You become hyperfocused on the prints and lose sight of where you're walking.")
            time.sleep(1)
            print("PLOP!!!")
            time.sleep(2)
            print("You have fallen into quicksand, you start to panic leading you sink further.")
            time.sleep(1)
            print("You continue to sink to your death. Ending 3/6 discovered! ")
            time.sleep(1)
            sys.exit()

        elif sandprints == 'no':
            print("You keep searching around and discover a structure to the left.")
            time.sleep(0.5)
            print("Upon searching the structure, you discover a rope.")
            rope_choice_d = input('Do you take the rope? \033[3myes\033[0m or \033[3mno\033[0m? ')

            if rope_choice_d == 'yes':
                print('You take the rope for safe keeping')
                inventory.append('rope')
                print('Your inventory has been updated.')

            elif rope_choice_d == 'no':
                print("You leave the rope behind..")

            time.sleep(2)

            merchant_encounter()
            snowy_town_scene()

elif start.lower() == 'resist':
    print("You come to your senses, realising you must get out of bed. You don't go back to sleep. Ending 1/6 discovered!")
    sys.exit()

else:
    print('You stay pondering your options...')

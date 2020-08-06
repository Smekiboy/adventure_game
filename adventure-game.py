import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro(item, alternativ):
    print_pause("You find yourself standing in an open field," 
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a gorgon is somewhere around here," 
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty" 
                "(but not very effective) dagger.\n")

def house(item, alternativ):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a" + alternativ + ".")
    print_pause("Eep! This is the" + alternativ + "'s house!")
    print_pause("The" + alternativ + "attacks you!")
    if "spear" not in item:
        print_pause("You feel a bit under-prepared for this, "
                     "what with only having a tiny dagger.")
    fight(item, alternativ)
        
def fight(item, alternativ):
    while True:
        response = input("Would you like to (1) fight or (2) run away?")
        if "1" in response:
            if "spear" in item:
                print_pause("As the" + alternativ + " moves to attack, "
                            "you unsheath your new spear.")
                print_pause("The Spear of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the attack.")
                print_pause("But the" + alternativ + "takes one "
                            "look at your shiny new toy and runs away!")
                print_pause("You have rid the town of the" + alternativ + ". " 
                            "You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("But your dagger is no match for the" + alternativ + ".")
                print_pause("You have been defeated!")
                break
        if "2" in response:
            print_pause("You run back into the field. Luckily, " 
                        "you don't seem to have been followed.")
            field(item, alternativ)
            break

def cave(item, alternativ):
    if "spear" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        item.append("spear")
    field(item, option)




def field(item, alternativ):  
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    while True:
        response = input("(Please enter 1 or 2).\n")
        if "1" in response:
            print_pause("You are in the house!")
            house(item, alternativ)
            break
        elif "2" in response:
            print_pause("You are in the cave!")
            cave(item, alternativ)
            break
        else:
            print_pause("I don't understand!")

def play_again():
    option = input("Would you like to play again? "
                    "Please say 'yes' or 'no'.\n",
                    "yes", "no").lower()
    if "yes" in response:
        print_pause("Great! We will restart the game\n")
        play_game()
    elif "no" in response:
        print_pause("Thank you for playng. You are welcome again!\n")
    else:
        play_game()


def play_game():
    item = []
    alternativ = random.choice(["pirate", "gorgon", "dragon", "troll" "wicked fairie"])
    intro(item, alternativ)
    field(item, alternativ)
play_game()

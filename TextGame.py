import time
import random

# Choose a Race!


def race_choice():
    print("Pick a race!")
    print("Here are your choices: Lizard, Bookshelf, Genie\n")
    race_input = input("What is your race?").lower()
    if race_input in race_choices:
        print("You are a", race_input, "\n")
        return race_input
    else:
        race_choice()


selected_race = race_choice()


def stats_gen():
    if selected_race == "lizard":
        stats["strength"] = 8
        stats["intelligence"] = 2
        stats["dexterity"] = 3
    elif selected_race == "bookshelf":
        stats["strength"] = 1
        stats["intelligence"] = 11
        stats["dexterity"] = 1
    elif selected_race == "genie":
        stats["strength"] = 2
        stats["intelligence"] = 4
        stats["dexterity"] = 7
    elif selected_race == "jesus_himself":
        stats["strength"] = 15
        stats["intelligence"] = 15
        stats["dexterity"] = 15


# Choose a Class!


class_choices = ["brute", "wet noodle", "missionary"]


def class_choice():
    print("Pick a class!")
    print("Here are your choices: Brute (+str, -int), "
          "Wet Noodle (+dex, -str), "
          "Missionary (+int, -dex)\n")
    class_input = input("What is your class?").lower()
    if class_input in class_choices:
        print("You are a", class_input, "\n")
        return class_input
    else:
        class_choice()


selected_class = class_choice()


def class_gen():
    my_ability = None
    if selected_class == "brute":
        my_ability = "bash"
        stats["strength"] += 1
        stats["intelligence"] -= 1

    elif selected_class == "wet noodle":
        my_ability = "noodle grab"
        stats["dexterity"] += 1
        stats["strength"] -= 1

    elif selected_class == "missionary":
        my_ability = "convert"
        stats["intelligence"] += 1
        stats["dexterity"] -= 1

    return my_ability


ability = class_gen()


def item_get():
    my_item = None
    items = ["sharp stick", "magic scroll", "odd gem"]
    item_choice = input("Would you like an item?").lower()
    if item_choice == "yes":
        item_choice2 = input("What item would you like?\n"
                             "Sharp Stick, Magic Scroll, Odd Gem").lower()
        if item_choice2 in items:
            print("You have chosen the", item_choice2, "\n")
        else:
            print("Please choose one of the items listed")
            item_get()
        my_item = item_choice2
    elif item_choice == "no":
        print("You will be given 1 gold coin instead\n")
        my_item = "1 gold"
    else:
        print("Please say yes or no")
        item_get()
    return my_item


item = item_get()

inventory = [item]


def print_char():
    time.sleep(0.5)
    print("====== Character Specifics ======")
    time.sleep(0.75)
    if selected_race == "lizard":
        print("You are a nomadic lizard hailing from the east. Your emerald scales glimmer as you lick your eyeball")
    elif selected_race == "bookshelf":
        print("You are a sentient bookshelf brought to life by unknown means. All your books are B-tier 80s sci-fi")
    elif selected_race == "genie":
        print("You are a familiar looking blue genie. You are wispy and magical and have a nice goatee")
    print("Your class is:", selected_class)
    print("Your ability is:", ability)
    print("Your item is:", item)
    for stat, stat_num in stats.items():
        print(stat, ":", stat_num)
    print("\n")


def run_attempt(chance):
    run = False
    print("You attempt to run away")
    if random.randint(1, 10) <= chance:
        print("You stumble away, the only thing wounded your pride")
        run = True
    else:
        print("You trip and fall flat on your face")
    return run


def fight_menu(monster):
    fight = True
    while fight:
        fight_input = input("[1] Fight\n"
                            "[2] Bag\n"
                            "[3] Run")
        if fight_input == "1":
            print("How will you fight the", monster, "?")
        elif fight_input == "2":
            print("You open your bag")
            print(inventory)
        elif fight_input == "3":
            if run_attempt(run_chance):
                fight = False
        else:
            print("Please select 1, 2, or 3")


def story():
    print("The bull shakes his head vigorously and stomps the ground")
    print("What would you like to do?")
    fight_menu("Big cow thing")


def main_menu():
    time.sleep(1)
    game = True
    roll = False
    while game:
        print(" [1]  Start\n",
              "[2]  Options\n",
              "[3]  Test dice roll\n",
              "[4]  Quit")

        user_input = input()
        if user_input == "1":
            time.sleep(1)
            print("Good luck adventurer")
            stats_gen()
            print_char()
            story()
            game = False
        elif user_input == "2":
            print("Here are your options")
        elif user_input == "3":
            roll = True
        elif user_input == "4":
            print("Goodbye!")
            exit()
        else:
            print("I can't do that dave")
            continue

        while roll:
            dice_type = input("What dice would you like to use?\n"
                              "[1] D20\n"
                              "[2] D12\n"
                              "[3] D10\n"
                              "[4] D8\n"
                              "[5] D6\n"
                              "[6] D4\n"
                              "[7] D2")
            dice_roll(dice_type)
            dice_next = input("Roll again?\n"
                              "[1] Yes\n"
                              "[2] No")

            if dice_next == "1":
                continue
            elif dice_next == "2":
                roll = False
            else:
                print("Y or N")


main_menu()

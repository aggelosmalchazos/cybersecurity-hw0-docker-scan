import random


#this is the monty hall problem, where you have 3 doors, one of them has a car behind it and the other two have goats.
def print_doors_with_goat(open_door):
    print("\n  _______    _______    _______")
    for i in range(3):
        if i == open_door:
            print(" |       |  ", end="") # Open door
        else:
            print(" |       |  ", end="") # Closed door
    print()

    for i in range(3):
        if i == open_door:
            print(" |  Goat |  ", end="") # Goat revealed
        else:
            print(f" |   {i}   |  ", end="") # Closed door with number
    print()

    print(" |_______|  |_______|  |_______|\n")

def print_doors_with_car(open_door):
    print("\n  _______    _______    _______")
    for i in range(3):
        if i == open_door:
            print(" |       |  ", end="") # Open door
        else:
            print(" |       |  ", end="") # Closed door
    print()

    for i in range(3):
        if i == open_door:
            print(" |  CAR |  ", end="") # Car revealed
        else:
            print(f" |   {i}   |  ", end="") # Closed door with number
    print()

    print(" |_______|  |_______|  |_______|\n")

def manual_game():
    doors = [0, 0, 0]
    
    prize_door = random.randint(0, 2)
    print(f"prize is {prize_door}")
    doors[prize_door] = 1

    print("  _______    _______    _______")
    print(" |       |  |       |  |       |")
    print(" |   0   |  |   1   |  |   2   |")
    print(" |_______|  |_______|  |_______|")
    
    choice = int(input("Time to pick a door!\nType number 0-2 to select door.\nYour choice:"))

    # in case input was out of bounds
    while choice < 0 or choice > 2:
        choice = int(input("Invalid input!\nType number 0-2 to select door.\nYour choice:"))

    print(f"you chose {choice}")

    # we have to find a door to open, that does not contain the prize and is not the one the player chose. 
    # We try randomly until we find one
    open_door = -1
    while open_door == -1:
        temp = random.randint(0, 2)
        if doors[temp] == 0 and temp != choice:
            open_door = temp

    print_doors_with_goat(open_door)
    
    print(f"You chose Door {choice}. The host reveals Door {open_door} to reveal a goat.")
    num = int(input("Would you like to change your choice?\nEnter 4 if you do not wish to change, otherwise enter the number of the door you are choosing:"))

    while num == open_door or num < 0 or (num > 2 and num != 4):
        num = int(input("You chose the open door, or your input was invalid. Try again:"))
        
    # contestant changed his mind
    if num != 4 and num != choice:
        choice = num

    print(f"Your final choice is {choice}.\nLet's see...")

    if doors[choice] == 1:
        print_doors_with_car(choice)
        print("YOU WIN\n")
    else:
        for i in range(3):
            if doors[i] == 1:
                print_doors_with_car(i)
                break
        print("YOU LOSE\n")

def simulated_game():
    wins_without_change = 0
    wins_with_change = 0
    num_of_iterations = 1000
    
    for iteration in range(num_of_iterations):
        # Initialize doors
        doors = [0, 0, 0]

        # Randomly place the prize
        prize_door = random.randint(0, 2)
        doors[prize_door] = 1

        # Player makes an initial choice
        choice = random.randint(0, 2)

        # Host opens a door with a goat (not the chosen door or the prize door)
        open_door = -1
        while open_door == -1:
            temp = random.randint(0, 2)
            if doors[temp] == 0 and temp != choice:
                open_door = temp

        # Determine the final choice
        final_choice = choice
        if iteration >= num_of_iterations // 2:
            # Simulate switching choice for iterations >= 500
            for i in range(3):
                if i != choice and i != open_door:
                    final_choice = i
                    break

        # Check if the final choice wins the prize
        if doors[final_choice] == 1:
            if iteration < num_of_iterations // 2:
                wins_without_change += 1
            else:
                wins_with_change += 1

    print(f"Results after {num_of_iterations} simulations:")
    print(f"Wins without changing choice: {wins_without_change}/{num_of_iterations // 2}")
    print(f"Wins with changing choice: {wins_with_change}/{num_of_iterations // 2}")

def main():
    print("Enter 1 to play the game manually, or enter 2 to simulate the game for 1000 iterations.")
    try:
        num = int(input())
        if num == 1:
            manual_game()
        elif num == 2:
            simulated_game()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
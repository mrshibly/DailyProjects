import pickle
import random

class Game:
    def __init__(self):
        self.current_scenario = None
        self.score = 0
        self.inventory = []
        self.journey_log = []
        self.turns = 0
        self.max_turns = 20
        self.health = 100

    def start(self):
        self.current_scenario = scenario1
        self.play()

    def play(self):
        while self.current_scenario and self.turns < self.max_turns and self.health > 0:
            self.turns += 1
            self.current_scenario.display()
            choice = self.get_player_choice()
            if choice == 'inventory':
                self.display_inventory()
                continue
            elif choice == 'log':
                self.display_journey_log()
                continue
            self.journey_log.append(self.current_scenario.choices[choice].description)
            self.score += self.current_scenario.choices[choice].points
            item = self.current_scenario.choices[choice].item
            if item:
                self.add_to_inventory(item)
            if self.current_scenario.choices[choice].combat:
                self.combat(self.current_scenario.choices[choice].combat)
            elif self.current_scenario.choices[choice].puzzle:
                self.solve_puzzle(self.current_scenario.choices[choice].puzzle)
            elif self.current_scenario.choices[choice].negotiation:
                self.negotiate(self.current_scenario.choices[choice].negotiation)
            self.current_scenario = self.current_scenario.get_choice(choice)

        if self.health <= 0:
            print(f"You have been defeated. Game Over. Your score: {self.score}")
        elif self.turns >= self.max_turns:
            print(f"You have run out of time. Game Over. Your score: {self.score}")
        else:
            print(f"Game Over. Your score: {self.score}")
        
        self.display_journey_log()

    def get_player_choice(self):
        while True:
            choice = input("Enter your choice (or 'inventory' to view items, 'log' to view journey log): ").strip().lower()
            if choice == 'inventory':
                return 'inventory'
            elif choice == 'log':
                return 'log'
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(self.current_scenario.choices):
                    if not self.current_scenario.choices[choice].requires or self.current_scenario.choices[choice].requires in self.inventory:
                        return choice
                    else:
                        print(f"You need {self.current_scenario.choices[choice].requires} to choose this option.")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def display_inventory(self):
        if self.inventory:
            print("Your inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    def display_journey_log(self):
        if self.journey_log:
            print("Your journey log:")
            for entry in self.journey_log:
                print(f"- {entry}")
        else:
            print("Your journey log is empty.")

    def combat(self, threat):
        print(f"Combat encounter: {threat['description']}")
        while threat['hp'] > 0 and self.health > 0:
            action = input("Do you want to (f)ight or (r)un? ").strip().lower()
            if action == 'f':
                player_attack = random.randint(5, 20)
                threat_attack = random.randint(5, 15)
                threat['hp'] -= player_attack
                self.health -= threat_attack
                print(f"You dealt {player_attack} damage. Threat HP is now {threat['hp']}.")
                print(f"You received {threat_attack} damage. Your HP is now {self.health}.")
            elif action == 'r':
                escape_chance = random.random()
                if escape_chance > 0.5:
                    print("You successfully escaped!")
                    break
                else:
                    threat_attack = random.randint(5, 15)
                    self.health -= threat_attack
                    print(f"You failed to escape and received {threat_attack} damage. Your HP is now {self.health}.")
            else:
                print("Invalid action. Choose 'f' to fight or 'r' to run.")

    def solve_puzzle(self, puzzle):
        print(f"Puzzle: {puzzle['description']}")
        attempts = 0
        while attempts < puzzle['max_attempts']:
            answer = input("Enter your answer: ").strip().lower()
            if answer == puzzle['solution']:
                print("Correct! You solved the puzzle.")
                self.score += puzzle['points']
                break
            else:
                print("Incorrect. Try again.")
                attempts += 1
        if attempts == puzzle['max_attempts']:
            print("You failed to solve the puzzle.")
            self.health -= puzzle['penalty']
            print(f"You lost {puzzle['penalty']} health points. Your HP is now {self.health}.")

    def negotiate(self, negotiation):
        print(f"Negotiation: {negotiation['description']}")
        success = False
        for option in negotiation['options']:
            print(f"{option['choice']}. {option['description']}")
        while not success:
            choice = input("Choose your negotiation option: ").strip().lower()
            for option in negotiation['options']:
                if choice == option['choice']:
                    print(option['outcome'])
                    if option['success']:
                        self.score += negotiation['points']
                        success = True
                    else:
                        self.health -= option['penalty']
                        print(f"You lost {option['penalty']} health points. Your HP is now {self.health}.")
                        if self.health <= 0:
                            success = True
                    break

    def save_game(self, filename='savegame.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump((self.current_scenario, self.score, self.inventory, self.journey_log, self.turns, self.health), f)
        print("Game saved.")

    def load_game(self, filename='savegame.pkl'):
        try:
            with open(filename, 'rb') as f:
                self.current_scenario, self.score, self.inventory, self.journey_log, self.turns, self.health = pickle.load(f)
            print("Game loaded.")
            self.play()
        except FileNotFoundError:
            print("Save file not found. Starting a new game.")
            self.start()

class Scenario:
    def __init__(self, description):
        self.description = description
        self.choices = []

    def add_choice(self, choice):
        self.choices.append(choice)

    def display(self):
        print(self.description)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice.description}")

    def get_choice(self, index):
        return self.choices[index].next_scenario

class Choice:
    def __init__(self, description, next_scenario, points=0, item=None, requires=None, combat=None, puzzle=None, negotiation=None):
        self.description = description
        self.next_scenario = next_scenario
        self.points = points
        self.item = item
        self.requires = requires
        self.combat = combat
        self.puzzle = puzzle
        self.negotiation = negotiation

# Define the scenarios
scenario1 = Scenario("You are in a Bangladeshi village near the Sundarbans. There are two paths ahead.")
scenario2 = Scenario("You find a treasure chest near an old banyan tree.")
scenario3 = Scenario("You encounter a wild tiger.")
scenario4 = Scenario("You find a hidden cave by the river.")
scenario5 = Scenario("You meet an old man inside the cave.")
scenario6 = Scenario("You find a magical river.")
scenario7 = Scenario("You discover an ancient ruin deep in the forest.")
scenario8 = Scenario("You find a mysterious key on the ground.")
scenario9 = Scenario("You come across a locked door in the ancient ruin.")
scenario10 = Scenario("You encounter a village chief who requires negotiation to pass.")
scenario11 = Scenario("You find a puzzle carved into a stone wall.")

# Define the choices
choice1_1 = Choice("Take the left path.", scenario2, 10)
choice1_2 = Choice("Take the right path.", scenario3, 10, combat={"description": "a wild tiger", "hp": 50})
choice2_1 = Choice("Open the chest.", None, 50, "golden coin")  # End of this path
choice2_2 = Choice("Leave the chest.", scenario1, 5)  # Loop back to start
choice3_1 = Choice("Fight the tiger.", None, 30)  # End of this path
choice3_2 = Choice("Run away.", scenario1, -10)  # Loop back to start
choice1_3 = Choice("Look around carefully.", scenario4, 20)
choice4_1 = Choice("Enter the cave.", scenario5, 20)
choice4_2 = Choice("Ignore the cave.", scenario1, 0)
choice5_1 = Choice("Talk to the old man.", None, 50, "mystical amulet")  # End of this path
choice5_2 = Choice("Leave the cave.", scenario1, 0)  # Loop back to start
choice1_4 = Choice("Follow a strange noise.", scenario6, 15)
choice6_1 = Choice("Drink from the river.", None, -20)  # End of this path
choice6_2 = Choice("Explore the riverbank.", scenario7, 30)
choice7_1 = Choice("Enter the ruins.", scenario11, 40)  # Leads to a puzzle
choice7_2 = Choice("Return to the forest.", scenario1, 5)
choice1_5 = Choice("Search the ground.", scenario8, 20)
choice8_1 = Choice("Pick up the key.", scenario1, 10, "mysterious key")
choice8_2 = Choice("Ignore the key.", scenario1, 0)
choice1_6 = Choice("Follow the distant light.", scenario9, 25)
choice9_1 = Choice("Use the key to open the door.", scenario7, 50, requires="mysterious key")  # Only available if player has key
choice9_2 = Choice("Turn back.", scenario1, 0)
choice1_7 = Choice("Talk to the village chief.", scenario10, 10, negotiation={
    "description": "The chief requires negotiation to let you pass.",
    "points": 30,
    "options": [
        {"choice": "a", "description": "Offer him the golden coin.", "success": True, "outcome": "The chief accepts the coin and lets you pass.", "penalty": 0},
        {"choice": "b", "description": "Try to intimidate him.", "success": False, "outcome": "The chief is not intimidated and you are injured.", "penalty": 20},
        {"choice": "c", "description": "Promise to help him later.", "success": False, "outcome": "The chief does not trust your promise and you are injured.", "penalty": 10}
    ]
})
choice11_1 = Choice("Solve the puzzle.", None, puzzle={
    "description": "Solve this riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'",
    "solution": "echo",
    "points": 50,
    "penalty": 20,
    "max_attempts": 3
})
choice11_2 = Choice("Leave the puzzle.", scenario1, 0)

# Add choices to scenarios
scenario1.add_choice(choice1_1)
scenario1.add_choice(choice1_2)
scenario1.add_choice(choice1_3)
scenario1.add_choice(choice1_4)
scenario1.add_choice(choice1_5)
scenario1.add_choice(choice1_6)
scenario1.add_choice(choice1_7)
scenario2.add_choice(choice2_1)
scenario2.add_choice(choice2_2)
scenario3.add_choice(choice3_1)
scenario3.add_choice(choice3_2)
scenario4.add_choice(choice4_1)
scenario4.add_choice(choice4_2)
scenario5.add_choice(choice5_1)
scenario5.add_choice(choice5_2)
scenario6.add_choice(choice6_1)
scenario6.add_choice(choice6_2)
scenario7.add_choice(choice7_1)
scenario7.add_choice(choice7_2)
scenario8.add_choice(choice8_1)
scenario8.add_choice(choice8_2)
scenario9.add_choice(choice9_1)
scenario9.add_choice(choice9_2)
scenario10.add_choice(choice11_1)
scenario10.add_choice(choice11_2)

# Start the game
game = Game()
print("Welcome to 'Operation in Sundarban'!")
print("Type 'save' to save the game or 'load' to load a previous game.")
command = input("Enter 'start' to begin the game or a command: ").strip().lower()

if command == 'start':
    game.start()
elif command == 'save':
    game.save_game()
elif command == 'load':
    game.load_game()
else:
    print("Unknown command. Exiting the game.")

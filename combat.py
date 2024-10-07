import random

# Define environments and associated creature types
environment_creatures = {
    'forest': ['wolves', 'dryads', 'treants'],
    'desert': ['scorpions', 'sand elementals', 'gnolls'],
    'mountains': ['griffons', 'giants', 'harpies'],
    'swamp': ['lizardfolk', 'will-o-wisps', 'hydras'],
    'urban': ['bandits', 'thieves', 'rogue mages'],
    'cave': ['goblins', 'kobolds', 'giant spiders'],
    'sea': ['merfolk', 'sharks', 'krakens'],
    'plains': ['centaurs', 'lions', 'bulette'],
    'underground': ['drow', 'mind flayers', 'umber hulks']
}

# Difficulty scaling for HP and DC
difficulty_stats = {
    'easy': {'hp_range': (10, 30), 'dc_range': (10, 12)},
    'medium': {'hp_range': (31, 60), 'dc_range': (13, 15)},
    'hard': {'hp_range': (61, 90), 'dc_range': (16, 18)},
    'deadly': {'hp_range': (91, 150), 'dc_range': (19, 22)}
}

# Descriptive prefixes based on difficulty level
difficulty_descriptions = {
    'easy': ['Weak', 'Meager', 'Fledgling', 'Fragile'],
    'medium': ['Skilled', 'Sturdy', 'Seasoned', 'Dangerous'],
    'hard': ['Formidable', 'Vicious', 'Savage', 'Elite'],
    'deadly': ['Mythic', 'Ancient', 'Celestial', 'Abyssal']
}

# Descriptive prefixes for environments
environment_descriptions = {
    'forest': ['of the Wild Wood', 'of the Enchanted Glade', 'of the Verdant Forest'],
    'desert': ['of the Scorching Sands', 'of the Burning Dunes', 'of the Endless Wastes'],
    'mountains': ['of the Jagged Peaks', 'of the High Cliffs', 'of the Mountain Pass'],
    'swamp': ['of the Murky Mire', 'of the Rotting Swamp', 'of the Sinking Marsh'],
    'urban': ['of the Dark Alleys', 'of the Shady Markets', 'of the City Slums'],
    'cave': ['of the Deep Caverns', 'of the Hidden Caves', 'of the Echoing Depths'],
    'sea': ['of the Dark Sea', 'of the Stormy Waters', 'of the Abyssal Depths'],
    'plains': ['of the Windswept Plains', 'of the Open Steppes', 'of the Rolling Fields'],
    'underground': ['of the Dark Depths', 'of the Shadowy Tunnels', 'of the Forgotten Catacombs']
}

# Function to generate a random combat encounter based on user input
def generate_combat_encounter(environment, difficulty):
    if environment not in environment_creatures:
        return "Invalid environment. Please choose from the available options."
    
    if difficulty not in difficulty_stats:
        return "Invalid difficulty. Please choose from the available difficulties."
    
    creature_type = random.choice(environment_creatures[environment])
    difficulty_prefix = random.choice(difficulty_descriptions[difficulty])
    environment_suffix = random.choice(environment_descriptions[environment])
    
    # Generate HP and DC based on difficulty
    hp = random.randint(*difficulty_stats[difficulty]['hp_range'])
    dc = random.randint(*difficulty_stats[difficulty]['dc_range'])
    
    # Create a descriptive name for the creature
    creature_description = f"{difficulty_prefix} {creature_type} {environment_suffix}"
    
    return {
        'creature_description': creature_description,
        'difficulty': difficulty,
        'hp': hp,
        'dc': dc
    }

# Function to get user input and generate the encounter
def user_input_encounter():
    print("Available environments: " + ', '.join(environment_creatures.keys()))
    environment = input("Enter the environment: ").strip().lower()
    
    print("Available difficulties: " + ', '.join(difficulty_stats.keys()))
    difficulty = input("Enter the difficulty (easy, medium, hard, deadly): ").strip().lower()
    
    encounter = generate_combat_encounter(environment, difficulty)
    
    if isinstance(encounter, dict):
        print(f"\nCombat Encounter: {encounter['creature_description']}")
        print(f"HP: {encounter['hp']} | DC: {encounter['dc']}")
    else:
        print(encounter)  # In case of invalid input, print the error message.

# Run the user input encounter generation
user_input_encounter()
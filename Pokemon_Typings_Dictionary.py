# This program is to present all the strengths, weaknesses, immunities of each pokemon type combination
# There's something wrong here...

types = ['Bug', 'Dark', 'Dragon',
        'Electric', 'Fairy', 'Fighting',
        'Fire',	'Flying',	'Ghost',
        'Grass', 'Ground',	'Ice',
       'Normal', 'Poison',	'Psychic',
        'Rock', 'Steel', 'Water'] # List of all typings in Pokemon as of Generation 8 arranged in alphabetical order

strength = {"Bug" : ['Dark','Grass', 'Psychic'], 
            'Dark' : ['Ghost', 'Psychic'], 
            "Dragon" : ['Dragon'], 
            "Electric" : ['Flying', 'Water'], 
            "Fairy" : ['Dark', 'Dragon', 'Fighting'], 
            "Fighting" : ['Dark', 'Ice', 'Normal', 'Rock', 'Steel'], 
            "Fire" : ['Bug', 'Grass', 'Ice', 'Steel'], 
            "Flying" : ['Bug', 'Fighting', 'Grass'], 
            "Ghost" : ['Ghost', 'Psychic'], 
            "Grass" : ['Ground', 'Rock', 'Water' ], 
            "Ground" : ['Electric', 'Fire', 'Poison', 'Rock', 'Steel'],
            "Ice" : ['Dragon', 'Flying', 'Grass', 'Ground'], 
            "Normal" : [], 
            "Poison" : ['Fairy', 'Grass'], 
            "Psychic" : ['Fighting', 'Poison'], 
            "Rock" : ['Bug', 'Fire', 'Flying', 'Ice'], 
            "Steel" : ['Fairy', 'Ice', 'Rock'], 
            "Water" : ['Fire', 'Ground', 'Rock']} # List of all the strenghts that each pokemon typing has against each other arranged in alphabetical order

weakness = {"Bug" : ['Fire', 'Flying', 'Rock'], 
            'Dark' : ['Bug','Fairy','Fighting'], 
            "Dragon" : ['Dragon', 'Fairy', 'Ice'], 
            "Electric" : ['Ground'], 
            "Fairy" : ['Poison', 'Steel'], 
            "Fighting" : ['Fairy', 'Flying', 'Psychic'], 
            "Fire" : ['Ground', 'Rock', 'Water'], 
            "Flying" : ['Electric', 'Ice', 'Rock'], 
            "Ghost" : ['Dark', 'Ghost'], 
            "Grass" : ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'], 
            "Ground" : ['Grass', 'Ice', 'Water'],
            "Ice" : ['Fighting', 'Fire', 'Rock', 'Steel'], 
            "Normal" : ['Fighting'], 
            "Poison" : ['Ground', 'Psychic'], 
            "Psychic" : ['Bug', 'Dark', 'Ghost'], 
            "Rock" : ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'], 
            "Steel" : ['Fighting', 'Fire', 'Ground'], 
            "Water" : ['Electric', 'Grass']} # List of all the weaknesses that each pokemon typing has against each other arranged in alphabetical order

resistances = {"Bug" : ['Fighting', 'Grass', 'Ground'], 
            'Dark' : ['Dark', 'Ghost'], 
            "Dragon" : ['Electric', 'Fire', 'Grass', 'Water'], 
            "Electric" : ['Electric', 'Flying', 'Steel'], 
            "Fairy" : ['Bug', 'Dark', 'Fighting'], 
            "Fighting" : ['Bug', 'Dark', 'Rock'], 
            "Fire" : ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'], 
            "Flying" : ['Bug', 'Fighting', 'Grass'], 
            "Ghost" : ['Bug', 'Poison'], 
            "Grass" : ['Electric', 'Grass', 'Ground', 'Water'], 
            "Ground" : ['Poison', 'Rock'],
            "Ice" : ['Ice'], 
            "Normal" : [], 
            "Poison" : ['Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'], 
            "Psychic" : ['Fighting', 'Psychic'], 
            "Rock" : ['Fire', 'Flying', 'Normal', 'Poison'], 
            "Steel" : ['Bug', 'Fairy', 'Dragon', 'Grass', 'Ice', 'Flying', 'Normal', 'Psychic', 'Rock', 'Steel'], 
            "Water" : ['Fire', 'Ice', 'Steel', 'Water']} #this list shows all resistances that each pokemon type has

immunities = {"Bug" : [], 
            'Dark' : ['Psychic'], 
            "Dragon" : [], 
            "Electric" : [], 
            "Fairy" : ['Dragon'], 
            "Fighting" : [], 
            "Fire" : [], 
            "Flying" : ['Ground'], 
            "Ghost" : ['Normal', 'Fighting'], 
            "Grass" : [], 
            "Ground" : ['Electric'],
            "Ice" : [], 
            "Normal" : ['Ghost'], 
            "Poison" : [], 
            "Psychic" : [], 
            "Rock" : [], 
            "Steel" : ['Poison'], 
            "Water" : []}  #this list shows all immunities that each pokemon type has


number_of_types = input("Will it be a monotype or a dualtype? Enter m for monotyping, d for dualtyping, all to see all typings, or q for quit\n")

if number_of_types == 'q':
    quit()

elif number_of_types == 'all':
    print(", ".join(types))

elif number_of_types == 'm':
    what_monotype = input("What typing would you like to see?\n").title()

    if what_monotype in types:
        index_monotype_strengths = strength.get(what_monotype)
        index_monotype_weaknesses = weakness.get(what_monotype)
        print(f"Strengths: {', '.join(list(index_monotype_strengths))}\nWeaknesses: {', '.join(list(index_monotype_weaknesses))}")
    else:
        print("Please input a valid Pokemon typing.")

elif number_of_types == 'd':
    what_dualtype1 = input("What is the primary typing?\n").title()
    what_dualtype2 = input("What is the secondary typing?\n").title()

    if what_dualtype1 == what_dualtype2:
        print("Please ensure that the two typings are not the same.")
        quit()

    if what_dualtype1 in types and what_dualtype2 in types:

        overall_weakness = [] # stores the overall weaknesses of the dual type
        overall_strength = [] # stores the overall strengths of the dual type
        
        resistance_immunities = [] # stores the overall resistances & immunities

        index_dualtype1_strengths = strength.get(what_dualtype1)
        index_dualtype1_weaknesses = weakness.get(what_dualtype1)
        index_dualtype2_strengths = strength.get(what_dualtype2)
        index_dualtype2_weaknesses = weakness.get(what_dualtype2)

        for typing in (index_dualtype1_strengths): # loop that adds all strengths from the primary type to the overall strengths list
            overall_strength.append(typing)

        for typing in (index_dualtype2_strengths): # loop that adds all strengths from the primary type to the overall strengths list
            overall_strength.append(typing)

        for typing in (index_dualtype1_weaknesses): # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing) 

        for typing in (index_dualtype2_weaknesses): # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing)
        
        immunities_dualtype1 = immunities.get(what_dualtype1)
        immunities_dualtype2 = immunities.get(what_dualtype2)
        resistances_dualtype1 = resistances.get(what_dualtype1)
        resistances_dualtype2 = resistances.get(what_dualtype2)
        
        for typing in overall_weakness: # this for loop goes through all typings in the overall_weakness list and checks out the resistances and immunities that each
            if typing in immunities_dualtype1 or typing in immunities_dualtype2: # types has. If it is present in the resistances or immunities, then it
                resistance_immunities.append(typing) # would be added to the resistances and immunities list
            elif typing in resistances_dualtype1 or typing in resistances_dualtype2:
                resistance_immunities.append(typing)
                
        print(f"Strengths: {', '.join(list((set(overall_strength))))}")
        print(f"Weaknesses: {', '.join(list((set(overall_weakness)) - set(resistance_immunities)))}") # this was set like this as it removes all types that were included in the
                                                                                                    #resistances and immunities and just prints a list that has all weaknesses.
    else:
        print("Please input the valid typing/s.")

else:
    print("Please enter a valid input.")


# created by Harry2166
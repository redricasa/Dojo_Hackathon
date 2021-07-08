from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo", 10,5,100)
jack_sparrow = Pirate("Jack Sparrow", 15,3,100)
Captain_Hook = Pirate("cpt Hook", 10,5,90)

# function to loop thru both characters until self.health <= 0
def see_who_dies_first(Pirate, Ninja, Pirate2):
    # for loop to loop thru until one of them have self.health == 0
    # TODO if/else to ensure Michelangelo doesn't 
    Ninja.attack(Pirate)
    Pirate.show_stats()
    # use die method

    Pirate.attack(Ninja)
    Ninja.show_stats()

    Pirate2.attack(Ninja)
    Ninja.show_stats()
# while loop with ninja and pirate atacking each other
def run_fight( Pirate, Ninja, Pirate2):
    
    while Pirate.health >= 0 and Ninja.health >=0 and Pirate2.health >= 0:
        see_who_dies_first(Pirate, Ninja , Pirate2)

run_fight(jack_sparrow, michelangelo, Captain_Hook)

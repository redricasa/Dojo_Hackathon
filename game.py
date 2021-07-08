from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo", 10,5,100)
jack_sparrow = Pirate("Jack Sparrow", 15,3,100)

# function to loop thru both characters until self.health <= 0
def see_who_dies_first(self ):
    # for loop to loop thru until one of them have self.health == 0
    for i in range(self.health >=0):
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
        # use die method

        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()
    # use die method?
    return self
# while loop with ninja and pirate atacking each other
def run_fight(self ):
    i = self.Pirate, self.Ninja
    while i >= 0:
        return see_who_dies_first()
    # return self

# self.Pirate.health >= 0 and self.Ninja.health >= 0
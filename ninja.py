class Ninja:

    def __init__( self , name, strength, speed, health ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate):
        pirate.health -= self.strength
        #code here
        if pirate.health <= 0:
            # modify to show the pirate's health 
            pirate.die()
        return self
    # die method to track health being depleted
    def die(self):
        # die when health == 0 
        print("Ninja is dead!")

        

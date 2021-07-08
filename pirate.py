class Pirate:

    def __init__( self , name, strength, speed, health ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    
    def attack ( self , ninja ):
        ninja.health -= self.strength
        #code here
        if ninja.health <= 0:
            # include a super here?
            self.die()
        return self

    def die(self):
        # die when health == 0 
        print("Ninja is dead!")
    
        # exit the game when pirate dies

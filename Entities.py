class Entity(Object):
    def __init__(self, health, attack, defence, speed):
        self.maxHealth = health
        self.maxAttack = attack
        self.maxDefence = defence
        self.maxSpeed = speed

        self.currentHealth = health
        self.currentAttack = attack
        self.currentDefence = defence
        self.currentSpeed = speed

        #self.isPoisoned = False
        #self.isCursed = False
        #self.isBlind = False
        #self.isFrosted = False
        #self.isBurned = False

    # attack enemy - based on user's attack
    def attack():
        pass
    # block next attack - based on user's defence
    def defend():
        pass
    # run away from battle - based on user's luck and speed
    def flee():
        pass
    

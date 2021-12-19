class Entity:
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
    

class Player(Entity):
    def __init__(self, health, attack, defence, speed, luck):
        super().__init__(health, attack, defence, speed)
        self.maxLuck = luck
        self.currentLuck = luck
        self.inventory = {}

    # method to use an item in player inventory
    def useItem():
        pass


class Chest(Entity):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health. attack, defence, speed)
        self.loot = []
        self.mimicChance = 0.15

    # method to check contents of chest
    def checkContents():
        pass

class Enemy(Entity):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.loot = {}

    def useAbility():
        pass

class Slime(Enemy):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.description = "A small green slime"

    def bounce():
        pass

class Skeleton(Enemy):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.description = "A rag-covered skeleton "

    def 

class Snake(Enemy):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.description = "A large purple snake with yellow stripes"
    
    def venomSpit():
        pass

class Wolf(Enemy):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.description = "A grey wolf with shaggy fur"
    
    def howl():
        pass

class Demon(Enemy):
    def __init__(self, health, attack, defence, speed):
        super().__init__(health, attack, defence, speed)
        self.description = "A terror-inducing, winged demon holding a giant scythe"

    def deathSickle():


class Boss(Enemy):
    def 

        




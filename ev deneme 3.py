class character :
    def __init__(self , name , health , damage):
        self.name = name 
        self._health = health 
        self.__damage = damage
        
    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.__damage} damage. ")
        target._take_damage(self.__damage)
        
    def _take_damage(self,damage):
        self._health -= damage
        if self._health > 0:
            print(f"{self.name} has {self._health} health left.")
        else:
            print(f"{self.name} has been defeated")
            
    def get_damage(self):
        return self.__damage
    
    def is_alive(self):
        return self._health > 0 
    
class player(character):
    def __init__(self, name ,health ,damage ,level ):
        self.level = level 
        super().__init__(name , health, damage)
        
    def display_info(self):
        print(f"player: {self.name}, health: {self._health}, damage: {self.get_damage()}, level: {self.level} ")
        
class enemy(character):
    def __init__(self, name ,health ,damage ,enemy_type):
        self.enemy_type = enemy_type
        super().__init__(name , health, damage)
        
    def display_info(self):
        print(f"player: {self.name}, health: {self._health}, damage: {self.get_damage()}, type: {self.enemy_type} ")
        
def create_player():
    name = input("enter player name: ")
    health = int(input("enter player health: "))
    damage = int(input("enter player damage: "))
    level = int(input("enter player level: "))

    return player(name, health, damage, level)  

def create_enemy():
    name = input("enter enemy name: ")
    health = int(input("enter enemy health: "))
    damage = int(input("enter enemy damage: "))
    enemy_type = input("enter enemy type: ")

    return enemy(name, health, damage, enemy_type)

player = create_player()
enemy = create_enemy()

player.display_info()
enemy.display_info()

while player.is_alive() and enemy.is_alive():
    player.attack(enemy)
    if not enemy.is_alive():
        break
    
    enemy.attack(player)
    
if player.is_alive():
    print(f"{player.name} wins the battle !!!")
else:
    print(f"{enemy.name} wins the battle !!!")
            
        
class Character:
    def __init__(self, name, health, damage):
        self.name = name  # public
        self._health = health  # protected
        self.__damage = damage  # private

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.__damage} damage.")
        target._take_damage(self.__damage)

    def _take_damage(self, damage):
        self._health -= damage
        if self._health > 0:
            print(f"{self.name} has {self._health} health left.")
        else:
            print(f"{self.name} has been defeated.")

    def get_damage(self):
        return self.__damage

    def is_alive(self):
        return self._health > 0


class Player(Character):
    def __init__(self, name, health, damage, level):
        super().__init__(name, health, damage)
        self.level = level

    def display_info(self):
        print(f"Player: {self.name}, Health: {self._health}, Damage: {self.get_damage()}, Level: {self.level}")


class Enemy(Character):
    def __init__(self, name, health, damage, enemy_type):
        super().__init__(name, health, damage)
        self.enemy_type = enemy_type

    def display_info(self):
        print(f"Enemy: {self.name}, Health: {self._health}, Damage: {self.get_damage()}, Type: {self.enemy_type}")


def create_player():
    name = input("Enter player name: ")
    health = int(input("Enter player health: "))
    damage = int(input("Enter player damage: "))
    level = int(input("Enter player level: "))

    return Player(name, health, damage, level)


def create_enemy():
    name = input("Enter enemy name: ")
    health = int(input("Enter enemy health: "))
    damage = int(input("Enter enemy damage: "))
    enemy_type = input("Enter enemy type: ")

    return Enemy(name, health, damage, enemy_type)


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
    print(f"{player.name} wins the battle!")
else:
    print(f"{enemy.name} wins the battle!")
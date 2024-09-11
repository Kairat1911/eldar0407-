import random

class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has died.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount}. Current health: {self.health}.")

class Witcher(Hero):
    def revive(self, fallen_hero):
        if fallen_hero and not fallen_hero.is_alive:
            fallen_hero.is_alive = True
            fallen_hero.health = fallen_hero.health // 2  # revive with half health
            print(f"{self.name} sacrificed himself to revive {fallen_hero.name}.")

class Magic(Hero):
    def __init__(self, name, health, attack, attack_increase):
        super().__init__(name, health, attack)
        self.attack_increase = attack_increase

    def increase_attack(self):
        self.attack += self.attack_increase
        print(f"{self.name}'s attack increased to {self.attack}.")

class Hacker(Hero):
    def __init__(self, name, health, attack, damage_to_boss):
        super().__init__(name, health, attack)
        self.damage_to_boss = damage_to_boss

    def steal_health(self, boss_health):
        boss_health -= self.damage_to_boss
        print(f"{self.name} stole {self.damage_to_boss} health from the boss.")
        return boss_health

class Golem(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health * 2, attack // 2)  # Increased health but weaker attack

    def absorb_damage(self, damage):
        absorbed = damage // 5
        return damage - absorbed

class Avrora(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.invisible = False

    def go_invisible(self):
        if not self.invisible:
            self.invisible = True
            print(f"{self.name} is now invisible for 2 rounds.")

# Пример использования классов
def main():
    # Создаем героев
    witcher = Witcher("Witcher", 100, 10)
    magic = Magic("Magic", 80, 15, 5)
    hacker = Hacker("Hacker", 70, 20, 10)
    golem = Golem("Golem", 60, 5)
    avrora = Avrora("Avrora", 50, 12)

    # Здоровье босса
    boss_health = 200

    # Бой с боссом
    while boss_health > 0 and (witcher.is_alive or magic.is_alive or hacker.is_alive or golem.is_alive or avrora.is_alive):
        print(f"\nBoss health: {boss_health}")

        # Герои атакуют босса
        if magic.is_alive:
            boss_health -= magic.attack
            magic.increase_attack()

        if hacker.is_alive:
            boss_health = hacker.steal_health(boss_health)

        if golem.is_alive:
            damage_taken = random.randint(10, 30)  # Random damage from the boss
            damage_after_absorb = golem.absorb_damage(damage_taken)
            for hero in [witcher, magic, hacker]:
                if hero.is_alive:
                    hero.take_damage(damage_after_absorb)

        if avrora.is_alive and not avrora.invisible:
            avrora.go_invisible()

        # Проверка состояния героев
        for hero in [witcher, magic, hacker, golem, avrora]:
            if not hero.is_alive:
                print(f"{hero.name} is dead.")

        # Ожидание ввода от пользователя для продолжения следующего раунда
        input("Press Enter to continue to the next round...")

    print("Battle ended.")

if __name__ == "__main__":
    main()
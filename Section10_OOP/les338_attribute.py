import random
 
 
class Goblin(object): 
    monster_size = 'small' 

    def __init__(self):
        self.height = (f"{2 + random.randrange(0, 3)}'")
        self.eye_color = random.choice(['yellow', 'red'])
        self.weapon_of_choice = random.choice(['sword', 'club', 'axe'])        
        self.atk = random.randint(10,15)
    
    @staticmethod
    def _critical() -> bool:
        return random.randint(1,5) == random.randint(1,5)

    def attack(self):
        is_critical =  Goblin._critical()

        return (self.atk + (self.atk * ( (1 if is_critical else 0) * 1.5))),is_critical

 
Dib = Goblin()
Bob = Goblin()
Tuk = Goblin()
 
print('Dib likes to fight with a {}.'.format(Dib.weapon_of_choice))
print('Bob likes to fight with a {}.'.format(Bob.weapon_of_choice))
print('Tuk likes to fight with a {}.'.format(Tuk.weapon_of_choice))
 
print('Dib is a {} type of monster. He is only {} tall'.format(
 Dib.monster_size, Dib.height))
print('Bob is a {} type of monster. He is only {} tall'.format(
 Bob.monster_size, Bob.height))
print('Tuk is a {} type of monster. He is only {} tall'.format(
 Tuk.monster_size, Tuk.height))

a , b = Dib.attack()
print('Dib attacks with critical {} make {} damages.'.format(b , a))

a , b = Bob.attack()
print('Bob attacks with critical {} make {} damages.'.format(b , a))

a , b = Tuk.attack()
print('Tuk attacks with critical {} make {} damages.'.format(b , a))
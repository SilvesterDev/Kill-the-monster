# here I import the library 'random'
import random
r = random.Random()

# here I let the player choose wich monster he wants to fight
input('Welcome in the dungeon of death!')
input('You can choose which monster you want to fight!')
wich_monster = input('So do you want to fight a mummy(easy), Frankenstein(medium) or a dragon(hard)? ')

# here I make the loops
loop_1 = False
loop_2 = False
loop_3 = False

# here I make the players health
player_health = 1500

# here I make the odds wich weapon the player gets
weapon_odds_easy = ['Goblin sword(common)', 'Goblin sword(common)', 'Goblin sword(common)', 'Goblin sword(common)', 'Goblin sword(common)', 
"Viking's axe(uncommon)", "Viking's axe(uncommon)", "Viking's axe(uncommon)", "Viking's axe(uncommon)",
'Explosive bow(rare)', 'Explosive bow(rare)', 'Explosive bow(rare)',
'Fire Sword(Epic)', 'Fire Sword(Epic)',
"Thor's hammer(LEGENDARY)"]

weapon_odds_medium = ["Viking's axe(uncommon)", "Viking's axe(uncommon)", "Viking's axe(uncommon)", "Viking's axe(uncommon)",
'Explosive bow(rare)', 'Explosive bow(rare)', 'Explosive bow(rare)',
'Fire Sword(Epic)', 'Fire Sword(Epic)', 'Fire Sword(Epic)',
"Thor's hammer(LEGENDARY)", "Thor's hammer(LEGENDARY)",
'Excalibur(MYTHIC)']

weapon_odds_hard = ['Explosive bow(rare)', 'Explosive bow(rare)', 'Explosive bow(rare)', 'Explosive bow(rare)',
'Fire Sword(Epic)', 'Fire Sword(Epic)', 'Fire Sword(Epic)',
"Thor's hammer(LEGENDARY)", "Thor's hammer(LEGENDARY)",
'Excalibur(MYTHIC)',
'Elder Wand(ALLMIGHTY!!)']

# here I make the odds wich piece of armor the player gets
armor_odds_easy = ['Goblin Steel chestplate(common)', 'Goblin Steel chestplate(common)', 'Goblin Steel chestplate(common)', 'Goblin Steel chestplate(common)', 'Goblin Steel chestplate(common)',
'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)',
'TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)',
'Flame shield(Epic)', 'Flame shield(Epic)',
"Thor's Chestpiece(LEGENDARY)"]

armor_odds_medium = ['Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)', 'Full Viking armor(Uncommmon)',
'TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)',
'Flame shield(Epic)', 'Flame shield(Epic)', 'Flame shield(Epic)',
"Thor's Chestpiece(LEGENDARY)", "Thor's Chestpiece(LEGENDARY)",
'Royal Chainmail(MYTHIC)']

armor_odds_hard = ['TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)', 'TNT Armor(rare)',
'Flame shield(Epic)', 'Flame shield(Epic)', 'Flame shield(Epic)', 'Flame shield(Epic)',
"Thor's Chestpiece(LEGENDARY)", "Thor's Chestpiece(LEGENDARY)", "Thor's Chestpiece(LEGENDARY)",
'Royal Chainmail(MYTHIC)', 'Royal Chainmail(MYTHIC)',
'Wizards Uniform(ALLMIGHTY!!)']

# here i make the number for what set of stuff the get
number_choice = r.randint(0, 9)

# here I choose wich loop i need to turn on and wich weapon the get
if wich_monster == 'mummy' or wich_monster == 'Mummy':
    loop_1 = True
    choice_weapon = weapon_odds_easy[number_choice]
    choice_armor = armor_odds_easy[number_choice]
elif wich_monster == 'frankenstein' or wich_monster == 'Frankenstein':
    loop_2 = True
    choice_weapon = weapon_odds_medium[number_choice]
    choice_armor = armor_odds_medium[number_choice]
elif wich_monster =='dragon' or wich_monster == 'Dragon':
    loop_3 = True
    choice_weapon = weapon_odds_hard[number_choice]
    choice_armor = armor_odds_hard[number_choice]
else:
    print('Did you make a typo? Run the program again and try again.')

# here I print what the player gets
input('You got a ' + choice_weapon + ' and ' + choice_armor + ' to fight with!')
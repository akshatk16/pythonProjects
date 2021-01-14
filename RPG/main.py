from classes.game import Person
import random


magic = [{"name":"Fire", "cost":10, "dmg":60},
	   {"name":"Thunder", "cost":15, "dmg":70},
	   {"name":"Fire", "cost":20, "dmg":80}]

player = Person(500, 10, 100, 30, magic)
enemy  = Person(600, 10, 50, 20, magic)

running = True
i = 0
print("AN ENEMY ATTACKS!\n")

while running:
	print("======================")
	player.choose_action()
	choice = int(input("\nChoose Action: "))
	choice -= 1
	print("\nYou chose", player.actions[choice])

	if choice == 0:
		dmg = player.gen_dmg()
		enemy.take_dmg(dmg)
		print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp(), "\n")

	elif choice == 1:
		if player.mp <= 0:
			print("\nNo Magic Points\n")
			continue
		player.choose_magic()
		spell = int(input("\nChoose spell:"))
		spell -= 1
		dmg = player.gen_spell_dmg(spell)
		enemy.take_dmg(dmg)
		print("\nYou attacked for", dmg, "points of damage using", player.get_spell_name(spell), ". Enemy HP:", enemy.get_hp(), "\n")
		player.reduce_mp(magic[spell]["cost"])

	if enemy.mp <= 0:
		enemy_choice = 0
	else:
		enemy_choice = random.randrange(0,2)
	print("Enemy chose", player.actions[enemy_choice])
	if enemy_choice == 0:
		dmg = enemy.gen_dmg()
		player.take_dmg(dmg)
		print("Enemy attacked for", dmg, "points of damage. Player HP:", player.get_hp(), "\n")

	elif enemy_choice == 1:
		enemy_spell = random.randrange(0,3)
		dmg = enemy.gen_spell_dmg(enemy_spell)
		player.take_dmg(dmg)
		print("Enemy attacked for", dmg, "points of damage using", enemy.get_spell_name(enemy_choice), ". Player HP:", player.get_hp(), "\n")
		enemy.reduce_mp(magic[enemy_spell]["cost"])



	if player.hp == 0:
		print("You lose!")
		running = False

	elif enemy.hp == 0:
		print("You win!")
		running = False

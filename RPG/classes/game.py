import random


class Person:
	def __init__(self, hp, mp, atk, dfc, magic):
		self.maxhp 	= hp
		self.hp	= hp
		self.maxmp	= mp
		self.mp	= mp
		self.atkL	= atk - 10
		self.atkH	= atk + 10
		self.dfc	= dfc
		self.magic	= magic
		self.actions= ["Attack", "Magic"]


	def gen_dmg(self):
		return random.randrange(self.atkL, self.atkH)


	def gen_spell_dmg(self, i):
		mgL = self.magic[i]["dmg"] - 5
		mgH = self.magic[i]["dmg"] + 5
		return random.randrange(mgL, mgH)


	def take_dmg(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp


	def get_hp(self):
		return self.hp


	def get_max_hp(self):
		return self.maxhp


	def get_mp(self):
		return self.mp


	def get_max_mp(self):
		return self.maxmp


	def reduce_mp(self, cost):
		self.mp -= cost


	def get_spell_name(self, i):
		return self.magic[i]["name"]


	def get_spell_cost(self, i):
		return self.magic[i]["cost"]


	def choose_action(self):
		i = 1
		print("Actions")
		for item in self.actions:
			print(str(i) + ": ", item)
			i += 1


	def choose_magic(self):
		i = 1
		print("\nMAGIC:")
		for item in self.magic:
			print(str(i) + ": ", item["name"], "(cost:",
			str(item["cost"]),")" )
			i += 1

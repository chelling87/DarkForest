from random import random


class Civilization(object):
    def __init__(self, malicious_percent):
        self.malicious = random() < malicious_percent
        self.tech_growth_rate = random()
        self.population = random()
        self.num_solar_systems_occupied = 1
        self.tech_prowess = random()
        self.resources = self.num_solar_systems_occupied

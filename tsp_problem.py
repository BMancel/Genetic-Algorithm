# -*- coding: utf-8 -*-
"""
04/03/2024

@author: MANCEL & KMET

Template file for your Exercise 3 submission
(GA solving TSP example)
"""
import random
from ga_solver import GAProblem
import cities


class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""

    def __init__(self, city_dict):
        """
        Initializes the TSProblem instance with a dictionary of cities.

        Args:
            city_dict (dict): Dictionary containing city names as keys
            and their coordinates as values.
        """
        self.city_dict = city_dict

    def new_chromosome(self):
        """ Create a random chromosome thanks to mastermind.py"""
        # initialize always the same chromosome
        chromosome = list(self.city_dict.keys())
        # shuffle the cities to get a random chromosome
        random.shuffle(chromosome)
        # return chromosome
        return chromosome

    def fitness(self, chromosome):
        """Calculate the fitness of a chromosome"""
        # calculate the distance to travel through all cities
        return - cities.road_length(city_dict, chromosome)

    def crossing(self, parent_a, parent_b):
        """Create a new chromosome from parent_a and parent_b"""
        # take the first half of the road from parent_a
        x_point = len(parent_a.chromosome) // 2
        # create a new chromosome first constituted of half of
        # parent_a's chromosome
        new_chrom = parent_a.chromosome[:x_point]

        # Add cities from parent_b
        # that are not already present in new_chrom
        for city in parent_b.chromosome[x_point:]:
            if city not in new_chrom:
                new_chrom.append(city)

        possible_cities = cities.default_road(city_dict)
        # If new_chrom is not long enough,
        # complete it with any remaining cities
        while len(new_chrom) < len(parent_a.chromosome):
            for city in possible_cities:
                if city not in new_chrom:
                    new_chrom.append(city)
                    # we stop as soon as new_chrom reaches the right size
                    if len(new_chrom) == len(parent_a.chromosome):
                        break
        return new_chrom

    def mutation(self, chromosome):
        """Create a mutation on a chromosome"""
        mutation_point = random.randint(0, len(chromosome)-1)
        mutation_point2 = random.randint(0, len(chromosome)-1)
        # mutation : swap genes present at the 2 generated indexes
        chromosome[mutation_point], chromosome[mutation_point2] = (
            chromosome[mutation_point2], chromosome[mutation_point]
        )
        return chromosome


if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem(city_dict)
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    solver.show_generation_summary()
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)

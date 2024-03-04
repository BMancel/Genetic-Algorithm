# -*- coding: utf-8 -*-
"""
04/03/2024

@author: MANCEL & KMET

Template file for your Exercise 3 submission
(generic genetic algorithm module)
"""
import random


class Individual:
    """Represents an Individual for a genetic algorithm"""
    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem():
    """Defines a Genetic algorithm problem to be solved by ga_solver"""

    def new_chromosome(self):
        """Create a new chromosome"""

    def fitness(self, chromosome):
        """Evaluate the fitness of a chromosome"""

    def crossing(self, parent_a, parent_b):
        """Create a new chromosome from parent_a and parent_b"""

    def mutation(self, chromosome):
        """Create a mutation on a chromosome"""


class GASolver:
    """ Solve the problem with an a genetic algorithm """
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem
        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional):
            Selection rate between 0 and 1.0 Defaults to 0.5
            mutation_rate (float, optional):
            mutation_rate between 0 and 1.0 Defaults to 0.1
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for _ in range(pop_size):
            # initialize a random chromosome
            chromosome = self._problem.new_chromosome()
            # calculate the score of the random chromosome
            fitness = self._problem.fitness(chromosome)
            # we create a new random individual, constituted of
            # - a random guess (chromosome)
            # - the associated score (fitness)
            new_individual = Individual(chromosome, fitness)
            # at each iteration, we add the new individual created to the list
            self._population.append(new_individual)

    def evolve_for_one_generation(self):
        """Improve the curent generation thanks to selection,
            reproduction & mutation
        """
        # Apply the process for one generation :
        # -	Sort the population (Descending order)
        self._population.sort(reverse=True)
        # -	Selection: Remove x% of population (less adapted)
        selected_population_index = int(len(self._population)
                                        * self._selection_rate)
        selected_population = self._population[:selected_population_index]
        new_population = selected_population

        # - Reproduction: Recreate the same quantity by crossing the
        #   surviving ones.
        while len(new_population) < len(self._population):
            # creation of a copy to select parent_b considering parent_a
            selected_population_temp = selected_population.copy()
            # parent_a is a random individual from new_population
            parent_a = random.choice(selected_population_temp)
            # remove parent_a from the new population
            selected_population_temp.remove(parent_a)
            # parent_b is a random individual (different from parent_a)
            # from the new population
            parent_b = random.choice(selected_population_temp)

            # create a new chromosome constituted of part of
            # parent_a's chromosome and parent_b's chromosome
            new_chrom = self._problem.crossing(parent_a,
                                               parent_b)

        # -	Mutation: For each new Individual, mutate with probability
        #   mutation_rate i.e., mutate it if a random value is below
        #   mutation_rate
            for _ in range(len(new_chrom)):
                # generates a number between 0 and 1
                # If it is lower than the mutation_rate
                # then creation of a mutation on the new chromosome
                if random.random() < self._mutation_rate:
                    # create a mutation on the new chromosome
                    new_chrom = self._problem.mutation(new_chrom)
            # calculate the fitness of the new chromosome
            new_fitness = self._problem.fitness(new_chrom)
            # creation of the new individual composed of new_chrome
            # (mutated or not) and its fitness
            new_individual = Individual(new_chrom, new_fitness)
            # add the new individual to new_population
            new_population.append(new_individual)
        # once the new_population is complete,
        # we assign self._population to this new population
        self._population = new_population

    def show_generation_summary(self):
        """ Print some debug information
            on the current state of the population
        """
        best_individual = max(self._population)
        worst_individual = min(self._population)
        average_fitness = sum(individual.fitness for individual in self._population) / len(self._population)
        print("Generation Summary:"
              "\n- Best Individual:", best_individual,
              "\n- Worst Individual:", worst_individual,
              "\n- Average Fitness:", average_fitness)

    def get_best_individual(self):
        """ Return the best Individual of the population """
        # sort the population in descending order of fitness
        self._population.sort(reverse=True)
        # return the higher score
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function
            until one of the two condition is achieved :
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        count_generation = 0
        # 1st condition : don't exceed 500 generations
        while count_generation < max_nb_of_generations:
            best_fitness = self.get_best_individual().fitness
            # 2nd condition : if threshold_fitness is specified,
            # stop if the best score is higher
            if (threshold_fitness is not None and
                    best_fitness >= threshold_fitness):
                # if threshold_fitness is provided and reached, break the loop
                break
            # else evolve the generation
            self.evolve_for_one_generation()
            # increment the counter until one of the conditions is met
            count_generation += 1
        return self._population, count_generation

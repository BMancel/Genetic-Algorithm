# -*- coding: utf-8 -*-
"""
04/03/2024

@author: MANCEL & KMET

Template file for your Exercise 3 submission
(GA solving Mastermind example)
"""
import random
from ga_solver import GAProblem
import mastermind as mm


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the Mastermind game"""

    def __init__(self, match):
        """Initialize the MastermindProblem instance
            with a MastermindMatch object.
            Args:
            match (MastermindMatch): An object
            representing a Mastermind game match.
        """
        self.match = match

    def __str__(self):
        """Return a string representation of the MastermindProblem object."""
        return f"MastermindProblem with match: {self.match}"

    def new_chromosome(self):
        """ Create a random chromosome thanks to mastermind.py"""
        return self.match.generate_random_guess()

    def fitness(self, chromosome):
        """Calculate the fitness of a chromosome"""
        return self.match.rate_guess(chromosome)

    def crossing(self, parent_a, parent_b):
        """Create a new chromosome from parent_a and parent_b"""
        # select a random index from parent_a
        x_point = random.randrange(0, len(parent_a.chromosome))
        # create a new chromosome constituted of part of
        # parent_a's chromosome and parent_b's chromosome
        new_chrom = (
            parent_a.chromosome[0:x_point]
            + parent_b.chromosome[x_point:]
            )
        return new_chrom

    def mutation(self, chromosome):
        """Create a mutation on a chromosome"""
        valid_colors = mm.get_possible_colors()
        # select a random index from new_chrom
        random_position = random.randint(0, len(chromosome)-1)
        # select a random color from valid_colors
        new_gene = random.choice(valid_colors)
        # apply the mutation to the index generated above
        new_chrom = (
            chromosome[0:random_position]
            + [new_gene]
            + chromosome[random_position+1:]
        )
        return new_chrom


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.reset_population(pop_size=10)
    solver.evolve_until()
    solver.show_generation_summary()
    print(
        f"Best guess {mm.encode_guess(solver.get_best_individual().chromosome)} {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")

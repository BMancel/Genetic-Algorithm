# How to implement reusability in practice

We use a genetic solver to solve many problems
## Authors

- [@BMancel](https://github.com/BMancel)
- [@Ratislav insert your account + URL]


## Installation

### 1. Download the files
Make sure that ga_solver is in the same folder as the _problem files

### 2. implement your problem 
with the four functions of the GAProblem class :

```python
def new_chromosome(self):
        """Create a new chromosome"""

def fitness(self, chromosome):
        """Evaluate the fitness of a chromosome"""

def crossing(self, parent_a, parent_b):
        """Create a new chromosome from parent_a and parent_b"""

def mutation(self, chromosome):
        """Create a mutation on a chromosome"""
```

### 3. run the algorithm

```python
from ga_solver import GASolver

problem = YourProblem()
solver = GASolver(problem)
solver.reset_population()
solver.evolve_until()
```

### 4. More information
you can read more information about your population with :

```python
solver.show_generation_summary()
```
## Running Tests

To run tests, run the following command

```bash
  python .\mastermind_problem.py
```
or
```bash
  python .\tsp_problem.py
```
## Optimizations

you can optimize the algorithm by adjusting the ga_solver.py file:
- init from GASolver class :
    - ```selection_rate=0.5```
    - ```mutation_rate=0.1```
- reset_population : 
    - ``` pop_size=50```
- evolve_until :
    - ```max_nb_of_generations=500```
    - ```threshold_fitness=None```
## Usage/Examples

Some exemples (mastermind & tsp) are in the repo.

All codes are commented for better understanding.

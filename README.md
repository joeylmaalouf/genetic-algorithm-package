# Genetic Algorithm Package

Contains a generalizable genetic algorithm written in Python.


## Installation
##### ([GenAlg on PyPI](https://pypi.python.org/pypi/genalg))

`sudo pip2 install genalg`


## Genetic Algorithm
##### (`genalg/main.py`)

class `Population`: Given problem specifications, create and run through a population of possible individual solutions until either the fitness goal or the generation limit is reached.

class `Individual`: Given problem specifications, randomly create a possible solution individual.


## Example Usage
##### (`examples/function-maximizer.py`)

```python
import genalg


def func_to_optimize(inputs):
  x, y, z = inputs
  return x * y / float(z)


if __name__ == "__main__":
  p = genalg.Population(
    popsize = 200,                # number of individuals in the population
    nchrom = 3,                   # number of chromosomes per individual
    chromset = range(1, 20)       # set from which to pick chromosomes
  )
  best = p.run(
    eval_fn = func_to_optimize,   # function to optimize
    fitness_goal = float("Inf"),  # maximum fitness to optimize towards
    generations = 400             # maximum generations to run for
  )
  print(best)
```


## Credits

* [@droundy](https://github.com/droundy) - mating options, misc. tweaks

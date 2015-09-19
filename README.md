#Genetic Algorithm Package

Contains a generalizable genetic algorithm written in Python.


##Installation
#####([GenAlg on PyPI](https://pypi.python.org/pypi/genalg/))

`sudo pip2 install genalg`


##Genetic Algorithm
#####(`genalg/main.py`)

class `Population`: Given problem specifications, create and run through a population of possible individual solutions until either the fitness goal or the generation limit is reached.

class `Individual`: Given problem specifications, randomly create a possible solution individual.


##Example Usage
#####(`examples/function-minimizer.py`)

```python
import genalg

def func_to_optimize(inputs):
  x, y, z = inputs
  return x * y / float(z)

if __name__ == "__main__":
  p = genalg.Population(
    popsize = 200,
    nchrom = 3,
    chromset = range(1, 20)
  )
  best = p.run(
    eval_fn = func_to_optimize,
    fitness_goal = -float("Inf"),
    generations = 300,
    minimize = True
  )
  print(best)
```


##To Do:

* Add crossover and release as v1.0.3

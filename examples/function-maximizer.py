import sys
sys.path.append("..")
from GeneticAlgorithm import genalg


def function_maximizer(inputs):
  x, y, z = inputs
  return x ** y / z


if __name__ == "__main__":
  p = genalg.Population(popsize = 100, nchrom = 3, chromset = range(1, 20))
  best = p.run(eval_fn = function_maximizer, fitness_goal = float("Inf"), generations = 300, verbose = True)

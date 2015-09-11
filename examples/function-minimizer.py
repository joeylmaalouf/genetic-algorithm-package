import sys
sys.path.append("..")
import genalg


def func_to_optimize(inputs):
  x, y, z = inputs
  return x * y / float(z)


if __name__ == "__main__":
  p = genalg.Population(popsize = 200, nchrom = 3, chromset = range(1, 20))
  best = p.run(eval_fn = func_to_optimize, fitness_goal = -float("Inf"), generations = 300, minimize = True)
  print(best)

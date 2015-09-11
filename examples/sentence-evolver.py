import string
import sys
sys.path.append("..")
from GeneticAlgorithm import genalg


def levenshtein_distance(s1, s2):
  # http://rosettacode.org/wiki/Levenshtein_distance#Python
  if len(s1) > len(s2):
    s1, s2 = s2, s1
  distances = range(len(s1) + 1)
  for index2, char2 in enumerate(s2):
    newDistances = [index2 + 1]
    for index1,char1 in enumerate(s1):
      if char1 == char2:
        newDistances.append(distances[index1])
      else:
        newDistances.append(1 + min((distances[index1],
                                     distances[index1 + 1],
                                     newDistances[-1])))
    distances = newDistances
  return distances[-1]


if __name__ == "__main__":
  target_string = "Evolution is cool"
  p = genalg.Population(popsize = 1000, nchrom = len(target_string), chromset = string.ascii_letters)
  best = p.run(eval_fn = lambda x: levenshtein_distance(x, target_string), fitness_goal = 0, generations = float("Inf"), minimize = True, verbose = True)

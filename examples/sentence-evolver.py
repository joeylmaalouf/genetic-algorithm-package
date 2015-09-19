from difflib import SequenceMatcher
import string
import genalg


def string_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == "__main__":
  target_string = "Joey"
  p = genalg.Population(
    popsize = 1000,
    nchrom = len(target_string),
    chromset = string.ascii_letters
  )
  p.run(
    eval_fn = lambda x: string_similarity(x, target_string),
    fitness_goal = 1.0,
    generations = float("Inf"),
    include_swap = True,
    verbose = True
  )

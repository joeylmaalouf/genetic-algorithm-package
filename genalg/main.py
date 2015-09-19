import random


class Population(object):
  # Population(): a group of individuals

  def __init__(self, popsize = 10000, nchrom = 32, chromset = range(10)):
    # __init__(): initialize the population with randomly created individuals
    # popsize: the number of individuals that the population has
    # nchrom: the number of chromosomes each individual in the population has
    # vals: the set of possible values each chromosome of each individual can take
    super(Population, self).__init__()
    self.size = popsize
    self.members = [Individual(nchrom, chromset) for _ in range(self.size)]

  def run(self, eval_fn, fitness_goal = float("Inf"), generations = 10000, minimize = False, include_swap = False, mutate_cutoff = 1 / 3.0, scramble_cutoff = 2 / 3.0, verbose = False):
    # run(): step the population forward through generations until it
    #        finds an optimal solution or the generation cap is reached
    # eval_fn: the function that takes in a list of chromosomes and returns a fitness
    # fitness_goal: the cutoff value at which to stop
    # generations: the maximum generation limit at which to return the best individual
    # minimize: boolean flag to minimize fitness instead of maximize
    # include_swap: boolean flag to add chromosome swap as a randomly selected alternative to standard mutation
    # mutate_cutoff: the ratio of the population at which to start mutating
    # scramble_cutoff: the ratio of the population at which to start scrambling
    # verbose: boolean flag to print each generation's best individual
    if fitness_goal == float("Inf") and generations == float("Inf"):
      raise ValueError("Either the fitness goal or the generation cap must not be set to infinity, or else the algorithm will evolve indefinitely.")

    current_generation = 0
    while current_generation < generations:
      current_generation += 1

      for individual in self.members:
        # evaluate each individual
        individual.fitness = eval_fn(individual.chromosomes)

        condition = (individual.fitness >= fitness_goal) if not minimize else (individual.fitness <= fitness_goal)
        if condition:
          if verbose:
            print("Generation {0}, found fit enough individual: {1} with fitness {2} ({3}= {4})".format(
              current_generation, individual, individual.fitness, ">" if not minimize else "<", fitness_goal))
          # return an individual if it surpasses the threshold
          return individual

      # leave the top segment alone
      # mutate the middle segment
      # scramble the bottom segment
      mid = slice(int(self.size * mutate_cutoff), int(self.size * scramble_cutoff))
      bot = slice(int(self.size * scramble_cutoff), None)
      for individual in self.members[mid]:
        individual.mutate(include_swap)
      for individual in self.members[bot]:
        individual.scramble()

      # sort the population by fitness
      self.members.sort(key = lambda i: i.fitness, reverse = not minimize)
      if verbose:
        print("Generation {0}, best individual: {1} with fitness {2}".format(current_generation, self.members[0], self.members[0].fitness))

    # generation limit reached, return the best member thus far
    if verbose:
      print("Generation limit reached ({0}), best individual: {1} with fitness {2}".format(generations, self.members[0], self.members[0].fitness))
    return self.members[0]

  def __str__(self):
    # __str__(): return a string representation of the population
    return "\n".join([str(i) for i in self.members])


class Individual(object):
  # Individual(): one member of a population, representing a possible solution

  def __init__(self, nchrom = 32, chromset = range(10)):
    # __init__(): initialize the individual with randomly assigned chromosomes
    # nchrom: the number of chromosomes each individual has
    # vals: the set of possible values each chromosome can take
    self.fitness = None
    self.length = nchrom
    self.possibilities = chromset
    self.chromosomes = []
    self.scramble() # randomly initialize the starting chromosomes

  def scramble(self):
    # scramble(): fully randomize the individual
    self.chromosomes = [random.choice(self.possibilities) for _ in range(self.length)]
    return self

  def mutate(self, include_swap):
    # mutate(): mutate a random chromosome into a new one, or swap the positions of two chromosomes
    if include_swap and random.random() >= 0.5:
    	i, j = random.randrange(self.length), random.randrange(self.length)
    	self.chromosomes[i], self.chromosomes[j] = self.chromosomes[j], self.chromosomes[i]
    else:
    	self.chromosomes[random.randrange(self.length)] = random.choice(self.possibilities)
    return self

  def __str__(self):
    # __str__(): return a string representation of the individual
    return str(self.chromosomes)


if __name__ == "__main__":
  # define an example problem
  population_size = 1000
  num_chromosomes = 15
  possible_values = range(20)
  fitness_goal = 16.0
  max_generations = 2000
  def evaluation_function(chromosomes):
    return float(sum(chromosomes)) / len(chromosomes)

  # create and run the population
  p = Population(population_size, num_chromosomes, possible_values)
  best = p.run(evaluation_function, fitness_goal, max_generations, verbose = True)

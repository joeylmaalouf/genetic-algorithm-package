from setuptools import setup

setup(
  name = "genalg",
  version = "1.0.0",
  author = "Joey L. Maalouf",
  author_email = "joeylmaalouf@gmail.com",
  description = "A generalizable genetic algorithm package written in Python.",
  long_description = "GenAlg is a generalizable genetic algorithm package written in Python. It was created for the purpose of providing developers with a simple yet powerful solution approximation technique that, given enough time, can also find exact answers.",
  url = "https://github.com/joeylmaalouf/genetic-algorithm-package",
  license = "MIT",
  classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2.7",
  ],
  keywords = "genetic algorithm optimization solution approximation machine learning",
  packages = ["genalg"]
)

from setuptools import setup
from genalg import __name__, __version__, __author__, __author_email__, __description__, __long_description__, __url__

setup(
  name = __name__,
  version = __version__,
  author = __author__,
  author_email = __author_email__,
  description = __description__,
  long_description = __long_description__,
  url = __url__,
  license = "MIT",
  classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2.7"
  ],
  keywords = "genetic algorithm optimization solution approximation machine learning",
  packages = [__name__]
)

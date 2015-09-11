# upload *.egg-info/PGK-INFO to https://pypi.python.org/pypi?%3Aaction=submit_form
python2 setup.py sdist
python2 setup.py bdist_wheel
sudo twine upload dist/*

python2 setup.py sdist
python2 setup.py bdist_wheel
sudo twine upload dist/*

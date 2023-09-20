@echo installing python lib..

set file=cbuff-1.0.0-py3-none-any.whl

pip uninstall %file%
python setup.py sdist bdist_wheel
cd dist
pip install %file%
cd ..
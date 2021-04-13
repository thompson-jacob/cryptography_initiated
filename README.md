**Activate the virtual environment**
set up a virtual environment using : python3 -m venv 'name_of_file_here'

Source of this repository below
```
source blockchain-env/bin/activate
```


**Install all packages**
this command will download all dependency packages written in the requirements file
```
pip3 install -r requirements.txt
```

**Make sure to test**

Activate the virtual environment and run pytest using
# this will run all tests in the tests folder
```
python3 -m pytest backend/tests
```

**Activate the virtual environment**
set up a virtual environment using : python3 -m venv 'name_of_file_here'

Source of this repository below
```
source blockchain-env/bin/activate
```
**Create config.py file**
this will hold your non-public data and adds a git-ignore file, it contains this data

```
NANOSECONDS = 1 
MICROSECONDS = 1000 * NANOSECONDS
MILLISECONDS = 1000 * MICROSECONDS
SECONDS = 1000 * MILLISECONDS

MINE_RATE = 4 * SECONDS
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

**Run The application and API**

Make sure to activate the virtual environment.

```
python3 -m backend.app
```



Scaffold for Python Projects
----------------------------

##Setting up a Virtual Environment
In your project directory create a new virtual environment:
```
virtualenv myenv
```

To get started with installing Python modules:
1. First activate the environment
```
source myenv/bin/activate
```
2. Install modules with pip
```
pip install flask
```
3. Save project dependencies
```
pip freeze > requirements.txt
```

*Have a requirements.txt already?*
```
pip install -r requirements.txt
```

##Running tests with unittest

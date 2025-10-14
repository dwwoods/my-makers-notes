# What is pytest?

Pytest is a kind of programming tool called a test framework. It is written for use with the programming language Python. We can use it to test that our systems do what they are supposed to do. We can also use it to build our test-driving practice.

## Setting up a new project

To set up a new pytest project:

```bash
# First, create a directory for your project
; mkdir your-project-directory
; cd your-project-directory

# Create your venv
; python -m venv project-name-venv

# Ensure your venv is activated
; source project-name-venv/bin/activate

# Remember, you will see if your venv is activated from the venv name in parenthesis like this
(project-name-venv) ; 


# Next, install pytest using pip (if you haven't already)
(project-name-venv) ; pip install pytest
# This may take a few minutes

# Create a folder for your testing files
(project-name-venv) ; mkdir tests
(project-name-venv) ; mkdir lib

# Create module init files in both `tests/` and `lib/` directories
(project-name-venv) ; touch tests/__init__.py
(project-name-venv) ; touch lib/__init__.py
# These might seem pointless, but they're important for Python to find
# all of your files.

# Verify your setup by running pytest
(project-name-venv) ; pytest
================================ test session starts ================================
platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
rootdir: .../your-project-directory
collected 0 items

=============================== no tests ran in 0.01s ===============================

# And create a repository for your changes
(project-name-venv) ; git init .
(project-name-venv) ; echo "*venv*" > .gitignore
(project-name-venv) ; git add .
(project-name-venv) ; git commit -m "Project setup"

# Then go and create a repository on github.com
# On the next screen after you have created the repository,
# follow the "Push an existing repository from the command line" section
# To push your project to your github repository
# It will look something like this...
(project-name-venv) ; git remote add origin YOUR_REMOTE_ADDRESS
(project-name-venv) ; git branch -M main
(project-name-venv) ; git push -u origin main
```
# PyApp
One of three Python related projects for my final semester, this one to build a Python Web App.
This was one of the hardest projects I've ever done, namely due to never creating a web application before.
In the end however, I learned alot on how web applications work, both front and back end, 
and gained a significant appreciation for the sites I visit on a daily basis. One app down, two more to go!

# Requirements:
### Python Version 3.9 or higher
To check if you have python installed run the following from any cli
         `python --version`
Otherwise, if you need to install or update Python, download it from:
        https://www.python.org/downloads/

### Flask
### Flask-SQLAcademy
### Flask-Login
Use pip to install the required Flask libraries, by running the following from any cli:
    `pip install Flask Flask-SQLAlchemy Flask-Login`

### If you need to install pip, follow the instructions here:
    https://pip.pypa.io/en/stable/installation/

# How To Run:
1) Download the files to a directory or to your desktop
2) Navigate to the folder where you downloaded your files using the terminal / cmd prompt
3) Setup your virtual environment
    Windows: `venv\Scripts\activate`
    Mac / Linux: `source venv/bin/activate`
4) If you don't have one setup, create one using the following:
    `python3 -m venv venv`
5) Run the following to install the dependencies
    `pip install flask`
6) Verify flask is installed:
    `pip list | grep Flask`
7) Finally, run the following command and navigate to the listed address on a web browser:
    `python3 main.py`


## Sources:
### Naming
Human Last Names sourced from the following GitHub: https://gist.github.com/craigh411/19a4479b289ae6c3f6edb95152214efc  
Human Female Names sourced from the following GitHub: https://github.com/stdlib-js/datasets-female-first-names-en?tab=readme-ov-file  
Human Male names sourced from the following GitHub: https://github.com/stdlib-js/datasets-male-first-names-en  
All other names were generated using an Ai, then imported as a JSON file in `PyApp/data/`
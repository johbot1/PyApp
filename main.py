#App.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc:
from website import create_app

# Flask constructor takes the name of
# from website import create_app
# current module (__name__) as argument.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)



# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


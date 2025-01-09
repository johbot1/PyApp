#Main.py
#Author: John Botonakis
#With help from "Tech With Tim" on Youtube
#Desc: This is the entry point for the web app.
# It initializes the app using the `create_app` function from the `website` package and starts the development server.
from website import create_app

# Flask constructor takes the name of
# from website import create_app
# current module (__name__) as argument.
app = create_app()

if __name__ == '__main__':
    # Starts the development server
    # `debug=True` enables debug mode, which provides detailed error messages
    # and automatically reloads the server when code changes.
    app.run(debug=True)
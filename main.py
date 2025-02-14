# Main.py
# Author: John Botonakis
# With some help from "Tech With Tim" on YouTube
# Desc:
# This is the entry point for the web app. It initializes the app
# using the `create_app` function from the `website` package and
# starts the development server.
from website import create_app

# Creates an application using the model defined in the website folder
# It then runs that created app.
app = create_app()

#FEEDBACK
# [] Errors shouldn't be dismissible
# [] Error for when pass don't match while signing up
# [] Success message for account creation
# [] Error when account is already created
# [X] Remove "GET" from auth login
# [] Allow logins to work


if __name__ == '__main__':
    # Starts the development server
    # `debug=True` enables debug mode, which provides detailed error messages
    # and automatically reloads the server when code changes.
    # Change to 'debug=False' when deploying.
    app.run(debug=True)

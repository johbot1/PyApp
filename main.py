#App.py
#Author: John Botonakis
#Desc:
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)



# # Flask constructor takes the name of
# from website import create_app
# # current module (__name__) as argument.
# app = Flask(__name__)
# app.register_blueprint(views, url_prefix='/views')
#
# # The route() function of the Flask class is a decorator,
# # which tells the application which URL should call
# # the associated function.
# @app.route("/")
# # ‘/’ URL is bound with home() function.
# def home():
#     return render_template("home.html")
#
# #If "login" is successful return the following page
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name
#
# #"Login Screen" to gather name data
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['nm']
#         return redirect(url_for('success',name = username))
#     else:
#         username = request.args.get('nm')
#         return redirect(url_for('success',name = username))
#
# #Main Driver function
# if __name__ == '__main__':
#     # run() method of Flask class runs the application
#     # on the local development server.
#     app.run(debug=True, port=8000)

from tna import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


#     @app.route('/')
# def startpage():
#     return "<h1>Hello, World!</h1>"


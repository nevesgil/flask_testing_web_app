from website import create_app

app = create_app()

if __name__ == '__main__':
    # only if we run this file, not if we import the file, we are gonna execute this file
    # avoids running the web app on just importing it
    app.run(debug=True)


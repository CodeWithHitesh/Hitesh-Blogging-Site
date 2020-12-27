from flaskblog import create_app

# You can do this import here in run.py but not in others because of circular import issue.


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

# Password is hs.
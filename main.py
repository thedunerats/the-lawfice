# This is a comment in Python. Please use comments to describe your code and please do not use comments
# to comment out huge chunks of code and confuse your teammates later.

# In reality, for reasons related to maintainability and scalability (and overall just keeping the structure
# less confusing), I would define my flask app and any configuration related to it elsewhere. I would then
# come here and actually start the app.

from src.app import flask_app

if __name__ == '__main__':
    flask_app.run()

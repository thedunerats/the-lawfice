from waitress import serve
from src import app

serve(app.flask_app, host='0.0.0.0', port=8080)

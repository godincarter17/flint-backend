from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# Add other extensions here as needed (e.g., Flask-JWT-Extended for authentication)

# Initialize extensions without linking them to the Flask app instance yet
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def init_extensions(app):
    """
    Function to initialize and register all extensions with the Flask application.
    This is called from within the create_app() factory function.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    # You could also initialize other extensions here, e.g., jwt.init_app(app)

import os, signal
from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user

# Local Imports
from config import Config
from app.extensions import db, logger
import app.globals as globals


def create_app(config_class=Config):
    app = Flask(__name__, static_folder=f"{globals.basedir}/static/",template_folder=f"{globals.basedir}/templates/")
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    from app.models import Anonymous, User
    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.anonymous_user = Anonymous
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.main.main import main as main_blueprint
    app.register_blueprint(main_blueprint)      # url_prefix='/' # -- If used, each blueprint can have its own templates & static folders.
    
    from app.auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    db.init_app(app)
    with app.app_context():
        db.create_all()

        def signal_handler(sig,frame):
            logger.info(f"Signal Received -- Shutting down site")
            os._exit(0)

        signal.signal(signal.SIGTSTP, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        @app.errorhandler(404)
        def page_not_found(e):
            if current_user.is_authenticated:
                return redirect(url_for("auth.home"))
            return redirect(url_for("main.login"))

    ### Use below code if you need to add templates/static files that are in a specific location not reachable by default    
    #app.jinja_loader.searchpath.append(os.path.join(os.path.dirname(__file__),"templates"))
    #app.jinja_loader.searchpath.append(os.path.join(os.path.dirname(__file__),"static"))
    
    return app

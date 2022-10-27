# flask_security_admin/app.py

from flask import Flask

# flask security imports
from flask_security import Security, auth_required, hash_password, \
    SQLAlchemySessionUserDatastore

# flask_admin imports
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

# flask_security_admin imports
from flask_security_admin.database import db_session, init_db
from flask_security_admin.models.system import User, Role


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


# Create app
app = Flask(__name__)
app.config.from_pyfile('demo_config.py')


# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)

admin = Admin(app, template_mode='bootstrap4')
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Role, db_session))


# Views
@app.route("/")
@auth_required()
def home():
    return '<p><a href="/admin/">Click me to get to Admin!</a></p>'


def main():
    with app.app_context():
        init_db()     # Uncomment this line to create initial database
        if not app.security.datastore.find_user(email="test@me.com"):
            app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db_session.commit()
    app.run()


if __name__ == '__main__':
    main()

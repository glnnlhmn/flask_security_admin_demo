import os

from flask import Flask, render_template_string
from flask_security import Security, current_user, auth_required, hash_password, \
    SQLAlchemySessionUserDatastore
from flask_security_admin.database import db_session, init_db
from flask_security_admin.models.system import User, Role, UsersRoles

from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True

# Generate a nice key using secrets.token_urlsafe()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT",
                                                      '146585145368132386173505678016728509634')

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)

admin = Admin(app)
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Role, db_session))


# Views
@app.route("/")
@auth_required()
def home():
    return '<p><a href="/admin/">Click me to get to Admin!</a></p>'


def main():
    with app.app_context():
        # init_db()     # Uncomment this line to create initial database
        if not app.security.datastore.find_user(email="test@me.com"):
            app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db_session.commit()
    app.run()


if __name__ == '__main__':
    main()

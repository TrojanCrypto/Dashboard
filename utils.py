from google.appengine.api import users
import os

ADMIN_USERS = ['jigarkub@usc.edu', 'pashints@usc.edu']


def authenticate_user(self, email_list=None):
    if not email_list:
        email_list = []
    email_list += ADMIN_USERS

    user = users.get_current_user()
    if user:
        if user.email().lower() in email_list:
            return user
        else:
            self.response.out.write(
                "{user_email} is not authorized.  Please <a href={logout_url}>Logout</a> and re-login.".format(
                    user_email=user.email(),
                    logout_url=users.create_login_url(self.request.url).replace("true", "false")))
            return False

    else:
        self.response.out.write("Please <a href='{login_url}'>Login...</a>".format(
            login_url=users.create_login_url(self.request.url).replace("true", "false")
        ))
        return False


def template(file_name, directory="templates"):
    return os.path.join(os.path.dirname(__file__), directory, file_name)
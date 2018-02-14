import webapp2
from google.appengine.ext.webapp import template

import utils


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = utils.authenticate_user(self)
        if not user:
            return

        template_values = {
            "user": user,
        }
        page = utils.template("main.html", "templates")
        self.response.out.write(template.render(page, template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

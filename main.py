import webapp2
import utils


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = utils.authenticate_user(self)
        if not user:
            return

        self.response.out.write("Hello {}!".format(user.nickname()))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

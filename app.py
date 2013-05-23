import webapp2

import handlers

app = webapp2.WSGIApplication([
	('/', handlers.MainPage),
	webapp2.Route(r'/dashboard/us', handler = handlers.UsDashboard),
	webapp2.Route(r'/dashboard/uk', handler = handlers.UkDashboard),],
                              debug=True)
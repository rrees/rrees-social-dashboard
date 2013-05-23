import webapp2
import jinja2
import os
import logging

import otter


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class UsDashboard(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('dashboard.html')
		
		template_values = {'results' : otter.most_shared('guardiannews.com'),
			'country_code' : 'US'}

		self.response.out.write(template.render(template_values))

class UkDashboard(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('dashboard.html')
		
		template_values = {'results' : otter.most_shared('guardian.co.uk'),
			'country_code' : 'UK'}

		self.response.out.write(template.render(template_values))

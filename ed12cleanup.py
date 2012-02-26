import os
from google.appengine.ext.webapp import template

import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.api import mail
from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class EarthDayIndex(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
        
        if users.get_current_user():
            hi = user.nickname()
            
        else:
            hi = ''

        template_values = {
            'hi': hi,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


# --- 	Run System		 --------------------------------------------

class Gate(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()

        if users.get_current_user():
            door = users.create_logout_url(self.request.uri)
            enter = 'Exit'
            hi = user.nickname()
            
        else:
            door = users.create_login_url(self.request.uri)
            enter = 'Enter'
            hi = ''
                    
        template_values = {
            'door': door,
            'enter': enter,
            'hi': hi,
        }    
            
        path = os.path.join(os.path.dirname(__file__), 'gate.html')
        self.response.out.write(template.render(path, template_values))

# --- 	System Fin		 --------------------------------------------

# --- 	Run Pages		 --------------------------------------------


class EarthDayAbout(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/about.html')
        self.response.out.write(template.render(path, template_values)) 
        
class EarthDayBlog(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/blog.html')
        self.response.out.write(template.render(path, template_values)) 

class EarthDayHome(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/home.html')
        self.response.out.write(template.render(path, template_values))

class EarthDayHow(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/how.html')
        self.response.out.write(template.render(path, template_values)) 

class EarthDayMap(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/map.html')
        self.response.out.write(template.render(path, template_values)) 

class EarthDayMedia(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/media.html')
        self.response.out.write(template.render(path, template_values))      
 
class EarthDayOther(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/other.html')
        self.response.out.write(template.render(path, template_values)) 
         
class EarthDayParters(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/partners.html')
        self.response.out.write(template.render(path, template_values)) 

class EarthDayPhotos(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	
    	if users.get_current_user():
    	    hi = user.nickname()
    	   
    	else:
    	    hi = ''
        
        template_values = {
            'hi': hi,

        }

        path = os.path.join(os.path.dirname(__file__), 'pages/photos.html')
        self.response.out.write(template.render(path, template_values)) 

# --- 	Pages Fin		 --------------------------------------------

application = webapp.WSGIApplication([
	('/', EarthDayIndex),
	('/gate/?', Gate),          
	('/about/?', EarthDayAbout),
	('/blog/?', EarthDayBlog),
	('/home/?', EarthDayHome),
	('/how/?', EarthDayHow),
	('/map/?', EarthDayMap),
	('/media/?', EarthDayMedia),
	('/other/?', EarthDayOther),
	('/partners/?', EarthDayPartners),
	('/photos/?', EarthDayPhotos),
	
], debug=True)


def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
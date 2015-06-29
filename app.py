from flask import *

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')

# Routes goes here

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )



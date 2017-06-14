from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from sqlalchemy.inspection import inspect
import sys
import threading

app = Flask(__name__)
db = SQLAlchemy()


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ''

    APP_NAME = 'ApplicationName'
    SECRET_KEY = 'add_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    DEBUG = True

class WebAPIServer:
	def __init__(self, port, logger):
		self.logger = logger
		self.port = port
		print "Starting web api server on http://localhost:"+str(port)
		self.logger.log("Starting web api server on http://localhost:"+str(port))
		
	def startServer(self):
		app.config.from_object(DevelopmentConfig)
		
		self.logger.log("db init")
		db.init_app(app)
		self.logger.log("db init done")
		
		with app.app_context():
			db.create_all()
		try:
			
			self.logger.log("web api starting...")
			apimanager = APIManager(app, flask_sqlalchemy_db=db)
			apimanager.create_api(TestItem,
				methods=['GET'],
				url_prefix='/api/v1',
				collection_name='test_item')
				
			apimanager.create_api(HTTP_Response,
				methods=['GET', 'POST'],
				url_prefix='/api/v1',
				collection_name='http_response')
			
			
			# cant run in another thread... weberver/flask needs to be in main thread.
			#self.thread = threading.Thread(target=app.run, args=({'port': self.port}))
			#self.thread.daemon = True
			#self.thread.start()
			app.run(port=self.port)
			
		except OSError as err:
			self.logger.log("OS error: {0}".format(err))
		except ValueError:
			self.logger.log("Could not convert data to an integer.")
		except:
			self.logger.log("Unexpected error: %s"%sys.exc_info()[0])
			raise
	
	# Views  ======================================================================
	@app.route('/')
	def home():
		return "w00p"

class TestItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    
    def serialize(self):
		d = Serializer.serialize(self)
		return d

class CustomLogger:
	def log(self, msg):
		print msg

class HTTP_Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Request_Path = db.Column(db.String)
    Request_FullUrl = db.Column(db.String)
    Request_Method = db.Column(db.String)
    Request_HttpVersion = db.Column(db.String)
    Request_Headers = db.Column(db.String)
    Request_Content = db.Column(db.String)
    Response_Code = db.Column(db.String)
    Response_CodeMsg = db.Column(db.String)
    Response_Headers = db.Column(db.String)
    Response_Content = db.Column(db.String)
    Response_HttpVersion = db.Column(db.String)
    Proxy_Name = db.Column(db.String)
    
    
    def serialize(self):
		d = Serializer.serialize(self)
		return d


if __name__ == '__main__':
	logger = CustomLogger()
	server = WebAPIServer(8010, logger)
	server.startServer()

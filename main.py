import os
import logging
import duckduckgo
import yaml

class Database:
	def __init__(self):
		pass

	def save(self):
		pass

	def compare(self):
		pass

class Main:
	def __init__(self):
		with open('utils/config/config.yml', 'r') as stream:
			data = yaml.load(stream, Loader=yaml.FullLoader)

			self.debug = data.get('debug', '')



		if self.debug:
			logging.basicConfig(
				level=logging.DEBUG,
				format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
				datefmt='%Y-%m-%d %H:%M:%S',				
			)
		else:
			logging.basicConfig(
				level=logging.INFO,
				format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
				datefmt='%Y-%m-%d %H:%M:%S',                    
			)
		self.logger = logging.getLogger('DuckSearch')
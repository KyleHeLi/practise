#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import json

class Student( object ):
	"""docstring for Student"""
	def __init__( self, name, age, score ):
		super( Student, self ).__init__()
		self.name = name
		self.age = age
		self.score = score
		
def student2dict( std ):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

if __name__ == '__main__':
	s = Student( 'Bob', 20, 88 )
	try:
		print( "Cannot change from Student Class to json" )
		print json.dumps( s )
	except Exception, e:
		print e
	print( "=========" )
	print( "After changing the default parameter of json.dump" )
	print json.dumps( s, default=student2dict )

	# d = dict( name='Bob', age=20, score=88 )
	# beforeS = json.dumps( d )
	# print( "Before pickling:" )
	# print beforeS
	# print( "=================" )
	# afterS = json.loads( beforeS )
	# print( "After pickling:" )
	# print afterS
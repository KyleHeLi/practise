#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def foo( s ):
	n = int( s )
	assert n != 0, 'n is zero'
	return 10 / n

def main():
	foo( '0' )

if __name__ == '__main__':
	main()
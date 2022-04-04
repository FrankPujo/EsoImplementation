import sys

pigSrc = open( sys.argv[1], "r" )
for line in pigSrc:
	fileName, content = line.split( "PIG" )
	file = open( fileName, "a" )
	file.write( content )
#open( "prova.txt", "a" )

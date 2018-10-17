from sys import argv

script, filename = argv

print "We are going to earse %r." % filename
print "if you don't want that, hit ^c"
print "if you do want that, hit return"

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file. goodbye!"

target.truncate()

print "now i'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

target.write(line1+"\n"+line2+"\n"+line3)
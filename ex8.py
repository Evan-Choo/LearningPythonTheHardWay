formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#if the sentense contains single quote, then the print result will have a double quote
print formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight."
)
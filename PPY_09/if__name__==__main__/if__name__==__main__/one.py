#one.py
#all the code that happens to be in INDETATION LEVEL ZERO is executed first; like this: 
#print('hello')
#in Python there is no such as main()

#if __name__="__main__": # if yes, run one.py directly

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

#that built-in variable actually allows you to see 
#if your script has been imported or run directly

if __name__ == '__main__':
	print('ONE.PY is being run directly\n(built-in variable __name__ has been assign to __main__)')
else:
	print('ONE.PY has been imported!')
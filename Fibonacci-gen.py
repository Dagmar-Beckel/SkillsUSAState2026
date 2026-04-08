#sys is a module that gives the code access to command-line arguments
import sys

#This function will return the full list of Fibonacci numbers based on how many numbers it needs to generate (n).
def fibonacci(n):
	seq = []
	a, b = 0, 1
	for i in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq


#sys.argv is a list (array-like) of arguments from the command line.
#It will store all the arguments from the command line. It will skip the first argument because it's just the filename.
#For example, "./Fibonacci-gen -c 6 -one-line" is entered and this function will make args = ['-c', '6', '-one-line']
args = sys.argv[1:]

def main():
    #This variable will hold the count of Fibonacci numbers to generate, which will be set based on user input
    #Right now the intial value is 6.
    count = 6

    #This calls the fibonacci function with the user entered "count"
    seq = fibonacci(count)

    #This is to test that the fibonacci function is working correctly. 
    #It will print the list of Fibonacci numbers generated.
    print(seq)


#this means that the program will run only if this file is executed
if __name__ == "__main__":
    main()


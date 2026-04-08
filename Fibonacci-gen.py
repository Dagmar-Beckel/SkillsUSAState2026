#sys is a module that gives the code access to command-line arguments
import sys

#This function will return the full list of Fibonacci numbers based on how many numbers it needs to generate (n).
def fibonacci(n):
	seq = []
	a, b = 0, 1
      
    #The loop will run n times, and in each iteration, it will append the current Fibonacci number (a) to the sequence list and then update a and b to the next two Fibonacci numbers.
	for i in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq

#This function will print the help message for the Fibonacci generator, explaining the various command-line options available to the user.
def print_help():
	print("""
    Help for Fibonacci generator:
	   
    --help : Print this help
	
    --count|-c : Calculate to this many places. IE: 0, 1, 1, 2, 3, 5 would be the result of -c 6
    
    --one-line: Print all the numbers on one line, separated by commas. Without this option,
    each number in the sequence will be printed on a new line.
    
    --numbering: Preface each number in the sequence with it's placement: IE for “-c 6 
	--numbering –-one-line” you would get this: “1:0, 2:1, 3:1, 4:2, 5:3, 6:5” where the first
    number is the count and the second is the Fibonacci sequence. Note: this argument should
    work with all other arguments.

    --last-only: Only print the last number in the sequence
    """)

#sys.argv is a list (array-like) of arguments from the command line.
#It will store all the arguments from the command line. It will skip the first argument because it's just the filename.
#For example, "./Fibonacci-gen -c 6 -one-line" is entered and this function will make args = ['-c', '6', '-one-line']
args = sys.argv[1:]

#This function will be called when the program is run. 
#It will check the arguments and call the correct functions based on what the user entered.
def main():
    #This variable will hold the count of Fibonacci numbers to generate, which will be set based on user input
    #Right now the intial value is 6.
    count = 6

    #This calls the fibonacci function with the user entered "count"
    seq = fibonacci(count)

    #if user types "--help", function print_help() will be called
    if "--help" in args:
        print_help()
        return

    #This is to test that the fibonacci function is working correctly. 
    #It will print the list of Fibonacci numbers generated.
    print(seq)


#this means that the program will run only if this file is executed
if __name__ == "__main__":
    main()


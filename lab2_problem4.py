# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 2 – Problem 4
# ==================================================
# Student Name: YOUR_NAME_HERE
# Student Email: YOUR_EMAIL_HERE
# ==================================================

def calculate_search_space(length, uppercase, lowercase, numbers):
    search_space = 0
    for i in range(1, length + 1):
        search_space += pow(26 * uppercase + 26 * lowercase + 10 * numbers, i)
    return search_space

def main():

    print("Welcome to the Password Security Checker!")

    # Initializing the variables to be used later in Part B
    uppercase = 0
    lowercase = 0
    numbers = 0

    # PART A
    # ======
    # You will obtain a desired password length from the user with the question "How
    # long is your desired password?" and save the value into the variable length

    ## YOUR CODE HERE ##
    length = int(input("How long is your desired password? "))

    # PART B
    # ======
    # You will ask the user three questions:
    #
    #     Would you like to use UPPERCASE characters? (1 = YES, 0 = NO)
    #     Would you like to use lowercase characters? (1 = YES, 0 = NO)
    #     Would you like to use numbers? (1 = YES, 0 = NO)
    #
    # You will save the values into three variables as integers, with the variables
    # named uppercase, lowercase, and numbers

    ## YOUR CODE HERE ##

    # PART C
    # ======
    # The assignment includes a function called calculate_search_space. This function
    # uses a loop to calculate a summation of the total number of possible combinations
    # given the characters used in a password. The equation (as used in this
    # assignment) is:
    #
    #     ∑(i=0,length)(26*uppercase + 26*lowercase + 10*numbers)^i
    #
    # Below, this function is called for you (functions are described in the next
    # module). The output of the function is saved into a variable search_space.
    #
    # Take the value in search space and display it to the user in the following
    # format:
    #
    #     Password search space (total possible combinations): XXXX
    #
    # Replace XXXX with the value in search space

    search_space = calculate_search_space(length, uppercase, lowercase, numbers)

    ## YOUR CODE HERE ##

    # PART D
    # ======
    # Let's assume it takes a (very slow) theoretical computer 1ms to attempt each 
    # possible password. Display the number of days it would take for this 
    # theoretical computer to crack the password in the worst case scenario given 
    # the search space. Output the result in the following format:
    #
    #     Worst case days to crack password: XXXX
    #
    # Where XXXX will be replaced by the number of days. Display the number of days as
    # an integer
    #
    # Hint: There are 86400000 milliseconds in a day

    ## YOUR CODE HERE ##

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":
    main()
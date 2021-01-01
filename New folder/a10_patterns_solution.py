#Python program to print the output in the desired format

# pattern method takes the input_char, line_count and display_mode
# Each formal argument provides a default value
# for incorrect display_mode, the method defaults to RIGHT
def pattern(input_char = '*', line_count = 5, display_mode = 'RIGHT'):
    for x in range(line_count):
        if(display_mode == 'LEFT'):
            print(''*(line_count-x-1) + input_char*(2*x+1))
        elif (display_mode == 'CENTER'):
            print(' '*(line_count-x-1) + input_char*(2*x+1))
        else:
            print('  '*(line_count-x-1) + input_char*(2*x+1))


# Assignment 10  test cases

#Test Case 1
print('Test Case 1:  pattern("*",5,"RIGHT")')
pattern("*",5,"RIGHT")

#Test Case 2
print('Test Case 2:  pattern("@",6,"LEFT")')
pattern("@",6,"LEFT")

#Test Case 3
print('Test Case 3:  pattern("#",10,"CENTER")')
pattern("#",10,"CENTER")

#Test Case 4 with all defaults
print('Test Case 4: pattern()')
pattern( )

#Test Case 5 pass in only two params and third is a default
print('Test Case 4: pattern("X", 5)')
pattern("X",5)

#Test Case 6: Take the inputs from the user on all three 
# and use those to test your method
a = input("Enter your character? ")
b = int(input("How many lines do you need? "))
c = input("How do you want to justify the display (LEFT, RIGHT, CENTER)? ")
pattern(a,b,c)

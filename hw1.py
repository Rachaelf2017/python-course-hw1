# Leave this line untouched
import os

#  Save this file as hw1.py

# 1.  Create a variable containing your full name.
#     Then print it, e.g. "My name is Benjamin Button."
name = "Rachael Feuerborn"
print "My name is %s" %name


# 2.  Create a variable for your age and another variable for the current year.
# (for reasons of privacy you can lie, just make it believable)
#  Then print your age and the current year, eg "My age is 29. The year is 2016."
age = 28
year = 2016
print "My age is %d. The year is %d." %(age,year)


# 3.  Using the modulo operator, deterimine whether your is odd or even, then print either:
#     "It is True that my age is odd." or
#     "It is False that my age is odd."
#     Hint:  you may want to use more than one line of code to do this
age_remainder= age % 2 > 0
print "It is %s that my age is odd." % age_remainder


# 4.  Now deterimine whether your is odd or even without using the modulo operator.
#     Hint:  you can do this in one line of code using a combination of integer and floating point math.
#     Hint:  in Python != means 'does not equal'
#     "It is True that my age is odd." or
a= int(age/2.0)!= (age/2.0)
print "It is %s that my age is odd." % a

# 5.  When you are ready to submit your homework, start a new terminal session.
#     Run this program once from one directory.
#     Then change to another directory and run this program again from there.
#     Note that the last line of the program prints the current directory
#     (the directory you are running it from).
#     Your terminal should show the output of the two runs and not much else.
#     Save your terminal output out to a file named hw1.output

#6.  Submit:  hw1.py and hw1.output


#  Leave this line untouched.
print 'The current working direcotry is %s ' % os.getcwd()

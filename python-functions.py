# Testing functions in Python

import sys
import time


def testfunc(myname):
    print("Hello %s" % myname)


testfunc("Tony")


def test2(fname, lname):
    print("Hello %s %s" % (fname, lname))


test2("Tony", "Stark")


firstname = "Tony"
lastname = "Stark"

test2(firstname, lastname)


def savings(pocketm, job, spending):
    return pocketm + job - spending


print(savings(10, 10, 5))


# Variable scope

anotherv = 100


def variabletest():
    firstv = 10
    secondv = 20
    return firstv * secondv * anotherv


print(variabletest())

# Building an iron man suit  out of tin cans. You can flatten 2 cans per week to create the body, but need 500 cans to finish.


def suit_building(week_cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + week_cans
        print('Week %s = %s cans' % (week, total_cans))


suit_building(2)
suit_building(13)


# Using modules
#import time
print(time.asctime())

#import sys
# print(sys.stdin.readline())


# More Practice!

# Moon weight function

def moonfunc(weight, gain):
    for i in range(1, 16):
        weight = weight + gain
        moonweight = weight * 0.165
        print("Your weight on the moon after %s years is %s kilos" %
              (i, moonweight))


moonfunc(91, 1)


# Moon weight with variable years

def newmoonfunc(weight, gain, years):
    weight = weight + gain * years
    moonweight = weight * 0.165
    print("Your weight on the moon after %s years would be %s kilos" %
          (years, moonweight))


newmoonfunc(91, 1, 5)

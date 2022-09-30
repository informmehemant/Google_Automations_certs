#!/bin/bash
# Basic arithmetic using let 
# let a=5+4
# echo $a #9

# let "a = 5 + 4"
# echo $a # 

# let a++
# echo $a

# let "a =  4 * 5"
# echo $a # 20

# let "a = $1 + 30"
# echo $a # 2- + first command line arguments

expr 5 + 4

expr "5 + 4"
expr 5+4

expr 5 \* $1
expr 11 % 2

a=$( expr 10 - 3)
echo $a #7

#  length of the variable

a='Hello World'
echo ${#a} # 11


b=3456

echo ${#b}

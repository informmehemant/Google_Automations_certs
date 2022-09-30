#!/bin/bash
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything Ok"
else 
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi 


if test -n "$PATH"; then echo "Your path is not ecmpty"; fi
#  or

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

cp $1 $2

# let's verify the copy worked
echo Details for $2


ls -lh $2


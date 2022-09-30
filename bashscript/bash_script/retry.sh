#!/bin/bash
#Filename: printf.sh


n=0
cmd=$1
while ! $cmd && [ $n -le 5 ]; do
   sleep $n
   echo "Retry: #$n"
   ((n+=1))
done


printf "%-5s %-10s %-4s\n" No  




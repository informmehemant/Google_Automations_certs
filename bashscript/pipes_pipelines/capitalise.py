#!/usr/bin/env python3


''' cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head  used to pipe as much we like'''

''''

➜  pipes_pipelines git:(main) ✗ chmod +x capitalise.py    

# using pipes for big program

➜  pipes_pipelines git:(main) ✗ cat haiku.txt | ./capitalise.py 
Advance your carrer,
Automatig with python,
It's so fun to learn.


# same things can be achived from redirections

➜  pipes_pipelines git:(main) ✗ ./capitalise.py < haiku.txt 
Advance your carrer,
Automatig with python,
It's so fun to learn.

# Grep command usage

➜  test git:(main) ✗ ls
test1 test2 test3 test4
➜  test git:(main) ✗ grep steve test1
steve
➜  test git:(main) ✗ grep steve test1 test2 test3 test4
test1:steve
test2:this is a long line of test that contains the name steve
test3:steven
➜  test git:(main) ✗ grep -i steve *
test1:steve
test2:this is a long line of test that contains the name steve
test3:steven
test4:Steve ?

'''

import sys
for line in sys.stdin:
    print(line.strip().capitalize())

#! /bin/sh

#read lines from theHeavenlyTestCase.txt.
#for each file, print out the number of lines grep prints out
#for a case-insensitive search on the file.
#sort the result treating the first thing as a number.
while read p; do
    echo $(grep -i $1 $p | sed $'s/$1/\\\n$1\\\n/Ig' | grep -ci "\<$1\>") $p
done < theHeavenlyTestCase.txt | sort -n -r

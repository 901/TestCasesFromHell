#What?

Test cases for the data structures expression evaluator.

#How to use

`e1.txt` is the file that encodes the variables that
will be referenced in the testcases.

Also, the expressions have been evaluated using the
python script in this folder and should work for
most things you throw at it - being identical to your
output.

#The testcases and their output.

Here are a few equations and their output.

These are all intended to work with a complete version.

Good luck!

|Expression | Eval |
|----------|-------|
|`B[A[0] + 1]` | 2 |
|`A[B[A[2] - 1 - 1]] * B[5]`| 18 |
|`3 -- 4 * A[B[3] - B[1]]` | 15 |
|`(a + b)/2 + A[B[2]] - (A[B[3]] - 2)`| 2.5|

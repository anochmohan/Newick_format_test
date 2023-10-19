# Newick_format_test

We have worked with Newick format trees. Part of the specification of Newick format is the each node of a tree must be enclosed within parentheses. i.e., each open parenthesis must have a corresponding closing parenthesis. Additionally, there can not be a close parenthesis that does not follow an open parenthesis.

If you were to write a script to validate Newick format, you would need to check the correct pairings of parentheses as well as the other format rules. This task is to write a script that checks whether parentheses are paired.

Write a script that uses one or more functions to assess whether or not all parentheses in an input string are paired.

The body of your script should only have a single line (except `import sys`) that is not within a function. That line should be calling a function and passing command line input as arguments.

The usage of your script should be `<script name>.py <test string>`

Your script should print a result of either "PAIRED" or "NOT PAIRED" to the terminal according to the result of your analysis.

Note that simply counting parentheses is not sufficient as a closing parenthesis followed by an opening parenthesis is not valid in Newick format.

Some example data showing inputs and expected output (Note, you will need to put the parentheses in quotes)

```text
$ ./q2_script.py "()"
PAIRED
$ ./q2_script.py "()()()"
PAIRED
$ ./q2_script.py "(()())"
PAIRED
$ ./q2_script.py "((()))"
PAIRED
$ ./q2_script.py "(()())"
PAIRED
$ ./q2_script.py "((())())"
PAIRED
$ ./q2_script.py ")"
NOT PAIRED
$ ./q2_script.py ")("
NOT PAIRED
$ ./q2_script.py "()()("
NOT PAIRED
$ ./q2_script.py ")((())"
NOT PAIRED
$ ./q2_script.py "))(("
NOT PAIRED
$ ./q2_script.py "())("
NOT PAIRED
```

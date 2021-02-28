# FOR LOOPS LESSON
# For Loop

# A “for ” loop is the most preferred control flow statement to be used in a Python program.
# It is best to use when you know the total no.of iterations required for execution.

# It has a clearer and simple syntax and can help
you
iterate
through
different
types
of
sequences.Python
supports
seven
sequence
data
types: standard / Unicode
strings, a
list, tuples, a
bytearray, and xrange
objects.There
are
sets and dictionaries as well, but
they
are
just
containers
for the sequence types.

What is a For Loop?
# A for loop in Python requires at least two variables to work.The first is the iterable object such as a list, tuple or a string.
# And second is the variable to store the successive values from the sequence in the loop.

# Python For Loop Syntax
for iter in sequence:
    statements(iter)
The “iter” represents
the
iterating
variable.It
gets
assigned
with the successive values from the input sequence.

The “sequence” may
refer
to
any
of
the
following
Python
objects
such as a
list, a
tuple or a
string.

1.2.For
Loop
WorkFlow in Python

The
for loop can include a single line or a block of code with multiple statements.Before executing the code inside the loop, the value from the sequence gets assigned to the iterating variable (“iter”).

Below is the
flowchart
representation
of
a
Python
For
Loop.

Regular
Python
For
Loop
Flowchart
Regular
Python
For
Loop
Flowchart
1.3
.1.Python
For
Loop
Example – Print
Characters
of
a
String

vowels = "AEIOU"
for iter in vowels:
    print("char:", iter)
The
above
code is traversing
the
characters in the
input
string
named as the
vowels.Its
output is as follows.

char: A
char: E
char: I
char: O
char: U
1.3
.2.Python
For
Loop
Example – Find
the
Average
of
N
Numbers

We’ll
use
the
following
steps
to
calculate
the
sum
of
N
numbers.

Create
a
list
of
integers and populate
with N(=6) values.
Initialize
a
variable(sum)
for storing the summation.
Loop
N( = 6) number
of
times
to
get
the
value
of
each
integer
from the list.
In
the
loop, add
each
value
with the previous and assign to a variable named as the sum.
Divide
the “sum” with N(=6).We used the len() function to determine the size of our list.
The
output
of
the
previous
step is the
average
we
wanted.
Finally, print
both
the “sum” and the
average.
Below is the
Python
code
for the above program.

int_list = [1, 2, 3, 4, 5, 6]
sum = 0
for iter in int_list:
    sum += iter
print("Sum =", sum)
print("Avg =", sum / len(int_list))
Here is the
output
after
executing
the
above
code.

Sum = 21
Avg = 3.5
2.
Range()
Function
with For Loop

2.1.What is Range()
Function?

The
range()
function
can
produce
an
integer
sequence
at
runtime.For
example, a
statement
like
range(0, 10)
will
generate
a
series
of
ten
integers
starting
from

0
to
9.

Below
snippet is interpreting
more
about
the
functional
aspect
of
the
range()
function.

>> > type(range(0, 10))
<

class 'range'>

>> > range(0, 10)[0]
0
>> > range(0, 10)[1]
1
>> > range(0, 10)[9]
9
>> > len(range(0, 10))
10
>> >
2.2.Range()
Function
Example

Let’s
now
use
the
range()
with a “ for ” loop.

for iter in range(0, 3):
    print("iter: %d" % (iter))
It
will
yield the
following
result.

iter: 0
iter: 1
iter: 2
By
default, the “for ” loop fetches elements from the sequence and assigns to the iterating variable.But you can also make the “ for ” loop returning the index by replacing the sequence with a range(len(seq)) expression.

books = ['C', 'C++', 'Java', 'Python']
for index in range(len(books)):
    print('Book (%d):' % index, books[index])
The
following
lines
will
get
printed.

Book(0): C
Book(1): C + +
Book(2): Java
Book(3): Python
Read
details
here – Python
range
function

3.
Else
Clause
with Python For Loop

Interestingly, Python
allows
using
an
optional else statement
along
with the “ for ” loop.

The
code
under
the else clause
executes
after
the
completion
of
the “for ” loop.However, if the loop stops due to a “break” call, then it’ll skip the “ else ” clause.

3.1.Syntax

# Foe-Else Syntax

for item in seq:
    statement
    1
    statement
    2
    if < cond >:
        break
else:
    statements
Look
at
the
below
For
Loop
with Else flowchart.

3.2.For - Else
Flowchart

Python
for loop with else clause flowchart

3.3.For - Else
Example

birds = ['Belle', 'Coco', 'Juniper', 'Lilly', 'Snow']
ignoreElse = False

for theBird in birds:
    print(theBird)
    if ignoreElse and theBird is 'Snow':
        break
else:
    print("No birds left.")
The
above
code
will
print
the
names
of
all
birds
plus
the
message in the “ else ” part.

Belle
Coco
Juniper
Lilly
Snow
No
birds
left.
Setting
the “ignoreElse” variable
to “True” will
get
the “ else ” part
ignored.And
only
the
names
will
get
displayed.

Python
For
Loop
Summary
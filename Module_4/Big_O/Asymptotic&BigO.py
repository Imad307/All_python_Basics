'''
Asymptotic analysis
One observation that helps us is that we want to worry about large input sizes only. 
If the input size is really small, how bad can a poorly-designed algorithm get, right? 
Mathematicians have a tool for this sort of analysis called the asymptotic notation.
The asymptotic notation compares two functions, say, f(n) and g(n)for very large values of. 
This fits in nicely with our need for comparing algorithms for very large input sizes.
'''
#BIG-O Notation:
'''
One of the asymptotic notations is the Big O notation. A function f(n) is considered O(g(n)), read as big oh of g(n), 
if there exists some positive real constant c and an integer n0≥0 n0 ≥0 such that the following inequality holds for all n≥n0:

        f(n)≤cg(n)
'''
# Other Common Asyptotic Notations
'''
Big-Omega(Ω):
Big ‘Omega’ -Ω Mathematically, a function f(n) is in Ω(g(n)) if there exists a real constant c>0 and there exists no>0 such that 
f(n)≥cg(n) for n≥no. In other words, for sufficiently large values of n, f(n) will grow at least as fast as g(n).
It is a common misconception that Big O characterizes the worst-case running time while 
Big Omega characterizes the best-case running time of an algorithm. 
There is no one-to-one relationship between any of the cases and the asymptotic notations.

Note: if f(n) belongs to O(g(n)) then g(n) belongs to Ω(f(n))
'''
'''
Big Theta 
if f(n) is in O(g(n)) and f(n) is also in Ω(g(n)) then it is theta(n)
'''

# Why Big O is preffered over other Asymptotic Notations 
'''
All of these notations have a variety of applications in mathematics. However, in algorithm analysis, 
we tend to focus on the worst-case time and space complexity. It tends to be more useful to know that 
the worst-case running time of a particular algorithm will grow at most as fast as a constant multiple of a certain function than 
to know that it will grow at least as fast as some other function. 
In other words, Big Omega is often not very useful for use with worst-case running time.

What about Big Theta, though? Indeed, it would be great to have a tight bound on the worst-case running time of an algorithm. 
Imagine that, there is a complex algorithm for which we haven’t yet found a tight bound on the worst-case running time. 
In such a case, we can’t use Big Theta, but we can still use a loose upper bound (Big O) until a tight bound is discovered. 
It is common to see Big O being used to characterize the worst-case running time even for simple algorithms where 
a Big Theta characterization is easily possible. That is not technically wrong, because Big O is a subset of Big Theta.

The Little o and Little omega notations require a strict level of inequality (< or >) and the ability to show that there is a valid 
n0 for any valid of choice of c. This is not always easy to do.

For all the above reasons, it is most common to see Big O being used when talking about an algorithm’s time or space complexity.
'''
# Note: Now, we will simplify the analysis by just counting the number of executions of each line of code, 
# instead of the number of operations.
#  For example, we will say print(sum) will take one primitive operation instead of two.

'''
General tips#
Every time a list or array gets iterated over c×length times, it is most likely in O(n) time.
When you see a problem where the number of elements in the problem space gets halved each time, 
that will most probably be in O(logn) runtime.
Whenever you have a singly nested loop, the problem is most likely in quadratic time.
'''
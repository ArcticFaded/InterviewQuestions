#Building solutions with backtracking

These type of questions require you to find some sort of permutation of an
original string. For this you can either build all possible strings and check if
they are valid. A smarter approach would be to make a decision of how you want
to build the string and then build up the smaller sub strings.

In this problem we need some way of knowing what point of the parenthesis string
we are building. We know for a fact that valid strings are composed of:

* An equal amount of left and right parenthesis
* Those parenthesis are in the correct order
  * left comes before right
  * any other character can be in their original positions inside of a valid string

So then our initial condition should be: our result is empty if there are no left
parenthesis. we pass in `DFS(result, []:empty current, 0:no left count, 0:no removal, s)`
and if left count never increases then no strings are built. If the result is empty
then a valid string to return should be the empty string, which is appended at the end.

In `DFS(result,current,lcount,maxcount,s):` we build strings by adding OR removing
left parenthesis. When we add a left parenthesis, we of course increase the count
and the **maxcount**. However if we choose not to use a left parenthesis, then this
counts towards our *correction* of the string s. Likewise right parenthesis are
only added when **lcount** allows for it. One important thing to note is at every
step of the iteration, we always have have a correct parenthesis inside of result. 

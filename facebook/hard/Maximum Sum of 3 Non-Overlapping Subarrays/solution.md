# 3 Maximum Sub-Array

This problem is a DP-sorts of problem. That is, the main solution will
have sub-solutions which are already being calculated on each pass.

Let `D[i][j]` be the maximum sum of length k where
* i -> 0 for left sum, 1 for right sum
* j -> the maximum value for an interval starting at j of length k

Immediatly we know that if a list cannot be seperated into 3 sub-arrays
of size k then there is no solution. After checking, then we compute the inital sums of every appropriate interval
and call it the partial sum. Afterwards we search through the list going
backwards and fowards to find the max sum among all the intervals. I claim that the proper solution will be, for any middle interval starting at j, max(A[0..j-1]),j,max(A[j+1,k]) is the correct solution.

So after calculating the partial sums and finding the max between them we simplying select the number j, and try to maximize the overall sum. In order to keep the lexigraphical ordering (when there are ties) we sum on the beginning and keep track of the ends of the intervals

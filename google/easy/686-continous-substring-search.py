class Solution:
  def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    base = A
    i = 1
    if base in B:
      while(B not in A) :
        if (A.length > 10000):
          return -1
        A = A + base
        i = i + 1
      return i
    else:
        return -1


print (Solution.repeatedStringMatch(A="abcd",B="cdabcdab"))

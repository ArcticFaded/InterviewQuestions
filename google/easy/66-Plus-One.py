class Solution:
  def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number = int(''.join(map(str,digits)))
    number = number + 1
    return [int(x) for x in list(str(number))]


print(Solution.plusOne([9,9,9,9]))


class Solution:
  def reverseVowels(s):
    copy = list(s)
    vowels = [{'vowel': copy[v], 'index': v} for v in range(len(copy)) if copy[v] in ['a','e','i','o','u']]

    print (vowels)
    reverse = vowels[::-1]

    for entry in range(len(vowels)):
      copy[vowels[entry]['index']] = reverse[entry]['vowel']
    print (('').join(copy))

#Simple is better? Sometimes

This question is labeled as hard, however I don't see it as a hard question.
The solution I submitted is infact very easy to digest, the main time complexity
here is actually in the steps before the code runs. The preprocessing step works
as follows:

* Convert a number **n** into its string representation
* Reverse the string **n** and then cut it into 3's
	* This is illustrated by `[num[i:i+3] for i in range(0,len(num),3]`
	* So given a number, say 12345, we would first turn 12345->'1245'
	* Then we would reverse '12345' -> '54321', we reverse because it will help us count the places like a human does, count 3 then mark its place
	* '54321' with the code above becomes ['543','21']
	* and finally we reverse it back `s[::-1] for s in token` -> ['12', '345']

The preprocessing lines are much more expensive than the code used to build up the integer to english solution so  improvements can be made.

as for the main code itself, there isnt much need for explination.

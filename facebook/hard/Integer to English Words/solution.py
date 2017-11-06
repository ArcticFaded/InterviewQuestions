class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        keywords = ['Billion', 'Million', 'Thousand']
        base10 = ['Ninety', 'Eighty', 'Seventy', 'Sixty', 'Fifty', 'Forty', 'Thirty', 'Twenty']
        baseTeen = ['Nineteen','Eighteen','Seventeen','Sixteen','Fifteen','Fourteen','Thirteen','Twelve','Eleven','Ten']
        base = [ 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
       #Reverse the list (or initlizate them correctly!!!)
	base = base[::-1]
	baseTeen = baseTeen[::-1]
	base10 = base10[::-1]
	keywords = keywords[::-1]

        num = str(num)[::-1]#Count in reverse
        token = [num[i:i+3] for i in range(0,len(num),3)][::-1]#tokenize them into sets of hundres
        token = [s[::-1] for s in token]#Un-reverse the list
        place = len(token) - 2#The amount of list which are created is the correct place (thousands,millions,etc.)
        s = ''#answer
        for i in token:
            flag = True
            if (i == '000'):#for example in 1000 or 1000000 -> [[1],[000]], we can skip past these
                place -= 1
                continue
            if len(i) == 3:#If we have to print hundred
                if(i[0] != '0'):#IF we have to print hundred, i.e., 081 we would skip past
			#We can also consider in the token stage above to turn digits into integers
                    s += base[int(i[0])] + ' Hundred '
                i = i[1::] #prepare tenth place
		#In fact you should (I WONT!)
		
            if len(i) == 2:
                if (i[0] == '0'):
                    if(i[1] != '0'):
                        s += base[int(i[1])] + ' ' #06 -> 6, because im working with digits
                    i = ''
                    flag = False
                else:
                    if(i[0] == '1'):
                        s += baseTeen[int(i[1])] + ' ' #1X -> use base teen's
                        i = ''
                        flag = False
                    else:
                        s += base10[int(i[0]) - 2] + ' '#XY -> print X 
                        i = i[1::] #prepare Y
                        flag = False
                    
            if len(i) == 1: #Y -> print Y
                zero = base[int(i[0])]
                if zero == 'Zero':
                    if flag:
                        s += base[int(i[0])] + ' '
                else:
                    s += base[int(i[0])] + ' '
                    
            if place >= 0:
                s += keywords[place] + ' '
                place -= 1
            
        return s[0:len(s)-1]#remove extra space at the end
                    
            
            
            

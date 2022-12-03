class Solution:
    def frequencySort(self, s: str) -> str:
       dict={} # to store frequency of each character
       result= '' # to store the final result
        
       for i in s: # each character in string s is stored in variable i
          if i in dict: # if i is in dictionary, we increase the frequency
            dict[i]= dict[i]+1
          else:
            dict[i]=1
            
       s = sorted(dict, key=lambda x: dict[x], reverse=True) # sorting dictionary in reverse order by using lambda function
    
       for char in s: # sorted dictionary in reverse order
            result = result + char*dict[char] # multiplying character with its frequencies
       return result
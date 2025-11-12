class Solution:
      def isPalindrome(self,s) :
          s= s.lower()
          clean=""
          for ch in s:
              if  ch.isalnum():
                   clean += ch
          if  clean == clean[::-1] :
               return True
          else :
                return False

        
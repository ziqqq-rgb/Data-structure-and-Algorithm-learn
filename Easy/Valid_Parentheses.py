##Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#Example 1:
#Input: s = "()"
#Output: true

#Example 3:
#Input: s = "(]"
#Output: false

#-----------------------------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {")": "(", "]": "[", "}": "{"}

        for char in s: #look at the closing brackets in the string, put the opening in the stack, then compare with close
            if char in bracket_map:

                #take the top element (opening bracket) of the stack if it exists, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                #compare the top element of the stack with the corresponding opening bracket from the map
                if bracket_map[char] != top_element:
                    return False
                
            else: #if not a closing bracket, it must be an opening bracket, so we add it to the stack
                stack.append(char)
        
        return len(stack) == 0 # If stack is empty (means all matched, and no more), all brackets were matched, in case if only one opening bracket is left, then it is not valid, so return false
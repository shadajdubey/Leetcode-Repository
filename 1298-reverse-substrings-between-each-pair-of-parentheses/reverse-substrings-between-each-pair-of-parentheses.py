class Solution:

  def reverseParentheses(self, s: str) -> str:
    stack = []
    for char in s:
      if char == ')':
        curr = []
        while stack and stack[-1] != '(':
          curr.append(stack.pop())
        if stack and stack[-1] == '(':
          stack.pop()
        stack.extend(curr)
      else:
        stack.append(char)
    return ''.join(stack)
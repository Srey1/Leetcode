def generateParenthesis(self, n: int) -> List[str]:
    stack = []
    result = []

    def inner(open_count, closed_count):
        if (open_count == n == closed_count):
            result.append("".join(stack)) 
            return
        if (open_count < n):
            stack.append("(")
            inner(open_count+1, closed_count)
            stack.pop()
        if (closed_count < open_count):
            stack.append(")")
            inner(open_count, closed_count+1)
            stack.pop()
    
    inner(0,0)
    return result
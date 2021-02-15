def solveMeFirst(a,b):
	# Hint: Type return a+b below
    allowed_range = list(range(1,1001))
    if (a and b) in allowed_range:
        return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
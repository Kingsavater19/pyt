def max_x(a,b,c):
    if a > b  and a > c:
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > b :
        return c
    elif a == b ==c : 
        return print("EQUAL")
    

nums=float(input("Enter the first number: "))
nums2=float(input("Enter the second number: "))
nums3=float(input("Enter the third number: "))

print(max_x(nums,nums2,nums3))



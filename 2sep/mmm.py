marks=[45,78,88,56,90]
a=max(marks)
b=min(marks)
n=len(marks)
sum=0
for i in marks:
    sum=sum+i
c=sum/n
print(a,b,c)
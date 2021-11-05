N = int(input("enter a number: "))
sum1 = 0
sum2 = 0
a = 0
for i in range(1,N+1):
    if i % 2 == 0:
        sum1 = sum1 + i
        a =  a + 1 
    else:
        sum2 = sum2 + i
average = sum1 / a
odd_sum = sum2
print(average, odd_sum)
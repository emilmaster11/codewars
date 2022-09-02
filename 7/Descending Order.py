
number=[1,5,6,9,0]

for i in range(len(number)):
  
  for j in range(i+1,len(number)):
    
    if number[i]<number[j]:
      number[i],number[j]=number[j],number[i]

print(number)

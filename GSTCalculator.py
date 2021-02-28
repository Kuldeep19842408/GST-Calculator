def Tax(cost,typ):
  if typ=="agriculture":
    c=cost+(cost*12)//100
  elif typ=="ecommerce":
    c=cost+(cost*15)//100
  elif typ=="medical":
    c=cost+(cost*8)//100
  elif typ=="grocery":
    c=cost+(cost*9)//100
  else:
    c=cost+(cost*20)//100
  return (c)

print("Total amount of product")
x=int(input())
print("Type of product")
y=input()

finalamount=Tax(x,y)
print(finalamount)

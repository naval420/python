a=int(input('enter the unit'))
if a<=100:
    print('pay:200 rs')
elif a>100 and a<=200:
    b=200 +(a-100)*2
    print('pay',b)
elif a>200 and a<=300:
    b=200 +200+ (a-200) *3
    print('pay',b)
elif a>300 and a<=400:

    b=200 +200 +200+(a-300)*5
    print('pay',b)
else:
    b=200+200+200+200+(a-400)*7
    print('pay',b)

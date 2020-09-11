n,m=map(int,input().split())
l=input().split(' ')
A=set(input().split(' '))
B=set(input().split(' '))
happiness=0

for i in l:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)
'''try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)'''

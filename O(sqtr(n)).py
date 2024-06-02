n = int(input())

simpl = True

i = 2
while i*i<=n:
  if n % i == 0:
      simpl = False
      break
  i+=1

print(simpl)
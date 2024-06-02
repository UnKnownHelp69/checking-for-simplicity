n = int(input())

simpl = True

for i in range(2, n):
  if n % i == 0:
      simpl = False
      break

print(simpl)
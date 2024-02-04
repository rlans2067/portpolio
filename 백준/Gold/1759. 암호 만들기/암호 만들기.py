import sys

L, C = map(int, input().split())
li = list(map(str, input().split()))
li.sort()
ans = []

def A(index, start, L, C):
  if index == L:
    cnt = 0
    cnta = 0
    for j in range(len(ans)):
      if ans[j] in ['a', 'e', 'i', 'o', 'u']:
        cnta += 1
      else:
        cnt += 1
    if cnt >= 2 and cnta >= 1:
      sys.stdout.write(''.join(map(str, ans))+'\n')
    return
      
  for i in range(start, C):
    ans.append(li[i])
    A(index+1, i+1, L, C)
    ans.pop()

A(0, 0, L, C)

def rev(nl: list[int]):
  nl.reverse()
  return nl
if __name__ == '__main__':
  for i in range(int(input())):
    nl = [int(x) for x in input().split()]
    res = rev(nl)
    print(' '.join(map(str, res)))

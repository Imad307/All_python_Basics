list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def foo(m):
  v = m[0][0]
  for row in m:
    for element in row:
      if v < element: v = element
      print (v)
  return v

print(foo(list[0]))
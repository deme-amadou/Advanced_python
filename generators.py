def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for i in x:
  print(i)

t = iter(["ab","db","cf"])

print(next(t))

def infinite_sequence():
  result = 1
  while True:
    yield result
    result*=5
values = infinite_sequence()

if __name__=="__main__":
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  print(next(values))
  
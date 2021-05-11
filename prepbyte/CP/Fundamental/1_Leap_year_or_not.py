def LeapYear(N):
  if N%4== 0:
    if N%100 == 0:
      if N%400 == 0:
        print("Yes")
      else:
        print("No")
    else:
      print("Yes")
  else:
    print("No")
  
# driver code
def main():
  T = int(input())
  while(T>0):
    Entry = input().split()
    N = int(Entry[0])
    
    LeapYear(N)
    
    T -= 1
    
if __name__ == "__main__":
  main()
  
    

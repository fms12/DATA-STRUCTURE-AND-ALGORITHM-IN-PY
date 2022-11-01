from collections import deque 
class que:
  def __init__(self):
    self.qq=deque()
  def enque(self,data):
    self.qq.appendleft(data)
  def deque(self):
    if self.qq==0:
      print("QUEUE is Empty")
      return 
    return self.qq.pop()
  def size(self):
    return len(self.qq)
  def is_empty(self):
    return len(self.qq)==0
  def front(self):
    return self.qq[-1]
  
obj=que()
obj.enque(1)
obj.enque(2)
obj.enque(3)
obj.enque(4)
obj.enque(5)
obj.enque(6)
obj.enque(7)
obj.enque(8)
obj.enque(9)
obj.enque(10)
t=obj.size()
for x in range(0,t):
  print(obj.deque())


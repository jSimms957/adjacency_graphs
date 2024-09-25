class Stack:
  def __init__(self, size):
    self.stack_array = [None] * size
    self.top_pointer = -1



  def push(self, new_item):
    if self.top_pointer + 1 == len(self.stack_array):
      print("Error: stack is full")
    else:
      self.top_pointer += 1
      self.stack_array[self.top_pointer] = new_item
      if self.top_pointer == len(self.stack_array):
        self.top_pointer = -1
      print(self.stack_array)


  def pop(self):
    if self.top_pointer == -1:
      print("Error: stack is empty")
    else:
      print(self.stack_array[self.top_pointer])
      self.stack_array[self.top_pointer] = None
      self.top_pointer -= 1
      print(self.stack_array)

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    if value is not None:
      self.head_node = Node(value)
    else:
      self.head_node = None
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() is not None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node



######################################################################



# Complete this function:
def nth_last_node(linked_list, n):
  
  pointer_1 = linked_list.head_node
  pointer_2 = linked_list.head_node
  count = 0

  # Move pointer_1 n nodes ahead
  while count < n:
    if pointer_1 is None:
      return None
    pointer_1 = pointer_1.get_next_node()
    count += 1

  # Move both pointers until pointer_1 reaches the end
  while pointer_1:
    pointer_1 = pointer_1.get_next_node()
    pointer_2 = pointer_2.get_next_node()

  # Return the value from pointer_2
  return pointer_2



######################################################################



# Driver Code
def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Test code
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.get_value() if nth_last else "None")

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()



flower_definitions = [['begonia', 'cautiousness'],
                      ['chrysanthemum', 'cheerfulness'],
                      ['carnation', 'memories'],
                      ['daisy', 'innocence'],
                      ['hyacinth', 'playfulness'], 
                      ['lavender', 'devotion'], 
                      ['magnolia', 'dignity'], 
                      ['morning glory', 'unrequited love'], 
                      ['periwinkle', 'new friendship'], 
                      ['poppy', 'rest'], 
                      ['rose', 'love'], 
                      ['snapdragon', 'grace'], 
                      ['sunflower', 'longevity'], 
                      ['wisteria', 'good luck']]



##########################################################################



class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]


  def hash(self, key):
    return sum(key.encode())
  

  def compress(self, hash_code):
    return hash_code % self.array_size
  

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
    list_at_array.insert(payload)


  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]  
    return None


blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('rose'))
print(blossom.retrieve('sunflower'))





class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, target_id):
    nodes_to_visit = [self.root]

    if self.root is None:
      return None
    
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop()
      if node['id'] == target_id:
        return node
      
      nodes_to_visit.extend(node['children'])
    return None
      
        
  
    
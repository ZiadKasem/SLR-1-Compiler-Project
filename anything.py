
def addNode(state):
    global NodeUniqueName , name_list
    name = str(NodeUniqueName)
    dot.node(name,state)

    name_list.append(state)

    name_list = [name for name in name_list if not name.isnumeric()]
    NodeUniqueName +=1
    return name

def addEgde(preState,currentState):
    dot.edge(preState,currentState)
dot = graphviz.Digraph('The Round Table', filename='ss.gv')
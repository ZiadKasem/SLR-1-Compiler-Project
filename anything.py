import graphviz
import os
dot = graphviz.Digraph('The Round Table',filename= 'parseTreeProject.gv')

def addNode(state):
    global NodeUniqueName , name_list
    name = str(NodeUniqueName)
    dot.node(name,state)

    name_list.append(state)
    name_list = [name for name in name_list if not name.isnumeric()]
    NodeUniqueName +=1
    return name

def addEgde(preState,currentState):
    dot.edge(preState,currentState,label = '')

name_list = []
NodeUniqueName = 0

A=addNode('state1')
B=addNode('state2')
addEgde(A,B)

dot.view()




dot.view()
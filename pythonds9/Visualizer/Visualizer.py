from graphviz import Digraph

g = Digraph()

def viz_graph(g):
    dot = Digraph()
    
    for v in g:
        for w in v.get_connections():
            dot.node(str(v.get_id()))
            dot.node(str(w.get_id()))

            dot.edge(str(v.get_id()), str(w.get_id()),
                    label=str(v.connected_to[w]))

def viz_graph_bh(g):
    dot = Digraph()
    
    for v in range(1, len(g)//2):
        dot.edge(str(g[v]), str(g[2*v]))
        dot.edge(str(g[v]), str(g[2*v + 1]))

    return dot

dot = Digraph()
def viz_graph_bst(root):
    if root.has_left_child():
        val = root.left_child.key
        pay = root.left_child.payload
        dot.edge(f'key={root.key}, payload={root.payload}', 
                f'key={val}, payload={pay}')
        viz_graph_bst(root.left_child)
    if root.has_right_child():
        val = root.right_child.key
        pay = root.right_child.payload
        dot.edge(f'key={root.key}, payload={root.payload}',
                f'key={val}, payload={pay}')
        viz_graph_bst(root.right_child)

    return dot

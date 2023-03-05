import graphviz


class Graph:
    def __init__(self):
        self.dot = graphviz.Digraph(
            'structs', filename='structs.gv', node_attr={'shape': 'record'})

    def addNodo(self, primero, siguiente):
        if siguiente:
            self.dot.node(str(primero.id), str(primero.getValor().getNombre()))
            self.dot.node(str(siguiente.id), str(
                siguiente.getValor().getNombre()))
            self.dot.edge(str(primero.id), str(siguiente.id))
            self.dot.edge(str(siguiente.id), str(primero.id))

    def generate(self):
        self.dot.render(directory='img').replace('\\', '/')
        'img/structs.pdf'

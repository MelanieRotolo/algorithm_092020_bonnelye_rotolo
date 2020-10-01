class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value: int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class FibonacciHeap():
    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.deg = 0
            self.mark = False

    root_list = None
    min_node = None
    total_num_elements = 0

    def insert(self, value: int) -> None:
        if (not isinstance(value, int)):
            raise ValueError('La valeur doit être un int !')
        node = self.Node(value)
        node.left = node.right = node
        self.meld_into_root_list(node)
        if self.min_node is not None:
            if self.min_node.value > node.value:
                self.min_node = node
        else:
            self.min_node = node
        self.total_num_elements += 1
        pass

    def meld_into_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node
        pass

    def remove_from_root_list(self, node):
        if self.root_list is None:
            raise ValueError(
                'Fibonacci heap vide, impossible de supprimer un noeud !')
        if self.root_list == node:
            if self.root_list == self.root_list.right:
                self.root_list = None
                return
            else:
                self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left
        return

    def find_min(self) -> int:
        if self.min_node is None:
            raise ValueError("Fibonacci heap vide, pas de minimum !")
        return self.min_node.value

    def iterate(self, head=None):
        if head is None:
            head = self.root_list
        current = head
        while True:
            yield current
            if current is None:
                break
            current = current.right
            if current == head:
                break

    def delete_min(self) -> int:
        m = self.min_node
        if m is None:
            raise ValueError(
                'Fibonacci heap vide, impossible d\'extraire le minimum !')
        if m.child is not None:
            children = [x for x in self.iterate(m.child)]
            for i in range(0, len(children)):
                self.meld_into_root_list(children[i])
                children[i].parent = None
        self.remove_from_root_list(m)
        self.total_num_elements -= 1
        self.consolidate()
        if m == m.right:
            self.min_node = None
            self.root_list = None
        else:
            self.min_node = self.find_min_node()
        return m.value

    def consolidate(self):
        if self.root_list is None:
            return
        ranks_mapping = [None] * self.total_num_elements
        nodes = [x for x in self.iterate(self.root_list)]
        for node in nodes:
            degree = node.deg
            while ranks_mapping[degree] != None:
                other = ranks_mapping[degree]
                if node.value > other.value:
                    node, other = other, node
                self.merge_nodes(node, other)
                ranks_mapping[degree] = None
                degree += 1
            ranks_mapping[degree] = node
        return

    def merge_nodes(self, node, other):
        self.remove_from_root_list(other)
        other.left = other.right = other
        self.merge_with_child_list(node, other)
        node.deg += 1
        other.parent = node
        other.mark = False
        return

    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def find_min_node(self):
        if self.root_list is None:
            return None
        else:
            min = self.root_list
            for x in self.iterate(self.root_list):
                if x.value < min.value:
                    min = x
            return min

    def merge(self, fibonnaci_heap: Heap) -> None:
        if fibonnaci_heap.total_num_elements == 0:
            return
        if fibonnaci_heap.min_node.value < self.min_node.value:
            self.min_node = fibonnaci_heap.min_node
        self.total_num_elements += fibonnaci_heap.total_num_elements
        last = fibonnaci_heap.root_list.left
        fibonnaci_heap.root_list.left = self.root_list.left
        self.root_list.left.right = fibonnaci_heap.root_list
        self.root_list.left = last
        self.root_list.left.right = self.root_list
        pass

    def print(self, head=None):
        if self.root_list is not None:
            for heap in self.iterate():
                print('---')
                self.print_tree(heap)
                print()
            print('---')

    def print_tree(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        if node.child is not None:
            print()
            for child in self.iterate(node.child):
                self.print_tree(child)


#---------

print("Création de l'arbre...\n")
f = FibonacciHeap()

print("Insertion d'éléments dans l'arbre...\n")
f.insert(2)
f.insert(3)
f.insert(7)
f.insert(12)
f.insert(19)
f.insert(4)
f.insert(5)
f.insert(1)
print("Fait.\n")

print("Affichage de l'arbre...\n")
f.print()

print("\nLa plus petite valeur est : \n")
print(f.find_min())

print("\nSuppression de la plus petite valeur : \n")
print(f.delete_min())
print("\nFait !\n")

print("Affichage de l'arbre...\n")
f.print()

print("\nLa plus petite valeur est : \n")
print(f.find_min())

f2 = FibonacciHeap()
f2.insert(60)
f2.insert(32)

print("\nCréation de l'arbre numéro deux: \n")
f2.print()

print("\nMerge :\n")
f.merge(f2)
f.print()

class Heap(object):
    def insert(self, value: int) -> None:
        pass

    def find_min(self) -> int:
        pass

    def delete_min(self) -> int:
        pass

    def decrease_key(self, current_value: int, new_value: int) -> None:
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        pass


class FibonacciHeap(Heap):

    step: list = []

    def insert(self, value: int) -> None:
        self.step.append(value)

    def find_min(self) -> int:
        return min(self.step)

    def delete_min(self) -> int:
        self.step.remove(min(self.step))

    def merge(self, fibonnaci_heap: Heap) -> None:
        pass


f = FibonacciHeap()
f.insert(11)
f.insert(5)
f.insert(3)
f.insert(7)

print('La plus petite valeur est : {}\n'.format(f.find_min()))

print('-- Ajout de la valeur "1" --\n')
f.insert(1)

print('La plus petite valeur est : {}\n'.format(f.find_min()))

print('-- Suppression de la valeur "1" --\n')
f.delete_min()

print('La plus petite valeur est : {}\n'.format(f.find_min()))

f2 = FibonacciHeap()
f2.insert(2)
f2.insert(4)
f2.insert(6)
f2.insert(8)

print('-- Merge des deux arbres --\n')
f.merge(f2)
print('La plus petite valeur est : {}\n'.format(f.find_min()))

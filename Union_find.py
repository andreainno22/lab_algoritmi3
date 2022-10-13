# classe set: ha un attributo set_list che contiene set_elements
class Set:
    def __init__(self):
        self.set_list = []

# crea un element set element e chiama insert
    def make_set(self, x):
        self.insert(set_element(x))

# aggiunge a set_list un set element
    def insert(self, s_element):
        self.set_list.append(s_element)

# elimina da set_list i set_element che hanno fra gli elements x e y,
# aggiunge un nuovo set_elements che ha come elements l'unione degli elements dei due set elements eliminati
    def union(self, x, y):
        i_elements = []
        j_elements = []
        for i in self.set_list:
            if i.find(x):
                i_elements = i.elements
                self.set_list.remove(i)
        for j in self.set_list:
            if j.find(y):
                j_elements = j.elements
                self.set_list.remove(j)
        self.make_set(x)
        self.set_list[len(self.set_list)-1].elements = i_elements + j_elements

# restituisce il main_node del set element contenente x
    def find_set(self, x):
        for i in self.set_list:
            if i.find(x):
                return i.main_node


class set_element:
    def __init__(self, x):
        self.elements = []
        self.main_node = x
        self.elements.append(x)

    def find(self, x):
        return x in self.elements


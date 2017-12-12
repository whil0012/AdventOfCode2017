import unittest
from input_utilities.inputfilepath import get_input_file_path


class ProgramNode():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def __lt__(self, other):
        return self.name < other.name


class TestDay07(unittest.TestCase):
    def create_nodes_list(self, *args):
        return [ProgramNode(x) for x in args]

    def test_create_node_whenInvoked_createsNodeWithName(self):
        actual = create_node(r'jovejmr (40)')
        self.assertEquals(actual.name, 'jovejmr')

    def test_create_node_whenInvoked_createsNodeWithNoChildren(self):
        actual = create_node(r'jovejmr (40)')
        self.assertListEqual(actual.children, [])

    def test_add_children_whenNoChildren_leavesChildrenEmpty(self):
        nodes = self.create_nodes_list('jovejmr')
        add_children(nodes, r'jovejmr (40)')
        self.assertListEqual(nodes[0].children, [])

    def test_add_children_whenOneChild_addsOneChild(self):
        nodes = self.create_nodes_list('jovejmr', 'sleezka')
        add_children(nodes, r'sleezka (36) -> jovejmr')
        self.assertListEqual(nodes[1].children, [nodes[0]])

    def test_add_children_whenThreeChildren_addsThreeChildren(self):
        nodes = self.create_nodes_list('jovejmr', 'sleezka', 'sdfxsnj', 'weyts')
        add_children(nodes, r'sleezka (36) -> sdfxsnj, weyts, jovejmr')
        expected_children = [nodes[2], nodes[3], nodes[0]]
        self.assertListEqual(sorted(nodes[1].children), sorted(expected_children))

    def test_add_children_whenThreeChildren_setsParentOnChildNodes(self):
        nodes = self.create_nodes_list('jovejmr', 'sleezka', 'sdfxsnj', 'weyts')
        add_children(nodes, r'sleezka (36) -> sdfxsnj, weyts, jovejmr')
        for node in [nodes[0], nodes[2], nodes[3]]:
            self.assertEquals(node.parent, nodes[1])

    def test_find_bottom_node_whenInvoked_returnsBottomNode(self):
        nodes = self.create_nodes_list('jovejmr', 'sleezka', 'sdfxsnj', 'weyts')
        for node in [nodes[2], nodes[3], nodes[0]]:
            node.parent = nodes[1]
            nodes[1].children.append(node)
        actual = find_bottom_node(nodes)
        self.assertEquals(actual, nodes[1])


def create_node(node_description):
    node_parts = node_description.split()
    name = get_node_name_from_parts(node_parts)
    return ProgramNode(name)


def get_node_name_from_parts(node_parts):
    return node_parts[0]


def get_children_node_names_from_parts(node_parts):
    result = []
    for i in range(3, len(node_parts)):
        result.append(node_parts[i].replace(',', ''))
    return result


def add_children(nodes, node_description):
    node_parts = node_description.split()
    name = get_node_name_from_parts(node_parts)
    child_node_names = get_children_node_names_from_parts(node_parts)
    if not child_node_names:
        pass
    node = [x for x in nodes if x.name == name][0]
    child_nodes = [x for x in nodes if x.name in child_node_names]
    for child_node in child_nodes:
        node.children.append(child_node)
        child_node.parent = node


def get_set_of_child_nodes(nodes):
    result = set()
    for node in nodes:
        child_node_names = [x.name for x in node.children]
        result.update(child_node_names)
    return result


def find_bottom_node(nodes):
    nodes_that_are_not_children = [x for x in nodes if x.parent is None]
    # will not work properly if multiple nodes are not children of other nodes
    return nodes_that_are_not_children[0]


def main():
    file_path = get_input_file_path('day07.txt')
    nodes = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            node = create_node(line.strip())
            nodes.append(node)
        input_file.seek(0)
        for line in input_file:
            add_children(nodes, line.strip())
    bottom_node = find_bottom_node(nodes)
    print('bottom node: ', bottom_node.name)



if __name__ == '__main__':
    main()

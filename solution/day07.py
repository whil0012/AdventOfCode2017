import unittest
from input_utilities.inputfilepath import get_input_file_path


class ProgramNode():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def __lt__(self, other):
        return self.name < other.name


class TestDay07(unittest.TestCase):
    def create_nodes_list(self, **kwargs):
        return [ProgramNode(x, y) for x, y in kwargs.items()]

    def test_create_node_whenInvoked_createsNodeWithName(self):
        actual = create_node(r'jovejmr (40)')
        self.assertEquals(actual.name, 'jovejmr')

    def test_create_node_whenInvoked_createsNodeWithNoChildren(self):
        actual = create_node(r'jovejmr (40)')
        self.assertListEqual(actual.children, [])

    def test_create_node_whenInvoked_createsNodeWithWeight(self):
        actual = create_node(r'jovejmr (40)')
        self.assertEqual(actual.weight, 40)

    def test_add_children_whenNoChildren_leavesChildrenEmpty(self):
        nodes = self.create_nodes_list(jovejmr=40)
        add_children(nodes, r'jovejmr (40)')
        self.assertListEqual(nodes[0].children, [])

    def test_add_children_whenOneChild_addsOneChild(self):
        child_nodes = self.create_nodes_list(jovejmr=40)
        parent_nodes = self.create_nodes_list(sleezka=36)
        add_children(parent_nodes + child_nodes, r'sleezka (36) -> jovejmr')
        self.assertListEqual(parent_nodes[0].children, [child_nodes[0]])

    def test_add_children_whenThreeChildren_addsThreeChildren(self):
        child_nodes = self.create_nodes_list(jovejmr=40, sdfxsnj=55, weyts=23)
        parent_nodes = self.create_nodes_list(sleezka=36)
        add_children(parent_nodes + child_nodes, r'sleezka (36) -> sdfxsnj, weyts, jovejmr')
        self.assertListEqual(sorted(parent_nodes[0].children), sorted(child_nodes))

    def test_add_children_whenThreeChildren_setsParentOnChildNodes(self):
        child_nodes = self.create_nodes_list(jovejmr=40, sdfxsnj=55, weyts=23)
        parent_nodes = self.create_nodes_list(sleezka=36)
        add_children(parent_nodes + child_nodes, r'sleezka (36) -> sdfxsnj, weyts, jovejmr')
        for node in child_nodes:
            self.assertEquals(node.parent, parent_nodes[0])

    def test_find_bottom_node_whenInvoked_returnsBottomNode(self):
        child_nodes = self.create_nodes_list(jovejmr=40, sdfxsnj=55, weyts=23)
        parent_nodes = self.create_nodes_list(sleezka=36)
        for node in child_nodes:
            node.parent = parent_nodes[0]
            parent_nodes[0].children.append(node)
        actual = find_bottom_node(parent_nodes + child_nodes)
        self.assertEquals(actual, parent_nodes[0])

    def set_up_children_nodes(self, parent_node, child_nodes):
        for node in child_nodes:
            node.parent = parent_node
            parent_node.children.append(node)

    def test_calculate_child_branch_weights_whenThreeChildrenWithChildren_returnsTotalWeights(self):
        child_nodes_1 = self.create_nodes_list(jovejmr=40)
        child_nodes_2 = self.create_nodes_list(sdfxsnj=55)
        child_nodes_3 = self.create_nodes_list(weyts=23)
        child_nodes_1_2 = self.create_nodes_list(pqjeof=20, faszmg=50, jvjlfb=42)
        child_nodes_2_2 = self.create_nodes_list(oxwpxqj=5, ryonf=12, jrgndow=100)
        child_nodes_3_2 = self.create_nodes_list(iayecc=86, lwuwrp=84, haxfzky=72)
        parent_nodes = self.create_nodes_list(sleezka=36)
        self.set_up_children_nodes(parent_nodes[0], child_nodes_1 + child_nodes_2 + child_nodes_3)
        self.set_up_children_nodes(child_nodes_1[0], child_nodes_1_2)
        self.set_up_children_nodes(child_nodes_2[0], child_nodes_2_2)
        self.set_up_children_nodes(child_nodes_3[0], child_nodes_3_2)
        expected_weights = {'jovejmr':152, 'sdfxsnj':172, 'weyts':265}
        actual_weights = calculate_child_branch_weights(parent_nodes[0])
        self.assertDictEqual(actual_weights, expected_weights)


def create_node(node_description):
    node_parts = node_description.split()
    name = get_node_name_from_parts(node_parts)
    weight = get_node_weight_from_parts(node_parts)
    return ProgramNode(name, weight)


def get_node_name_from_parts(node_parts):
    return node_parts[0]


def get_node_weight_from_parts(node_parts):
    node_weight_part = node_parts[1].replace('(', '').replace(')', '')
    return int(node_weight_part)


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


def calculate_child_branch_weight(child_node):
    result = child_node.weight
    for sub_child_node in child_node.children:
        result += calculate_child_branch_weight(sub_child_node)
    return result


def calculate_child_branch_weights(parent_node):
    result = {}
    for child_node in parent_node.children:
        child_branch_weight = calculate_child_branch_weight(child_node)
        result[child_node.name] = child_branch_weight
    return result


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
    child_branch_weights = calculate_child_branch_weights(bottom_node)
    print('child branch weights: ', child_branch_weights)
    unbalanced_node = [x for x in nodes if x.name == 'luralcy'][0]
    child_branch_weights = calculate_child_branch_weights(unbalanced_node)
    print('child branch weights: ', child_branch_weights)

    unbalanced_node = [x for x in nodes if x.name == 'bvrxeo'][0]
    child_branch_weights = calculate_child_branch_weights(unbalanced_node)
    print('child branch weights: ', child_branch_weights)

    unbalanced_node = [x for x in nodes if x.name == 'ltleg'][0]
    child_branch_weights = calculate_child_branch_weights(unbalanced_node)
    print('child branch weights: ', child_branch_weights)
    print('unbalanced node weight: ', unbalanced_node.weight)



if __name__ == '__main__':
    main()

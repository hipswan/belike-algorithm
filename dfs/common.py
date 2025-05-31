import json
import pickle
import xml.etree.ElementTree as ET
import yaml
import csv
from io import StringIO
from bs4 import BeautifulSoup

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result
def list_to_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
def tree_to_string(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    # Remove trailing "null" values
    while result and result[-1] == "null":
        result.pop()
    return "[" + ", ".join(result) + "]"
def string_to_tree(s):
    if s == "[]":
        return None
    s = s.strip("[]")
    if not s:
        return None
    arr = [int(x) if x != "null" else None for x in s.split(",")]
    return list_to_tree(arr)
def tree_to_dict(root):
    if not root:
        return {}
    result = {}
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node:
            if depth not in result:
                result[depth] = []
            result[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return result
def dict_to_tree(d):
    if not d:
        return None
    max_depth = max(d.keys())
    nodes = {}
    for depth in range(max_depth + 1):
        for val in d.get(depth, []):
            nodes[val] = TreeNode(val)
    root = nodes[d[0][0]] if 0 in d else None
    for depth in range(max_depth):
        for val in d.get(depth, []):
            node = nodes[val]
            left_vals = d.get(depth + 1, [])
            right_vals = d.get(depth + 1, [])
            if left_vals:
                node.left = nodes[left_vals[0]] if left_vals else None
                left_vals.pop(0)
            if right_vals:
                node.right = nodes[right_vals[0]] if right_vals else None
                right_vals.pop(0)
    return root
def tree_to_json(root):
    import json
    return json.dumps(tree_to_dict(root))
def json_to_tree(json_str):
    import json
    d = json.loads(json_str)
    return dict_to_tree(d)
def tree_to_tuple(root):
    if not root:
        return ()
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return tuple(result)
def tuple_to_tree(tup):
    if not tup:
        return None
    arr = [val if val is not None else "null" for val in tup]
    return list_to_tree(arr)
def tree_to_set(root):
    if not root:
        return set()
    result = set()
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.add(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result
def set_to_tree(s):
    if not s:
        return None
    arr = [val for val in s]
    return list_to_tree(arr)
def tree_to_frozen_set(root):
    if not root:
        return frozenset()
    result = set()
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.add(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return frozenset(result)
def frozen_set_to_tree(fs):
    if not fs:
        return None
    arr = [val for val in fs]
    return list_to_tree(arr)
def tree_to_bytes(root):
    import pickle
    return pickle.dumps(tree_to_dict(root))
def bytes_to_tree(b):
    import pickle
    d = pickle.loads(b)
    return dict_to_tree(d)
def tree_to_xml(root):
    import xml.etree.ElementTree as ET

    def build_xml(node):
        if not node:
            return ET.Element("node", attrib={"val": "null"})
        elem = ET.Element("node", attrib={"val": str(node.val)})
        elem.append(build_xml(node.left))
        elem.append(build_xml(node.right))
        return elem

    root_elem = build_xml(root)
    return ET.tostring(root_elem, encoding='unicode')
def xml_to_tree(xml_str):
    import xml.etree.ElementTree as ET

    def parse_xml(elem):
        if elem.attrib['val'] == 'null':
            return None
        node = TreeNode(int(elem.attrib['val']))
        node.left = parse_xml(elem[0]) if len(elem) > 0 else None
        node.right = parse_xml(elem[1]) if len(elem) > 1 else None
        return node

    root_elem = ET.fromstring(xml_str)
    return parse_xml(root_elem)
def tree_to_yaml(root):
    import yaml

    def build_yaml(node):
        if not node:
            return None
        return {
            'val': node.val,
            'left': build_yaml(node.left),
            'right': build_yaml(node.right)
        }

    return yaml.dump(build_yaml(root), default_flow_style=False)
def yaml_to_tree(yaml_str):
    import yaml

    def parse_yaml(data):
        if data is None:
            return None
        node = TreeNode(data['val'])
        node.left = parse_yaml(data.get('left'))
        node.right = parse_yaml(data.get('right'))
        return node

    data = yaml.safe_load(yaml_str)
    return parse_yaml(data)
def tree_to_csv(root):
    import csv
    from io import StringIO

    def build_csv(node):
        if not node:
            return ["null", "null"]
        return [node.val, build_csv(node.left), build_csv(node.right)]

    csv_data = build_csv(root)
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(csv_data)
    return output.getvalue()
def csv_to_tree(csv_str):
    import csv
    from io import StringIO

    def parse_csv(data):
        if not data or data[0] == "null":
            return None
        node = TreeNode(int(data[0]))
        node.left = parse_csv(data[1]) if len(data) > 1 else None
        node.right = parse_csv(data[2]) if len(data) > 2 else None
        return node

    reader = csv.reader(StringIO(csv_str))
    for row in reader:
        return parse_csv(row)
def tree_to_html(root):
    def build_html(node):
        if not node:
            return "<li>null</li>"
        html = f"<li>{node.val}</li>"
        html += "<ul>"
        html += build_html(node.left)
        html += build_html(node.right)
        html += "</ul>"
        return html

    return f"<ul>{build_html(root)}</ul>"
def html_to_tree(html_str):     
    from bs4 import BeautifulSoup

    def parse_html(elem):
        if elem.name != 'li':
            return None
        if elem.text == 'null':
            return None
        node = TreeNode(int(elem.text))
        children = elem.find_all('ul', recursive=False)
        if children:
            node.left = parse_html(children[0].find('li')) if children[0].find('li') else None
            node.right = parse_html(children[1].find('li')) if len(children) > 1 and children[1].find('li') else None
        return node

    soup = BeautifulSoup(html_str, 'html.parser')
    return parse_html(soup.ul.find('li')) if soup.ul else None
def tree_to_markdown(root):
    def build_markdown(node, depth=0):
        if not node:
            return "  " * depth + "- null\n"
        markdown = "  " * depth + f"- {node.val}\n"
        markdown += build_markdown(node.left, depth + 1)
        markdown += build_markdown(node.right, depth + 1)
        return markdown

    return build_markdown(root)
def markdown_to_tree(markdown_str):
    lines = markdown_str.strip().split('\n')
    stack = []
    root = None

    for line in lines:
        depth = (len(line) - len(line.lstrip())) // 2
        value = line.strip().lstrip('- ').strip()

        if value == 'null':
            node = None
        else:
            node = TreeNode(int(value))

        if depth == 0:
            root = node
            stack = [node]
        else:
            while len(stack) > depth:
                stack.pop()
            parent = stack[-1]
            if parent:
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)

    return root
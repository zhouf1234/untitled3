import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

# 读取xml内容
print(root.tag)
for child in root:
    print(child.tag, child.attrib, child.attrib['name'])
print()

# 修改xml 内容
for node in root.iter('year'):
    # print(node.tag, node.text)
    new_year = int(node.text) + 10
    node.text = str(new_year)
    node.set('update', 'yes')
tree.write('data.xml')


# 删除节点
for country in root:
    rank = int(country.find('rank').text)
    if rank > 5:
        root.remove(country)
tree.write('data.xml')
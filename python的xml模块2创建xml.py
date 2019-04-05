import xml.etree.ElementTree as ET


# 创建标签
namelist = ET.Element('namelist')

# 给namelist 创建子元素
name = ET.SubElement(namelist, 'name', {"src":'1.jpg', "title":"hello"})
name.text = '丹丹'

name1 = ET.SubElement(namelist, 'name', {"src":'1.jpg', "title":"hello"})
name1.text = '莉莉'

et = ET.ElementTree(namelist)
et.write('namelist.xml', encoding='utf-8', xml_declaration=True)

# 显示字符串
ET.dump(namelist)


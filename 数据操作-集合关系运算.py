#两个集合：会写代码的集合和会做饭的集合
python_names = {'赵','钱','孙','李','周'}
cook_names = {'吴','郑','王','赵','周'}
#即会写代码的和又会做饭的集合   ：交集
print(python_names & cook_names)
#会写代码的集合或会做饭的集合的合集：合集
print(python_names | cook_names)
#会写代码的集合但是不会做饭的集合：差集
print(python_names - cook_names)
#只会写代码的集合和只会做饭的集合：对称差集
print(python_names ^ cook_names)

#集合比较大小:比的是子集
s1 = {122,233,433,533,111}
s2 = {122,533,111}
print(s1 > s2)      #s1包含s2
print(s1 < s2)

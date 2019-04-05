#一个字典
boy_firends = {'name':'李白','age':'17','height':'178','weight':'130'}

#深层复制（引用）
boy_firends2 = boy_firends
boy_firends2['age'] = 20
print(boy_firends)                  #age改成了20

boy_firends2 = boy_firends.copy()    #即把boy_firends复制给boy_firends2
print(boy_firends)
# -*- coding:utf-8 -*-  

import MySQLdb
import time

class Exesql:
    def __init__(self, sql):
        '''连接数据库，返回所有成语'''
        with MySQLdb.connect("localhost","root","123456","chengyu", charset='utf8') as cur:
            cur.execute(sql)
            self.data = cur.fetchall()

class Dictionary:   
    def __init__(self, data_set):
        self.data = data_set

    def get_head(self, char):
        '''获取以某个字开头的成语列表'''
        word_list = []
        for word in self.data:
            if word[0] == char:
                word_list.append(word)
        return word_list

class LevelSearch:
    '''
        广度优先进行遍历
        遍历的结果存储在level_list中
        level_list是个三级数组构成的树：
            第一级是树的每一层
            第二级是处于同层的成语节点列表
            第三级是单个成语节点，每个节点包括成语本身和它的父节点在上一层中的位置
    '''
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.has_searched = set()#如果已经查过以某个字开头的成语，将这个字存入集合
        top_level = [[self.first, -1]]#顶层
        self.level_list = [top_level]
        self.level = 0#查询的层数
        self.count = 1#遍历的成语数量
    
    def do_search(self, data):
        '''
            每次查询都生成树的新层
        '''
        new_level = []
        position = 0
        for c in self.level_list[self.level]:
            if c[0][-1:] not in self.has_searched:#已查找过的字不再查找
                chengyu = Dictionary(data)
                chengyu_list = chengyu.get_head(c[0][-1:])
                for word in chengyu_list:
                    self.count += 1
                    new_level.append([word, position])
                    if self.last == word:
                        self.level_list.append(new_level)
                        return position #匹配到最后一个成语，返回父节点在上层的位置, 结束
            position += 1
            self.has_searched.add(c[0][-1:])
        
        if len(new_level) == 0:
            return -2#新层没有数据，说明没有找到对应的成语，结束
        else:
            self.level += 1
            self.level_list.append(new_level)
            return -1#还没有匹配到最后一个成语，需要继续在下一层查找

    def gen_result(self, position):
        '''生成查询结果'''
        result = []
        result.append(self.last)
        for l in range(self.level):
            result.insert(0, self.level_list[self.level - l][position][0])
            position = self.level_list[self.level - l][position][1]
        result.insert(0, self.first)
        return result
            
if __name__=='__main__':
    sql = """select chengyu from pre_org_chengyu"""
    data = Exesql(sql).data

    data_set = []
    for i in data:
        data_set.append(i[0])

    first = raw_input("请输入第一个成语: ")
    last = raw_input("请输入最后一个成语: ")
    first = unicode(first, 'utf8')
    last = unicode(last, 'utf8')
    Search = LevelSearch(first, last)
    print u'开始查找第{}层...'.format(Search.level + 1)
    position = Search.do_search(data_set)
    while position == -1:
            print u'开始查找第{}层...'.format(Search.level + 1)
            position = Search.do_search(data_set)

    print u'=================='
    if position == -2:
        print u'没有匹配到'
    else:
        print u'成语接龙的结果是：'
        result = Search.gen_result(position)
        for word in result:
            print word

    print u'查找了{}个成语'.format(Search.count)

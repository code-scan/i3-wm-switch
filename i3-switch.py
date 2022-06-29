#coding=utf-8
import json
import os
import sys

result = []
def get_current_worksapce():
    result = os.popen('i3-msg -t get_workspaces').read()
    data = json.loads(result)
    for i in data:
        if i.get('focused'):
            return i.get('num')
    return False
def fetch_node(num,node,nodes=[]):
    for value in node:
        if value.get('num') and value.get('num') == num:
            hit_node(value.get('nodes'))
        if value.get('nodes'):
            fetch_node(num,value.get('nodes'),nodes)
def hit_node(node):
    global result
    for value in node[0].get('nodes'):
        print(value.get('id'),value.get('layout'),value.get('name'))
        result.append(value.get('id'))
        # if value.get('nodes'):
        #     hit_node(value.get('nodes'))
    return result
def swtich_wm(id):
    os.popen('i3-msg  "[con_id={0}]" focus'.format(id)).read()
def get_workspace_windows(num):
    result = os.popen('i3-msg -t get_tree').read()
    data = json.loads(result)
    if data.get('nodes'):
        return fetch_node(num,data.get('nodes'))
    return False
num = get_current_worksapce()
get_workspace_windows(num)
if len(sys.argv) == 2 and len(result) >= (int(sys.argv[1])-1):
    index = int(sys.argv[1])-1
    swtich_wm(result[index])

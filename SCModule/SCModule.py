# -*- coding: utf-8 -*-
import json
import re

class _act_ele:
    name = ""
    constraint = None
    priority = None

class _action:
    name = ""
    act_element = []

class _tactics:
    name = ""
    opmode = None           #运行方式
    flt_type = None         #故障方式
    flt_ele  = []           #故障元件
    tac_constraint = None   #策略约束
    action_name = ""        #措施名称
    action = None           #措施




class SCModule:
    E_Conf = None   #E文件基本配置
    Tactics = []    #

    def __init__(self, file = None):
        self.read_module_conf(file)

    def read_module_conf(self, file):
        with open(file, 'r', encoding='gbk') as f:
            self.E_Conf = json.load(f)

    def resolve_tactics_def(self, content):
        pattern = "^#"
        clt = content.split()
        if re.match(pattern, content) == None:
            return
        if len(clt) < 14:
            return

        isFound = False
        for tac in self.Tactics:
            if clt[self.E_Conf['tactics_def']['tac_opmode']] == tac.opmode and clt[self.E_Conf['tactics_def']['tac_flt']] == tac.flt_type:
                isFound = True





    def read_module_file(file):
        with open(file, 'r', encoding='gbk') as f:
            lines = f.readlines()
            pattern = "^[<@#]"
            for line in lines:
                #content = line.strip(" ")
                if re.match('#define', line):
                    continue
                if re.match(pattern, line):
                    fd.writelines(line)







if __name__ == "__main__":
    #data = read_module_conf('../module.json')
    #read_module_file('../tactics_CFG.txt')
    sc = SCModule('../module.json')
    print(sc.E_Conf['element_def']['ele_id'])



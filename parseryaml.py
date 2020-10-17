# -*- coding: utf-8 -*-
'''
Filename:
Author: mac
Date:
Desc:
'''
import yaml
with open('rad/rad_config.yml', 'r', encoding='utf-8') as f:
	aa=(yaml.load(f.read(),Loader=yaml.Loader))
print(aa["request-config"]["cookies"])
print(aa.keys())


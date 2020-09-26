# -*- coding: UTF-8 -*-
import os,json
data = []
i = 0
os.chdir('sound')
files = os.listdir('.')
files.sort()
for file in files:
		if os.path.isfile(file) and file.endswith('mp3') or file.endswith('ogg'):
			name = os.path.splitext(file)[0].split('_')[-1]
			url = "https://gitee.com/Bave/giao-tone-server/raw/master/sound/" + file
			item = {'name' : name, 'url' : url}
			data.append(item)

list = {"list" : data}

file_name = '../data.json'
with open(file_name,'w') as file_obj:
	str = json.dumps(list).encode('utf-8').decode("unicode_escape")
	print(str)
	file_obj.write(str)

# -*- coding: UTF-8 -*-
import os,json
data = []
i = 0
os.chdir('sound')
for file in os.listdir('.'):
		if os.path.isfile(file) and file.endswith('mp3') or file.endswith('ogg'):
			name = os.path.splitext(file)[0]
			url = "https://gitee.com/Bave/giao-tone-server/raw/master/sound/" + file
			item = {'name' : name, 'url' : url}
			data.append(item)

list = {"list" : data}

file_name = '../data.json'
with open(file_name,'w') as file_obj:
	file_obj.write(json.dumps(list).encode('utf-8').decode("unicode_escape"))

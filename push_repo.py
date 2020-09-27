# -*- coding: UTF-8 -*-
import os, json, codecs
data = []
os.chdir('sound')
files = os.listdir('.')
files.sort()
for file in files:
		if os.path.isfile(file) and file.endswith('mp3') or file.endswith('ogg'):
			name = os.path.splitext(file)[0].split('_')[-1]
			url = "https://gitee.com/Bave/giao-tone-server/raw/master/sound/" + file
			item = {'name' : name, 'url' : url, 'url2' : file}
			data.append(item)

list = {"list" : data}

file_name = '../data.json'
with codecs.open(file_name, 'w', encoding='utf-8') as file_obj:
	file_obj.write(json.dumps(list).encode('utf-8').decode("unicode_escape"))

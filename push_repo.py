# -*- coding: UTF-8 -*-
import os, json, codecs, time
data = []
os.chdir('sound')
files = os.listdir('.')
files.sort()
for file in files:
		if os.path.isfile(file) and file.endswith('mp3') or file.endswith('ogg'):
			name = os.path.splitext(file)[0].split('_')[-1]
			url = "https://imbavelee.coding.net/p/GiaoTone/d/giao-tone-server/git/raw/master/sound/" + file
			item = {'name' : name, 'url' : url}
			data.append(item)

list = {"list" : data}

file_name = '../data.json'
with codecs.open(file_name, 'w', encoding='utf-8') as file_obj:
	file_obj.write(json.dumps(list).encode('utf-8').decode("unicode_escape"))

os.chdir('..')
t = time.strftime("%Y%m%d", time.localtime())
os.system("git add .")
os.system('git commit -m Update:' + t)
os.system("git push gitee master")
os.system("git push coding master")
os.system("git push github master")

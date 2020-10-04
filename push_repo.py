# -*- coding: UTF-8 -*-
import os, json, codecs, time
data = []
os.chdir('sound')
categories = os.listdir('.')
categories.sort()

for category in categories:
	category_name = os.path.splitext(category)[0].split('_')[-1]
	sounds = os.listdir('./' + category)
	sounds.sort()
	for sound_file in sounds:
		name = os.path.splitext(sound_file)[0].split('_')[-1]
		url = "https://imbavelee.coding.net/p/GiaoTone/d/giao-tone-server/git/raw/master/sound/" + category + '/' + sound_file
		# item = {'name' : category_name + '|' + name, 'url' : url, 'category' : category_name}
		item = {'name' : name, 'url' : url, 'category' : category_name}
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

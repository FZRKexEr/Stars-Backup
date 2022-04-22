import requests
import json
from git import Repo

def sol(content):
	# 格式化 json, 类型是 str
	# print(json.dumps(content, indent=2))
	for i in content:
		repo = Repo.clone_from(url=i['clone_url'], to_path='../github_stars/' + i['name'])
		print(i['name'] + "备份完成")

def main():
	user = 'fzrkexer'
	for i in range(100):
		star = requests.get('https://api.github.com/users/' + user + '/starred?page=' + str(i))
		if len(json.loads(star.content)) == 0:
			break
		if star.ok:
			# json.loads() 把 star.content 转换成 list
			sol(json.loads(star.content))
		else:
			print(star.raise_for_status())

if __name__ == '__main__':
	main()


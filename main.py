import requests
import json
from git import Repo

def sol(content):
	# 格式化 json, 类型是 str
	# print(json.dumps(content, indent=2))
	address = []
	for i in content:
		address.append(i['clone_url'])
	print(address)

def main():
	user = 'fzrkexer'
	star = requests.get('https://api.github.com/users/' + user + '/starred')
	if star.ok:
		# json.loads() 把 star.content 转换成 list
		sol(json.loads(star.content))
	else:
		print(star.raise_for_status())

if __name__ == '__main__':
	main()

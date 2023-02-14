t = 0
with open('sourceslist.txt', 'r') as f:
	t = f.read()

with open('/etc/apt/sources.list', 'w') as f:
	f.write(t)
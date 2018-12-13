# first session

pwd = "abc123"
database.write(username, sha256(pwd))

# second session

pwd = input('give pass')
if (database.check(username, sha256(pwd))):
	login(user)
else:
	print('wrong pass')
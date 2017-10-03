import crypt

passwd = str(input("password in ./htpasswd file: "))

wlname = str(input("wordlist: "))

wordlist = open(wlname)

for word in wordlist:
	if(crypt.crypt(word[:-1], passwd[:2]) == passwd):
		print("Senha encontrada: ", word)
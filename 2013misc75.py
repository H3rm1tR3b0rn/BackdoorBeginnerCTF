from math import sqrt

p = 1
primos = [2]
limite = 10000

for n in range(2,limite):
	ep = 1
	for i in primos:
		if n%i == 0:
			ep=0
			break
		if i > sqrt(n):
			break
	if(ep==1):
		primos.append(n)

sp=[]
for i in range(len(primos)):
	s = 0 
	for j in range(i):
		s = s + primos[j]
	sp.append(s)


import requests

url = "http://hack.bckdr.in/2013-MISC-75/misc75.php"

with requests.Session() as c:
	http1 = c.get(url)
	httpc = str(http1.content)
	list = httpc.split(" ")
	w = int(list[16])
	print(w, ": ", sp[w])
	resp = str(sp[w])
	http = c.post(url, data={"answer":resp}, headers={"Referer":"http://hack.bckdr.in/2013-MISC-75/misc75.php"})
	
	print("\n", http.content)



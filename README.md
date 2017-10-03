# BackdoorBeginnerCTF

## 2013-bin-50

This is a simple challenge. The file (binary50) is a ELF file. This can be discovered using 'file' command on terminal. 
Executing the file, we see:

```bash
      $./binary50  
      Please provide the password  
      $./binary50 password  
      Nothing to see here.  
```


Using 'strings', i found: 

```bash
      t$(L  
      |$0H  
      Password is Advicemallard  
      qie////3213/wqeqwe/qwqweqsxcf/d/////  
      Password is Butter  
      Password is Hoobastank  
      Password is Darth  
      Password is Jedimaster  
      Password is Masternamer  
      Password is Morpheus  
      Password is Neutron  
      Password is Coyote  
      Password is Tweety  
      Nothing to see here.  
      Please provide the password   
      ;*3$"  
      GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3  
```

So, trying the passwords one by one:

```bash
      $ ./binaary50 Masternamer  
      3cd50c6be9bbede06e51741928d88b7e  
```

Using some SHA256 calculator, I found:  
dad827e94c609b76424287f2523b2117475df29e4ca8475444a9976faedc00f7  

## 2013-web-50

The proglem give a link: http://hack.bckdr.in/2013-WEB-50/getflag.php  

![2015web50-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2013web50-1.png)

The problem give a very useful hint: Cookies!!!  
So, I tried to read the cookie of the link using a cookie manager called 'EditThisCookie', a extension of chrome.  

![2015web50-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2015web50-2.png)

The cookie called 'username' had the value 'john', so i changed it to 'admin':  

![2015web50-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2015web50-3.png)

Refreshing the page, i got:  

![2015web50-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2015web50-4.png)

That was the answer to the problem!  

## 2013-misc-75

That is one of my favorites!  
So, the link of challenge is: http://hack.bckdr.in/2013-MISC-75/misc75.php  

![2013misc75](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2013misc75-1.png)

Everytime I refresh the link, the number of first primes change, so, i had to code!!  
In python, we have: 

```python
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

```

The firts part of the code make a list which have the sum of the first n primes as the nth term. The second part of the code just send a POST request to the link with the answer and i got:    

![2013misc75](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2013misc75-2.png)

## secret area  

The best one!  

So, we open the link and find:

![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-1.png)  
![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-2.png)  

The hint for this challenge is: htaccess! So, I had to look for a 'htaccess' file or a 'htpasswd' file. Noticing that there is a /secure/ folder on the web server, I decided to try change the url to http://hack.bckdr.in/SECR/index.php?page=secure/.htpasswd, and i got:  

![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-3.png)  

Exactly what I want! A 'user:password' file! But, I had to decrypt that! It's time to code again:  

```python
      import crypt

      passwd = str(input("password in ./htpasswd file: "))

      wlname = str(input("wordlist: "))

      wordlist = open(wlname)

      for word in wordlist:
            if(crypt.crypt(word[:-1], passwd[:2]) == passwd):
                  print("Senha encontrada: ", word)
```

Using a wordlist downloaded in https://github.com/duyetdev/bruteforce-database, i got: 

![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-4.png)  

Using the username/password in the site, I got:  

![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-5.png)  

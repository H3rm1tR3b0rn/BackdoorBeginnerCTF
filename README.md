# Backdoorv Beginner CTF

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

![2013misc75-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2013misc75-1.png)

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

![2013misc75-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/2013misc75-2.png)

## secret area  

The best one!  

So, we open the link and find:

![SecretArea-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-1.png)  
![SecretArea-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-2.png)  

The hint for this challenge is: htaccess! So, I had to look for a 'htaccess' file or a 'htpasswd' file. Noticing that there is a /secure/ folder on the web server, I decided to try change the url to http://hack.bckdr.in/SECR/index.php?page=secure/.htpasswd, and i got:  

![SecretArea-3](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-3.png)  

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

![SecretArea-5](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-4.png)  

Using the username/password in the site, I got:  

![SecretArea-5](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/SecretArea-5.png)  

## file reader

So, the file reader show what is in a text file and the flag is in the parent directory of /FLREAD/app/viewer. Writing '.../flag.php' on the file reader, I got:  

```javascript
<?php
	$flag = "93b9e8c732573769fac43d744fad4120bde8d1f98cc1f6e9011045ff72f45b96";  
?>
```

## browser

## authorized persons only

## simple cipher 
the text 'lkw qlby av qtpfyieidwnpawseycnicsdynjicklqevaciipoksabidpletelbmlpskkupsrrl' on the link in the challeng seems to be a text encrypted by a simple substitutional cryptography. After trying decrypt this with vigenere with SDSLabs as a key, I got:
'the flag is yipegqbqswmxitatybvqzasymrqzsaqddizqxpnsaxjxdotmqmabltxpszuoazot'

## undisputed

A .ext4. Huuuum... I had to mount this... so:

![undisputed](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/undisputed.png)

## sound

Well, this one is about a mp3 file. Opening it with audacity, reversing the audio and slowing the speed, I heard a woman speaking:

```
The flag is sha256 of upside_down
```

## nosignal

Well, two meaningless images, apparently. Opening the two images on gimp and changing the Opacity of the layer to 50% of one of them, i got: 

![nosignal](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/nosignal.png)

## hidden flag - medium

So, this one ie very cool! The file `hide_medium` is a ELF file, so i tried to use strings but, as expected, it returned:  

![hidemedium-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/hidemedium-1.png)

```
It's not that easy as you think so
```  

So, I thouthg: It's time for gdb! Opening gdb, the first think I did was use `disass main` to see what was happening, but it was useless.  

![hidemedium-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/hidemedium-2.png)

Using the `info functions` command, I found a function with a real shameless name: `print_flag`:    

![hidemedium-3](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/hidemedium-3.png)

In this moment, I had to enter in that function but, the normal flux of the program don't do this.  So, i had to compile a new part of the code using `compile code -- print_flag()`after a breakpoint on the address :  

![hidemedium-4](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/hidemedium-4.png)

And there it is: 841f980abd04b26fe804ca0c207a574bef504cb6a3c3599a449e845ca993d2cf

## lost

The link of challenge is: http://hack.bckdr.in/LOST/:  

![LOST-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/LOST-1.png)

When I open the console, the following strings appears: 

```
      Welcome n00b to the ctf
      n00b sometimes you need to POST to flag.php
```

first, i tried to open the flag.php file, but:  

![LOST-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/LOST-2.png)

I tried to use curl to do a POST request to the link: hack.bckdr.in/LOST/flag.php and ...  

![LOST-3](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/LOST-3.png)


## search

The file given in the challenge is a .txt file, but, when I opened in terminal, some strange characters appeared:  

![search-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/search-1.png)  

Using the 'file' command, it returned: 

```
search.txt: JPEG image data, JFIF standard 1.01, resolution (DPI), density 1x1, segment length 16, baseline, precision 8, 200x200, frames 1
```

Changing the extension of the file to .jpeg, I've got:  

![search-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/search.jpeg) 

Using a QR-code reader, i've got the url: https://dhavalkapil.com/assets/files/flag.txt  

The flag is in the link.

## hidden flag - easy

So, the challenge give a file named hide_easy. Using the 'file' command, I've got:  

```
hide_easy: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=cf56f38a7483f0f337aa3b25644426028885c9b9, not stripped
```

Using the 'strings' command, I've got, in some part of the code:  

```
      QVhl  
      [^_]  
      939d9556640d4  
      47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36  
      What do you think you will get here?  
      ;*2$"  
      GCC: (Ubuntu/Linaro 4.7.3-1ubuntu1) 4.7.3  
      .symtab  
```

So, that's the flag: 47f5847d92e9fbbd4d762036ff684ccde6a80d3a171c4dcd0b724fae25826c36

![hidden](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/hidden.png)

## location 51

When I clicked on the link, I was asked for a password... opening the page source code, I found some code on javascript, then i tried to execute that on console:  

![location-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/location-1.png)

Clicking on the link again, i noticed that is was redirected from '/index.html' to '/trap.html'. So, I had to access the index page. So, I tring to access the index source directly using view-source:http://hack.bckdr.in/LOCATION-51/index.html:  

![location-2](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/location-2.png)


## path

Weel, the challenge say that there is a flag in the domaing flag.bckdr.in. I had to do a dns recon. Using the python script downloaded in https://github.com/darkoperator/dnsrecon, I got: 

## robot
## batman

Noticing that the end url change when we click on differentes parts of the site, I thought I should try to change the url by myself.  
With the link "http://hack.bckdr.in/BATMAN/?st=10", I got:

"Flag is "y0u_4r3_b47m4n"
You are Batman now. Proudly say, I'm Batman"

## wahtzdis

This is a easy one! Here is what appears in the link: http://hack.bckdr.in/WAHTZDIS/:  

![WAHTZDIS-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/wahtzdis-1.png)

So... I thougth: WTF?? Then I remembered the brainfuck...  
With some search in google, i found the JSfuck, something like brainfuck, but with other objective. JSfuck is just a way to obfuscate the code of JavaScript to protect it. The cool thing is that the code in JSfuck can be runned in console, on chrome or other browser:  

![WAHTZDIS-1](https://github.com/Dalbukerk/BackdoorBeginnerCTF/blob/master/wahtzdis-2.png)  

The script that i received is:

```javascript
ƒ anonymous() {
alert('window.atob("eTB1X3czcjNfbHVja3lfN2gxNV83MW0zX24wMGI=")')
}
```

So, the solution is:

```javascript
> atob("eTB1X3czcjNfbHVja3lfN2gxNV83MW0zX24wMGI=")
< "y0u_w3r3_lucky_7h15_71m3_n00b"
```

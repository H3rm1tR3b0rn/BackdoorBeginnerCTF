# BackdoorBeginnerCTF

## 2013-bin-50

This is a simple challenge. The file (binary50) is a ELF file. This can be discovered using 'file' command on terminal. 
Executing the file, we see:

'''
$./binary50
Please provide the password
$./binary50 password
Nothing to see here.
'''

Using 'strings', i found:

'''
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
'''

So, trying the passwords one by one:

'''
$ ./binaary50 Masternamer
3cd50c6be9bbede06e51741928d88b7e
'''


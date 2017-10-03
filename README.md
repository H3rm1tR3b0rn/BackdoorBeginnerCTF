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

##2013-web-50

The proglem give a link: http://hack.bckdr.in/2013-WEB-50/getflag.php  


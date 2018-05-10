# hooker_ZIP_password

## Description:
Microsoft in Windows 10, for user-friendly I think, released new functionality for encrypted zip files. When you open one time encrypted ZIP file, Windows 10 saves the password in the memory. When you will try to open again this ZIP file, Windows 10 will take the path of the file, search in the memory real path of last open ZIP files, and if he will found ZIP-password couple then he will try to open the encrypted ZIP file. 

I saw that if you will try to hook SHUnicodeToAnsi function from ShLwApi.dll in ZIP opening time, then you can know the password of an encrypted ZIP file. 

The passwords stored in explorer.exe memory.

![](https://github.com/vah13/hooker_ZIP_password/blob/master/hook2.gif)

## Windows 10 version
```
OS Name:                   Майкрософт Windows 10 Pro
OS Version:                10.0.17134 N/A Build 17134
explorer.exe               10.0.17134.1
```

## TODO

Need to 
1. Get all ZIP files paths from explorer.exe memory and extract passwords
2. Analyze password storage

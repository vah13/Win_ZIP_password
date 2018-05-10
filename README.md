# Win_ZIP_password

## Description:
Here's an updated description:

With Windows 10, Microsoft added a new feature for encrypted ZIP files to increase user-friendliness. When you open an encrypted ZIP file, Windows 10 saves the password to memory. When you try to open the same ZIP file again, Windows takes the file path, searches the memory and will use the stored password.

I saw that if you hook SHUnicodeToAnsi from ShLwApi.dll while opening a ZIP, you can see the password of the encrypted ZIP file.

![](https://github.com/vah13/hooker_ZIP_password/blob/master/hook2.gif)
(https://raw.githubusercontent.com/vah13/Win_ZIP_password/master/hook2.gif)

## Windows 10 version
```
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.17134 N/A Build 17134
explorer.exe               10.0.17134.1
```

## TODO

Need to 
1. Get all ZIP files paths from explorer.exe and extract passwords
2. Analyze password storage (**because if you kill explorer.exe process and run it, the method works**)

## Useful for
CTF/Forensic

## Thank you
https://twitter.com/NewFranny
https://www.reddit.com/user/TheMooligan101

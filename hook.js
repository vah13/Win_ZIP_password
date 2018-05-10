var hndl;
hndl = Module.findExportByName("ShLwApi.dll", "SHUnicodeToAnsi"); 
//find  SHUnicodeToAnsi function from  ShLwApi.dll DLL
// hooked function has this view - SHUnicodeToAnsi("password",0x11bedee4,260) , where  args[0] = password
Interceptor.attach(hndl, {
    onEnter: function(args) {
        console.log("[!] Hooked SHUnicodeToAnsi function")
        console.log( Memory.readUtf16String(args[0])) // getting password
    }
});

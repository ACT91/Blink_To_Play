from pynput.keyboard import Key, Controller

keyboard = Controller()

def press_ctrl_key(key):
    keyboard.press(Key.ctrl)
    keyboard.press(key)
    keyboard.release(key)
    keyboard.release(Key.ctrl)

def play_pause():
    press_ctrl_key('p')

def next_track():
    press_ctrl_key('f')

def prev_track():
    press_ctrl_key('b')

def seek_forward():
    press_ctrl_key(Key.right)

def seek_backward():
    press_ctrl_key(Key.left)

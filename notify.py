__module_name__='Notify'
__module_description__='Notification through notify-send'
__module_author__='AdGold'
__module_version__='1.0'

import os
import xchat

def notify(title, msg, icon='/home/adrian/scripts/Xchat-notify/Xchat-icon.png'):
    os.system('notify-send %r %r -i %s' % (title, msg, icon))

def hilight_callback(word, word_eol, userdata):
    notify('Xchat: Highlight - ' + word[0], word[1])

def pm_callback(word, word_eol, userdata):
    notify('Xchat: Private Message - ' + word[0], word[1])

def test_callback(word, word_eol, userdata):
    print(word, word_eol, userdata)
    notify('Xchat: Private Message - ' + word[0], word[1])

xchat.hook_print("Channel Msg Hilight", hilight_callback)
xchat.hook_print("Channel Action Hilight", hilight_callback)
xchat.hook_print("Private Message to Dialog", pm_callback)
xchat.hook_print("Private Action to Dialog", pm_callback)
#xchat.hook_print("Channel Message", test_callback)

print(__module_name__ + ' version ' + __module_version__ + ' loaded.')

import keyboard
import webbrowser


while True:
    event = keyboard.read_event()

    if (event == keyboard.KeyboardEvent(scan_code=keyboard.key_to_scan_codes('q')[0], event_type=keyboard.KEY_DOWN)):
        exit()
    if (event == keyboard.KeyboardEvent(scan_code=keyboard.key_to_scan_codes('home')[0], event_type=keyboard.KEY_DOWN)):            
        webbrowser.open_new_tab('https://web.whatsapp.com/')
        webbrowser.open_new_tab('https://www.twitch.tv/')
        webbrowser.open_new_tab('https://www.youtube.com/?hl=es&gl=ES')




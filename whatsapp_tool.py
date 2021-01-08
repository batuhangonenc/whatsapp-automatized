def sendmsg():
    import os, sys
    from datetime import datetime

    print("\npackage-installation-section-start\n")
    ct = 0
    try:
        import webbrowser, time, re, pyautogui
        from pynput.keyboard import Key, Controller
    except:
        try:
            os.system("pip3 install pynput")
            os.system("pip3 install pyautogui")
            ct += 1
            from pynput.keyboard import Key, Controller

        except:
            os.system("pip install pynput")
            os.system("pip install pyautogui")
            ct += 1
            from pynput.keyboard import Key, Controller


    print(f"\npackage-installation-section-end\n{ct} packages downloaded.\n")

    keyboard = Controller()

    pattern = r"^\+[0-9]{1,3} [0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]$"

    while 1:
        phone = input("phone number (ex. +90 000 000 00 00):")
        
        match = re.match(pattern, phone)

        if match:
            break

        print("unvalid format\n\n")


    text = input("text :")

    pattern = r"^[0-9][0-9] : [0-9][0-9]$"

    while 1:

        timing = input("time (ex. 16 : 32):")
    
        match = re.match(pattern, timing)

        if match:
            break

        print("-\nunvalid format\n-")


    url = f"https://web.whatsapp.com/send?phone={phone}&text={text}"
    
    oldx, oldy = pyautogui.position()
    loopcounter = 0
    flag = 0
    while 1:
        if flag == 1:
            keyboard.release(Key.enter)
            sys.exit()

        thetime = datetime.now().strftime("%H : %M")

        if loopcounter % 300000 == 0:
            print(f"---\ncurrent -- > {thetime} |target --> {timing}")


        if thetime == timing :

            oldx, oldy = pyautogui.position()
            webbrowser.open(url)
            time.sleep(15)

            while 1:

                newx, newy = pyautogui.position()

                if newx == oldx and newy == oldy:
                    break

                webbrowser.open(url)
                time.sleep(15)

                oldx, oldy = newx, newy    

            keyboard.press(Key.enter)
            flag = 1

        loopcounter += 1    
    
sendmsg()

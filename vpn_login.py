import subprocess
import time

client_title = 'Cisco AnyConnect Secure Mobility Client'
login_title = 'Cisco AnyConnect Login'

subprocess.Popen(['/opt/cisco/anyconnect/bin/vpnui'])
try:
    # Activate client window
    if not window.wait_for_exist(client_title, timeOut=5):
        raise Exception(f"Opening window {client_title} timed out")
    window.activate(client_title)

    # Click on connect button
    mouse.click_relative(224, 448, 1)

    # Activate login window
    if not window.wait_for_exist(login_title, timeOut=5):
        raise Exception(f"Opening window {login_title} timed out")
    window.activate(login_title)

    # Wait for window to finish loading
    time.sleep(3)

    # Fill in Username
    mouse.click_relative(420, 265, 1)
    keyboard.send_keys("USERNAME")
    time.sleep(.1)

    # Fill in Password
    mouse.click_relative(420, 335, 1)
    keyboard.send_keys("PASSWORD")
    time.sleep(.1)

    # Click on Login button
    mouse.click_relative(420, 395, 1)

except BaseException as err:
    dialog.info_dialog('AutoKey Error', f'AutoKey script exception: "{err}"')

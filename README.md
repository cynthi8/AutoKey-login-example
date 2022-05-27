# AutoKey-login-example
Example of using AutoKey to automatically fill fields in a GUI.

There may be better ways to do this.

### Demo
https://user-images.githubusercontent.com/71356003/170627362-1a7d487f-14b6-4b9e-b164-d29833b7986b.mov

### Installation
1. Install [AutoKey](https://github.com/autokey/autokey)
2. Copy *get_mouse_location.py* and *vpn_login.py* to a folder managed by AutoKey. I use *~/.config/autokey/data/CustomScripts/*
3. Modify *vpn_login.py* with your login info and button coordinates (found from *get_mouse_location.py*)
4. Run `autokey-run -s "vpn_login"`

### Caveats
This will store your username + password in plain text, easily accessible to anyone with access to your files. So, keep that in mind.

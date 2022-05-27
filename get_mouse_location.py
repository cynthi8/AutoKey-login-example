from Xlib import display

d = display.Display().screen().root.query_pointer()
x = d.root_x
y = d.root_y

win_title = window.get_active_title()
win_x, win_y, _, _ = window.get_active_geometry()

dialog.info_dialog("Mouse Info",
                   f"Absolute Mouse Location: ({x}, {y})\n"
                   f"Relative to Active Window ({win_title}): ({x-win_x}, {y-win_y})\n")

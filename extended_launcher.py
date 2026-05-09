"""
Add apps to your Launcher!
Just append the commands below to your boot.py. Any parameter can be omitted):

import extended_launcher as launcher, lvgl as lv

launcher.add_text( index = 1, label = 'My Apps', label_color = lv.PALETTE.GREEN)
launcher.add_app( index = 2, label = 'Doom', path = 'doom.py', symbol = lv.SYMBOL.PLAY, symbol_color = lv.PALETTE.RED, label_color = lv.PALETTE.ORANGE)
launcher.add_text( index = 3, label = "System")
launcher.set_height(500)

Created by Laszlo Andras Halak / kreativkodok (v1.0 2026.05)
"""

import sequencer
import ui
import tulip
import lvgl as lv


button_holder = None
override_height = -1

entries = []

class Launcher_Entry:
    def __init__( self, index = 1, path = '',symbol=lv.SYMBOL.NEW_LINE, label="", symbol_color = lv.PALETTE.TEAL, label_color = None, is_separator = False):
        self.path = path
        self.symbol = symbol
        self.label = label
        self.symbol_color = symbol_color
        self.label_color = symbol_color if label_color is None else label_color
        self.index = index
        self.is_separator = is_separator


def check_launcher(_):
    def inject_entries(event):
        if ui.lv_launcher is None:
            return
        for entry in entries:
            if not entry.is_separator:
                button = ui.lv_launcher.add_button(entry.symbol, entry.label)
                button.get_child(0).set_style_text_color(lv.palette_main(entry.symbol_color),0)
                button.get_child(1).set_style_text_color(lv.palette_main(entry.label_color),0)
                button.move_to_index(entry.index)
                button.add_event_cb(lambda e: tulip.run(entry.path), lv.EVENT.CLICKED, None) 
            else:
                label = ui.lv_launcher.add_text(entry.label)
                label.set_style_text_color(lv.palette_main(entry.label_color),0)
                label.move_to_index(entry.index)
        if override_height > 0:
            ui.lv_launcher.set_height(override_height)
    
    global button_holder
    if ui.repl_screen.launcher_button is not None and ui.repl_screen.launcher_button != button_holder:
        button_holder = ui.repl_screen.launcher_button
        ui.repl_screen.launcher_button.add_event_cb(lambda e: inject_entries(e), lv.EVENT.CLICKED, None) 
    if ui.lv_launcher is not None and override_height > 0:
        ui.lv_launcher.set_height(override_height)
 
    
def add_app(index = 1, path = '', symbol=lv.SYMBOL.NEW_LINE, label="", symbol_color = lv.PALETTE.TEAL, label_color = None):
    entries.append(Launcher_Entry(index, path, symbol, label, symbol_color, label_color))

def add_text(index = 1, label = "_____", label_color = lv.PALETTE.TEAL):
    entries.append(Launcher_Entry(index = index, label = label, label_color = label_color, is_separator = True))
    
def set_height(height):
    global override_height
    override_height = height
    
seq = sequencer.TulipSequence(2,check_launcher)
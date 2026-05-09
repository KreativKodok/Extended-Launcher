# Extended Launcher for your [Tulip Creative Computer](https://tulip.computer/)
<img width="1100" height="644" alt="image" src="https://github.com/user-attachments/assets/4a1d0e1d-bc23-4694-be49-f26afb99a2b2" />
<br>

## How to use:
1. Download from [releases](https://github.com/KreativKodok/Extended-Launcher/releases) or from Tulip World with the following command:
```
world.download('extended_launcher.py', 'kreativkodok')
```
2. Import it into your `boot.py`
```
import extended_launcher as launcher, lvgl as lv
```
3. Use the following commands to your hearts delight. Any parameter can be omitted.
```
#Increases the height of the launcher
launcher.set_height(500)

#Adds a label below the 'Close' button
launcher.add_text( index = 1, label = 'My Apps', label_color = lv.PALETTE.ORANGE)

#Adds a button to execute yur chosen app
launcher.add_app( index = 2, label = 'Bulb File Explorer', path = 'bulb.py', symbol = lv.SYMBOL.EYE_OPEN, symbol_color = lv.PALETTE.TEAL, label_color = lv.PALETTE.TEAL)

#Adds a label above the preinstalled Systen apps
launcher.add_text( index = 3, label = "System")
```


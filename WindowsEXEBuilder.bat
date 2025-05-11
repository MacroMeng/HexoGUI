pyinstaller HexoGUI.py ^
            --onefile ^
            -n HexoGUI ^
            --add-data ./HarmonyOS_Sans_SC_Regular.ttf;. ^
            --add-data ./JetBrainsMapleMono-Regular.ttf;. ^
            --add-data ./ICOs.ico;. ^
            --splash "loading.png" ^
            --noconsole ^
            --icon "./ICOs.ico"
@pause
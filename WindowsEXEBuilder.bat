pyinstaller HexoGUI.py ^
            --onefile ^
            -n HexoGUI ^
            --add-data "./HarmonyOS_Sans_SC_Regular.ttf:." ^
            --add-data "JetBrainsMapleMono-Regular.ttf:." ^
            --add-data "./ICONs.ico:." ^
            --collect-all pyglet ^
            --collect-all sv_ttk ^
            --collect-all darkdetect ^
            --splash "loading.png" ^
            --noconsole ^
            --icon ICOs.ico
@pause
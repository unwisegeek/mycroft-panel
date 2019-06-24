# mycroft-panel
A panel application to interact with the Mycroft Assistant

Purpose
-------

This program was written so John the Unwise Geek could learn how to create Qt-based programs.

It's also useful to communicate with an installation of Mycroft when a microphone is unavail-
able or inadvisable, or when the user themselves is non-verbal for any given reason. As the
author is verbal, any suggestions for how this aspect of the program can be improved are most
welcome.

Features
--------

* Keyboard Interaction with Mycroft
* Audio Controls (see Known Issues)
* Six Custom Keys
* Configurable Mycroft URI

Requirements
------------

Mycroft    - https://mycroft.ai
PyQt5      - pip3 install pyqt5
Websockets - pip3 install websockets
YAML       - pip3 install yaml

Tested primarily in KDE Neon and Ubuntu MATE 19.04, theoretically multi-platform.

Operation
---------

To run, start mycroft-panel.py in your favorite python3 intepreter. A file called .mycroft-panel
will be created in your user home directory to save your custom button commands. Type text in
the text box as you would say it to Mycroft. To add custom commands and change the address of
the Mycroft listener, click the "..." button.

Known Issues
------------

Mycroft sometimes loses track of Spotify when it comes to the play button. If this happens, simply
tell Mycroft to "play spotify" and it should get right back to work.

Issues and Suggestions
----------------------

Please report all issues to the github repository at https://github.com/unwisegeek/mycroft-panel

Please use the 'bug' label for issues and the 'enhancement' label for suggestions and requests
for features.

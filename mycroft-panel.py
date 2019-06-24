#!/usr/bin/python3
# Have you read your README today?

import sys
import os
import yaml
from websocket import WebSocket
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog

from ui_MainWin import Ui_MainWindow
from ui_Config import Ui_Config

# Variables of a Utilitarian Nature

configFile = os.path.expanduser("~") + "/.mycroft-panel"

# Variables of a Silly Nature

swedishChef = "bjork bjork bjork smash"


# Load Configuration File or Create Configuration File at ~/.mycroft-panel
def load_config():
    if os.path.isfile(configFile):
        panel_config = yaml.safe_load(open(configFile, "r"))
    else:
        panel_config = {
            "customButton6": ["Custom6", "Custom Command 6"],
            "customButton5": ["Custom5", "Custom Command 5"],
            "customButton4": ["Custom4", "Custom Command 4"],
            "customButton3": ["Custom3", "Custom Command 3"],
            "customButton2": ["Custom2", "Custom Command 2"],
            "customButton1": ["Custom1", "Custom Command 1"],
            "uri": "localhost"}
        yaml.safe_dump(panel_config, open(configFile, "w+"))
    return panel_config


def send_message(msg_type, data):
    panel_config = load_config()
    ws = WebSocket()
    ws.connect("ws://" + panel_config['uri'][0] + "/core")
    message = '{"type": "' + msg_type + '", "data":' + data + '}'
    ws.send(message)
    ws.recv()
    ws.close()


class ConfigWindow(QDialog, Ui_Config):
    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__(parent)
        self.setupUi(self)

        # Put Configuration Variables Into Place

        panel_config = load_config()
        self.lineURI.setText(panel_config['uri'][0])
        self.button1Name.setText(panel_config['customButton1'][0])
        self.button2Name.setText(panel_config['customButton2'][0])
        self.button3Name.setText(panel_config['customButton3'][0])
        self.button4Name.setText(panel_config['customButton4'][0])
        self.button5Name.setText(panel_config['customButton5'][0])
        self.button6Name.setText(panel_config['customButton6'][0])

        self.button1Command.setText(panel_config['customButton1'][1])
        self.button2Command.setText(panel_config['customButton2'][1])
        self.button3Command.setText(panel_config['customButton3'][1])
        self.button4Command.setText(panel_config['customButton4'][1])
        self.button5Command.setText(panel_config['customButton5'][1])
        self.button6Command.setText(panel_config['customButton6'][1])

        self.okButton.clicked.connect(self.write_configuration)

        self.cancelButton.clicked.connect(self.close)

    def show(self):
        self.conf_window.show()

    def write_configuration(self):
        panel_config = load_config()
        panel_config['uri'] = [self.lineURI.text()]
        panel_config['customButton1'] = [self.button1Name.text(), self.button1Command.text()]
        panel_config['customButton2'] = [self.button2Name.text(), self.button2Command.text()]
        panel_config['customButton3'] = [self.button3Name.text(), self.button3Command.text()]
        panel_config['customButton4'] = [self.button4Name.text(), self.button4Command.text()]
        panel_config['customButton5'] = [self.button5Name.text(), self.button5Command.text()]
        panel_config['customButton6'] = [self.button6Name.text(), self.button6Command.text()]
        yaml.safe_dump(panel_config, open(configFile, "w+"))
        self.close()


def audio_button_clicked(command):
    if command == "play":
        msg_type = "recognizer_loop:utterance"
        data = '{"utterances": ["' + command + '"]}'
    else:
        msg_type = "mycroft.audio.service." + command
        data = "{}"
    send_message(msg_type, data)


def custom_button_clicked(num):
    panel_config = load_config()
    msg_type = "recognizer_loop:utterance"
    if "Custom Command" in panel_config[num][1]:
        data = '{"utterances": ["say Please enter the configuration panel and assign a command to this button."]}'
    else:
        data = '{"utterances": ["' + panel_config[num][1] + '"]}'
    send_message(msg_type, data)


def on_cancel_button_clicked():
    sys.exit(0)


class MainWindow:
    def __init__(self):
        panel_config = load_config()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Connect signals to slots
        # Send Button
        self.ui.sendButton.clicked.connect(self.on_send_button_clicked)
        self.ui.sendButton.setAutoDefault(True)

        # Config Button
        self.ui.configButton.clicked.connect(self.on_config_button_clicked)

        # Audio Buttons
        self.ui.audioPrevButton.clicked.connect(lambda: audio_button_clicked("prev"))
        self.ui.audioPauseButton.clicked.connect(lambda: audio_button_clicked("pause"))
        self.ui.audioPlayButton.clicked.connect(lambda: audio_button_clicked("play"))
        self.ui.audioNextButton.clicked.connect(lambda: audio_button_clicked("next"))

        self.load_buttons()

        self.ui.customButton1.clicked.connect(lambda: custom_button_clicked("customButton1"))
        self.ui.customButton2.clicked.connect(lambda: custom_button_clicked("customButton2"))
        self.ui.customButton3.clicked.connect(lambda: custom_button_clicked("customButton3"))
        self.ui.customButton4.clicked.connect(lambda: custom_button_clicked("customButton4"))
        self.ui.customButton5.clicked.connect(lambda: custom_button_clicked("customButton5"))
        self.ui.customButton6.clicked.connect(lambda: custom_button_clicked("customButton6"))

        # Exit Button
        self.ui.exitButton.clicked.connect(on_cancel_button_clicked)

        # Text Bar
        self.ui.lineEdit.returnPressed.connect(self.ui.sendButton.click)

        # Status Bar
        self.ui.statusbar.showMessage("Mycroft: " + panel_config['uri'][0])

    def refresh(self):
        self.main_win.repaint()

    def show(self):
        self.main_win.show()

    def load_buttons(self):
        # Custom Buttons
        panel_config = load_config()
        self.ui.customButton1.setText(panel_config['customButton1'][0])
        self.ui.customButton2.setText(panel_config['customButton2'][0])
        self.ui.customButton3.setText(panel_config['customButton3'][0])
        self.ui.customButton4.setText(panel_config['customButton4'][0])
        self.ui.customButton5.setText(panel_config['customButton5'][0])
        self.ui.customButton6.setText(panel_config['customButton6'][0])
        self.ui.statusbar.showMessage("Mycroft: " + panel_config['uri'][0])

    def on_send_button_clicked(self):
        text_input = self.ui.lineEdit.text()
        msg_type = "recognizer_loop:utterance"
        data = '{"utterances": ["' + text_input + '"]}'
        send_message(msg_type, data)
        self.ui.lineEdit.selectAll()
        self.ui.lineEdit.setFocus()

    def on_config_button_clicked(self):
        child_win = ConfigWindow()
        child_win.exec_()
        self.load_buttons()
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

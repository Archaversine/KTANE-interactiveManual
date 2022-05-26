#!/usr/bin/python3
import os
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = os.path.join(PROJECT_PATH, "manual.ui")

MORSE_CODE_DICT = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

MORSE_MATCHES = {
    "SHELL":  "3.505 MHz",
    "HALLS":  "3.515 MHz",
    "SLICK":  "3.522 MHz",
    "TRICK":  "3.532 MHz",
    "BOXES":  "3.535 MHz",
    "LEAKS":  "3.542 MHz",
    "STROBE": "3.545 MHz",
    "BISTRO": "3.552 MHz",
    "FLICK":  "3.555 MHz",
    "BOMBS":  "3.565 MHz",
    "BREAK":  "3.572 MHz",
    "BRICK":  "3.575 MHz",
    "STEAK":  "3.582 MHz",
    "STING":  "3.592 MHz",
    "VECTOR": "3.595 MHz",
    "BEATS":  "3.600 MHz",
}

COMPLEX_WIRES_VALUES = [
    "Cut.",
    "Don't cut.",
    "Cut.",
    "Cut if >= 2 batteries.",
    "Cut if last serial digit even.",
    "Cut if parallel port.",
    "Don't cut.",
    "Cut if parallel port.",
    "Cut if last serial digit even.",
    "Cut if >= 2 batteries.",
    "Cut.",
    "Cut if >= 2 batteries.",
    "Cut if last serial digit even.",
    "Cut if last serial digit even.",
    "Cut if parallel port.",
    "Dont' cut"
]

RED_WIRE_OCCURENCES = [
    "C",
    "B",
    "A",
    "AC",
    "B",
    "AC",
    "ABC",
    "AB",
    "B"
]

BLUE_WIRE_OCCURENCES = [
    "B",
    "AC",
    "B",
    "A",
    "B",
    "BC",
    "C",
    "AC",
    "A"
]

BLACK_WIRE_OCCURENCES = [
    "ABC",
    "AC",
    "B",
    "AC",
    "B",
    "BC",
    "AB",
    "C",
    "C"
]

PASSWORDS = [
    "ABOUT", "AFTER", "AGAIN", "BELOW", "COULD",
    "EVERY", "FIRST", "FOUND", "GREAT", "HOUSE",
    "LARGE", "LEARN", "NEVER", "OTHER", "PLACE",
    "PLANT", "POINT", "RIGHT", "SMALL", "SOUND",
    "SPELL", "STILL", "STUDY", "THEIR", "THERE",
    "THESE", "THING", "THINK", "THREE", "WATER",
    "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"
]

class ManualApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()

        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        self.mainwindow = builder.get_object("toplevel1", master)

        self._init_wire_vars(master)
        self._init_bigButton_vars(master)
        self._init_morseCode_vars(master)
        self._init_complicatedWires_vars(master)
        self._init_wireSequences_vars(master)
        self._init_passwords_vars(master)

        builder.connect_callbacks(self)

    def _init_wire_vars(self, master) -> None:
        self.checkbox_wires_serialOdd = self.builder.get_object("checkbox_wires_serialOdd", master)
        self.entry_wires_wireCombo = self.builder.get_object("entry_wires_wireCombo", master)
        self.label_wires_output = self.builder.get_object("label_wires_output", master)

        # Set checkbox state to false
        for i in range(2):
            self.checkbox_wires_serialOdd.invoke()

    def _init_bigButton_vars(self, master) -> None:
        self.spinbox_bigButton_batteryc = self.builder.get_object("spinbox_bigButton_batteryc", master)
        self.checkbox_bigButton_FRK = self.builder.get_object("checkbox_bigButton_FRK", master)
        self.checkbox_bigButton_CAR = self.builder.get_object("checkbox_bigButton_CAR", master)
        self.label_bigButton_output = self.builder.get_object("label_bigButton_output", master)

        # Set checkbox states to false
        for i in range(2):
            self.checkbox_bigButton_FRK.invoke()
            self.checkbox_bigButton_CAR.invoke()

    def _init_morseCode_vars(self, master) -> None:
        self.entry_morseCode_input = self.builder.get_object("entry_morseCode_input", master)
        self.treeview_morseCode_matches = self.builder.get_object("treeview_morseCode_matches", master)

        self.treeview_morseCode_matches['columns'] = ("deciphered", "match", "frequency")
        self.treeview_morseCode_matches.column("#0", width=25, stretch=tk.NO)
        self.treeview_morseCode_matches.column("deciphered", width=95, stretch=tk.NO)
        self.treeview_morseCode_matches.column("match", width=65, stretch=tk.NO)
        self.treeview_morseCode_matches.column("frequency", width=100, stretch=tk.NO)

        self.treeview_morseCode_matches.heading("deciphered", text="Deciphered")
        self.treeview_morseCode_matches.heading("match", text="Match")
        self.treeview_morseCode_matches.heading("frequency", text="Frequency")

    def _init_complicatedWires_vars(self, master) -> None:
        self.checkbox_complicatedWires_red = self.builder.get_object("checkbox_complicatedWires_red", master)
        self.checkbox_complicatedWires_blue = self.builder.get_object("checkbox_complicatedWires_blue", master)
        self.checkbox_complicatedWires_star = self.builder.get_object("checkbox_complicatedWires_star", master)
        self.checkbox_complicatedWires_LED = self.builder.get_object("checkbox_complicatedWires_LED", master)
        self.label_complicatedWires_output = self.builder.get_object("label_complicatedWires_output", master)

        # Initialize checkboxes to false
        for i in range(2):
            self.checkbox_complicatedWires_red.invoke()
            self.checkbox_complicatedWires_blue.invoke()
            self.checkbox_complicatedWires_star.invoke()
            self.checkbox_complicatedWires_LED.invoke()

    def _init_wireSequences_vars(self, master) -> None:
        self.spinbox_wireSequences_reds = self.builder.get_object("spinbox_wireSequences_reds", master)
        self.spinbox_wireSequences_blues = self.builder.get_object("spinbox_wireSequences_blues", master)
        self.spinbox_wireSequences_blacks = self.builder.get_object("spinbox_wireSequences_blacks", master)
        self.entry_wireSequences_wireSymbol = self.builder.get_object("entry_wireSequences_wireSymbol", master)
        self.label_wireSequences_output = self.builder.get_object("label_wireSequences_output", master)

    def _init_passwords_vars(self, master) -> None:
        self.entry_passwords_first = self.builder.get_object("entry_passwords_first", master)
        self.entry_passwords_second = self.builder.get_object("entry_passwords_second", master)
        self.entry_passwords_third = self.builder.get_object("entry_passwords_third", master)
        self.treeview_passwords = self.builder.get_object("treeview_passwords", master)

        self.treeview_passwords['columns'] = ("match")
        self.treeview_passwords.column("#0", width=25, stretch=tk.NO)
        self.treeview_passwords.column("match", width=65)

        self.treeview_passwords.heading("match", text="Match")

    def _is_valid_bigButton_color(self, color: str) -> bool:
        return color in ("RED", "BLUE", "YELLOW", "WHITE", "BLACK")

    def run(self) -> None:
        self.mainwindow.mainloop()

    def cmd_symbols(self) -> None:
        os.system("xdg-open ./symbols.png")

    def cmd_simon_says(self) -> None:
        os.system("xdg-open ./simon-says.png")

    def cmd_whos_on_first1(self) -> None:
        os.system("xdg-open ./whos-on-first1.png")

    def cmd_whos_on_first2(self) -> None:
        os.system("xdg-open ./whos-on-first2.png")

    def cmd_memory(self) -> None:
        os.system("xdg-open ./memory.png")

    def cmd_mazes(self) -> None:
        os.system("xdg-open ./maze.png")

    def cmd_knob(self) -> None:
        os.system("xdg-open ./knob.png")

    def button_wires_red(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "R")

    def button_wires_yellow(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "Y")

    def button_wires_blue(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "U")

    def button_wires_white(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "W")

    def button_wires_green(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "G")

    def button_wires_black(self) -> None:
        self.entry_wires_wireCombo.insert(len(self.entry_wires_wireCombo.get()), "K")

    def button_wires_clear(self) -> None:
        self.label_wires_output["text"] = "???"
        self.entry_wires_wireCombo.delete(0, len(self.entry_wires_wireCombo.get()))

        if 'selected' in self.checkbox_wires_serialOdd.state():
            self.checkbox_wires_serialOdd.invoke()

    def button_wires_process(self) -> None:
        text = self.entry_wires_wireCombo.get().upper()
        length = len(text)

        serialOdd = 'selected' in self.checkbox_wires_serialOdd.state()

        if length < 3:
            self.label_wires_output["text"] = "Not enough wires."
        elif length > 6:
            self.label_wires_output["text"] = "Too many wires."
        
        if length == 3:
            if not 'R' in text:
                self.label_wires_output["text"] = "Cut the second wire."
            elif text[-1] == 'W':
                self.label_wires_output["text"] = "Cut the last wire."
            elif text.count('U') > 1:
                self.label_wires_output["text"] = "Cut the last blue wire."
            else:
                self.label_wires_output["text"] = "Cut the last wire."

        elif length == 4:
            if text.count('R') > 1 and serialOdd:
                self.label_wires_output["text"] = "Cut the last red wire."
            elif text[-1] == 'Y' and not 'R' in text:
                self.label_wires_output["text"] = "Cut the first wire."
            elif text.count('U') == 1:
                self.label_wires_output["text"] = "Cut the first wire."
            elif text.count('Y') > 1:
                self.label_wires_output["text"] = "Cut the last wire."
            else:
                self.label_wires_output["text"] = "Cut the second wire."

        elif length == 5:
            if text[-1] == 'K' and serialOdd:
                self.label_wires_output["text"] = "Cut the fourth wire."
            elif text.count('R') == 1 and text.count('Y') > 1:
                self.label_wires_output["text"] = "Cut the first wire."
            elif not 'K' in text:
                self.label_wires_output["text"] = "Cut the second wire."
            else:
                self.label_wires_output["text"] = "Cut the first wire."

        elif length == 6:
            if not 'Y' in text and serialOdd:
                self.label_wires_output["text"] = "Cut the third wire."
            elif text.count('Y') == 1 and text.count('W') > 1:
                self.label_wires_output["text"] = "Cut the fourth wire."
            elif not 'R' in text:
                self.label_wires_output["text"] = "Cut the last wire."
            else:
                self.label_wires_output["text"] = "Cut the fourth wire."

    def _button_bigButton_setSuffix(self, suffix: str) -> None:
        text = self.label_bigButton_output['text']

        if '-' in text:
            if not self._is_valid_bigButton_color(text[:text.find('-')]):
                return

            self.label_bigButton_output['text'] = text[:text.find('-') + 1] + suffix
        else:
            if not self._is_valid_bigButton_color(text):
                return

            self.label_bigButton_output['text'] += '-' + suffix

    def button_bigButton_red(self) -> None:
        self.label_bigButton_output["text"] = "RED"

    def button_bigButton_blue(self) -> None:
        self.label_bigButton_output["text"] = "BLUE"

    def button_bigButton_yellow(self) -> None:
        self.label_bigButton_output["text"] = "YELLOW"

    def button_bigButton_white(self) -> None:
        self.label_bigButton_output["text"] = "WHITE"

    def button_bigButton_black(self) -> None:
        self.label_bigButton_output["text"] = "BLACK"

    def button_bigButton_abort(self) -> None:
        self._button_bigButton_setSuffix("ABORT")

    def button_bigButton_detonate(self) -> None:
        self._button_bigButton_setSuffix("DETONATE")

    def button_bigButton_hold(self) -> None:
        self._button_bigButton_setSuffix("HOLD")

    def button_bigButton_press(self) -> None:
        self._button_bigButton_setSuffix("PRESS")

    def button_bigButton_clear(self) -> None:
        self.label_bigButton_output['text'] = '???'
        self.spinbox_bigButton_batteryc.set(0)

        if 'selected' in self.checkbox_bigButton_FRK.state():
            self.checkbox_bigButton_FRK.invoke()
        if 'selected' in self.checkbox_bigButton_CAR.state():
            self.checkbox_bigButton_CAR.invoke()

    def button_bigButton_process(self) -> None:
        text = self.label_bigButton_output['text']

        if not '-' in text:
            return

        color = text[:text.find('-')]
        label = text[text.find('-') + 1:]

        if color == "BLUE" and label == "ABORT":
            self.label_bigButton_output['text'] = '[HOLD]'
        elif int(self.spinbox_bigButton_batteryc.get()) > 1 and label == "DETONATE":
            self.label_bigButton_output['text'] = '[PRESS & RELEASE]'
        elif color == 'WHITE' and 'selected' in self.checkbox_bigButton_CAR.state():
            self.label_bigButton_output['text'] = '[HOLD]'
        elif int(self.spinbox_bigButton_batteryc.get()) > 2 and 'selected' in self.checkbox_bigButton_FRK.state():
            self.label_bigButton_output['text'] = '[PRESS & RELEASE]'
        elif color == 'YELLOW':
            self.label_bigButton_output['text'] = '[HOLD]'
        elif color == 'RED' and label == 'HOLD':
            self.label_bigButton_output['text'] = '[PRESS & RELEASE]'
        else:
            self.label_bigButton_output['text'] = '[HOLD]'

    def update_entry_morseCode_input(self, stuff) -> None:
        text = self.entry_morseCode_input.get()

        # Empty tree
        for child in self.treeview_morseCode_matches.get_children():
            self.treeview_morseCode_matches.delete(child)

        if len(text) == 0:
            return

        string = ''

        for pattern in text.split():
            if not pattern in MORSE_CODE_DICT.keys():
                return
            string += MORSE_CODE_DICT[pattern]

        for word in MORSE_MATCHES.keys():
            if word.startswith(string):
                self.treeview_morseCode_matches.insert('', len(self.treeview_morseCode_matches.get_children()), values=(string, word, MORSE_MATCHES[word]))

    def button_complicatedWires_clear(self) -> None:
        if 'selected' in self.checkbox_complicatedWires_LED.state():
            self.checkbox_complicatedWires_LED.invoke()

        if 'selected' in self.checkbox_complicatedWires_star.state():
            self.checkbox_complicatedWires_star.invoke()

        if 'selected' in self.checkbox_complicatedWires_blue.state():
            self.checkbox_complicatedWires_blue.invoke()

        if 'selected' in self.checkbox_complicatedWires_red.state():
            self.checkbox_complicatedWires_red.invoke()

        self.label_complicatedWires_output['text'] = '???'


    def button_complicatedWires_process(self) -> None:
        index = 0;

        if 'selected' in self.checkbox_complicatedWires_LED.state():
            index += 1

        if 'selected' in self.checkbox_complicatedWires_star.state():
            index += 2

        if 'selected' in self.checkbox_complicatedWires_blue.state():
            index += 4

        if 'selected' in self.checkbox_complicatedWires_red.state():
            index += 8

        self.label_complicatedWires_output['text'] = COMPLEX_WIRES_VALUES[index]

    def button_wireSequences_reset(self) -> None:
        self.spinbox_wireSequences_reds.set(0)
        self.spinbox_wireSequences_blues.set(0)
        self.spinbox_wireSequences_blacks.set(0)

        self.entry_wireSequences_wireSymbol.delete(0, len(self.entry_wireSequences_wireSymbol.get()))
        self.label_wireSequences_output['text'] = '???'

    def button_wireSequences_red(self) -> None:
        self.entry_wireSequences_wireSymbol.delete(0, len(self.entry_wireSequences_wireSymbol.get()))
        self.entry_wireSequences_wireSymbol.insert(len(self.entry_wireSequences_wireSymbol.get()), 'R')
        self.label_wireSequences_output['text'] = '???'

    def button_wireSequences_blue(self) -> None:
        self.entry_wireSequences_wireSymbol.delete(0, len(self.entry_wireSequences_wireSymbol.get()))
        self.entry_wireSequences_wireSymbol.insert(len(self.entry_wireSequences_wireSymbol.get()), 'U')
        self.label_wireSequences_output['text'] = '???'

    def button_wireSequences_black(self) -> None:
        self.entry_wireSequences_wireSymbol.delete(0, len(self.entry_wireSequences_wireSymbol.get()))
        self.entry_wireSequences_wireSymbol.insert(len(self.entry_wireSequences_wireSymbol.get()), 'K')
        self.label_wireSequences_output['text'] = '???'

    def button_wireSequences_A(self) -> None:
        self.label_wireSequences_output['text'] = '???'

        if len(self.entry_wireSequences_wireSymbol.get()) == 1:
            self.entry_wireSequences_wireSymbol.insert(2, 'A')
        elif len(self.entry_wireSequences_wireSymbol.get()) == 2:
            self.entry_wireSequences_wireSymbol.delete(1, 2)
            self.entry_wireSequences_wireSymbol.insert(2, 'A')

    def button_wireSequences_B(self) -> None:
        self.label_wireSequences_output['text'] = '???'

        if len(self.entry_wireSequences_wireSymbol.get()) == 1:
            self.entry_wireSequences_wireSymbol.insert(2, 'B')
        elif len(self.entry_wireSequences_wireSymbol.get()) == 2:
            self.entry_wireSequences_wireSymbol.delete(1, 2)
            self.entry_wireSequences_wireSymbol.insert(2, 'B')

    def button_wireSequences_C(self) -> None:
        self.label_wireSequences_output['text'] = '???'

        if len(self.entry_wireSequences_wireSymbol.get()) == 1:
            self.entry_wireSequences_wireSymbol.insert(2, 'C')
        elif len(self.entry_wireSequences_wireSymbol.get()) == 2:
            self.entry_wireSequences_wireSymbol.delete(1, 2)
            self.entry_wireSequences_wireSymbol.insert(2, 'C')

    def button_wireSequences_process(self) -> None:
        text = self.entry_wireSequences_wireSymbol.get()

        if len(text) != 2:
            return

        color = text[0]
        dest = text[1]

        if color == 'R':
            if dest in RED_WIRE_OCCURENCES[int(self.spinbox_wireSequences_reds.get())]:
                self.label_wireSequences_output['text'] = 'Cut Wire.'
            else:
                self.label_wireSequences_output['text'] = "Don't cut wire."

            self.spinbox_wireSequences_reds.set(int(self.spinbox_wireSequences_reds.get()) + 1)
        elif color == 'U':
            if dest in BLUE_WIRE_OCCURENCES[int(self.spinbox_wireSequences_blues.get())]:
                self.label_wireSequences_output['text'] = 'Cut Wire.'
            else:
                self.label_wireSequences_output['text'] = "Don't cut wire."

            self.spinbox_wireSequences_blues.set(int(self.spinbox_wireSequences_blues.get()) + 1)
        elif color == 'K':
            if dest in BLACK_WIRE_OCCURENCES[int(self.spinbox_wireSequences_blacks.get())]:
                self.label_wireSequences_output['text'] = 'Cut Wire.'
            else:
                self.label_wireSequences_output['text'] = "Don't cut wire."

            self.spinbox_wireSequences_blacks.set(int(self.spinbox_wireSequences_blacks.get()) + 1)

    def update_treeview_passwords(self, data) -> None:
        first_chars = self.entry_passwords_first.get().upper()
        second_chars = self.entry_passwords_second.get().upper()
        third_chars = self.entry_passwords_third.get().upper()

        # Empty tree
        for child in self.treeview_passwords.get_children():
            self.treeview_passwords.delete(child)

        if len(first_chars) == 0:
            return

        for password in PASSWORDS:
            has_first = False
            has_second = False
            has_third = False

            for char in first_chars:
                if char == password[0]:
                    has_first = True
                    break
            for char in second_chars:
                if char == password[1]:
                    has_second = True
                    break
            for char in third_chars:
                if char == password[2]:
                    has_third = True
                    break

            if len(second_chars) == 0:
                has_second = True

            if len(third_chars) == 0:
                has_third = True
            
            if has_first and has_second and has_third:
                self.treeview_passwords.insert('', len(self.treeview_passwords.get_children()), values=(password))

if __name__ == "__main__":
    app = ManualApp()
    app.run()

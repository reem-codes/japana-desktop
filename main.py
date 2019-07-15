import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QLabel, QRadioButton, QCheckBox, QProgressBar,
                             QVBoxLayout, QApplication, QGridLayout, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from process import process


class Main(QWidget):

    OUTPUT_PATH = os.path.expanduser('~{}Desktop{}japana{}output.txt'.format(os.path.sep, os.path.sep, os.path.sep))
    INPUT_PATH = ""

    def __init__(self):
        super().__init__()
        self.setProperty('class', 'body')
        self.pbar = QProgressBar(self)
        self.init_ui()

    def init_ui(self):
        input_label = QLabel('file path:')
        self.input_path = QLabel(self.INPUT_PATH)
        self.input_path.setProperty('class', 'files')
        input_change = QPushButton('change')
        output_label = QLabel('output path:')
        self.output_path = QLabel(self.OUTPUT_PATH)
        self.output_path.setProperty('class', 'files')

        output_change = QPushButton('change')

        frequency_label = QLabel('Frequency:')

        self.asc = QRadioButton("ascending")
        self.asc.setChecked(True)
        desc = QRadioButton("descending")

        kana_label = QLabel('include kana words')
        self.kana_check = QCheckBox()

        dic_label = QLabel('include dictionary definitions')
        self.dic_check = QCheckBox()
        self.dic_check.setChecked(True)

        submit = QPushButton("Submit")

        input_details = QGridLayout()
        input_details.addWidget(input_label, 1, 0)
        input_details.addWidget(self.input_path, 1, 2)
        input_details.addWidget(input_change, 1, 10)

        output_details = QGridLayout()
        output_details.addWidget(output_label, 1, 0)
        output_details.addWidget(self.output_path, 1, 2)
        output_details.addWidget(output_change, 1, 10)

        f_hbox = QHBoxLayout()
        f_hbox.setAlignment(Qt.AlignLeft)
        f_hbox.addWidget(frequency_label)
        f_hbox.addWidget(self.asc)
        f_hbox.addWidget(desc)

        k_hbox = QHBoxLayout()
        k_hbox.setAlignment(Qt.AlignLeft)
        k_hbox.addWidget(self.kana_check)
        k_hbox.addWidget(kana_label)

        d_hbox = QHBoxLayout()
        d_hbox.setAlignment(Qt.AlignLeft)
        d_hbox.addWidget(self.dic_check)
        d_hbox.addWidget(dic_label)

        vbox = QVBoxLayout()
        vbox.setSpacing(20)

        vbox.setAlignment(Qt.AlignCenter)
        vbox.addLayout(input_details)
        vbox.addLayout(f_hbox)
        vbox.addLayout(k_hbox)
        vbox.addLayout(d_hbox)
        vbox.addLayout(output_details)
        vbox.addWidget(submit)
        vbox.addWidget(self.pbar)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Japana')
        self.show()
        output_change.clicked.connect(self.output_change_path)
        input_change.clicked.connect(self.input_change_path)
        submit.clicked.connect(self.start)
        return

    def output_change_path(self):
        f = QFileDialog.getSaveFileName(self, 'choose output path', "oo.txt")[0]

        self.OUTPUT_PATH = str(f)
        if self.OUTPUT_PATH:
            self.output_path.setText(self.OUTPUT_PATH)

        return

    def input_change_path(self):
        self.INPUT_PATH = str(QFileDialog.getOpenFileName(self, 'choose file')[0])
        if self.INPUT_PATH:
            self.input_path.setText(self.INPUT_PATH)

        return

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == (Qt.Key_Enter or Qt.Key_Space):
            self.start()
        return

    def start(self):
        if self.INPUT_PATH == "":
            QMessageBox.about(self, "Error", "No file provided")

        else:
            process(self.INPUT_PATH, self.OUTPUT_PATH, self.kana_check.isChecked(), self.asc.isChecked(), self.dic_check.isChecked(), self.pbar)
            QMessageBox.about(self, "My message box", "Done")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('style/style.css').read())
    ex = Main()
    sys.exit(app.exec_())

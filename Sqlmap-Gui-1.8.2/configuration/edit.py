from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from . import tishi
from .edit_ui import Ui_Form
from PyQt5.QtWidgets import QWidget


class Edit(QWidget, Ui_Form):
    closed = pyqtSignal()  # 定义一个信号

    def __init__(self):
        super(Edit, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 设置窗口标志为只显示关闭按钮
        self.edit_file = ""
        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.save_txt)

    def save_txt(self):
        fp = open(self.edit_file, "w", encoding="utf-8")
        fp.write(self.textEdit.toPlainText())
        self.open_tishiwindow("保存成功", "img/成功.PNG")
        self.close()

    # 消息弹窗
    def open_tishiwindow(self, text, img):
        self.tishi_window = tishi.TiShi()
        icon = QIcon('img/logo.PNG')
        self.tishi_window.setWindowIcon(icon)
        if text:
            self.tishi_window.label.setText(text)
        if img:
            self.tishi_window.label_2.setPixmap(QtGui.QPixmap(img))
        self.tishi_window.setWindowModality(Qt.ApplicationModal)  # 设置子窗口为应用程序模态
        # 获取主界面的几何信息
        main_geometry = self.geometry()
        main_x = main_geometry.x()
        main_y = main_geometry.y()
        main_width = main_geometry.width()
        main_height = main_geometry.height()

        # 获取提示窗口的大小
        tishi_width = self.tishi_window.width()
        tishi_height = self.tishi_window.height()

        # 计算提示窗口的位置
        tishi_x = main_x + (main_width - tishi_width) // 2
        tishi_y = main_y + (main_height - tishi_height) // 2

        # 设置提示窗口的位置
        self.tishi_window.move(tishi_x, tishi_y)
        self.tishi_window.show()

    def closeEvent(self, event):
        self.closed.emit()  # 发出信号
        event.accept()

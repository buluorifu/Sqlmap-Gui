from PyQt5.QtCore import Qt, pyqtSignal
from .tishi_ui import Ui_Form
from PyQt5.QtWidgets import QWidget


class TiShi(QWidget, Ui_Form):
    closed = pyqtSignal()  # 定义一个信号

    def __init__(self):
        super(TiShi, self).__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 设置窗口标志为只显示关闭按钮

        def closeEvent(self, event):
            self.closed.emit()  # 发出信号
            event.accept()

# 这是一个示例 Python 脚本。

import string
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from password_generator import Ui_passwordgenerator
import random
import datetime


class mypasswordgenerator(Ui_passwordgenerator, QDialog):
    # 构造函数
    def __init__(self):
        super().__init__()  # 初始化父类对象的属性
        self.setupUi(self)  # 继承QDialog
        self.show()  # 展示窗口
        self.pushButton.clicked.connect(self.new_password)

    def new_password(self):
        target = self.lineEdit_target.text()
        username = self.lineEdit_username.text()
        if not username:
            username_result = random.sample((string.ascii_uppercase
                                             + string.ascii_lowercase
                                             + string.digits
                                             ), int(self.spinBox_count.text()))
            self.lineEdit_username.setText(''.join(username_result))
            username = self.lineEdit_username.text()
        if not target:
            QMessageBox.warning(self, "信息提示", "请输入目标站点，以便保存！")
        words = []
        if self.checkBox_num.isChecked():
            words.append(string.digits * 2)
        if self.checkBox_upper.isChecked():
            words.append(string.ascii_uppercase * 2)
        if self.checkBox_lower.isChecked():
            words.append(string.ascii_lowercase * 2)
        if self.checkBox_puc.isChecked():
            words.append(string.punctuation * 2)
        # word = random.sample(list(words), 10)

        if not words:
            words = random.sample((string.ascii_uppercase
                                   + string.ascii_lowercase
                                   + string.digits
                                   + string.punctuation), int(self.spinBox_count.text()))
        else:

            words = "".join(words)
        passwords = random.sample(list(words), int(self.spinBox_count.text()))
        self.lineEdit_result.setText(''.join(passwords))
        password = self.lineEdit_result.text()
        date = datetime.datetime.now()
        print(date)
        with open('密码记录.txt', "a", encoding='utf-8') as f:
            f.write(f"目标站点：{target}\t\t\t用户名：{username}\t\t\t密码：{password}\t\t\t\t生成日期：{date}\n")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mypasswordgenerator()
    sys.exit(app.exec())

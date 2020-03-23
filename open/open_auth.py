from window import Window
from PyQt5.QtWidgets import QPushButton, QLineEdit, QVBoxLayout, QStatusBar

class AuthWindow(Window):
    def __init__(self, parent):
        super().__init__(parent, 'Авторизация', size = (300, 130), font_size = 11)

        self.vertical_layout = QVBoxLayout(self.widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.button_url = QPushButton(self)
        self.edit_auth = QLineEdit(self)
        self.button_auth = QPushButton(self)
        self.vertical_layout.addWidget(self.button_url)
        self.vertical_layout.addWidget(self.edit_auth)
        self.vertical_layout.addWidget(self.button_auth)
        
        self.setWindowTitle("Авторизация")
        self.button_url.setText(self.text_button_url())
        self.button_url.clicked.connect(self.start_auth)
        self.button_auth.setText("Авторизоваться")
        self.button_auth.clicked.connect(self.auth)

        self.status_auth = QStatusBar(self.widget)
        self.vertical_layout.addWidget(self.status_auth)
  
    def auth(self):
        if self.func_auth():
            self.status_auth.showMessage('Авторизация прошла успешно')
        else:
            self.status_auth.showMessage('Ошибка авторизации...')
    
    def start_auth(self):
        self.func_auth_start()
        self.status_auth.showMessage('Ожидание авторизации...')
    
      
    def text_button_url(self): return "Получить ссылку для авторизации"

    def func_auth_start(self): return True

    def func_auth(self): return False




if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    ex = AuthWindow(None)
    ex.show()
    sys.exit(app.exec_())
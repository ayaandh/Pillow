import sys
from PyQt5.QtWidgets import QApplication
from browser import Browser

def main():
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
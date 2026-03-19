from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

from ui import BookmarksUI, HistoryUI
from history import add as add_history

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ayaan Browser")
        self.resize(1200, 800)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.browser_tab = self.create_browser_tab()
        self.bookmarks_ui = BookmarksUI()
        self.history_ui = HistoryUI()

        self.tabs.addTab(self.browser_tab, "Browser")
        self.tabs.addTab(self.bookmarks_ui, "Bookmarks")
        self.tabs.addTab(self.history_ui, "History")

    def create_browser_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        top_bar = QHBoxLayout()

        self.back_btn = QPushButton("<")
        self.forward_btn = QPushButton(">")
        self.reload_btn = QPushButton("⟳")
        self.go_btn = QPushButton("Go")

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search...")

        top_bar.addWidget(self.back_btn)
        top_bar.addWidget(self.forward_btn)
        top_bar.addWidget(self.reload_btn)
        top_bar.addWidget(self.url_bar)
        top_bar.addWidget(self.go_btn)

        self.web = QWebEngineView()
        self.web.setUrl(QUrl("https://www.google.com"))

        self.back_btn.clicked.connect(self.web.back)
        self.forward_btn.clicked.connect(self.web.forward)
        self.reload_btn.clicked.connect(self.web.reload)
        self.go_btn.clicked.connect(self.load_url)
        self.url_bar.returnPressed.connect(self.load_url)

        self.web.urlChanged.connect(self.update_url)
        self.web.loadFinished.connect(self.on_load)

        layout.addLayout(top_bar)
        layout.addWidget(self.web)

        return widget

    def load_url(self):
        url = self.url_bar.text()

        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url.replace(" ", "+")

        self.web.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def on_load(self):
        url = self.web.url().toString()
        add_history(url)
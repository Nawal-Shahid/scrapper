import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class WebScraperApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        layout = QVBoxLayout()

        # Create and set a pastel blue background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        # Create and set a label
        label = QLabel("Enter URL:")
        layout.addWidget(label)

        # Create and set an input field
        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        # Create and set a search button
        search_button = QPushButton("Scrape")
        search_button.clicked.connect(self.scrape_website)
        layout.addWidget(search_button)

        # Create and set a text browser for displaying results
        self.results_browser = QTextBrowser()
        layout.addWidget(self.results_browser)

        # Create and set a "Save to File" button
        save_button = QPushButton("Save to File")
        save_button.clicked.connect(self.save_to_file)
        layout.addWidget(save_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set up the main window
        self.setWindowTitle('Web Scraper')
        self.setGeometry(300, 300, 500, 400)

    def scrape_website(self):
        url = self.url_input.text()
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            # Example: Extracting all paragraphs from the HTML
            paragraphs = soup.find_all('p')

            # Display the results in the text browser
            self.results_browser.clear()
            for paragraph in paragraphs:
                self.results_browser.append(str(paragraph))

        except requests.exceptions.RequestException as e:
            self.results_browser.clear()
            self.results_browser.append(f"Error: {e}")

    def save_to_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save to File", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.results_browser.toPlainText())
                self.results_browser.append(f"\nData saved to {file_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebScraperApp()
    window.show()
    sys.exit(app.exec_())

#Nawal Shahid
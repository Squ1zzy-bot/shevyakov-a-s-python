from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QTextEdit
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


def seo_analysis(text):
    if not text.strip():
        return "ТЕКСТ ПУСТОЙ"
    
    try:
        tokens = [word.lower() for word in word_tokenize(text)]
        russian_stopwords = stopwords.words('russian')
        filtered_words = []

        for word in tokens:
            if word not in russian_stopwords and word.isalpha():
                filtered_words.append(word)

        if not filtered_words:
            return "Нет значимых слов для анализа после фильтрации стоп-слов"

        frequency = nltk.FreqDist(filtered_words)
        top_keywords = frequency.most_common(5)

        result = "SEO:\n\n"
        result += "Ключевые слова:\n"
        for word, count in top_keywords:
            result += f"- {word}: {count} раз(а)\n"
        result += f"\nВсего уникальных слов после фильтрации: {len(filtered_words)}"
        return result

    except Exception as error:
        return f"Ошибка при анализе: {str(error)}"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SEO")

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Введите текст...")

        self.analyze_button = QPushButton("Запустить Анализ")

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("Здесь могла быть ваша реклама)")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Введите текст:"))
        layout.addWidget(self.text_input)
        layout.addWidget(self.analyze_button)
        layout.addWidget(QLabel("Результаты:"))
        layout.addWidget(self.result_display)

        self.analyze_button.clicked.connect(self.run_analysis)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_analysis(self):
        user_text = self.text_input.text()
        analysis_result = seo_analysis(user_text)
        self.result_display.setText(analysis_result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

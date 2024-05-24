from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(300, 300)
        self.bmi = 0
        self.layout = QVBoxLayout()
        weightLabel = QLabel("Weight(kg):")
        heightLabel = QLabel("Height(cm):")
        
        font = weightLabel.font()
        font.setPointSize(20)
        weightLabel.setFont(font)
        heightLabel.setFont(font)
        
        self.weightInput = QLineEdit(parent=self)
        self.weightInput.setMaxLength(10)
        self.weightInput.setPlaceholderText("Enter your weight")
        
        self.heightInput = QLineEdit(parent=self)
        self.heightInput.setMaxLength(10)
        self.heightInput.setPlaceholderText("Enter your height")
        self.calculatedBMI = QLabel(f"Your BMI: {self.bmi}")
        
        calculate_btn = QPushButton(text='Calculate BMI')
        calculate_btn.clicked.connect(self.calculateBMI)
        
        self.layout.addWidget(weightLabel)
        self.layout.addWidget(self.weightInput)
        self.layout.addWidget(heightLabel)
        self.layout.addWidget(self.heightInput)
        self.layout.addWidget(calculate_btn)
        self.layout.addWidget(self.calculatedBMI)
        
        widget = QWidget()
        widget.setLayout(self.layout)
        # self.setCentralWidget(weightInput, weightLabel)
        self.setCentralWidget(widget)
        
    def calculateBMI(self):
        self.bmi = float(self.weightInput.text()) / ((float(self.heightInput.text()) / 100) ** 2  )
        self.calculatedBMI.setText(f"Your BMI: {self.bmi}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
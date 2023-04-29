import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QComboBox, QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
import MySQLdb as mdb
import queryWindows as qw


# THIS IS FOR AIRPLANE QUERIES
class AirplaneWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('airplane window')
        self.setGeometry(400, 400, 200, 80)
        # Create 8 buttons with different text on them
        self.add_airplane_button = QPushButton('Add Airplane', self)
        self.add_airplane_button.setGeometry(20, 20, 150, 30)

        self.add_airplane_button.clicked.connect(self.openAddAirportQueryWindow)

    def openAddAirportQueryWindow(self):
        self.w = qw.airportQueryWindow()
        self.w.show()


class PilotsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('pilots window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()

class RoutesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('routes window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()

class TicketsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('tickets window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()

class PeopleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('people window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()

class FlightsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('flights window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()


class AirportsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('airports window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()


class ViewsSimulationCycleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('views/simulation cycle window')
        self.setGeometry(400, 400, 400, 300)
        # Create 8 buttons with different text on them
        button1 = QPushButton('query 1', self)
        button2 = QPushButton('query 2', self)
        button3 = QPushButton('query 3', self)
        button4 = QPushButton('query 4', self)
        button5 = QPushButton('query 5', self)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button3)
        column1_layout.addWidget(button4)
        column1_layout.addWidget(button5)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        layout.addLayout(column1_layout)

        self.setLayout(layout)

        # Show the window
        self.show()

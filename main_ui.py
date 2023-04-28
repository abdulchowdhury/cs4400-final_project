import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
import MySQLdb as mdb


class DatabaseConnection(QWidget):
    def __init__(self):
        super().__init__()
        print('testing database connection')
        db = mdb.connect(host='localhost', user='root',
                         password='test123123', database='flight_management')
        QMessageBox.about(self, 'Connection', 'Database Connected Successfully')

        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM airline')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            # Close the connection
        db.close()
        print('data gather success')

# THIS IS FOR AIRPLANE QUERIES
class AirplaneWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('airplane window')
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



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Airline Management System (SAMS)')
        self.setGeometry(100, 100, 300, 200)

        # Create 8 buttons with different text on them
        button1 = QPushButton('Airplanes', self)
        button2 = QPushButton('Pilots', self)
        button3 = QPushButton('People', self)
        button4 = QPushButton('Flights', self)
        button5 = QPushButton('Routes', self)
        button6 = QPushButton('Tickets', self)
        button7 = QPushButton('Airports', self)
        button8 = QPushButton('Views and Simulation Cycle', self)

        # Connect the buttons to a function that opens a new window
        button1.clicked.connect(self.openAirplaneWindow)
        button2.clicked.connect(self.openPilotsWindow)
        button3.clicked.connect(self.openPeopleWindow)
        button4.clicked.connect(self.openFlightsWindow)
        button5.clicked.connect(self.openRoutesWindow)
        button6.clicked.connect(self.openTicketsWindow)
        button7.clicked.connect(self.openAirportsWindow)
        button8.clicked.connect(self.openViewsWindow)

        # Create a vertical layout for each column
        column1_layout = QVBoxLayout()
        column2_layout = QVBoxLayout()

        # Add the buttons to each column
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)
        column1_layout.addWidget(button5)
        column1_layout.addWidget(button6)
        column2_layout.addWidget(button3)
        column2_layout.addWidget(button4)
        column2_layout.addWidget(button7)
        column2_layout.addWidget(button8)

        # Create a horizontal layout for the window
        layout = QHBoxLayout()

        # Add the column layouts to the window layout
        layout.addLayout(column1_layout)
        layout.addLayout(column2_layout)

        # Set the window layout to the horizontal layout
        self.setLayout(layout)

        # Show the window
        self.show()

    def openAirplaneWindow(self):
        self.w = AirplaneWindow()
        self.w.show()

    def openPilotsWindow(self):
        self.w = PilotsWindow()
        self.w.show()

    def openRoutesWindow(self):
        self.w = RoutesWindow()
        self.w.show()

    def openTicketsWindow(self):
        self.w = TicketsWindow()
        self.w.show()

    def openPeopleWindow(self):
        self.w = PeopleWindow()
        self.w.show()

    def openFlightsWindow(self):
        self.w = FlightsWindow()
        self.w.show()

    def openAirportsWindow(self):
        self.w = AirportsWindow()
        self.w.show()

    def openViewsWindow(self):
        self.w = ViewsSimulationCycleWindow()
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = DatabaseConnection();
    window = MyWindow()
    sys.exit(app.exec_())
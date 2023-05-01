import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QComboBox, QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
import MySQLdb as mdb

import main_ui


class airportQueryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Airplane Query Window')
        self.setGeometry(400, 400, 400, 300)
        self.display_airplane_fields()

    def display_airplane_fields(self):
        db = mdb.connect(host='localhost', user='root',
                         password='test123123', database='flight_management')
        with db.cursor() as cursor:
            # ----------- GETTING AIRLINE IDS -----------#
            cursor.execute("SELECT DISTINCT airlineID FROM airline")
            # Fetch all the rows as a list
            rows = cursor.fetchall()
            # Combine all the strings into one array
            airline_ids = []
            for row in rows:
                airline_ids.append(row[0])
            rows = cursor.fetchall()

            # ----------- GETTING LOCATION IDS -----------#
            cursor.execute("SELECT DISTINCT locationID FROM location")
            # Fetch all the rows as a list
            rows = cursor.fetchall()
            # Combine all the strings into one array
            location_ids = []
            for row in rows:
                location_ids.append(row[0])
            rows = cursor.fetchall()

        # Close the connection
        db.close()

        self.airlineid_label = QLabel('Airline ID:', self)
        self.airlineid_dropdown = QComboBox(self)

        # dropdown for airlineID
        for curr_id in airline_ids:
            self.airlineid_dropdown.addItem(curr_id)

        self.tail_num_label = QLabel('Tail Number:', self)
        self.tail_num_input = QLineEdit(self)
        self.seat_capacity_label = QLabel('Seat Capacity:', self)
        self.seat_capacity_input = QLineEdit(self)
        self.speed_label = QLabel('Speed:', self)
        self.speed_input = QLineEdit(self)
        self.location_id_label = QLabel('Location ID:', self)
        self.location_id_dropdown = QComboBox(self)

        # dropdown for locationID
        for curr_loc_id in location_ids:
            self.location_id_dropdown.addItem(curr_loc_id)

        self.plane_type_label = QLabel('Plane Type:', self)
        self.plane_type_input = QLineEdit(self)
        self.skids_label = QLabel('Skids:', self)
        self.skids_input = QLineEdit(self)
        self.propeller_label = QLabel('Propeller:', self)
        self.propeller_input = QLineEdit(self)
        self.jet_engines_label = QLabel('Jet Engines:', self)
        self.jet_engines_input = QLineEdit(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.airlineid_label)
        layout.addWidget(self.airlineid_dropdown)
        layout.addWidget(self.tail_num_label)
        layout.addWidget(self.tail_num_input)
        layout.addWidget(self.seat_capacity_label)
        layout.addWidget(self.seat_capacity_input)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_input)
        layout.addWidget(self.location_id_label)
        layout.addWidget(self.location_id_dropdown)
        layout.addWidget(self.plane_type_label)
        layout.addWidget(self.plane_type_input)
        layout.addWidget(self.skids_label)
        layout.addWidget(self.skids_input)
        layout.addWidget(self.propeller_label)
        layout.addWidget(self.propeller_input)
        layout.addWidget(self.jet_engines_label)
        layout.addWidget(self.jet_engines_input)

        add_airplane_button = QPushButton('Add Airplane', self)
        add_airplane_button.clicked.connect(self.add_airplane)
        layout.addWidget(add_airplane_button)

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.close)
        layout.addWidget(cancel_button)

    def add_airplane(self):
        airlineid = self.airlineid_dropdown.currentText()
        tail_num = self.tail_num_input.text()
        seat_capacity = self.seat_capacity_input.text()
        speed = self.speed_input.text()
        location_id = self.location_id_dropdown.currentText()
        plane_type = self.plane_type_input.text()
        skids = self.skids_input.text()
        propeller = self.propeller_input.text()
        jet_engines = self.jet_engines_input.text()

        airplane_data = [self.airlineid_dropdown.currentText(),
                         self.tail_num_input.text(),
                         self.seat_capacity_input.text(),
                         self.speed_input.text(),
                         self.location_id_dropdown.currentText(),
                         self.plane_type_input.text(),
                         self.skids_input.text(),
                         self.propeller_input.text(),
                         self.jet_engines_input.text()]

        for i in range(len(airplane_data)):
            if airplane_data[i] == "":
                airplane_data[i] = None

        print(airplane_data)

        db = mdb.connect(host='localhost', user='root',
                         password='test123123', database='flight_management')
        # Add code to insert data into database here
        with db.cursor() as cursor:
            cursor.callproc('add_airplane', args=airplane_data)
            print('test')
        db.commit()

        self.close()

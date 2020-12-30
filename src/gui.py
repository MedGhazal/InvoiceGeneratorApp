import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import script_methods
from script_methods import VerificationWindow

flag = 0


def destroy_all():
    sys.exit()


class ErrorWindow(QWidget):
    def __init__(self, error_message = None):
        QWidget.__init__(self)
        self.setFixedSize(350, 100)
        self.setWindowTitle("Invoice Generator")
        self.label = QtWidgets.QLabel(self)
        self.label.setText(error_message)
        self.label.move(100, 20)
        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setText("continue")
        self.button_confirm.move(240, 65)


class ClientAdderWindow(QWidget):

    def __init__(self, add_change='add'):
        QWidget.__init__(self)
        self.flag = add_change
        self.setFixedSize(300, 250)
        self.setWindowTitle("Invoice Generator")

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Adding client')
        self.label.move(120, 20)

        self.field_client = QtWidgets.QLineEdit(self)
        self.field_client.setText("")
        self.field_client.move(150, 60)
        self.label_client = QtWidgets.QLabel(self)
        self.label_client.setText('Client')
        self.label_client.move(20, 60)

        self.field_n_street = QtWidgets.QLineEdit(self)
        self.field_n_street.setText("")
        self.field_n_street.move(150, 90)
        self.label_client = QtWidgets.QLabel(self)
        self.label_client.setText('Street and number')
        self.label_client.move(20, 90)

        self.field_pcode_city = QtWidgets.QLineEdit(self)
        self.field_pcode_city.setText("")
        self.field_pcode_city.move(150, 120)
        self.label_pcode_city = QtWidgets.QLabel(self)
        self.label_pcode_city.setText('P-Code and city')
        self.label_pcode_city.move(20, 120)

        self.field_country = QtWidgets.QLineEdit(self)
        self.field_country.setText("")
        self.field_country.move(150, 150)
        self.label_country = QtWidgets.QLabel(self)
        self.label_country.setText('Country')
        self.label_country.move(20, 150)

        self.button = QtWidgets.QPushButton(self)
        if self.flag == 'change':
            self.button.setText("Change address")
        if self.flag == 'add':
            self.button.setText("Add client")
        self.button.move(60, 200)
        self.button.clicked.connect(lambda: self.verify())

        self.button_quit = QtWidgets.QPushButton(self)
        self.button_quit.setText("quit")
        self.button_quit.move(160, 200)
        self.button_quit.clicked.connect(destroy_all)

        self.verify_window = None
    
    def destroy_app(self):
        self.destroy()

    def verify(self):
        self.verify_window = VerificationWindow()
        self.verify_window.show()
        print("confirming")
        if self.flag == 'add':
            self.verify_window.button_confirm.clicked.connect(self.add_client)
        elif self.flag == 'change':
            self.verify_window.button_confirm.clicked.connect(self.change_client_address)
        self.verify_window.button_cancel.clicked.connect(self.destroy_verify_window)

    def destroy_verify_window(self):
        self.verify_window.destroy()

    def change_client_address(self):
        self.verify_window.destroy()
        print("Changing client address")
        script_methods.change_client_address(self.field_client.text(),
                                             self.field_n_street.text(),
                                             self.field_pcode_city.text(),
                                             self.field_country.text())
        global flag
        flag = 1

    def add_client(self):
        self.verify_window.destroy()
        print("Adding client")
        script_methods.add_client(self.field_client.text(),
                                  self.field_n_street.text(),
                                  self.field_pcode_city.text(),
                                  self.field_country.text())
        global flag
        flag = 1


class InvoiceGeneratorWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(900, 330)
        self.setWindowTitle("Invoice Generator")

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Generating new invoice')
        self.label.move(60, 20)

        self.field_client = QtWidgets.QLineEdit(self)
        self.field_client.setText('')
        self.field_client.move(110, 50)
        self.label_client = QtWidgets.QLabel(self)
        self.label_client.setText('Client')
        self.label_client.move(20, 50)

        self.field_date = QtWidgets.QLineEdit(self)
        self.field_date.move(110, 80)
        self.label_date = QtWidgets.QLabel(self)
        self.label_date.setText('Date')
        self.label_date.move(20, 80)

        self.field_tva = QtWidgets.QLineEdit(self)      
        self.field_tva.move(110, 110)
        self.field_tva.setText('0')
        self.label_tva = QtWidgets.QLabel(self)
        self.label_tva.setText('TVA')
        self.label_tva.move(20, 110)

        self.field_designation = QtWidgets.QLineEdit(self)
        self.field_designation.move(110, 140)
        self.field_designation1 = QtWidgets.QLineEdit(self)
        self.field_designation1.move(240, 140)
        self.field_designation2 = QtWidgets.QLineEdit(self)
        self.field_designation2.move(370, 140)
        self.field_designation3 = QtWidgets.QLineEdit(self)
        self.field_designation3.move(500, 140)
        self.field_designation4 = QtWidgets.QLineEdit(self)
        self.field_designation4.move(630, 140)
        self.field_designation5 = QtWidgets.QLineEdit(self)
        self.field_designation5.move(760, 140)
        self.label_date = QtWidgets.QLabel(self)
        self.label_date.setText('Designation')
        self.label_date.move(20, 140)

        self.field_amount = QtWidgets.QLineEdit(self)
        self.field_amount.setText('0')
        self.field_amount.move(110, 170)
        self.field_amount1 = QtWidgets.QLineEdit(self)
        self.field_amount1.setText('0')
        self.field_amount1.move(240, 170)
        self.field_amount2 = QtWidgets.QLineEdit(self)
        self.field_amount2.setText('0')
        self.field_amount2.move(370, 170)
        self.field_amount3 = QtWidgets.QLineEdit(self)
        self.field_amount3.setText('0')
        self.field_amount3.move(500, 170)
        self.field_amount4 = QtWidgets.QLineEdit(self)
        self.field_amount4.setText('0')
        self.field_amount4.move(630, 170)
        self.field_amount5 = QtWidgets.QLineEdit(self)
        self.field_amount5.setText('0')
        self.field_amount5.move(760, 170)
        self.label_amount = QtWidgets.QLabel(self)
        self.label_amount.setText('Amount')
        self.label_amount.move(20, 170)

        self.field_currency = QtWidgets.QLineEdit(self)
        self.field_currency.move(110, 200)
        self.label_currency = QtWidgets.QLabel(self)
        self.label_currency.setText('Currency')
        self.label_currency.move(20, 200)

        self.field_rate = QtWidgets.QLineEdit(self)
        self.field_rate.setText('0')
        self.field_rate.move(110, 230)
        self.label_rate = QtWidgets.QLabel(self)
        self.label_rate.setText('Rate')
        self.label_rate.move(20, 230)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Generate invoice")
        self.button.move(20, 270)
        self.button.clicked.connect(lambda: self.verify())

        self.error_window = None

        self.button_quit = QtWidgets.QPushButton(self)
        self.button_quit.setText("quit")
        self.button_quit.move(160, 270)
        self.button_quit.clicked.connect(destroy_all)
        self.button.clicked.connect(lambda: self.verify())

        self.verify_window = None

    def destroy_app(self):
        self.destroy()

    def verify(self):
        self.verify_window = VerificationWindow()
        self.verify_window.show()
        self.verify_window.button_confirm.clicked.connect(self.generate_invoice)
        self.verify_window.button_cancel.clicked.connect(self.destroy_verify_window)

    def destroy_verify_window(self):
        self.verify_window.destroy()

    def generate_invoice(self):
        self.verify_window.destroy()
        flag_generate_invoice = script_methods.generate_invoice(self.field_client.text(),
                                                                [self.field_designation.text(),
                                                                 self.field_designation1.text(),
                                                                 self.field_designation2.text(),
                                                                 self.field_designation3.text(),
                                                                 self.field_designation4.text(),
                                                                 self.field_designation5.text()],
                                                                self.field_date.text(),
                                                                float(self.field_tva.text()),
                                                                [float(self.field_amount.text()),
                                                                 float(self.field_amount1.text()),
                                                                 float(self.field_amount2.text()),
                                                                 float(self.field_amount3.text()),
                                                                 float(self.field_amount4.text()),
                                                                 float(self.field_amount5.text())],
                                                                self.field_currency.text(),
                                                                float(self.field_rate.text()))
        if flag_generate_invoice == 1:
            self.error_window = ErrorWindow(error_message="Client not found\n add client first")
            self.error_window.show()
            self.error_window.button_confirm.clicked.connect(self.destroy_error_message)
        elif flag_generate_invoice == 2:
            self.error_window = ErrorWindow(error_message="TVA should be greater than 0")
            self.error_window.show()
            self.error_window.button_confirm.clicked.connect(self.destroy_error_message)
        elif flag_generate_invoice == 4:
            self.error_window = ErrorWindow(error_message="Rate should be positive")
            self.error_window.show()
            self.error_window.button_confirm.clicked.connect(self.destroy_error_message)
        global flag
        flag = 2

    def destroy_error_message(self):
        self.error_window.destroy()


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(730, 100)
        self.setWindowTitle('Invoice Generator')
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Welcome to Invoice Generator')
        self.label.move(245, 20)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Generate a new invoice")
        self.button1.move(455, 65)
        self.button1.clicked.connect(lambda: self.generate_invoice())

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("Add a new client")
        self.button2.move(20, 65)
        self.button2.clicked.connect(lambda: self.add_client())

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText("Restore invoice number and delete history")
        self.button3.move(160, 65)
        self.button3.clicked.connect(lambda: self.verify())

        self.button_change_address = QtWidgets.QPushButton(self)
        self.button_change_address.setText("Change address of a client")
        self.button_change_address.move(20, 15)
        self.button_change_address.clicked.connect(self.change_client_address)

        self.button_quit = QtWidgets.QPushButton(self)
        self.button_quit.setText("quit")
        self.button_quit.move(640, 65)
        self.button_quit.clicked.connect(destroy_all)

        self.generate_invoice_window = None

        self.add_client_window = None
        self.change_client_address_window = None

        self.verify_window = None
        self.label_reset = None
        self.label_generate_invoice = None
        self.label_add_client = None

    def destroy_verify_window(self):
        self.verify_window.destroy()

    def verify(self):
        self.verify_window = VerificationWindow()
        self.verify_window.show()
        self.verify_window.button_confirm.clicked.connect(self.restore)
        self.verify_window.button_cancel.clicked.connect(self.destroy_verify_window)

    def restore(self):
        global flag
        flag = script_methods.restore()
        self.destroy()
        if self.label_generate_invoice:
            self.label_generate_invoice.hide()
        if self.label_add_client:
            self.label_add_client.hide()
        self.label_reset = QtWidgets.QLabel(self)
        self.label_reset.setText('History deleted and counter reset to 1')
        self.label_reset.move(250, 40)
        if flag == 3:
            destroy_all()

    def change_client_address(self):
        self.change_client_address_window = ClientAdderWindow(add_change="change")
        self.change_client_address_window.label.setText("Change client")
        self.change_client_address_window.button.move(40, 200)
        self.change_client_address_window.button_quit.move(180, 200)
        self.change_client_address_window.label.show()
        self.change_client_address_window.show()
        global flag
        if flag == 2:
            self.label_generate_invoice.show()

    def generate_invoice(self):
        self.generate_invoice_window = InvoiceGeneratorWindow()
        self.generate_invoice_window.show()
        if self.label_reset:
            self.label_reset.hide()
        if self.label_add_client:
            self.label_add_client.hide()
        self.label_generate_invoice = QtWidgets.QLabel(self)
        self.label_generate_invoice.setText('Invoice generated')
        self.label_generate_invoice.move(250, 40)
        global flag
        if flag == 2:
            self.label_generate_invoice.show()

    def add_client(self):
        self.add_client_window = ClientAdderWindow()
        self.add_client_window.show()
        if self.label_reset:
            self.label_reset.hide()
        if self.label_generate_invoice:
            self.label_generate_invoice.hide()
        self.label_add_client = QtWidgets.QLabel(self)
        self.label_add_client.setText('Client added')
        self.label_add_client.move(250, 40)
        global flag
        if flag == 1:
            self.label_add_client.show()

import sys
from PyQt5.QtWidgets import QWidget, QCompleter, QLabel, QPushButton, QLineEdit, QComboBox
from script_methods import *

flag = 0


def destroy_all():
    sys.exit()


class ErrorWindow(QWidget):
    def __init__(self, error_message = None):
        QWidget.__init__(self)
        self.setFixedSize(350, 100)
        self.setWindowTitle("Invoice Generator")
        self.label =QLabel(self)
        self.label.setText(error_message)
        self.label.move(100, 20)
        self.button_confirm = QPushButton(self)
        self.button_confirm.setText("continue")
        self.button_confirm.move(240, 65)


class ClientAdderWindow(QWidget):
    def __init__(self, add_change="add"):
        QWidget.__init__(self)
        self.flag = add_change

        if self.flag == "add":
            self.setFixedSize(300, 230)
            self.setWindowTitle("Add client")

            self.field_client = QLineEdit(self)
            self.field_client.move(150, 30)
            self.field_client.setText("")

            self.field_ice = QLineEdit(self)
            self.field_ice.setText("")
            self.field_ice.move(150, 150)
            self.label_ice = QLabel(self)
            self.label_ice.setText("ICE")
            self.label_ice.move(20, 150)

            self.button_add = QPushButton(self)
            self.button_add.setText("Add client")
            self.button_add.move(60, 190)
            self.button_add.clicked.connect(lambda: self.verify())

            self.button_quit = QPushButton(self)
            self.button_quit.setText("quit")
            self.button_quit.move(160, 190)
            self.button_quit.clicked.connect(destroy_all)

        elif self.flag == "change":
            self.setFixedSize(300, 200)
            self.setWindowTitle("Change address")
            clients = []
            with open("La Mome_infos.txt", encoding="utf-8") as file:
                text = file.read()
                for client in text.split(";")[2].split(","):
                    clients.append(client.split(r"\\")[0])
            self.field_client = QLineEdit(self)
            self.field_client.move(150, 30)
            self.field_client.setCompleter(QCompleter(clients))

            self.button_change = QPushButton(self)
            self.button_change.setText("Change address")
            self.button_change.clicked.connect(lambda: self.verify())
            self.button_change.move(40, 160)

            self.button_quit = QPushButton(self)
            self.button_quit.setText("quit")
            self.button_quit.clicked.connect(destroy_all)
            self.button_quit.move(180, 160)

        self.label_client = QLabel(self)
        self.label_client.setText("Client")
        self.label_client.move(20, 30)

        self.field_n_street = QLineEdit(self)
        self.field_n_street.setText("")
        self.field_n_street.move(150, 60)
        self.label_client = QLabel(self)
        self.label_client.setText("Street and number")
        self.label_client.move(20, 60)

        self.field_pcode_city = QLineEdit(self)
        self.field_pcode_city.setText("")
        self.field_pcode_city.move(150, 90)
        self.label_pcode_city = QLabel(self)
        self.label_pcode_city.setText("P-Code and city")
        self.label_pcode_city.move(20, 90)

        self.field_country = QLineEdit(self)
        self.field_country.setText("")
        self.field_country.move(150, 120)
        self.label_country = QLabel(self)
        self.label_country.setText("Country")
        self.label_country.move(20, 120)

        self.verify_window = None

    def destroy_app(self):
        self.destroy()

    def verify(self):
        self.verify_window = VerificationWindow()
        self.verify_window.show()
        if self.flag == "add":
            self.verify_window.button_confirm.clicked.connect(self.add_client)
        elif self.flag == "change":
            self.verify_window.button_confirm.clicked.connect(
                self.change_client_address
            )
        self.verify_window.button_cancel.clicked.connect(self.destroy_verify_window)

    def destroy_verify_window(self):
        self.verify_window.destroy()

    def change_client_address(self):
        self.verify_window.destroy()
        change_client_address(
            self.field_client.text(),
            self.field_n_street.text(),
            "{} {}".format(self.field_pcode_city.text(), self.field_country.text()),
        )
        global flag
        flag = 1

    def add_client(self):
        self.verify_window.destroy()
        try:
            add_client(
                self.field_client.text(),
                self.field_n_street.text(),
                "{} {}".format(self.field_pcode_city.text(), self.field_country.text()),
                self.field_ice.text(),
            )
        except ClientAlreadyInDatabase:
            self.error_window = ErrorWindow(error_message="Client Already In Database")
            self.error_window.show()
            self.error_window.button_confirm.clicked.connect(self.destroy_error_message)
        global flag
        flag = 1

    def destroy_error_message(self):
        self.error_window.destroy()


class InvoiceGeneratorWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(460, 620)
        self.setWindowTitle("Invoice Generator")

        clients = []
        with open("La Mome_infos.txt", encoding="utf-8") as file:
            text = file.read()
            for client in text.split(";")[2].split(","):
                clients.append(client.split(r"\\")[0])
        self.field_client = QLineEdit(self)
        self.field_client.setCompleter(QCompleter(clients))
        self.field_client.move(100, 20)
        self.label_client = QLabel(self)
        self.label_client.setText('Client')
        self.label_client.move(20, 20)

        self.field_invoicer = QLineEdit(self)
        self.field_invoicer.setCompleter(QCompleter(['La Mome', 'Marina']))
        self.field_invoicer.move(310, 20)
        self.label_invoicer = QLabel(self)
        self.label_invoicer.setText('Invoicer')
        self.label_invoicer.move(240, 20)

        self.field_date_f = QLineEdit(self)
        self.field_date_f.move(100, 50)
        self.label_date_f = QLabel(self)
        self.label_date_f.setText('Facturation')
        self.label_date_f.move(20, 50)

        self.field_date_e = QLineEdit(self)
        self.field_date_e.move(310, 50)
        self.label_date_e = QLabel(self)
        self.label_date_e.setText('Échéance')
        self.label_date_e.move(240, 50)

        self.field_tva = QLineEdit(self)      
        self.field_tva.move(100, 80)
        self.field_tva.setText('0')
        self.label_tva = QLabel(self)
        self.label_tva.setText('TVA')
        self.label_tva.move(20, 80)

        self.field_rate = QLineEdit(self)
        self.field_rate.move(310, 80)
        self.label_rate = QLabel(self)
        self.label_rate.setText('Rate')
        self.label_rate.move(240, 80)

        self.field_designation = QLineEdit(self)
        self.field_designation.move(110, 140)
        self.field_designation1 = QLineEdit(self)
        self.field_designation1.move(110, 165)
        self.field_designation2 = QLineEdit(self)
        self.field_designation2.move(110, 190)
        self.field_designation3 = QLineEdit(self)
        self.field_designation3.move(110, 215)
        self.field_designation4 = QLineEdit(self)
        self.field_designation4.move(110, 240)
        self.field_designation5 = QLineEdit(self)
        self.field_designation5.move(110, 265)
        self.field_designation6 = QLineEdit(self)
        self.field_designation6.move(110, 290) 
        self.field_designation7 = QLineEdit(self)
        self.field_designation7.move(110, 315) 
        self.field_designation8 = QLineEdit(self)
        self.field_designation8.move(110, 340) 
        self.field_designation9 = QLineEdit(self)
        self.field_designation9.move(110, 365) 
        self.field_designation10 = QLineEdit(self)
        self.field_designation10.move(110, 390) 
        self.field_designation11 = QLineEdit(self)
        self.field_designation11.move(110, 415) 
        self.field_designation12 = QLineEdit(self)
        self.field_designation12.move(110, 440) 
        self.field_designation13 = QLineEdit(self)
        self.field_designation13.move(110, 465) 
        self.field_designation14 = QLineEdit(self)
        self.field_designation14.move(110, 490) 
        self.field_designation15 = QLineEdit(self)
        self.field_designation15.move(110, 515) 


        self.label_date = QLabel(self)
        self.label_date.setText("Designations")
        self.label_date.move(110, 120)

        self.field_amount = QLineEdit(self)
        self.field_amount.setText('0')
        self.field_amount.move(240, 140)
        self.field_amount1 = QLineEdit(self)
        self.field_amount1.setText("0")
        self.field_amount1.move(240, 165)
        self.field_amount2 = QLineEdit(self)
        self.field_amount2.setText("0")
        self.field_amount2.move(240, 190)
        self.field_amount3 = QLineEdit(self)
        self.field_amount3.setText("0")
        self.field_amount3.move(240, 215)
        self.field_amount4 = QLineEdit(self)
        self.field_amount4.setText("0")
        self.field_amount4.move(240, 240)
        self.field_amount5 = QLineEdit(self)
        self.field_amount5.setText("0")
        self.field_amount5.move(240, 265)
        self.field_amount6 = QLineEdit(self)
        self.field_amount6.setText("0")
        self.field_amount6.move(240, 290)
        self.field_amount7 = QLineEdit(self)
        self.field_amount7.setText("0")
        self.field_amount7.move(240, 315)
        self.field_amount8 = QLineEdit(self)
        self.field_amount8.setText("0")
        self.field_amount8.move(240, 340)
        self.field_amount9 = QLineEdit(self)
        self.field_amount9.setText("0")
        self.field_amount9.move(240, 365)
        self.field_amount10 = QLineEdit(self)
        self.field_amount10.setText("0")
        self.field_amount10.move(240, 390)
        self.field_amount11 = QLineEdit(self)
        self.field_amount11.setText("0")
        self.field_amount11.move(240, 415)
        self.field_amount12 = QLineEdit(self)
        self.field_amount12.setText("0")
        self.field_amount12.move(240, 440)
        self.field_amount13 = QLineEdit(self)
        self.field_amount13.setText("0")
        self.field_amount13.move(240, 465)
        self.field_amount14 = QLineEdit(self)
        self.field_amount14.setText("0")
        self.field_amount14.move(240, 490)
        self.field_amount15 = QLineEdit(self)
        self.field_amount15.setText("0")
        self.field_amount15.move(240, 515)

        self.label_amount = QLabel(self)
        self.label_amount.setText("Amounts")
        self.label_amount.move(240, 120)

        self.field_currency = QLineEdit(self)
        self.field_currency.setCompleter(QCompleter(['EURO', 'MAD']))
        self.field_currency.move(100, 550)
        self.label_currency = QLabel(self)
        self.label_currency.setText('Currency')
        self.label_currency.move(20, 550)

        self.paiment_mode = QComboBox(self)
        self.paiment_mode.addItems(["Transfer", "By check", "In cash"])
        self.paiment_mode.move(240, 547)

        self.button = QPushButton(self)
        self.button.setText("Generate Invoice")
        self.button.move(120, 580)
        self.button.clicked.connect(lambda: self.verify())

        self.error_window = None

        self.button_quit = QPushButton(self)
        self.button_quit.setText("quit")
        self.button_quit.move(260, 580)
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
        flag_generate_invoice = generate_invoice(self.field_client.text(),
                                                self.field_invoicer.text(),
                                                [self.field_designation.text(),
                                                self.field_designation1.text(),
                                                self.field_designation2.text(),
                                                self.field_designation3.text(),
                                                self.field_designation4.text(),
                                                self.field_designation5.text(),
                                                self.field_designation6.text(),
                                                self.field_designation7.text(),
                                                self.field_designation8.text(),
                                                self.field_designation9.text(),
                                                self.field_designation10.text(),
                                                self.field_designation11.text(),
                                                self.field_designation12.text(),
                                                self.field_designation13.text(),
                                                self.field_designation14.text(),
                                                self.field_designation15.text()],
                                                self.field_date_f.text(),
                                                self.field_date_e.text(),
                                                float(self.field_tva.text()),
                                                [float(self.field_amount.text()),
                                                float(self.field_amount1.text()),
                                                float(self.field_amount2.text()),
                                                float(self.field_amount3.text()),
                                                float(self.field_amount4.text()),
                                                float(self.field_amount5.text()),
                                                float(self.field_amount6.text()),
                                                float(self.field_amount7.text()),  
                                                float(self.field_amount8.text()), 
                                                float(self.field_amount9.text()),
                                                float(self.field_amount10.text()),  
                                                float(self.field_amount11.text()),
                                                float(self.field_amount12.text()), 
                                                float(self.field_amount13.text()),  
                                                float(self.field_amount14.text()),
                                                float(self.field_amount15.text())],
                                                self.field_currency.text(),
                                                float(self.field_rate.text()) 
                                                if self.field_rate.text() != '' 
                                                else 0,
                                                self.paiment_mode.currentText())
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
        self.setFixedSize(665, 100)
        self.setWindowTitle("Invoice Generator")
        self.label = QLabel(self)
        self.label.setText("Welcome to Invoice Generator")
        self.label.move(245, 15)

        self.button1 = QPushButton(self)
        self.button1.setText("Generate a new invoice")
        self.button1.move(455, 65)
        self.button1.clicked.connect(lambda: self.generate_invoice())

        self.button2 = QPushButton(self)
        self.button2.setText("Add a new client")
        self.button2.move(20, 65)
        self.button2.clicked.connect(lambda: self.add_client())

        self.button3 = QPushButton(self)
        self.button3.setText("Restore invoice number and delete history")
        self.button3.move(160, 65)
        self.button3.clicked.connect(lambda: self.verify())

        self.button_change_address =QPushButton(self)
        self.button_change_address.setText("Change address of a client")
        self.button_change_address.move(20, 30)
        self.button_change_address.clicked.connect(self.change_client_address)

        self.button_quit = QPushButton(self)
        self.button_quit.setText("quit")
        self.button_quit.move(575, 30)
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
        flag = restore()
        self.destroy()
        if self.label_generate_invoice:
            self.label_generate_invoice.hide()
        if self.label_add_client:
            self.label_add_client.hide()
        self.label_reset = QLabel(self)
        self.label_reset.setText("History deleted and counter reset to 1")
        self.label_reset.move(250, 40)
        if flag == 3:
            destroy_all()

    def change_client_address(self):
        self.change_client_address_window = ClientAdderWindow(add_change="change")
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
        self.label_generate_invoice = QLabel(self)
        self.label_generate_invoice.setText("Invoice generated")
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
        self.label_add_client = QLabel(self)
        self.label_add_client.setText("Client added")
        self.label_add_client.move(250, 40)
        global flag
        if flag == 1:
            self.label_add_client.show()

import os
import subprocess
import csv
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets


class VerificationWindow(QWidget):
    def __init__(self,
                 flag="Ordinary",
                 counter=None,
                 date=None,
                 client=None,
                 currency=None,
                 tva=None,
                 amounts=None,
                 rate=None):
        QWidget.__init__(self)
        self.setFixedSize(350, 100)
        self.setWindowTitle("Invoice Generator")
        if flag == "Generate":
            self.counter = counter
            self.date = date
            self.client = client
            self.currency = currency
            self.tva = tva
            self.amounts = amounts
            self.rate = rate
            self.label = QtWidgets.QLabel(self)
            self.label.setText('Do you want to generate finalize invoice?')
            self.label.move(60, 20)

            self.button_confirm = QtWidgets.QPushButton(self)
            self.button_confirm.setText("continue")
            self.button_confirm.move(240, 65)
            self.button_confirm.clicked.connect(lambda: self.finalise())

            self.button_roll_Back = QtWidgets.QPushButton(self)
            self.button_roll_Back.setText("Rollback")
            self.button_roll_Back.move(20, 65)
            self.button_roll_Back.clicked.connect(lambda: self.roll_back())

        elif flag == "Ordinary":
            self.label = QtWidgets.QLabel(self)
            self.label.setText('Do you want to proceed?')
            self.label.move(100, 20)

            self.button_confirm = QtWidgets.QPushButton(self)
            self.button_confirm.setText("continue")
            self.button_confirm.move(240, 65)

            self.button_cancel = QtWidgets.QPushButton(self)
            self.button_cancel.setText("Cancel")
            self.button_cancel.move(20, 65)

    def finalise(self):
        print("Finalising")
        fieldnames = ['N.',
                      'Client',
                      'Date',
                      'Amount in MAD HT',
                      'Amount in MAD TTC',
                      'TVA',
                      'Amount in EURO',
                      'Rate of conversion']
        self.client = self.client.split("\\\\")[0]
        if os.path.exists('invoices.csv'):
            with open('invoices.csv', 'a', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writerow(get_dict(self.currency,
                                         self.counter,
                                         self.client,
                                         self.date,
                                         self.tva,
                                         sum(self.amounts),
                                         self.rate))
        else:
            with open('invoices.csv', 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writeheader()
                writer.writerow(get_dict(self.currency,
                                         self.counter,
                                         self.client,
                                         self.date,
                                         self.tva,
                                         sum(self.amounts),
                                         self.rate))
        x = subprocess.run(
            "mv invoice.pdf factures/{}.pdf".format(
                (str(self.counter) if self.counter > 9 else '0' + str(self.counter)) + '_' +
                self.date + '_' +
                '-'.join(self.client.split(" "))), shell=True, check=True)
        if x != 0:
            print('Exit-code not 0, file invoice.pdf moved to folder factures!')
        with open('src/infos.txt', 'r') as file:
            text = file.read()
        with open('src/infos.txt', 'w') as file:
            self.counter += 1
            new_text = str(self.counter) + ';' + text[1] + ';' + text[2]
            file.write(new_text)
        self.destroy()

    def roll_back(self):
        print("Rolling back")
        x = subprocess.run('rm invoice.pdf', shell=True, check=True)
        if x != 0:
            print('Exit-code not 0, rolled back!')
        self.destroy()


def get_dict(currency, counter, client, date, tva, amount, rate):
    if currency == "EURO":
        return {'N.': counter,
                'Client': client,
                'Date': date,
                'Amount in MAD HT': rate * amount,
                'Amount in MAD TTC': rate * amount,
                'TVA': 0,
                'Amount in EURO': amount,
                'Rate of conversion': rate}
    elif currency == "MAD":
        return {'N.': counter,
                'Client': client.split("\\\\")[0],
                'Date': date,
                'Amount in MAD HT': amount,
                'Amount in MAD TTC': (tva / 100 + 1) * amount,
                'TVA': (tva * amount) / 100,
                'Amount in EURO': None,
                'Rate of conversion': rate}


def add_client(name, n_street, p_code_city, country):
    client = name + "\\\\"
    client += n_street + "\\\\"
    client += p_code_city + "\\\\"
    client += country
    print("Adding client")
    if os.path.exists('src/infos.txt'):
        with open('src/infos.txt', 'r') as file:
            text = file.read()
        with open('src/infos.txt', 'w') as file:
            new_text = text + ',' + client
            file.write(new_text)
    else:
        with open('src/infos.txt', 'w') as file:
            new_text = str(1) + ';' + str(2020) + ';' + client
            file.write(new_text)
    print('Client Added')


def change_client_address(name, n_street, p_code_city, country):
    with open('src/infos.txt', 'r') as file:
        text = file.read().split(';')
        counter = int(text[0])
        clients = text[2].split(',')
        for i, client in enumerate(clients):
            if name.lower() == client.split("\\\\")[0].lower():
                clients[i] = name + "\\\\" + \
                             n_street + "\\\\" + \
                             p_code_city + "\\\\" + \
                             country
            else:
                return 1
        with open('src/infos.txt', 'w') as file:
            new_text = text[0] + ';' + text[1] + ';' + ','.join(clients)
            file.write(new_text)
    print('Address changed')


def generate_invoice(client, activities, date, tva, amounts, currency, rate):
    currency = "EURO" if currency.lower() in "euro" else "MAD"
    with open('src/infos.txt', 'r') as file:
        text = file.read().split(';')
        counter = int(text[0])
        lines = text[2].split(',')
        for line in lines:
            if client.lower() == line.split("\\\\")[0].lower():
                client = line
                break
        else:
            return 1
    if tva < 0:
        return 2
    if rate < 0:
        return 4
    with open('template.tex', 'r') as tex_file:
        text = tex_file.read()
        text_new = text.replace('ADDRESS', client)
        text_new = text_new.replace('CURRENCY', currency)
        text_new = text_new.replace('DATE', date)
        text_new = text_new.replace('TVA', str(tva))
        text_new = text_new.replace('ACTIVITY1', '\\Fee{' + str(activities[0]) + '}{' + str(amounts[0]) + '} {1}')
        if amounts[1] != 0:
            text_new = text_new.replace('ACTIVITY2', '\\Fee{' + str(activities[1]) + '}{' + str(amounts[1]) + '} {1}')
        else:
            text_new = text_new.replace('ACTIVITY2', '')
        if amounts[2] != 0:
            text_new = text_new.replace('ACTIVITY3', '\\Fee{' + str(activities[2]) + '}{' + str(amounts[2]) + '} {1}')
        else:
            text_new = text_new.replace('ACTIVITY3', '')
        if amounts[3] != 0:
            text_new = text_new.replace('ACTIVITY4', '\\Fee{' + str(activities[3]) + '}{' + str(amounts[3]) + '} {1}')
        else:
            text_new = text_new.replace('ACTIVITY4', '')
        if amounts[4] != 0:
            text_new = text_new.replace('ACTIVITY4', '\\Fee{' + str(activities[4]) + '}{' + str(amounts[4]) + '} {1}')
        else:
            text_new = text_new.replace('ACTIVITY4', '')
        if amounts[5] != 0:
            text_new = text_new.replace('ACTIVITY5', '\\Fee{' + str(activities[5]) + '}{' + str(amounts[5]) + '} {1}')
        else:
            text_new = text_new.replace('ACTIVITY5', '')
        text_new = text_new.replace('COUNTER', str(counter))
        if sum(amounts) < 0:
            text_new = text_new.replace('Facture', 'Avoir')
        if tva == 0:
            text_new = text_new.replace('NOTE',
                                        '''\\begin{center}
                                         \\footnotesize
                                         \\textsc{ARTICLE 92 - Exonération avec droit à déduction}
                                         \\end{center}''')
        else:
            text_new = text_new.replace('NOTE', ' ')
        with open('invoice.tex', 'w') as output:
            output.write(text_new)
        with open('src/infos.txt', 'r') as file:
            print("READING TEXT")
            text = file.read().split(';')
    x = subprocess.run('pdflatex invoice.tex', shell=True, check=True)
    if x != 0:
        print('Exit-code not 0, generating invoice.pdf file')
    x = subprocess.run('rm invoice.log invoice.aux invoice.tex', shell=True, check=True)
    if x != 0:
        print('Exit-code not 0, removing auxiliary files!')
    counter -= 1
    verify_window = VerificationWindow(flag="Generate",
                                       counter=counter,
                                       date=date,
                                       client=client,
                                       currency=currency,
                                       tva=tva,
                                       amounts=amounts,
                                       rate=rate)
    verify_window.show()
    x = subprocess.run("open invoice.pdf", shell=True, check=True)
    if x != 0:
        print('Exit-code not 0, check result in the folder!')
    return 0


def restore():
    if os.path.exists('src/infos.txt'):
        with open('src/infos.txt', 'r') as file:
            text = file.read().split(';')
        with open('src/infos.txt', 'w') as file:
            new_text = str(1) + ';' + str(int(text[1]) + 1) + ";" + text[2]
            file.write(new_text)
        if os.path.exists('invoices.csv'):
            x = subprocess.run('mv invoices.csv factures/invoices_{}.csv'.format(text[1]), shell=True, check=True)
            if x != 0:
                print('Exit-code not 0, deleted history')
    return 3

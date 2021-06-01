import os
import subprocess
import csv
import shutil
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from tex_files import *

DEFAULT_ROOT = r"~/Documents/Invoices"


def preamble(invoicer):
    current_path = os.getcwd()
    os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
    with open("invoicelabels.sty", "w", encoding="utf-8") as tex_file:
        tex_file.write(tex_invoicelabels)
    with open("invoice.sty", "w", encoding="utf-8") as tex_file:
        tex_file.write(tex_invoice)
    os.chdir(os.path.expanduser(current_path))


def check_exists(root):
    return os.path.isfile(root)


def check_path():
    current_path = os.getcwd()
    os.chdir(os.path.expanduser(r"~/Documents"))
    if not os.path.isdir("Invoices"):
        os.mkdir("Invoices")
        os.chdir(os.path.expanduser(DEFAULT_ROOT))
        for invoicer in ['La Mome', 'Marina']:
            os.mkdir(invoicer)
            if invoicer == 'La Mome':
                shutil.copyfile(os.path.join(current_path, "logo.png"), 
                                os.path.join(os.path.expanduser(invoicer), "logo.png"))
    os.chdir(os.path.expanduser(current_path))


def compile_tex(invoicer):
    current_path = os.getcwd()
    try:
        os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
    except FileNotFoundError:
        os.mkdir(invoicer)
        os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
        if invoicer == 'La Mome':
            shutil.copyfile(os.path.join(current_path, "logo.png"), "logo.png")
        preamble(invoicer)
    os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))    
    try:
        subprocess.run(["pdflatex", "invoice.tex"], shell=False)
    except (OSError, IOError) as _:
         pass
    files = ["invoice.tex", "invoice.aux", "invoice.log", "invoice.sty", "invoicelabels.sty"]
    for file in files:
        try:
            os.remove(file)   
        except FileNotFoundError:
            pass 
    os.chdir(os.path.expanduser(current_path))


class ClientAlreadyInDatabase(Exception):
    pass


class ClientNotFoundException(Exception):
    pass


class VerificationWindow(QWidget):
    def __init__(self,
                 flag="Ordinary",
                 counter=None,
                 date=None,
                 client=None,
                 invoicer=None,
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
            self.invoicer = invoicer
            self.rate = rate
            self.label = QLabel(self)
            self.label.setText('Do you want to generate finalize invoice?')
            self.label.move(60, 20)

            self.button_confirm = QPushButton(self)
            self.button_confirm.setText("continue")
            self.button_confirm.move(240, 65)
            self.button_confirm.clicked.connect(lambda: self.finalise())

            self.button_roll_Back = QPushButton(self)
            self.button_roll_Back.setText("Rollback")
            self.button_roll_Back.move(20, 65)
            self.button_roll_Back.clicked.connect(lambda: self.roll_back())

        elif flag == "Ordinary":
            self.label = QLabel(self)
            self.label.setText('Do you want to proceed?')
            self.label.move(100, 20)

            self.button_confirm = QPushButton(self)
            self.button_confirm.setText("continue")
            self.button_confirm.move(240, 65)

            self.button_cancel = QPushButton(self)
            self.button_cancel.setText("Cancel")
            self.button_cancel.move(20, 65)

    def finalise(self):
        fieldnames = ['N.',
                      'Client',
                      'Date',
                      'Amount in MAD HT',
                      'Amount in MAD TTC',
                      'TVA',
                      'Amount in EURO',
                      'Rate of conversion']
        self.client = self.client.split("\\\\")[0]
        if os.path.exists(self.invoicer + '_invoices.csv'):
            with open(self.invoicer + '_invoices.csv', 'a', encoding="utf-8", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writerow(get_dict(self.currency,
                                         self.counter,
                                         self.client,
                                         self.date,
                                         self.tva,
                                         sum(self.amounts),
                                         self.rate))
        else:
            with open(self.invoicer + '_invoices.csv', 'w', encoding="utf-8", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writeheader()
                writer.writerow(get_dict(self.currency,
                                         self.counter,
                                         self.client,
                                         self.date,
                                         self.tva,
                                         sum(self.amounts),
                                         self.rate))
        if self.counter < 10:
            padding = "000"
        elif self.counter < 100:
            padding = "00"
        elif self.counter < 1000:
            padding = "0"
        file_name = padding + str(self.counter) + "_" + self.date + "_" + self.client
        current_path = os.getcwd()
        os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), self.invoicer))
        subprocess.call(
            [
                "mv",
                "invoice.pdf",
                "{}.pdf".format(file_name),
            ],
            shell=False,
        )
        os.chdir(os.path.expanduser(current_path))
        if os.path.exists(self.invoicer + '_invoices.csv'):
            # os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
            shutil.copy(
                self.invoicer + '_invoices.csv',
                os.path.join(os.path.join(os.path.expanduser(DEFAULT_ROOT), self.invoicer), self.invoicer + '_invoices.csv'),
            )
        self.counter += 1
        with open(self.invoicer + "_infos.txt", "r", encoding="utf-8") as file:
            text = file.read().split(";")
        with open(self.invoicer + "_infos.txt", "w", encoding="utf-8") as file:
            new_text = str(self.counter) + ";" + text[1] + ";" + text[2]
            file.write(new_text)
        self.destroy()

    def roll_back(self):
        current_path = os.getcwd()
        os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), self.invoicer))
        subprocess.call(
            ["rm", "invoice.pdf"],
            shell=False,
        )
        os.chdir(os.path.expanduser(current_path))
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


def add_client(name, n_street, rest, ice):
    if os.path.exists("La Mome_infos.txt"):
        with open("La Mome_infos.txt", "r", encoding="utf-8") as file:
            text = file.read()
        for client in text.split(";")[2].split(","):
            if name == client.split("\\\\")[0]:
                raise ClientAlreadyInDatabase
        client = "\\textbf{{name}}" + "\\\\"
        client += n_street + "\\\\"
        client += rest + "\\\\"
        if ice != "":
            client += "\\textbf{ICE}: " + ice
        with open("La Mome_infos.txt", "w", encoding="utf-8") as file:
            new_text = text + "," + client
            file.write(new_text)
    else:
        with open("La Mome_infos.txt", "w", encoding="utf-8") as file:
            new_text = str(1) + ";" + str(2020) + ";Divers"
            file.write(new_text)
        add_client(name, n_street, rest, ice)


def change_client_address(name, n_street, rest):
    try:
        with open("La Mome_infos.txt", "r", encoding="utf-8") as file:
            text = file.read().split(";")
            clients = text[2].split(",")
            found = False
            for i in range(len(clients)):
                if name.lower() == clients[i].split("\\\\")[0].lower():
                    clients[i] = (
                        name
                        + "\\\\"
                        + n_street
                        + "\\\\"
                        + rest
                        + (
                            "\\\\" + clients[i].split("\\\\")[-1]
                            if "ICE" in clients[i].split("\\\\")[-1]
                            else ""
                        )
                    )
                    found = True
            if not found:
                raise ClientNotFoundException
            with open("La Mome_infos.txt", "w", encoding="utf-8") as file:
                new_text = text[0] + ";" + text[1] + ";" + ",".join(clients)
                file.write(new_text)
    except:
        return 1


def get_tex_invoice(
    paiment_mode,
    invoicer,
    client,
    date_e,
    date_f,
    tva,
    year,
    amounts,
    designations,
    counter,
    currency,
):
    if invoicer == 'La Mome':
        tex_new = tex_template_la_mome.replace("ADDRESS", client)
    elif invoicer == 'Marina':
        tex_new = tex_template_marina.replace("ADDRESS", client)
    if date_e == "":
        tex_new = tex_new.replace("DATEE", "")
    else:
        tex_new = tex_new.replace("DATEE", "Date d'écheance: " + date_e + "\\\\")
    tex_new = tex_new.replace("DATEF", date_f)
    tex_new = tex_new.replace("TVA", str(tva))
    tex_new = tex_new.replace('CURRENCY', currency)
    tex_new = tex_new.replace("YEAR", year)
    if paiment_mode == "Transfer":
        tex_new = tex_new.replace("PAIMENTMODE", "Par virement")
    elif paiment_mode == "In cash":
        tex_new = tex_new.replace("PAIMENTMODE", "En espèce")
    else:
        tex_new = tex_new.replace("PAIMENTMODE", "Par chèque")
    activities = []
    for i in range(len(amounts)):
        if amounts[i] != 0:
            activities += ["\\Fee{{{}}}{{{}}} {{1}}".format(designations[i], amounts[i])]
        else:
            break
    tex_new = tex_new.replace("ACTIVITIES", "".join(activities))
    padding = ""
    if counter < 10:
        padding = "000"
    elif counter < 100:
        padding = "00"
    elif counter < 1000:
        padding = "0"
    tex_new = tex_new.replace("COUNTER", padding + str(counter))
    if sum(amounts) < 0:
        tex_new = tex_new.replace("Facture", "Avoir")
    if tva == 0:
        tex_new = tex_new.replace('NOTE','''\\begin{center}
                                            \\footnotesize
                                            \\textsc{ARTICLE 92 - Exonération avec droit à déduction}
                                            \\end{center}''')
    else:
         tex_new = tex_new.replace('NOTE', ' ')                          
    return tex_new
    

def generate_invoice(client, invoicer, activities, date_f, date_e, tva, amounts, currency, rate, paiment_mode,):
    currency = "EURO" if currency.lower() in "euro" else "MAD"
    with open('La Mome_infos.txt', 'r', encoding="utf-8") as file:
        text = file.read().split(';')
        counter = int(text[0])
        lines = text[2].split(',')
        for line in lines:
            infos = line.split("\\\\")
            if client == infos[0]:
                client = line.replace('\\textbf\\textsc{{{}}}'.format(infos[0]),
                                      infos[0],)
                break
        else:
            return 1
    year = text[1]
    if tva < 0:
        return 2
    if rate < 0:
        return 4
    current_path = os.getcwd()
    preamble(invoicer)
    os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
    with open('invoice.tex', 'w', encoding="utf-8") as output:
        output.write(get_tex_invoice(paiment_mode,
                                    invoicer,
                                    client,
                                    date_e,
                                    date_f,
                                    tva,
                                    year,
                                    amounts,
                                    activities,
                                    counter,
                                    currency,))
    compile_tex(invoicer)
    verify_window = VerificationWindow(
        flag="Generate",
        counter=counter,
        date=date_e,
        client=client,
        invoicer=invoicer,
        tva=tva,
        amounts=[
            amount for amount in amounts
        ],
        currency=currency,
        rate=rate,
    )
    verify_window.show()
    subprocess.Popen(
        ["open", "invoice.pdf"],
        shell=False,
    )
    os.chdir(os.path.expanduser(current_path))
    return 0


def restore():
    for invoicer in ['La Mome', 'Marina']:
        if os.path.exists(invoicer + '_infos.txt'):
            with open(invoicer + '_infos.txt', "r", encoding="utf-8") as file:
                text = file.read().split(";")
            with open(invoicer + '_infos.txt', "w", encoding="utf-8") as file:
                new_text = str(1) + ";" + str(int(text[1]) + 1) + ";" + text[2]
                file.write(new_text)
        if os.path.exists(invoicer + '_invoices.csv'):
            current_path = os.getcwd()
            os.chdir(os.path.join(os.path.expanduser(DEFAULT_ROOT), invoicer))
            shutil.move(
                os.path.join(current_path, invoicer + '_invoices.csv'),
                "invoices_{}.csv".format(text[1]),
            )
        os.mkdir("Invoices " + str(text[1]))
        for file in os.listdir("."):
            if os.path.isfile(file) and file[0].isnumeric():
                shutil.move(
                    file,
                    os.path.join("Invoices " + str(text[1]), file),
                )
        os.chdir(os.path.expanduser(current_path))
    return 3

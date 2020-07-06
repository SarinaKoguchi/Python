class CellPhone:
    def __init__(self, tel_numer, mail_address):
        self.tel_numer = tel_numer
        self.mail_address = mail_address

    def call(self):
        print(f"{self.tel_numer}から発信します")
    
    def send_mail(self):
        print(f"{self.mail_address}から送信します")
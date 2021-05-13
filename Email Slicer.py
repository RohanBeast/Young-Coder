import random

class Extractor:
    def __init__(self, email, name):
        self.email = email
        self.name = name
    
    def emailSlicer(self):
        email = self.email

        witCOM = ""
        domain = ""

        if "www" in email:
            email = email.replace("www.", "")
            witCOM = witCOM + email
        
        if ".com" in witCOM:
            e = witCOM.replace(".com", "")
            domain = domain + e
        
        return domain
    
    def emailMaker(self):
        name = self.name

        ext_ls = [".com", ".co.in", ".in"]
        ext = random.choices(ext_ls)[0]

        web = f"www.{name}{ext}"

        return web


if __name__ == "__main__":
    inp1 = input("Enter the name: ")
    inp2 = input("Enter an email: ")

    app = Extractor(inp2, inp1)
    print(app.emailMaker())
    print(app.emailSlicer())
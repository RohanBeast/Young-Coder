import os

class Extractor:
    def __init__(self, path):
        self.path = path
    
    def main(self):
        os.chdir(self.path)
        files = os.listdir(self.path)
        req = []
        emails = []

        for item in files:
            ext = os.path.splitext(item)[1]

            if ext == ".txt":
                req.append(item)
            
        if len(req) == 0:
            return "No Text File Found"
        else:
            for item in req:
                with open(item) as f:
                    r = f.read().split()

                for item in r:
                    if "@" in item:
                        emails.append(item)
                    else:
                        pass
        
            return emails

if __name__ == "__main__":
    app = Extractor("E:/Python_projects")

    if app.main() != "No Text File Found":
        for item in enumerate(app.main()):
            print(f"Email{item[0] + 1}: {item[1]}")
    else:
        print(app.main())
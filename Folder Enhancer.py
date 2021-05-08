import os

class Prettifier:
    def __init__(self, path):
        self.path = path
    
    def fileList(self):
        os.chdir(self.path)
        files = os.listdir(self.path)

        for item in enumerate(files):
            ext = os.path.splitext(item[1])[1]
            os.rename(item[1], f"File_{item[0]}.{ext}")

if __name__ == "__main__":
    path = input("Enter the path: ")
    a = Prettifier(path)
    a.fileList()
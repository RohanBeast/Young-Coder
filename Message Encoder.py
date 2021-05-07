import random
import time

class Encoder:
    def __init__(self, message):
        self.message = message
    
    def randomGenerator(self):
        letters = [
            "$",
            "%",
            "*",
            "@",
            "!",
            "/",
            "^"
        ]

        n1 = random.randint(0, len(letters))

        chosen = []
        for item in enumerate(letters):
            if item[0] == n1:
                try:
                    chosen.append(item[1])
                    chosen.append(letters[n1 - 1])
                except Exception:
                    chosen.append(item[1])
                    chosen.append(letters[n1 + 1])
        
        return chosen
    
    def encoder(self):
        variables = self.randomGenerator()

        index1 = random.randint(0, len(self.message))
        index2 = random.randint(0, len(self.message))

        if index1 == index2:
            index2 = random.randint(0, len(self.message))
        else:
            pass
        
        ls = []        
        for item in self.message:
            if item != " ":
                ls.append(item)
            else:
                item = ""
                ls.append(item)
        
        ls.insert(index1, variables[0])
        ls.insert(index2, variables[1])

        final_str = "".join(ls)
        return final_str
    
if __name__ == "__main__":
    message = input("Enter the Message: ")
    a = Encoder(message=message)
    print(a.encoder())
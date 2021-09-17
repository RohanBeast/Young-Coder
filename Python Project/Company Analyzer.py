import requests
import json

def main(key):
    url = f"https://api.polygon.io/v1/meta/symbols/{key}/company?apiKey=CJCWHxWZis6VyrFZKJnp392ogEbimsdC"

    try:
        index = requests.get(url)
        js = json.loads(index.text)
        obj = {"name":js["name"], "sector":js["sector"], "symbol":js["symbol"], "description":js["description"]}

        for item in obj.keys():
            print(f"{item}: {obj.get(item)}")
        
        print("\n")
    except Exception as error:
        print(error)
        print("\n")

if __name__ == "__main__":
    while True:
        key = input("Enter the key: ")
        main(key)

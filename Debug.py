import os
os.remove("./log.txt")

env = "dev"

def debugLog(msg,/,title=""):
    if env == "dev":
        with open("./log.txt","a") as f:
            f.write(f"{title} => {msg}\n")
        print(f"debugLog: {title} => {msg}")

def logging(title, msg):
    with open("./log.txt","a") as f:
        f.write(f"{title} : {msg}\n")
    print(f"{title} : {msg}")
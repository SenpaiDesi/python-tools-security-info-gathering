import zipfile
from tqdm import tqdm

# title screen
print("*"  * 100 + "")
print("Zip cracker made by Senpai_Desi\n")
print("*" * 100)


#config
passlist = input("Please provide the wordlist file (example: rockyou.txt) ")
to_crack_zip = input("Please provide the zip file you want to crack... (example: test.zip)")



# init
zf= zipfile.ZipFile

# Count the words
wordcounter = len(list(open(passlist, "rb")))
print(f"Checking {wordcounter} passwords....\n ")


with open(passlist, "rb") as wl:
    for word in tqdm(wl, total=wordcounter, unit = "Word"):
        try:
            zf.extractall(pwd = word.strip())
        except Exception:
            continue
        else:
            print(f"[==] Password found: ", word.decode().strip())
            exit(0)

print("[!] Password not found in the list. Try another list instead.")

import crypt

def cracker(cryptPass):
    global passfile
    salt = cryptPass[0:2]
    tries = 0

    print("-" * 100)
    print("Please input the file location with extension for the list...")
    print("-" * 100)
    dictfile = input("Provide full path + extension. Example: Path/To/File.txt")

    dictfile = open(dictfile, 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word.salt)
        tries + 1
        if cryptWord == cryptPass:
            print(f"Password Found at try {tries}! Password {word}")
        print("No password was found!")    
        return
    
    def main():
        passFile_request = input("Please provide the path to the password file: ")
        passFile = open(passFile_request)
        for line in passFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                cryptPass = line.split(':')[1].strip(' ')
                print(f"Craclomg password for {user}")
                cracker(cryptPass)
    
    if __name__ == '__main__':
        main()
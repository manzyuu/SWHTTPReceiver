import sys
import threading

class CUIApp:
    def __init__(self):
        self.log_lines = []
        self.command = ""

    def run(self):
        threading.Thread(target=self.display_log,daemon=True).start()
        while True:
            self.command = input("\033[1F\033[K> ")

    def display_log(self):
        while True:
            sys.stdout.write("\033[2J\033[H")
            for line in self.log_lines[-20:]:
                print(line)
            sys.stdout.flush()
            sys.stdout.write("\033[K" + self.command + "\n")
            sys.stdout.flush()
            threading.Event().wait(1)

    def add_log(self, message):
        self.log_lines.append(message)
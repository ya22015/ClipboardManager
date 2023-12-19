import pyperclip
import time
from pystray import MenuItem as item
from pystray import Icon as icon, Menu as menu
from PIL import Image

class ClipboardManager:
    def __init__(self, max_history_size=50, history_file_path='clipboard_history.txt'):
        self.max_history_size = max_history_size
        self.history_file_path = history_file_path
        self.icon = self.create_system_tray_icon()
        self.counter = 1  # Initialize counter
        self.load_history_from_file()

    def add_to_history(self, text):
        if text in self.unique_entries:
            # Remove the old entry with the same text
            self.clipboard_history = [e for e in self.clipboard_history if not e.endswith(text)]
            self.unique_entries.discard(text)

        entry = text
        self.counter += 1

        # Add the new entry to the beginning of the history
        self.clipboard_history.insert(0, entry)
        self.unique_entries.add(text)

        # Trim history to the maximum size
        self.clipboard_history = self.clipboard_history[:self.max_history_size]
        self.unique_entries = set(self.clipboard_history)

        self.save_history_to_file()

    def load_history_from_file(self):
        try:
            with open(self.history_file_path, 'r') as file:
                self.clipboard_history = [line.strip() for line in file.readlines()]
                self.unique_entries = set(self.clipboard_history)
        except FileNotFoundError:
            self.clipboard_history = []
            self.unique_entries = set()

        # Trim loaded history to the maximum size
        self.clipboard_history = self.clipboard_history[:self.max_history_size]
        self.unique_entries = set(self.clipboard_history)

    def save_history_to_file(self):
        with open(self.history_file_path, 'w') as file:
            for entry in self.clipboard_history:
                file.write(f"{entry}\n")
                file.write("-" * 60 + "\n")  # Add a separator after each entry

    def get_clipboard_history(self):
        return self.clipboard_history

    def clear_clipboard_history(self):
        self.clipboard_history = []
        self.unique_entries = set()
        self.save_history_to_file()

    def create_system_tray_icon(self):
        # Update the path to your icon image
        image_path = "clippy.png"
        image = Image.open(image_path)
        menu_items = [item('Exit', self.exit)]
        return icon("name", image, menu=menu(*menu_items))

    def run_clipboard_manager(self):
        print("Clipboard Manager is running. Right-click the system tray icon to exit.")

        try:
            while True:
                current_clipboard_data = pyperclip.paste()
                self.add_to_history(current_clipboard_data)
                time.sleep(1)

        except KeyboardInterrupt:
            self.icon.stop()

    def exit(self, icon, item):
        print("Clipboard Manager terminated.")
        icon.stop()

if __name__ == "__main__":
    clipboard_manager = ClipboardManager()
    clipboard_manager.run_clipboard_manager()

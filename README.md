# ClipboardManager

Great! Here's a write-up for your GitHub repository:

---

# Clipboard Manager

## Overview

The Clipboard Manager is a simple Python script that serves as a background clipboard manager, monitoring the system clipboard and maintaining a history of clipboard entries. Users can conveniently access this history through a system tray icon.

## Features

### 1. ClipboardManager Class

- **Initialization:** The `ClipboardManager` class is initialized with parameters such as `max_history_size` (indicating the maximum number of entries to keep in the history) and `history_file_path` (specifying the file for persisting clipboard history).

- **Functionality:** The class provides various methods for managing clipboard entries, including adding entries to the history, loading history from a file, saving history to a file, retrieving the clipboard history, clearing the clipboard history, and creating a system tray icon.

### 2. System Tray Icon

- **Creation:** The system tray icon is implemented using the `pystray` library.

- **Context Menu:** The icon is associated with a right-click context menu that includes a single option, "Exit." Selecting this option triggers the `exit` method, terminating the program.

### 3. Main Execution

- **Continuous Monitoring:** Upon instantiation of the `ClipboardManager` class, the `run_clipboard_manager` method is called, initiating the continuous monitoring of the system clipboard.

- **History Management:** The script adds new entries to the clipboard history and sleeps for 1 second between checks.

- **Termination:** The program can be gracefully terminated by right-clicking on the system tray icon and selecting "Exit."

### 4. Exit Method

- **Graceful Termination:** The `exit` method is responsible for stopping the system tray icon when the program is terminated.

### 5. File Handling

- **Persistence:** The clipboard history is loaded from and saved to a file (`clipboard_history.txt`).

- **Separator:** Entries in the file are separated by a line of dashes ("----------") for improved readability.

## Usage

1. Clone the repository: `git clone https://github.com/ya22015/clipboard-manager.git`
2. Navigate to the project directory: `cd clipboard-manager`
3. Run the script: `python clipboard_manager.py`

## Configuration

- Update the path to your icon image in the `create_system_tray_icon` method.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.

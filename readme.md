# Flow Track

Flow Track is a desktop application built using Electron and Python that allows users to track tasks and replay recorded events. It provides a simple interface to start and stop task tracking, save task data, and replay tasks for analysis.

## Features

- Start and stop task tracking.
- Save task data as JSON files.
- Replay recorded tasks using Python scripts.
- User-friendly tray menu for quick access.

## Installation Guide

### Prerequisites

1. Install [Node.js](https://nodejs.org/) (v14 or higher).
2. Install [Python](https://www.python.org/) (v3.6 or higher).
3. Ensure `pip` is installed for Python package management.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flow-track
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Install Python dependencies:
   ```bash
   pip install pynput
   ```

4. Create a `tasks` folder in the project directory (if not already created):
   ```bash
   mkdir tasks
   ```

## Usage Guide

### Starting the Application

1. Run the application:
   ```bash
   npm run start
   ```

2. The application will open a window with options to start a task or replay tasks.

### Task Tracking

1. Enter a task name in the input field and click "Start Task" to begin tracking.
2. Click "Stop Task" to end tracking. The task data will be saved as a JSON file in the `tasks` folder.

### Replaying Tasks

1. The application lists all saved tasks in the `tasks` folder.
2. Click the "Replay" button next to a task to replay it. The replay is handled by the Python `replay.py` script.

### Tray Menu

- The tray menu provides quick access to:
  - Show the application window.
  - Quit the application.

### Error Handling

- If an error occurs while starting the app, it will be logged in the console.
- Ensure all dependencies are installed and the `tasks` folder exists.

## File Structure

- `main.js`: Main Electron process handling app lifecycle and IPC communication.
- `preload.js`: Exposes APIs to the renderer process securely.
- `index.html`: Frontend interface for task management.
- `logger.py`: Python script for logging task events.
- `replay.py`: Python script for replaying recorded tasks.
- `tasks/`: Directory where task JSON files are stored.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

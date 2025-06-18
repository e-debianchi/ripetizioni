# Ripetizioni

`ripetizioni.py` is a Python-based application designed to help tutors manage their lessons and payments efficiently. The application provides a simple and intuitive interface for tracking lesson counts, monthly progress, and total earnings for each student.

## 📦 Features

- **Dynamic Table Management**: Displays a table with students' names, payment rates, and lesson counts for each month.
- **Increment Buttons**: Easily update lesson counts for each student using "+1" and "+2" buttons.
- **Monthly Totals**: Automatically calculates and displays monthly totals based on lesson counts and payment rates.
- **Add New Students**: Add new rows dynamically by entering the student's name and payment rate. The table and JSON file are updated automatically.
- **Data Persistence**: Saves all data to a JSON file, ensuring that progress is not lost when the application is closed.
- **Customizable UI**: Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern and user-friendly interface.

## ⚙️ How It Works

1. **Table Setup**: The table includes columns for payment rates and lesson counts for each month (September to June).
2. **Increment Lessons**: Use the "+1" and "+2" buttons to update lesson counts for the current month.
3. **Add New Students**: Click the "Add Row" button to input a new student's name and payment rate. A new row is added to the table with zeroed-out lesson counts.
4. **Save and Load Data**: All changes are saved to a JSON file (`ripetizioni.json`) and automatically loaded when the application starts.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/5e77e/ripetizioni.git
   cd ripetizioni

2. Install Custom TkInter
   ```bash
   pip install customtkinter
  
3. Run the application
   ```bash
   python ripetizioni.py

## 🚀 Usage

- Use the buttons in the table to update lesson counts.
- Add new students by clicking the "Add Row" button.
- Close the application to automatically save data.

## 📝 JSON File

The application uses a JSON file (`ripetizioni.json`) to store all data. If the file does not exist, it will be created automatically.

## 💾 Build as Executable

To create a standalone executable, use [PyInstaller](https://pyinstaller.org/):
```bash
   pyinstaller ripetizioni.py --onefile --windowed

# Maple Buff Timer

## Description

The Maple Buff Timer is a Python script designed to manage multiple buff timers for MapleStory. It allows you to set customizable timers for buffs, reset them with specific keys, and alerts you when it's time to refresh your buffs. The script saves your timer settings in a configuration file and can be easily run from an executable.

## Features

- Configurable buff timers with customizable durations.
- Reset timers using specific keys.
- Alarm sound to alert you when the timer expires.
- Saves timer settings to a configuration file for easy reuse.
- Compiled executable for easy distribution and use.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. [Download Python](https://www.python.org/downloads/)
- **Dependencies**: The script requires the `keyboard` library. This will be installed automatically when you install the executable.

### Running executable (easiest option)
  1. Download: **Maple Buff Timer v1.0** folder from releases on right hand side of git page and run maple_buff_timer.exe


### Running the Script from source

1. **Download the Repository**:

   Clone the repository or download the ZIP file from GitHub.

   ```bash
   git clone https://github.com/Fontodbz/maple_buff_timer.git
   ```
2. **Navigate to the Project Directory**:
   Open cmd
   ```
   cd path/to/maple_buff_timer
   ```
4. **Install Dependencies**:
  ```
  pip install -r requirements.txt
  ```
5. **Run the script using Python**:
   ```
   python maple_buff_timer.py
   ```
   
The script will automatically create a config.json file in the same directory where it is run. This file contains your timer settings and will be loaded automatically each time you start the script or executable.

You can manually edit config.json to change your buff settings. The format is as follows:

```JSON
{
    "buffs": [
        {
            "name": "Holy Symbol",
            "duration": 120,
            "reset_key": "r"
        },
        {
            "name": "Maple Warrior",
            "duration": 330,
            "reset_key": "5"
        }
    ]
}
```

Troubleshooting:
Executable Not Found: Ensure that the executable is in the correct directory and has the right permissions. On Windows, right-click and select Run as administrator.

Dependencies Issue: If running the script from source, make sure all dependencies are installed. 
Run 
```
pip install -r requirements.txt to resolve missing packages.
```

Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests for any new features or bug fixes.

License:

This project is licensed under the MIT License - see the LICENSE file for details.

Contact:

For any questions or feedback, please open an issue on the GitHub repository.

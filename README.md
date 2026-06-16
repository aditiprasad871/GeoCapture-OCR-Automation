A Python automation script that opens Google Maps in Chrome, activates live location, extracts the current latitude and longitude, overlays the coordinates on the map, takes a screenshot, performs OCR on the screenshot, and saves the results to a text file.

## Features

- Launches Google Maps with geolocation permission enabled
- Activates the "Your location" button
- Extracts GPS coordinates from the map URL
- Displays live coordinates on the map page
- Simulates a blink effect with desktop automation
- Captures a screenshot of Google Maps
- Uses Spire OCR to read text from the screenshot
- Logs the coordinates and OCR output to `location_output.txt`
- Runs continuously until `ESC` is pressed

## Requirements

- Python 3.x
- Google Chrome installed
- ChromeDriver installed and available in `PATH`
- `selenium` Python package
- `pyautogui` Python package
- `keyboard` Python package
- Spire OCR package and a local model path

## Installation

1. Install Python dependencies:

```powershell
pip install selenium pyautogui keyboard
```

2. Download the ChromeDriver version that matches your installed Chrome browser and add it to `PATH`.

3. Ensure the Spire OCR model files are available and update the path in `Autolocation.py` if needed.

## Usage

1. Open a terminal in `d:\Downloads Backup\model`
2. Run the script:

```powershell
python Autolocation.py
```

3. Wait for the script to open Google Maps and activate live location.
4. Press `ESC` at any time to stop the script.

## Output

- `google_map.png`: latest screenshot of Google Maps
- `location_output.txt`: appended GPS coordinates, timestamp, and OCR text

## Notes

- The script uses desktop automation and may require the system to remain unlocked and the browser window visible.
- If the script cannot find the live location button, it will continue running and retry on the next refresh.
- Update `configureOptions.ModelPath` in `Autolocation.py` to point to your Spire OCR model directory.

## Important

This automation is designed for Windows and depends on the current UI and browser behavior. If Google Maps changes its page structure or button labels, the script may require updates.

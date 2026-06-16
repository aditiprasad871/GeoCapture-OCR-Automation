import time
import keyboard
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from spire.ocr import *

# ==========================================
# 1. CHROME + LIVE GPS SETUP
# ==========================================

chrome_options = Options()

chrome_options.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.geolocation": 1
    },
)

driver = webdriver.Chrome(options=chrome_options)

print("Opening Google Maps...")

driver.get("https://www.google.com/maps")

time.sleep(10)

# ==========================================
# 2. CLICK LIVE LOCATION BUTTON
# ==========================================

try:
    location_btn = driver.find_element(
        By.CSS_SELECTOR,
        'button[aria-label*="Your location"]'
    )

    location_btn.click()

    print("Live location activated")

except Exception as e:
    print("Location button not found:", e)

time.sleep(10)

# ==========================================
# 3. GET GEO COORDINATES
# ==========================================

def get_coordinates():

    try:
        current_url = driver.current_url

        # example:
        # https://www.google.com/maps/@22.5726,88.3639,15z

        if "/@" in current_url:

            coords_part = current_url.split("/@")[1]

            latitude = coords_part.split(",")[0]
            longitude = coords_part.split(",")[1]

            return latitude, longitude

    except:
        pass

    return "Not Found", "Not Found"

# ==========================================
# 4. SHOW COORDINATES ON MAP
# ==========================================

def show_coordinates_on_map(lat, lon):

    js = f"""
    let oldBox = document.getElementById('liveCoords');

    if(oldBox){{
        oldBox.remove();
    }}

    let div = document.createElement('div');

    div.id = 'liveCoords';

    div.innerHTML =
        'Latitude : {lat}<br>Longitude : {lon}';

    div.style.position = 'fixed';
    div.style.top = '18px';
    div.style.left = '20px';
    div.style.zIndex = '999999';
    div.style.background = 'black';
    div.style.color = 'white';
    div.style.fontSize = '18px';
    div.style.padding = '9px';
    div.style.borderRadius = '10px';
    div.style.fontWeight = 'bold';

    document.body.appendChild(div);
    """

    driver.execute_script(js)

# ==========================================
# 5. BLINK EFFECT
# ==========================================

def blink_effect():

    print("Simulating blink effect...")

    pyautogui.moveRel(20, 0, duration=0.1)
    pyautogui.moveRel(-20, 0, duration=0.1)

    time.sleep(1)

    pyautogui.hotkey('alt', 'tab')

    time.sleep(0.3)

    pyautogui.hotkey('alt', 'tab')

    time.sleep(2)

# ==========================================
# 6. TAKE SCREENSHOT
# ==========================================

def take_map_screenshot():

    img_path = "google_map.png"

    driver.save_screenshot(img_path)

    print("Google Maps screenshot saved")

    return img_path

# ==========================================
# 7. OCR
# ==========================================

def run_ocr(img_path):

    scanner = OcrScanner()

    configureOptions = ConfigureOptions()

    configureOptions.ModelPath = r"D:\Downloads Backup\Downloads\win-x64"

    configureOptions.Language = "English"

    scanner.ConfigureDependencies(configureOptions)

    scanner.Scan(img_path)

    text = scanner.Text.ToString()

    return text

# ==========================================
# 8. SAVE OUTPUT
# ==========================================

def save_output(text, lat, lon):

    output_file = "location_output.txt"

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, "a", encoding="utf-8") as file:

        file.write("\n\n====================================\n")
        file.write("TIME : " + current_time + "\n")
        file.write("====================================\n\n")

        file.write(f"Latitude : {lat}\n")
        file.write(f"Longitude : {lon}\n\n")

        file.write(text)

    print("Text saved")

# ==========================================
# 9. MAIN LOOP
# ==========================================

print("\nSTARTED LIVE MAP TRACKING")
print("Press ESC anytime to stop\n")

while True:

    if keyboard.is_pressed('esc'):

        print("\nESC PRESSED")
        print("Stopping program...")

        break

    # refresh map
    driver.refresh()

    print("\nRefreshing live GPS map...")

    time.sleep(10)

    # click live location again
    try:
        location_btn = driver.find_element(
            By.CSS_SELECTOR,
            'button[aria-label*="Your location"]'
        )

        location_btn.click()

    except:
        pass

    time.sleep(8)

    # ======================================
    # GET LATITUDE & LONGITUDE
    # ======================================

    lat, lon = get_coordinates()

    print("Latitude :", lat)
    print("Longitude:", lon)

    # ======================================
    # SHOW COORDINATES ON MAP
    # ======================================

    show_coordinates_on_map(lat, lon)

    time.sleep(2)

    # ======================================
    # BLINK EFFECT
    # ======================================

    blink_effect()

    # ======================================
    # SCREENSHOT
    # ======================================

    img_path = take_map_screenshot()

    # ======================================
    # OCR
    # ======================================

    text = run_ocr(img_path)

    print("\n===== OCR OUTPUT =====\n")
    print(text)

    # ======================================
    # SAVE
    # ======================================

    save_output(text, lat, lon)

    print("\nLIVE LOCATION UPDATED ✔")

    # ======================================
    # WAIT
    # ======================================

    for i in range(300):

        if keyboard.is_pressed('esc'):

            print("\nESC PRESSED")
            print("Stopping instantly..")

            driver.quit()

            exit()

        time.sleep(0.1)

# ==========================================
# CLOSE
# ==========================================

driver.quit()

print("\nPROGRAM STOPPED SUCCESSFULLY")
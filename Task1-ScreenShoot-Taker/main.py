import pyautogui
import datetime

def take_screenshot():
    # Get the current date and time to use in the screenshot filename
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d")

    # Define the filename for the screenshot
    screenshot_file = f"Python_screenshot_{timestamp}.png"

    try:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot to the current working directory
        screenshot.save(screenshot_file)

        print(f"Screenshot saved as {screenshot_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    take_screenshot()

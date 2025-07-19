import pyautogui
import time
from ahk import AHK

def get_mouse_position():
    """Get current mouse position and display it"""
    x, y = pyautogui.position()
    print(f"Mouse position: X={x}, Y={y}")

def main():
    print("Mouse Position Tracker")
    print("Press 'b' to get mouse coordinates")
    print("Press 'q' to quit")
    print("-" * 30)

    # Initialize AHK
    ahk = AHK()

    try:
        while True:
            # Check if 'b' key is pressed
            if ahk.key_state('b'):
                get_mouse_position()
                # Wait for key to be released to prevent multiple readings
                while ahk.key_state('b'):
                    time.sleep(0.01)

            # Check if 'q' key is pressed to quit
            if ahk.key_state('q'):
                print("Exiting...")
                break

            # Small delay to prevent excessive CPU usage
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

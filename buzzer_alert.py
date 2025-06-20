import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def trigger_alert(reason):
    print(f"Alert: {reason}")
    for _ in range(3):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.2)

import requests, json
import pigpio
import time

API_KEY = ""

RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

pi = pigpio.pi()

# API Doc: https://openweathermap.org/current
def main():
	apiUrl = "http://api.openweathermap.org/data/2.5/weather"
	params = "?q=Berlin,de&units=metric&APPID=" + API_KEY
	url = apiUrl + params

	response = requests.get(url)
	data = json.loads(response.text)

	temperature = data["main"]["temp"]

	if temperature >= 20:
		pi.set_PWM_dutycycle(RED_PIN, 255)
		pi.set_PWM_dutycycle(GREEN_PIN, 0)
		pi.set_PWM_dutycycle(BLUE_PIN, 0)
		print("red light")

	if temperature >= 12 and temperature < 20:
		pi.set_PWM_dutycycle(RED_PIN, 255)
		pi.set_PWM_dutycycle(GREEN_PIN, 128)
		pi.set_PWM_dutycycle(BLUE_PIN, 0)
		print("orange light")

	if temperature < 12:
		pi.set_PWM_dutycycle(RED_PIN, 0)
		pi.set_PWM_dutycycle(GREEN_PIN, 0)
		pi.set_PWM_dutycycle(BLUE_PIN, 255)
		print("blue light")

	print(temperature)

if __name__ == "__main__":
	main()

time.sleep(0.5)

pi.stop()

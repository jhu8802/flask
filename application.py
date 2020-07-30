from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
	sensor = Adafruit_DHT.DHT11
	pin = 17
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	DHT = { 'temp' : temperature, 'humi' : humidity}
	return render_template('index.html',**DHT)
	
if __name__ == '__main__':
	app.run()
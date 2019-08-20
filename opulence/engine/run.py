from celery import Celery


ENGINE_BROKER = {
	"BROKER_URL" : 'redis://localhost:6379/0',
	"CELERY_RESULT_BACKEND" : 'redis://localhost:6379/0',
	"CELERY_DEFAULT_QUEUE": "engine"
}

app = Celery("engine")
app.conf.update(ENGINE_BROKER)


@app.task
def add():
	print("LOOOOOOOOOOOOL")
	return "loool"

from flask import Flask
from jinja2 import Environment, FileSystemLoader
import analysis

env = Environment(loader=FileSystemLoader('/home/manu/imagequick-analytics/web/templates/'))
template = env.get_template('base.html')


app = Flask(__name__)


@app.route('/')
def index():
	return template.render(items=analysis.voice_play)

if __name__ == '__main__':
    app.run(debug=True)
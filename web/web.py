from flask import Flask
from flask import render_template
import sys
sys.path.insert(0, '/home/manu/imagequick-analytics/')
import analysis
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('base.html',items=analysis.pretty_print(analysis.analyse_templates))

@app.route('/templates')
def web_templates_all():
	t =	analysis.pretty_print(analysis.analyse_templates)
	return render_template('base.html',items=t,title='Templates')

@app.route('/formats')
def web_formats_all():
	return render_template('base.html',title='Formats',items=analysis.pretty_print(analysis.analyse_formats))

@app.route('/voices')
def web_voices_all():
	return render_template('base.html',title='Voices',items=analysis.pretty_print(analysis.analyse_voices))

@app.route('/<i_type>/<name>')
def web_analyse(i_type,name):
	case = i_type.lower()
	if case =='voice':
		play,buy = analysis.analyse_voice(name.title())
		return render_template('single.html',b=buy,p=play,analyse_object=name,analyse_type=i_type)
	elif case == 'template':
		play,buy = analysis.analyse_template(name.lower())
		return render_template('single.html',b=buy,p=play,analyse_object=name,analyse_type=i_type)

if __name__ == '__main__':
    app.run(debug=True)
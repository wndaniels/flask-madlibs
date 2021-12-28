from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yupp1234'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route('/story')
def your_story():
    """Show Story"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)

from flask import Flask, render_template, flash, redirect, url_for, request
from snowplow_tracker import Tracker, Emitter, Subject, SelfDescribingJson
from forms import PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

e = Emitter('127.0.0.1:9090')
tracker = Tracker(e)

tracker.track_self_describing_event(SelfDescribingJson(
    "iglu:com.mustafa/post-hover/jsonschema/1-0-2",
    {
        "hover_time": 120

    }
))


@app.route('/')
def home():
    tracker.subject.set_useragent(request.headers.get('User-Agent'))
    return render_template('index.html')


@app.route('/posts')
def posts():
    tracker.track_page_view("http://127.0.0.1:5000")
    tracker.track_link_click("http://127.0.0.1:5000/posts")
    return render_template('post.html')


@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        tracker.track_form_submit("postForm")
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('newPost.html', title='New Post',
                           form=form, legend='New Post')


if __name__ == '__main__':
    app.run()

## Brief Description ##
This application mimics some of the processes of a standard blog site created using Flask, the tracker used was the Snowplow python tracker. There are three various things 
tracked by the piepline I established. Firstly when the user vists the home page, user agent data collected from the application is sent to the snowplow micro collector. Secondly 
when vieweing previous blogs the page and any links clicked are tracked and finally the submission of new entries via the form are also tracked.

## Initialisation ##
A basic emitter and tracker are established in the app.py file at 0.0.0.:9090 based on the included files in micro

```
e = Emitter('127.0.0.1:9090')
tracker = Tracker(e)
```

## User Agent ##
The user agent data is collected and sent to micro via the available set_useragent function
```
 tracker.subject.set_useragent(request.headers.get('User-Agent'))
```

## Post views ## 
Viewing of previous posts was tracked to determine everytime someone visited the page and how often the user used the link to access the page 

```
  tracker.track_page_view("http://127.0.0.1:5000")
  tracker.track_link_click("http://127.0.0.1:5000/posts")
```
## New Post submissions ##
Finally new post submissions can be tracked everytime the user submits a new blog post and after the validation has occured. A message is also displayed alerting the user that 
their blog post was created sucessfully. Currently blog posts aren't actually creeated this is to mimic the process of a potential user creating a blog post to allow for the ability
track this

```
form = PostForm()
if form.validate_on_submit():
    tracker.track_form_submit("postForm")
    flash('Your post has been created!', 'success')
    return redirect(url_for('home'))
 return render_template('newPost.html', title='New Post',
                           form=form, legend='New Post')
```
## Scope for improvement ##
This tracking strategy could be improved by using some self-describing events such as seeing how long a user takes between starting a blog post and submitting it. I was unable 
to implement this but this would definitely improve insights. 

## Setup ##
The application was developed using PyCharm and the environment variables are included below:
* FLASK_APP = app.py
* FLASK_ENV = development
* FLASK_DEBUG = 0

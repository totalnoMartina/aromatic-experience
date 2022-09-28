# Testing
## Validators
HTML5 and CSS3 documents have been validated using [Validator W3](https://validator.w3.org/)
### HTML5
Index Page
![Index Validator](media/images/homepage-ar-validated-html.png?raw=true)
Detail Page
![Detail page Validator](media/images/detail-valid-html.png?raw=true)

Add Post - draft
![Add post page Validator](media/images/add-post-valid-html.png?raw=true)

Edit post - drafts
![Edit post page Validator](media/images/edit-draft-valid-html.png?raw=true)

My Drafts
![Drafts page Validator](media/images/drafts-valid-html.png?raw=true)

Delete post - drafts
![Delete posts page Validator](media/images/delete_post-valid-html.png?raw=true)

Edit post
![Edit post page Validator](media/images/edit-draft-valid-html.png?raw=true)


### CSS3
Image of the CSS3 validation shows an error in the '.blog' class (line 198) that specifies positioning of the blog elements which are rendered using Jinja (Django), and that includes image, date, title, author's name, likes and content of the post. The code for this styling is helping responsiveness, and works impeccable on different screen devices keeping a consistent layout and this is why I am keeping it this way. I will look more into better ways of doing this so there is no errors.
![CSS3 Validator](media/images/css-validation-error.png?raw=true)
### JavaScript Validator
For validating JavaScript code [JSHint](https://jshint.com/) is used 
![CSS3 Validator](media/images/jshint-validation.png?raw=true)
Python Validation
Python code was checked using [PEP8 Validator](http://pep8online.com/)

-- admin.py

![PEP8 Validator](media/images/admin-pep8.png?raw=true)

-- app.py

![PEP8 Validator](media/images/pep8-app.png?raw=true)

-- settings.py

![PEP8 Validator](media/images/pep8-settings-indent-line-too-long.png?raw=true)

-- forms.py

![PEP8 Validator](media/images/pep8-forms.png?raw=true)

-- views.py

![PEP8 Validator](media/images/pep8-indent-or-line-too-long-views.png?raw=true)

-- models.py
![PEP8 Validator](media/images/pep8indent-or-line-too-long-models.png?raw=true)

-- test-forms.py

![PEP8 Validator](media/images/pep8-test-forms.png?raw=true)

-- url.py(project)

![PEP8 Validator](media/images/pep8-urls-project.png?raw=true)

-- urls.py(app)

![PEP8 Validator](media/images/pep8-urls.png?raw=true)

-- wsgi.py

![PEP8 Validator](media/images/pep8-wsgi.png?raw=true)

## Database Entity Relationship Diagram
![ERD](media/images/erd-full.png?raw=true)

The relationship between data models are straightforward, there is a User with an 'ID' that is able to create posts, and related to an 'author' . The comment model is relating to the post, and in the model,a 'name' represents a user who, for now, can only comment the posts. Likes are an optin that is set to 'False' initially.
## Database Models Scheme
![Database models scheme](media/images/erd-models.png?raw=true)
## User journey
![User journey through site](media/images/users-journey.png?raw=true)
## User story MOSCOW on Github

![Database models scheme](media/images/git-opened-stories.png?raw=true)
![Database models scheme](media/images/user-stories-git.png?raw=true)
## Bugs 
### Fixed Bugs
A 'favicon' error showing up in Chrome Developer Tools while Inspecting, resolved with code for HTML that uses element of 'link' for and empty 'href'.
A smooth scroll was tried with JavaScript code, with a method of 'animate' which somehow did not work and after the idea of 'scroll-behavior: smooth;' in css for html element it worked better.

### Unfixed bugs
At the moment 'Facebook Login' is in the 'Login' page, instead on a 'SignUp Page', I cannot seem to find any videos about controlling 'allauth' templates, also, waiting until last moment to check if this if working.
Tried to implement Update/Delete Comments, most tutorials show how to do same, but with Post only, so I could not understand how to manipulate a comment that is between a post and user. I tried about 4 times and unfrotunately, it seems to me I did not understand some important part that needs to be to put these pieces together. 
Iphone S6 screen outlook is not fixable, also smooth-scroll behaviour doesn't work on 'Safari'
I will keep learning.
Many of my bugs are connected to all these three months of working on this project, as there was a 'Contact Form', 'Sending Email' function, 'Booking apartments' function, and now while learning they seem all like 'Bugs' but I am completely aware that the steps that I am taking are possibly not as accurate as I am wanting them to be, so I am really planning on making PP5 so much better, and not to go astray in many topics. I could say that this is the outcome of my personal panic mode. Just keep trying until the last moment. There were times, while making this project, when the new type of bug would make me happy as opposed to the same ones.
## Issues

The early deployment worked quite well from the start, as I practiced with redoing the walthrough projects within LMS, and all documents were rendering well from the start as I gathered only relevant dependencies combining videos of 'I Think, Therefore I Blog' and 'Boutique Ado'. 

I tried implementing the 'Contact Form' in a seperate app, to be more accurate in my 'Booking Apartments' Project, since it was followed with an Email sending feature, and I was not sure will this cause for my Aromatic app to crash if I dont manage to implement it correctly. The instructions were followed from [Twilio](https://docs.sendgrid.com/for-developers/sending-email/api-getting-started) and even thought I tried twice, I still did not manage to get 'sendgrid' module to help me send emails using google. I must be missing some piece of the puzzle in my understanding. I also tried Django's builtin modules like 'send()' and 'send_mail()' , trying also with Google and no luck

Later on, while trying to add a 'category' to the model of Post, I made a mistake of not migrating changes while as admin trying to add a category, so somewhere in the database the system caught the additional 'category' feature. It did not work out at the end and I tried deleting it, but then I confused the whole system with one attempt. Thinking I will again have to redo, Tim, my mentor helped me resolve the issue as we were with ascheduled call on at the time. The solution was destroying a database on heroku, deleting, and re-creating a new database, and make a fresh migration. This solved the issue.

Media files were not rendering if targeted using Jinja, like the hero images of flower.png and olive.png that are stored in 'media' folder, did not load originally, but following 'Boutique Ado' the teacher is using css rule for targeting an element, adding property of background image (in his case homepage image) and rendering it through an 'url' and later they were loading properly.

There was some issues while setting up Facebook Login, as I had another app connected to Facebook Login button earler, deleting it did not yet solve the issue as this is what I am getting, possibly when fully deployet it should work as I triple checked everything and have not found yet a better solution then setting Debug to 'False' and trying it again.

Last moment issue was that static media images for landing page are showing a 404 Error, and before this, Heroku deployment failed specifically because of these images of an olive and a flower. I searched on Slack about these and found that Cloudinary must have all the used images, so I tried storing my two just there, that did not work. I read the [Docs](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/) but it seems to be right like needed.
 ![Issue - Should be rendering images](media/images/chrom-front.png?raw=true)
 ![Issue - no images](media/images/last-issue.png?raw=true)

# Testing Python code with 'unittest' module - automated

-- Testing Comment Form for the fields that are required to be filled before posting 

![Test forms.py](media/images/test-comment-form.png?raw=true)

-- Test passing as the content is rendering on the homepage i view function

![Test views.py view1](media/images/views_test_pass1.png?raw=true)

-- Testing fails if I enter a wrong character - as it should. As far as testing python, these were helpful since they were presented in 'I Think Therefore I Blog' walthrough, and unfortunately I haven't been able to figure out tests manipulation entirely, after having spent over a week exploring and trying it out in different ways.
![Test views.py view1](media/images/test-view-failed-with-a-typo.png?raw=true)



# Testing JavaScript manually

There are two functions that are written in JavaScript, one for the Navigation bar to close on clicking/touching anywhere in the page when navigation is toggled down and has been checked on Linux Chromebook in [Chrome](https://www.google.com/chrome/?brand=FKPE&gclid=Cj0KCQjwgMqSBhDCARIsAIIVN1XJTFLf7Smggn3UEcd8GRZYuT51exkyCHhR5AqWR5V6U1EGsDtVT1QaAu7oEALw_wcB&gclsrc=aw.ds) Browser and it works well. Also in [Ecosia](https://www.ecosia.org/?c=en) mobile version, closing navigation works well, as well as in the laptop version of Ecosia. It also works on Iphone [Safari](https://www.apple.com/safari/) version.

Another function is a 'Timeout' function for the 'django-messages' to disappear after certain time. It  works on all the browsers, same as the toggle function.
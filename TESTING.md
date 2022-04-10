# Testing

## Validators of Front End


HTML5 and CSS3 documents have been validated using [Validator W3](https://validator.w3.org/)

### HTML5

Images for index and detail pages
![Index Validator](media/images/index-validated.png?raw=true)
![Detail page Validator](media/images/detail-validated.png?raw=true)

### CSS3

Image of the CSS3 validation shows an error in the '.blog' class (line 198) that specifies positioning of the blog elements which are rendered using Jinja (Django), and that includes image, date, title, author's name, likes and content of the post. The code for this styling is helping responsiveness, and works impeccable on different screen devices keeping a consistent layout and this is why I am keeping it this way. I will look more into better ways of doing this.
![CSS3 Validator](media/images/css-validation-error.png?raw=true)


Add Python PEP8 validation



## Database Entity Relationship Diagram

![ERD](media/images/erd-full.png?raw=true)

The relationship between data models are straightforward, there is a User with an 'ID' that is able to create posts, and related to an 'author' . The comment model is relating to the post, and in the model,a 'name' represents a user who, for now, can only comment the posts. Likes are an optin that is set to 'False' initially.


## Database Models Scheme

![Database models scheme](media/images/erd-models.png?raw=true)

## User journey

![CSS3 Validator](media/images/users-journey.png?raw=true)

## User story testing

| User story   | Requirement met  | Image |
|                                     |                                                   
| **Returning visitors:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to easily log into my account                                                        | Log in from the top navigation                                                                              
| **Site administrator:**                                                                                                                  |                                                                                                                   |   
| 1. I want to log into the admin
## Issues


The early deployment worked quite well from the start, as I practiced with redoing the walthrough projects within LMS, and all documents were rendering well from the start as I gathered only relevant dependencies combining videos of 'I Think, Therefore I Blog' and 'Boutique Ado'. 

I tried implementing the 'Contact Form' in a seperate app, to be more accurate in my 'Booking Apartments' Project, since it was followed with an Email sending feature, and I was not sure will this cause for my Aromatic app to crash if I dont manage to implement it correctly. The instructions were followed from [Twilio](https://docs.sendgrid.com/for-developers/sending-email/api-getting-started) and even thought I tried twice, I still did not manage to get 'sendgrid' module to help me send emails using google. I must be missing some piece of the puzzle in my understanding. I also tried Django's builtin modules like 'send()' and 'send_mail()' , trying also with Google and no luck

Later on, while trying to add a 'category' to the model of Post, I made a mistake of not migrating changes while as admin trying to add a category, so somewhere in the database the system caught the additional 'category' feature. It did not work out at the end and I tried deleting it, but then I confused the whole system with one attempt. Thinking I will again have to redo, Tim, my mentor helped me resolve the issue as we were with ascheduled call on at the time. The solution was destroying a database on heroku, deleting, and re-creating a new database, and make a fresh migration. This solved the issue.

Media files were not rendering if targeted using Jinja, like the hero images of flower.png and olive.png that are stored in 'media' folder, did not load originally, but following 'Boutique Ado' the teacher is using css rule for targeting an element, adding property of background image (in his case homepage image) and rendering it through an 'url' and later they were loading properly.

There was some issues while setting up Facebook Login, as I had another app connecte to Facebook Login button earler, deleting it did not yet solve the issue as this is what I am getting, possibly when fully deployet it should work as I triple checked everything and have not found yet a better solution then setting Debug to 'False' and trying it again.


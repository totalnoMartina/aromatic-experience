# Aromatic Experience

A personal blog website, focused on Aromatherapy and essential oils, used to improve one's wellbeing in a natural way. The website is working on all screen devices for a good UX as preented in the image.

![](media/images/responsiveness.png?raw=true)

# Contents

* [Project Overview](#project-overview)
* [User Experience Design](#user-experience-design)
   * [Strategy](#strategy)
   * [Target audience](#target-audience)
   * [User Stories](#user-stories)
   * [Scope](#scope)
   * [Features](#features)
   * [Structure](#structure)
   * [Browser Compatibility](#browser-compatibility)
* [Skeleton](#skeleton)
   * [Wireframes](#wireframes)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Project Overview

Aromatic Experience is a blog started by a passionate individual who wants the world to know about benefits of oils. As a Representation oils and sponsored by [Doterra](https://www.doterra.com/GB/en_GB), this website is for all lovers of oils, aromatherapy and 'DYI' blends that can be shared in this platform. With an option to like/unlike a post or leave a comment.

# User Experience Design

## Strategy
As a small business owner, a representative for Doterra Company, I want to have a way to promote the importance of using essential oils in every day life. The strategy here is to start small, gather a community and together 'smell the roses'. There is a possibility to make more income based on this blog, since audience will know some secret recipes here. Main Objective: To grow small business, share ideas.

## Target audience

- Users passionate about skin/hair/nails care in natural ways
- Users interested in healing with sense of smell
- Users looking for natural ways to improve their wellbeing
- Users who want to share their ideas about oils and mixing them
- Users who dont know anything about oils but have a keen interest to find out
- Users who have some emotional imbalance and looking for natural way of getting back to balance
- Users who want to connect to more alike-thinkers
## User stories

**First-time User:**

1. I want to understand the purpose of the site and the topic objective easily 
2. I want to easily register an account, possibly using social media account
3. I want to feel confident that the data I enter is secure
4. I want to understand the benefits of creating an account
5. I want to connect to new people by commenting, liking posts

**Returning Users:**

1. I want to easily log back into my account
2. I want to be able to see the latest posts displaying in the homepage
3. I want to be able to have good Ux in all versions pf screens

**Site administrator:**

1. I want to log in quickly and easily
2. I want to see what comments have been recently requested to be published
3. I want to have an option on my navigation to go straight to Admnistration when logged in
## Scope

Mostly for a small business owners usage, possibly for the ones who work from home, even though it is easily maintained to be a regular little hobby on the side. Essential oils - topic oriented, targeting aromatherapy benefits and connect all interested with the commenting feature, providing relevant informations. Help small business connected to aromatherapy grow.
## Features

- Authentication System - Users can login and easily comment/like

Homepage for first time users to 'Register' or 'Login'
![](media/images/login-reg.png?raw=true)

'Sign Up' page
![](media/images/signup.png?raw=true)

- Administrator can manipulate comments that are going to be published, approve them![](media/images/admin-comment-approve.png?raw=true)

- Django Messages are used to let user know on 'login/logout' status and on commenting sent to be approved![](media/images/messages-signedin.png?raw=true)
- ![](media/images/messages-signedout.png?raw=true)

- Not able to screenshot but there is a snippet of JavaScipt code for Navigation to toggle close (if clicked) when user cliks outside of the navbar
- Facebook login set up (At the moment, there is a bug, which does not allow login using Facebook, but it worked once before, so after trying, I decided to leave it there until I turn debug to False to see final effect)

![](media/images/messages-signedin.png?raw=true)
**Future features**

- Add an oil review section/category - where users can review oils from specific companies and share amongst each other which are high/low quality, since entering a category this time and made me destroy my db, I left it for future feature
- Add login using Google - tried many times, postponed
- Inspired by the app called [abillion](https://www.abillion.com/) it would be great to make every review giving users 1Euro for every review they make and then, this one euro would go to a specific company that already is involved in production of oils or contributing in some way, as this can be collected and donated. No money can be withdrawn, which makes it even more noble. 
## Structure

A Structure of this website is aiming to be simple, with warm color palette and a simple navbar. The content main objective is in the center split into two columns when seeing published posts on 14inch screens -the screen size in which this website is made, in  a Chrome Browser.While seeing one post, the title and front image streches to improve visual experience.

This is the original, first idea of a layout ![](media/images/first_layout.png?raw=true)

Second idea of a layout ![](media/images/final-layout.png?raw=true)

Final idea of a layout ![](media/images/final-img.png?raw=true)
## Browser Compatibility

The Website is made in [Chrome Browser](https://www.google.com/intl/en_ie/chrome/) on a Chromebook, to be exact --> Chrome is made possible by the Chromium open source project as well as other open source software.
Chrome OS is made possible by Linux OS, as is Linux [development environment](chrome://crostini-credits/).

![Chrome Image](media/images/chrom-front.png?raw=true)
![Chrome Image](media/images/chrome-post.png?raw=true)
![Chrome Image](media/images/chrome-footer-submit.png?raw=true)
![Chrome Image](media/images/chrome-signout.png?raw=true)
![Chrome Image](media/images/chrome-loggedin.png?raw=true)

There were some issues on IPhone 6S, showing unstable alignment which doesn't show in dev tools like that, but here are some screenshots

![IOS Image](media/images/image_from_ios.png?raw=true)
![IOS Image](media/images/iphone-bad.png?raw=true)
![IOS Image](media/images/iphone2-bad.png?raw=true)
![IOS Image](media/images/iphone-good.png?raw=true)
![IOS Image](media/images/iphone2-good.png?raw=true)
# Skeleton
## Wireframes

Original setup is similar to the end product, navigation is chaged about 3+ times

![Wireframe](media/images/aromatic-wireframe.png?raw=true)

**Color scheme**

This site uses a [ColorSpace](https://mycolor.space/) palette picker, and this is the final choice
![Color Palette](media/images/final_color_palette.png?raw=true)

# Technologies Used

The site uses the following technologies;

* HTML5
* CSS3
* Bootstrap
* JavaScript
* Python (Django)
* Postgres
* Cloudinary
# Testing
[See separate Testing file](TESTING.md) for information on testing and issues.
# Deployment Steps

This website is deployed on Github for Front End and on Heroku for Backend

**How to fork this GitHub Repository**

1. Log onto Github.
2. Navigate to this direct link for the repository [here](https://github.com/totalnoMartina/aromatic-experience) or type in search 'totalnoMartina/aromatic-experience'
3. You can fork any repo by clicking the fork button in the upper right hand corner of a repo page. Now click Fork.
4. When you fork a repo on GitHub, the forked repo is copied to your GitHub account, and you can edit it as the repo owner.
5. GitHub will take you to your copy (your fork) of the 'aromatic-experience' repository.
4. This should create a copy within your account.

**How to run this project locally - clone**

1. Log onto Github: create an account if required.
2. From the list of repositories, select 'the repo name/project name'
3. Click the "Code" dropdown within the menu above the commits.
4. Copy the URL address, or Download ZIP and save locally.
5. Open your chosen IDE and navigate to the location you want the cloned directory to be saved.
6. Type git clone and copy the URL within the CLI and press enter.
7. Alternatively, select "Open with Github Desktop".

## Deployment on Heroku
This project was developed using Gitpod, committed to git and pushed to Github using the built-in functionality.

At early stages it was then deployed to Heroku with guidance of videos for 'I Think Therefore I Blog' walkthrough
### Steps for Heroku

* Create an account or log into Heroku.
* Navigate to Create New App within the New dropdown.
* Enter App name and select a region

Reveal the Config Variables and enter the following information to connect to Postgress with 'DATABASE_URL', connect to Media database using 'CLOUDINARY_URL', and the last two are for the Facebook login button to work:

* DATABASE_URL
* CLOUDINARY_URL
* SECRET_KEY
* SOCIAL_AUTH_FACEBOOK_ID
* SOCIAL_AUTH_FACEBOOK_SECRET

![Heroku](media/images/heroku-config.png?raw=true)
Connect using Github (if appropriate) with a button in the middle of 'Deploy' section and search for the name of your Github repository, when you find, click 'Connect'.
![Heroku](media/images/heroku-github-deploy.png?raw=true)

Next, select the branch for deployment(commonly 'main')
Click 'Deploy' button. After a few moments the building of your app with the log can be observed, right under the 'Deploy' button.
Finally, the app can now be viewed live on this link [here](https://aromatic-martina.herokuapp.com/)

![Heroku](media/images/heroku-build-fin.png?raw=true)
# Credits

- [Stackoverflow](https://stackoverflow.com/)
- [YouTube](www.youtube.com) tutorials
- Code Institute Slack community
- Tutors at the Code Institute, in particular Igor, Ed and Ger for help with testing and deployment
- A tutorial that helped me understand [Testing in Django](https://www.youtube.com/watch?v=GBgRMdjAx_c&list=PLOLrQ9Pn6cay7t8VZ3wmn6QdAxzTx60F3&index=4) a bit better
- I used this help for trying to do testing python code [this link here](https://stackoverflow.com/questions/44604686/how-to-test-a-model-that-has-a-foreign-key-in-django#:~:text=To%20write%20a%20test%20for,target%20model%20for%20the%20test.)
- [Django Docs on Testing Tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/#django.test.SimpleTestCase)
- The original idea is based on CI Walkthrough project 'I Think Therefore I Blog'
- The code for messages is also inspired by the same project, and the step further was to create you custom message for when user comments. 
- The images were found using Google Search for anything connected to topic, and here are the respective links:
 [Image of the grapefruit](https://www.doterra.com/GB/en_GB/p/grapefruit-oil) , [Aroma Image](https://5.imimg.com/data5/TK/QV/MY-45444487/aroma-oil-500x500.jpg)

- Text that inspired posts is also taken from [Doterra](https://www.doterra.com/GB/en_GB) as an example of relevant information this Blog would be about
- [Google Fonts](https://fonts.google.com/specimen/Playfair+Display?query=play) for the 'Playfair Display'

- For people that helped me throught the journey of creating this project, credits go to my mentor for moral and technical support, at times when I really needed it, resolving the authentication issues, image setting in carousel and many many more problems that Tim helped me solve, eternally grateful for that

- Also, one of CI students, in my opinon an expert in Front End, [Julia Konovalova](https://github.com/IuliiaKonovalova) and became a good friend for some time now, helped me think outside of (flex)box and grid, made me learn so much while she advised me on front end outlook, as originally I was a 'linear-gradient-fan' and she helped me organize footer better. She is such an amazing teacher, and we learned a lot together. Very grateful for CI and all connection made here, and still continue to make.

- Also, while making this project, I had many doubts, mostly in myself, and that made me make a few more applications which were all my ideas in how to use Django in Full Stack Development. My first idea was a 'Django Chatbot' that would be a source of communication for people when they want to chat, to be responded by AI Chatbot. I got as far as creating 'intentions' file and a module for storing data was not working. I followed this [tutorial](https://www.google.com/search?q=chatbot+module+th+django&rlz=1CAKDUD_enIE947&sxsrf=APq-WBvyn1KR_8LIDcKa-76rblEZSiGMYw%3A1649660280638&ei=eNFTYqfWJoOo8gKa74ioBA&ved=0ahUKEwin8pu4t4v3AhUDlFwKHZo3AkUQ4dUDCA4&uact=5&oq=chatbot+module+th+django&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAE6BwgAEEcQsAM6BQghEKABSgQIQRgASgQIRhgAUMkCWOcJYJkMaAFwAXgAgAGGAYgBmgWSAQM1LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz). Other ideas were: Apartment booking website - for my parents house in Croatia (over 4 versions of this project on Github can be seen 
* [version1](https://github.com/totalnoMartina/apartments-django)
* [version2](https://github.com/totalnoMartina/jasna-apartments)
* [version3](https://github.com/totalnoMartina/happy-holiday)
* [version4](https://github.com/totalnoMartina/booking-klanfari)
* [version5](https://github.com/totalnoMartina/holiday-home) -> very similar to the heroku one
), 
some of them deleted due to limited space on 'Heroku', [link for Apartments](https://holiday-martina.herokuapp.com/)), Wholesale Bakery Website (only on Github, [Bakery Website](https://github.com/totalnoMartina/golden-mine-bakery)), Blog about plants&plant swapping (one of the deleted, based on CI walkthrough 'I think Therefore I Blog').
Each of them helped me grow enormously

- As my original idea was 'Apartments Booking' I found modules for 'booking' in django docs, but only compatible with Django 4.0, and I found reservation module 'reservations' which is compatible with older versions of Django, so I kept hopeful, thinking I can make up the function for booking myself, Thanks to the tutorials on [YouTube](www.youtube.com) I learned about the compatibility between apps and modules a lot.

- Links for some of the YouTube tutorials I used to better understand Django: 
[Booking HMS](https://www.youtube.com/watch?v=-9dhCQ7FdD0&) - watched over 10 times, list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=2), 
[Facebook Login](https://www.youtube.com/watch?v=E6LxUleoloU),
[Building Social Login](https://www.youtube.com/watch?v=oAWUyg_PPLk), [Django Restaurant System](https://www.youtube.com/watch?v=r0mjZRKmNC8&t=25s),
[Create a Diary App](https://www.youtube.com/watch?v=YkpEtE_x6xk)
- The ERD was made using [SmartDraw](https://www.smartdraw.com/)

- Help with documenting deployment was found on this link [How to get started with Git](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#forking-a-repository) and inspired by [Catherine Trevor](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#forking-a-repository)'s README.md example as well as ideas from Iulia Konovalova and Tim Nelson for making README better in details.

Also in the last moment, after having dealt with 'staticfiles' numerous times, I had to find out how to render hero images properly an used the example from Catherine Trevor's 'The Marketing Ally's website.


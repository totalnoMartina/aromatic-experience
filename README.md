# Aromatic Experience

A personal blog website, focused on Aromatherapy and essential oils, working on all screen devices for a good UX

![](media/images/responsiveness.png?raw=true)


# Contents

* [Project Overview](#project-overview)
* [User Experience Design](#user-experience-design)
   * [Strategy](#strategy)
   * [Scope](#scope)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Issues](#issues)
* [Deployment](#deployment)
* [Credits](#credits)

# Project Overview

Aromatic Experience is a blog started by a passionate individual who wants the world to know about benefits of oils. As a Representation oils and sponsored by [Doterra](https://www.doterra.com/GB/en_GB), this website is for all lovers of oils, aromatherapy and 'DYI' blends that can be shared in this platform. With an option to like/unlike a post or leave a comment.

# User Experience Design Thinking

## Strategy
As a small business owner, a representative for Doterra Company, I want to have a way to promote the importance of using essential oils in every day life. The strategy here is to start small, gather a community and together 'smell the roses'. There is a possibility to make more income based on this blog, since audience will know some secret recipes here. Main Objective: To grow small business, share ideas.

### Target audience

- Users passionate about skin/hair/nails care in natural ways
- Users interested in healing with sense of smell
- Users looking for natural ways to improve their wellbeing
- Users who want to share their ideas about oils and mixing them
- Users who dont know anything about oils but have a keen interest to find out
- Users who have some emotional imbalance and looking for natural way of getting back to balance
- Users who want to connect to more alike-thinkers


### User stories

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

Mostly for a small business owners usage, possibly for the ones who work from home, even though it is easily maintained to be a regular little hobby on the side. And the scope here is to be topic oriented, targeting aromatherapy benefits and connect all interested with the commenting feature, providing relevant informations. Help small business connected to aromatherapy grow.
### Features

- Authentication System - Users can login and easily comment/like
- Administrator can mainpulate comments that are going to be published, approve them
- Facebook login set up (At the moment, there is a bug, which does not allow login using Facebook, but it worked once before, so I keep trying)

**Future features**

- Add an oil review section/category - where users can review oils from specific companie and share amongst each other which are high/low quality
- Add login using Google
- Inspired by the app called [abillion](https://www.abillion.com/) it would be great to make every review giving users 1Euro for every review they make and then, this one euro would go to a specific company that already is involved in production of oils or contributing in some way, as this can be collected and donated. No money can be withdrawn, which makes it even more noble. 

## Structure

A Structure of this Website is aiming to be simple, with warm color palette and a simple navbar. The content main objective is in the center split into two columns when seeing published posts.While seeing one post, the title and front image streches to improve visual experience.

Thi original, first idea of a layout ![](media/images/first_layout.png?raw=true)

Second idea of a layout ![](media/images/final-layout.png?raw=true)

Final idea of a layout ![](media/images/final-img.png?raw=true)




## Skeleton

### Wireframes

![Wireframe](media/images/aromatic.png?raw=true)

### Database schema


## Surface

**Database models**


**Color scheme**


This site uses a [ColorSpace](https://mycolor.space/) palette picker, and this is the final choice
![Color Palette](media/images/final_color_palette.png?raw=true)
**Imagery**

# Technologies Used

The site uses the following languages;

* HTML5
* CSS
* JavaScript
* Django
* Python

Django is a framework, relational database is postgres, check for heroku to share more details

# Testing


# Issues
# Deployment

**How to fork the GitHub Repository**

Forking the repository allows you to make a copy of the original in your GitHub account, and make changes without affecting the original.

1. Log onto Github.
2. From the list of repositories, select CatherineTrevor/the_marketing_ally.
3. At the top of the repository, select the "Fork" button.
4. This should create a copy within your account.

**How to run this project locally**

1. Log onto Github: create an account if required.
2. From the list of repositories, select 'the repo name/project name'
3. Click the "Code" dropdown within the menu above the commits.
4. Copy the URL address, or Download ZIP and save locally.
5. Open your chosen IDE and navigate to the location you want the cloned directory to be saved.
6. Type git clone and copy the URL within the CLI and press enter.
7. Alternatively, select "Open with Github Desktop".

## Deployment on Heroku

This project was developed using Gitpod, committed to git and pushed to Github using the built-in functionality.

It was then deployed to Heroku.

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

Connect using Github (if appropriate)

Select the branch for deployment

Deploy. The app can now be viewed live.

![Heroku](media/images/heroku-build-fin.png?raw=true)



# Credits

- The original idea is based on CI Walkthrough project 'codestar' providing users a signup/login system and to comment posts and like
- The code for messages is also inspired by the same project, and the step further was to create you custom message for when user comments. 
- The images were found using Google Search for anything connected to topic, and here are the respective links:
 [Image of the grapefruit](https://www.doterra.com/GB/en_GB/p/grapefruit-oil) , [Aroma Image](https://5.imimg.com/data5/TK/QV/MY-45444487/aroma-oil-500x500.jpg)

- Text that inspired posts is also taken from [Doterra](https://www.doterra.com/GB/en_GB) as an example of relevant information this Blog would be about
- [Google Fonts](https://fonts.google.com/specimen/Playfair+Display?query=play) for the 'Playfair Display'

- For people that helped me throught the journey of creating this project, credits got to my mentor for moral and technical support, at times when I really needed it, resolving the authentication issues, image setting in carousel and many many more problems that Tim helped me solve, eternally grateful for that

- Also, one of CI students, in my opinon an expert in Front End, [Julia Konovalova](https://github.com/IuliiaKonovalova) and became a good friend for some time, help me think outside of (flex)box and grid, made me learn so much while she advised me on front end outlook, as originally I was a 'linear-gradient-fan' and she helped me organize footer better. Very grateful for CI and all connection made here, and still making.

- Also, while making this project, I had many doubts, mostly in myself, and that made me make a few more applications which were all my ideas in how to use Django in Full Stack Development. Some of them are: Apartment booking website - for my parents house in Croatia (over 3 versions of this project on Github can be seen 
* [version1](https://github.com/totalnoMartina/apartments-django)
* [version2](https://github.com/totalnoMartina/jasna-apartments)
* [version3](https://github.com/totalnoMartina/happy-holiday)
* [version4](https://github.com/totalnoMartina/booking-klanfari)
* [version5](https://github.com/totalnoMartina/holiday-home) -> very similar to the heroku one
), 
some of them deleted due to small space on 'Heroku', [link for Apartments](https://holiday-martina.herokuapp.com/)), Wholesale Bakery Website (only on Github, [Bakery Website](https://github.com/totalnoMartina/golden-mine-bakery)), Blog about plats&plant swapping (one of the deleted, based on CI walkthrough 'I think Therefore I Blog'), Aromatic Blog as the final website that I am submitting. 

- As my original idea was 'Apartments Booking' I found modules for 'booking' in django docs, but only compatible with Django 4.0, and I found reservation module 'reservartions' which is compatible with older versions of Django, so I kept hopeful, thinking I can make up the function for booking myself, Thanks to the tutorials on [YouTube](www.youtube.com) I learned about the compatibility between apps and modules matters a lot.

- Links for some of the YouTube tutorials I used to better understand Django: 
[Booking HMS](https://www.youtube.com/watch?v=-9dhCQ7FdD0&) - watched over 10 times, list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=2), 
[Facebook Login](https://www.youtube.com/watch?v=E6LxUleoloU),
[Building Social Login](https://www.youtube.com/watch?v=oAWUyg_PPLk), [Django Restaurant System](https://www.youtube.com/watch?v=r0mjZRKmNC8&t=25s),
[Create a Diary App](https://www.youtube.com/watch?v=YkpEtE_x6xk)

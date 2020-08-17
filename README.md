# ARC_Django_MS4
['ARC_Community'](https://arc-community-aglz.herokuapp.com/), books community (Milestone PJ 4 -CI FSC)

# ARC Community
Book community for reviews [(access here)](https://arc-community-aglz.herokuapp.com/) *beware that doesn't open on a new tab*.

**(Full-Stack Frameworks with Django - Code Institute by Ángel González)**

This is a books social community, where you can review and rate books. The WebApp is available to be used both in browser and in portable device. The app supports users login and access to a database to store the entries.

If you want to try out with a test user, sign in with this information: **user:** *test*, **password:** *trivialtest*.

---

## **Table of Contents**

1. [UX](#UX)
    * [User Stories](#User-Stories)
    * [Strategy](#Strategy)
    * [Wireframes](#Wireframes)
    * [Scope](#Scope)
    * [App Structure](#App-Display-Structure)
    * [DB Structure](#DB-Structure)
    * [Theming](#Theming)
2. [Features](#Features)
    * [Future Features](#Future-Features-Objectives)

3. [Testing](#Testing)
4. [Deployment](#Deployment)

    * [Tech Used](#Tech-Used)
    * [Github Pages](#Configuration-on-Heroku-Apps)
    * [Cloning Repository](#Cloning-the-GitHub-Repository)
    * [Running it localy](#Running-it-localy)

5. [Credits](#Credits)

    * [Images](#Images)
    * [Acknowledgements](#Acknowledgements)

6. [Contact](#Contact)

---
## UX
### User Stories
Users of this WebApp will be people wanting to review their favourite books or discover new ones than the people are promoting and recommending.

Examples of the user stories:
* User wants to have a profile in the social community, and be able to personalize it.
* User wants to be able to search for the book catalog inside the WebApp.
* User wants to be able to review a book, and be able to edit or delete if after.
* User wants to be able see all the reviews of a book and be able to filter and sort them.
* User wants to see the rankings of best books and users.
* User wants to have a opportunity to promote books they like.
* User wants easy access from its profile to the books and reviews connected.
* User wants to have a list of books they are currently reading in its profile.

The site [(see full-size preview)](/media/screenshots/home-full.png) is based on the Django framework. This system consists of "Views" with different "Models" filling inside of "Templates" depending on the route taken by the user. The way this system works makes all transitions easy and smooth for the user, being highly intuitive, but also for the developer, making it very easy to connect the models and views from different apps. In this specific WebApp, user experience is supported with toast messages each time an action is completed, giving this way direct informations to the user of any progress made.

Both the browser version and the portable device version are distributed in the same way, navigation stays fix at top and deploys as sidebar [(see Features)](#Features) making it easier to access every part of the WebApp when needed. In the portable device version, navbar is reduced to the logo and a menu icon [(see protable device preview)](/media/screenshots/home-phone.png).

### Strategy
The goal is that the user has creates a profile and uses the WebApp to review and recommend books.

To achieve this, first, the home page has several CTA and slogans to prompt the user to participate in the book community. Secondly, and helped by the template system, the design is very stable and similar among all the views, getting to be familiar with the user in very little time.

The most ambitious goal, which wasn't fully implemented due to scarce time, is to make writers subscribe to plans for promoting their books to a featured section in order to get more reviews, [(see Future Features)](#Future-Features-Objectives). Actual implementation was for the regular users/readers to promote the books they like, [(see Features)](#Features).

### Wireframes
Here are the first concept wireframes:

* [Index Page](/media/screenshots/wf-index.png "Index Page")

* Profile Page:

    ![Profile Page](/media/screenshots/wf-profile.png "Profile Page")

* [Books Page](/media/screenshots/wf-books.png "Books Page")

* [Book Profile](/media/screenshots/wf-detail.png "Book Profile")

Final concept wireframes:

* Index Page: 

    ![Browser-View](/media/screenshots/wf-index-final.png "Index Page")

* [Profile Page](/media/screenshots/wf-profile-final.png "Profile Page")

* [Books Page](/media/screenshots/wf-books-final.png "Books Page")

* [Book Profile](/media/screenshots/wf-detail-final.png "Book Profile")

### Scope
Considering the goals set in [Strategy](#Strategy), it has been necessary to create modern desing with an grey and amber sharp style, [(see Theming)](#Theming).

The project itself was very product oriented so I kept the scope as big as possible regarding the 2-week-timespan, focusing on the user experience of reviewing books, the power of editing and deleting them after; having a manageable profile and being able to promote the books they like if they subscribe.

Read more about future increase of Scope in [(Future Features)](#Future-Features-Objectives).

### App Display Structure
Both in the browser and in the portable device display the structuring focus is the paralelism beetween the views themselves to promote familiarism with the WebApp. We will analyze the main views:

  ![Home Page](/media/screenshots/home-full.png "Home Page")

The **navbar**, displays top on every view.

The **CTA's**, both slogans and buttons display along the whole home page, calling for user attention.

The **carousel** featured books section, displays featured books, [(see Features)](#Features).

The **features** section, displays between the CTA's, avoiding also visual conflict with the background parallax images. Informs the user of the main purposes and features of the ARC Community, [(see Features)](#Features).

  ![Books Page](/media/screenshots/books-full.png "Books Page")

The **search-bar**, allows users to search for books by title or author.

The **book-cards**, deploy some information about the book, allows access to book detail page, [(see Features)](#Features).

The **pagination**, books paginate exceding 24, [(see Features)](#Features).

  ![Profile Page](/media/screenshots/profile-full.png "Profile Page")

The **user info**, allows users to edit their personal information and their profile picture.

The **asked books** section, allows user to have a reading list and update it if needed, [(see Features)](#Features).

The **user reviews** section, displays latest reviews made by user, [(see Features)](#Features).

### DB Structure
A crucial part of the project is the database and its structure for the relations between models, [check schema](/media/screenshots/dbschema.png). The cluster consists of a dataset found in Kaggle.com and processed by me to a json file to load the data as Django fixtures. Here's the explanation of the main database tables:

* **User:** produced from *Sign Up* form by the allauth extension, contains the username and e-mail, password stored and managed by the extension itself. Check a stored example from admin [here](/media/screenshots/dbuser.png).

* **UserProfile:** collects from the User and extends it for a profile making. Contains de asked books for a profile feature, the profile picture url and the date until which is subscribed in the case user is subscribed. Check a stored example from admin [here](/media/screenshots/dbprofile.png).

* **AskBook:** produces the content of the asked_books in the User Profile by collecting user and book selected.

* **Book:** contains all the data collected from the dataset fixtures, sinopsis was lacking on the dataset so the same 'Lorem Ipsum' was placed on the display for the 2500 books. A promoted boolean field was added as perk for subscribed. Check a stored example from admin [here](/media/screenshots/dbbook.png).

* **Review:** contains all the data collected from the review creation form and relates to user and book. A value_count field was added for future features, [(check Futrure Features)](#Future-Features-Objectives). Check a stored example from admin [here](/media/screenshots/dbreview.png).

* **Subscription:** created after User payment subscription is made. Connect User Profile and sets the sub_untill field.

  ![DB Schema](/media/screenshots/dbschema.png "DB Schema")

### Theming
The font for the site is the default Materialize CSS, [Roboto](https://fonts.google.com/specimen/Roboto), which is very clear and ideal for the display of information.

The background pictures, and avatars were taken and adjusted in [Canva](https://www.canva.com/).

The color palette, as mentioned before, sticks to greyscale tones that are interpellated with the amber used for the CTA's.

---

## Features
As explained, this WebApp consists on several Django Apps containing different views:

* **Site Icon**: a personalized WebApp icon display on the browser. Also, it appears in the case someone bookmarks the game page.

    ![Favicon](/static/favicon.png "Favicon")

* **Home App**: this app contains two views. One is the index from which we can extract the promoted books carousel as feature.

    ![Book Carousel](/media/screenshots/index-carousel.png "Navbar logged off")

    In this app is also placed another view which contains the *Top Listings* feature, this view contains three rankings for book and users, [(see rankings page preview)](/media/screenshots/rankings-full.png "Rankings Page").

    More related to a base template but associated with the home page nonetheless, there a hidden *side navigation bar* that displays when manu icon is clicked or finger swiped left on touchscreen devices, [(see sidebar preview)](/media/screenshots/sidebar-full.png "Sidebar Menu").

* **Profiles App**: Users are registered by using Allauth extension for Django and associted with a User Profile, [(see DB Schema)](/media/screenshots/dbschema.png "DB Schema"). Login required decorator is also used to protect the views that are made not available for anonimous. Here we can see a test, empty, user profile, with the diferent sections: user info and avatar, user read list and preview of the latest user reviews, [(see empty user profile)](/media/screenshots/profile-full.png "Empty Profile"):

    *User Info Edit*: this link to a form to edit the account details, [(check)](/media/screenshots/profile-edit.png "Profile Edit").

    *User Books Edit*: this link to a form to edit the user books list, [(check)](/media/screenshots/profile-books.png "Profile Books").

    *User Review*: this link to a view for all the user reviews, [(check)](/media/screenshots/profile-reviews.png "Profile Review"). This view contains both filtering by rating and sorting by date features. From the reviews book-details view can be accessed clicking on the book title inside the review.

* **Books App**: books were loaded adapting the model to the dataset processed. Book cover image is provided by an url, and sinopsis isn't provided so a Lorem Ipsum text was used for all the 2500 books. Features and views contained on this app:

    *All book display*: this view displays all the available books on cards that can be oppened to display some information and provide access to the book details page, [(check)](/media/screenshots/books-all.png "Books All"). This view has a 24-books pagination, 109 pages.

    *Book search*: this view displays books related to the search word by title ot author, [(check)](/media/screenshots/books-search.png "Books Search"). Displays information for the user about the number of results and the text used for the search.

    *Book details*: this view displays all the details for a selected book, [(check)](/media/screenshots/books-details.png "Books Details"). Contains information for the book in the upper part, a deployable sinopsis and information about the ratings underneath. In the lower part of the view the user can find the lastest reviews made for that book and access to a view with all the reviews for this book. As an extra, if the user is logged in, a form for publishing a new review is displayed.

    *Book Review*: this link to a view for all the book reviews, [(check)](/media/screenshots/books-reviews.png "Books Reviews"). This view contains both filtering by rating and sorting by date features. From the reviews user-reviews view can be accessed by clicking on the user info of the review. As an extra, if the user is logged in, a form for publishing a new review is displayed.

* **Reviews App**: reviews are related with users and books as explained in previous App descriptions. Extra features from this app that are available if the user logged is the author of the review:

    *Edit review*: this view displays the review form autocomplete with the old review data and allows to update the content, [(check)](/media/screenshots/reviews-edit.png "Edit Reviews").

    *Delete review*: this route deletes selected review. Check display of this links on [(user reviews)](/media/screenshots/reviews-user.png "User Reviews"), [(book reviews)](/media/screenshots/reviews-books.png "Book Reviews"), [(profile reviews)](/media/screenshots/reviews-profile.png "Profile Reviews").

* **Subscriptions App**: subscriptions are related available users, allowing them to promote books. Check subscription trigger view evolve from [anonimous-user](/media/screenshots/subscriptions-anon.png "Anon Subs") with log-in prompt, to [logged-user](/media/screenshots/subscriptions-logged.png "Logged Subs") with from to subscribe, to [already-promoted-user](/media/screenshots/subscriptions-subbed.png "Subbed Subs") with information about the on-going subscription:

    *User profile*: user profile who is promted has the perk in their profile info, [(check)](/media/screenshots/subscriptions-user.png "User Promoted").

    *Book promotion*: book-details displays a new option to promote the book for the users that have the promoted feature active, [(check)](/media/screenshots/subscriptions-book.png "Book Promoted"), if the book is already promoted, info is displayed, [(check)](/media/screenshots/subscriptions-book-on.png "Book Promoted On").

* **Toasts**: on the whole WebApp, messages are displayed in the form of toasts prompting the user each time an action is performed, complete or an error has been caught. Colour changes depending on the type of message: info, error, etc...

The whole site has response from small devices to larger screens, moving sections from sideways to top/bottom when needed to achieve the best display. It is not responsive on 4k at the moment. A 404 template was included to provide a way back to the home page in the case a bad route is taken by the user.

### Future Features Objectives
Ordering the possibilities in a list of viability, considering both complexity and relevance:

1. Putting to use the value_count of the reviews model to allow the users to vote for usefull or not usefull reviews, being able to use this feature for rankings, short displays and such. (LOW complexity / MED relevance)

2. Putting to use the is_writer feature of the user-profile model, allowing users to upload their own books. (MED complexity / MED relevance)

3. Adding a database to upload the e-pubs for the books so users receive a copy of the e-pub after asking for the book. (HIG complexity / HIG relevance)

---

## Testing
During the development phase, using VS Code and running a local server in a virtual environment made it very easy to adjust response and test the majority as was coded, via Developer Tools and terminal outputs.

After finishing the coding phase, used "HTML validator", "CSS lint" and "PEP 8 validator" checking for possible warnings or errors.

During production phase and with the help of some beta testers:

**Global Display:** tests were made on browsers (Chrome, Edge, Firefox), tablets and phones ensuring responsiveness of the WebApp on every screen size. Some examples of portable devices used by testers involved or myself were:

 * Huawei Mate 9 Lite, Huawei GR5 2017
 * Apple iPhone 11
 * Apple iPhone 8
 * Samsung Galaxy A50
 * BQ Aquaris M10 Ubuntu Edition
 * Microsoft Surface 2

**Views:** profiting of the Django debug model template were error messages are displayed and detailed. Django debug template shows which Model or Variable in the view is producing the error so it becomes very easy to target the bug. Is also remarkable that the 404 template doesn't colide with this feature when debug is set to *True* in the root settings.

Specific and common errors are: missing field on table (missing migrations of models), bad method/attributes applied (confusing querysets with objects on the view logic), missing value queryset (bad logic on the view when obtaining a queryset due to not existing or a bad method appliance) or missing variable (often caused by misspelling and non-complete renamings).

**Buttons and Forms Actions:** as no automated tests were implemented for this project, it was crucial to test every button and every form with proper, but also incorrect inputs, to prove that every output is the intended one. Beta testers were very handy in correcting some of the bad behaving buttons that lead to the wrong view, especially in the latest implemented features that connect several apps.

**Links hrefs:** a single external link is present. It was tested after deployment at Heroku and opens on a new tab with the repository containing the code for the project.

**Stripe WebHooks:** stripe WebHook needs to be tested on set up and in this case as I set it up inside the *subscriptions* app during the development phase, using the virtual enviroment. Stripe provides the *stripe-cli* feature which you can install and use to check the webhooks in your local machine before publishing the WebApp, [(read the Docs)](https://stripe.com/docs/stripe-cli/webhooks "Stripe Docs").

**Bugs:** no more bugs have been found until this moment.

---

## Deployment
This site is temporarily hosted on Heroku Apps, [(access here)](https://arc-community-aglz.herokuapp.com/). 

Deployment on Heroku was made before submitting the project for final testing. The project was kept in a virtual environment on my end for testing and modifications, even though it was committed to GitHub and updated via GitBash on a frequent basis.

#### Tech Used
1. HTML5
2. CSS3
3. [Materialize CSS](https://materializecss.com/about.html)
4. Python
5. Postgres for Heroku (plugin)
6. Django + django-extensions [(see requirements.txt)](requirements.txt)

#### Configuration on Heroku Apps
1. Subscribe to Heroku and create your new app.
2. In your GitBash/Terminal go to your master directory.
3. Type **"heroku login"** and follow the prompts.
4. Once logged in, type **"git push heroku master"** and wait until the process finishes.
5. Once your app is loaded on Heroku, type **"heroku ps:scale web=1"** to set Heroku on a basic level.
6. After scarce time, your app should be ready. Either follow your terminal prompted link or go to your Heroku profile.
7. Mind that this App needs access to a database and the "Config Vars", see all 'get.os.environ' in the settings.py at the root folder.

#### Cloning the GitHub Repository
To run it on your local computer with a virtual environment, see below, the repository must be cloned beforehand.

1. Once in the repository locate the *Clone or Download* dropdown menu.
2. Copy either the HTTPS or SSH route to your clipboard.
3. Open *GitBash* and move to the folder where you want to place the cloned repository files.
4. Type **"git clone"**, **tap space-bar once** and then paste the route copied in your clipboard at *step 2*.
5. Press Enter to exec the command and the local cloned files will be created.

#### Running it localy
To run it on your local computer with a virtual environment, the repository must be cloned beforehand, see above.

1. Install python3 on your computer.
2. Access to the master directory in your terminal and type **"python3 -m venv venv"** to create a virtual environment called "venv" in this case (second venv on command).
3. After venv files are created, if you are using Mac/Linux type **"source venv/bin/activate"**, on Windows type **"venv\Scripts\activate"** instead.
4. Your terminal should be placed on your master directory, but one level further in your virtual environment "venv".
5. You will access from your virtual environment through the *manage.py* file so got to the terminal and write **"python manage.py runserver"** and the terminal itself will give you a local port to access the app live.

---

## Credits

All the ideas, materials displayed, database entry, AWS Storage and all the site designs belong to Ángel González.

### Images
[*Canva.com*](https://www.canva.com/)

**Disclaimer:** This site and its contents or any portion thereof may not be reproduced or used in any manner whatsoever without the express written permission of the publisher except for the use of brief quotations as credits and/or recommendation. Copyright © 2020.

### Acknowledgements
Great help once more from the documentation of these two sites, you can really learn as you go and adapt their examples to your own code:

* [w3schools](https://www.w3schools.com/)
* [MDN](https://developer.mozilla.org/en-US/)
* [Django](https://docs.djangoproject.com/en/3.1/)

Also a shoutout to my mentor on this project [Maranatha A. Ilesanmi](https://github.com/mbilesanmi) for providing guidance when needed.

---

## Contact

**E-mail:** a.cruzana88@gmail.com :technologist:

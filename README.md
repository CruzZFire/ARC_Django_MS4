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
* User wants to see the rankings of best books and users.
* User wants to have a opportunity to promote books they like.
* User wants easy access from its profile to the books and reviews connected.
* User wants to have a list of books they are currently reading in its profile.

The site [(see full-size preview)](/media/screenshots/home-full.png) is based on the Django framework. This system consists of "Views" with different "Models" filling inside of "Templates" depending on the route taken by the user. The way this system works makes all transitions easy and smooth for the user, being highly intuitive, but also for the developer, making it very easy to connect the models and views from different apps. In this specific WebApp, user experience is supported with toast messages each time an action is completed, giving this way direct informations to the user of any progress made.

Both the browser version and the portable device version are distributed in the same way, navigation stays fix at top and deploys as sidebar [(see browser preview)](/media/screenshots/home-full.png) making it easier to access every part of the WebApp when needed. In the portable device version, navbar is reduced to the logo and a menu icon [(see protable device preview)](/media/screenshots/home-phone.png).

### Strategy
The goal is that the user has creates a profile and uses the WebApp to review and recommend books.

To achieve this, first, the home page has several CTA and slogans to prompt the user to participate in the book community. Secondly, and helped by the template system, the design is very stable and similar among all the views, getting to be familiar with the user in very little time.

The most ambitious goal, which wasn't fully implemented due to scarce time, is to make writers subscribe to plans for promoting their books to a featured section in order to get more reviews, [(see Future Features)](#Future-Features-Objectives). Actual implementation was for the regular users/readers to promote the books they like, [(see Features)](#Features).

### Wireframes
Here are the first concept wireframes:

* [Index Page](/packageapp/static/wireframes/draft/Home.png "Index Page")

![Profile Page](/packageapp/static/wireframes/draft/LogIn.png "Profile Page")

* [Books Page](/packageapp/static/wireframes/draft/LogIn.png "Books Page")

* [Book Profile](/packageapp/static/wireframes/draft/Search_Result.png "Book Profile")

Final concept wireframes:

* Index Page: 

    ![Browser-View](/packageapp/static/wireframes/idea/Home.png "Browser View")

* [Profile Page](/packageapp/static/wireframes/idea/LogIn.png "Profile Page")

* [Books Page](/packageapp/static/wireframes/draft/LogIn.png "Books Page")

* [Book Profile](/packageapp/static/wireframes/draft/Search_Result.png "Book Profile")

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
A crucial part of the project is the database and its structure, [check schema](/media/screenshots/dbschema.png). The cluster consists of a dataset found in Kaggle.com and processed by me to a json file to add as Django fixtures. Here's the explanation of the database tables and relations between them:


## Contact

**E-mail:** a.cruzana88@gmail.com :technologist:

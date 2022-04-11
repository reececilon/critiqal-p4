# Critiqal

Critiqal is review site for the coolest movies of all time, whether they are old classics or hot new blockbusters. This site offers users the opportunity to sign up, read reviews, and discuss their thoughts in the comments section. The reviews are organised into cards showing only the most crucial information about the movies. Users can chose to read more information about the reviews for better insite.

![Image of Critiqal app on different screen sizes](static/media/responsive.png)

# UX

## Visitor Goal

* Allow users to browse reviews about movies.
* Enable users to register to the review site.
* Allow the users to like reviews.
* Allow the user to engage in discussions in the comments section.
* Enable users to read a reviews to gain information about a movie.
* Allow users to watch a movie trailer to understand the plot.

### User Stories

### User

* As a **site User** I can **view a review list** so that **I can select a review to read**.
* As a **site User** I can **view a paginated list of reviews** so that **I can easily select one to view**.
* As a **site User** I can **Register and account** so that **comment and like a review**.
* As a **site User** I can **comment on review posts** so that **I can share my opinion and engage in discussion**.
* As a **site User** I can **like/unlike a review** so that **I can show whether I agree with it**.
* As a **site User** I can **view a trailer from the review post** so that **I can know what the movie is about and whether I like it**.
* As a **site User** I can **click a button** so that **I can view full content on a review**.
* As a **site User** I can **View the likes on a review** so that **I can see whether audience is in agreement**.
* As a **site User** I can **view the comments on a post** so that **I can read the discussion**.
* As a **site User** I can **view a star rating** so that **I can know quickly how good a movie is**.

### Admin

* As a **Site admin** I can **upload a youtube link to a trailer** so that **audience can view trailer directly from the review**.
* As a **Site admin** I can **create, read, update and delete reviews** so that **I can manage content**.
* As a **Site admin** I can **approve the comments on a review** so that **I can ensure comments are unobjectionable**.
* As a **site admin** I can **create drafts** so that **submit a review at a later time**.
* As a **site admin** I can **View the likes on a review** so that **I can see whether audience is in agreement**.
* As a **site admin** I can **view the comments on a post** so that **read the discussion**.

### Developer

* As a **developer** I want to **ensure that the user can't break the flow of the site** by **applying defensive design choices**.
* As a **developer** I want to **enable the authenticated user to access all features of the site correctly**.
* As a **developer** I want to **provide options for the admin to quickly modify site**.

### Design Features

#### Fonts:

For the logo of Critical I wanted a font that was sharp, to emphasise the idea that created the name. 
To be critical and to critique. Hence, I chose a font that was narrow to embody this idea. 
The Font I chose for this is [League Gothic](https://fonts.google.com/specimen/League+Gothic?query=league+gothic) font.
This font is the main font for this site.

The second font I used was [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto), which is a very simple font that compliments the League Gothic font well.

#### Colours:

The main colour I used for this site is #C1EBFC, which is a light blue colour. I thought it was an very striking colour which allowed the logo to stand out. 
To compliment this I chose a few different tones of grey, which further allowed the light blue to stand out whereit was applied.

![Image of colour bar displaying colour options for Critical site.](static/media/colours.png)

### Wireframes

Some pages are not shown to be on different screen sizes. This is because the page is the same for smaller screen sizes but for narrower screens.

#### Desktop:

The home page has been slightly adapted to include a main image since the wireframing was decided. But all other features remained the same.

- [Desktop view of Home page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/dthome.png)
- [Desktop view of Review content page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/dtreview.png)
- [Desktop view of Registration page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/dtregister.png)
- [Desktop view of Login page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/dtlogin.png)

#### Tablet:

- [Tablet view of Home page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/thome.png)
- [Tablet view of Review content page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/treview.png)

#### Home page Mobile:

- [Mobile view of Home page](https://github.com/reececilon/critiqal-p4/blob/main/static/media/mhome.png)

## Features

### Existing Features

* Header
    * The header starts at the beginning of the page which includes the site logo, **Critiqal**, which acts as a link to the Home page.
    * Navigation is also present in the header, allowing the user to Register, Login/Logout, or return to the home page.
    * The logo is displayed in the main colour of the site, light blue, against the grey background.
    * And finally a quote about cinema.

![Image of the header](static/media/header.png)

* Main Image
    * The main image section changes depending on whether the user is authenticated. If the user is not authenticated, The main section displays a registration button followed by the site logo.
    * I the user is Authenticated, the mainsection describes the purpose of the site.
    * The registration button changes colour when hovered over to indicate to the user that it is clickable.

![Image of main section](static/media/main.png)

* Review List 
    * The movie reviews are paginated to hold only 8 reviews per page.
    * Each review is desplayed on a card which has an overlay providing only the most essential information about the movie review.
    * When Hovered over, the overlay of the cards is displayed, showing: the movie name, the rating, the excerpt, the author, the created-on date, and the no. of likes.
    * A clickable button is also displayed enabling the user to **Read** the review. And to further encourage this to the user, the button is designed to turn light-blue when hovered over.
    * A **Next** button is also featured on the section to enable the user to view more reviews.

![Image of the review list](static/media/list.png)

* Footer
    * The footer uses the same styling as the rest of the site. Containing the sicial links of the site, to enable the user to keep updated with the reviews through social media.
    * The links show an icon for each social in a dark grey colour.
    * When hovered over Each link will turn light blue.

![Image of the footer](static/media/footer.png)

* Review Content 
    * This section displays the main information of the review. With text about the movie that wraps around the main image card.
    * The image card shows the rating of the movie when hovered over, the auther, the created-on date, and a heart icon followed by the no. of likes.
    * The heart icon signifies likes of the reviews.
    * The heart icon is clickable, and will like or unlike of the uses clicks.
    * The icon is only clickable in the review content section to encourage the user to read the content before deciding whether they like the movie.
    * If a Youtube link for the movie is provided, the review will automatically show an iframe, enabling the user to watch the movie trailer directly from this site.
    * If a link is not provided, the site will tell the user that no trailer is available.

![Image of review content section](static/media/content.png)

* Comments Section
    * The comments section shows past comments on the left side of the screen with each comment in descending order, based on created date. Where older comments are displayed at the top. Allowing conversation to flow better.
    * If the user is authenticated, a comment box will be displayed on the right, allowing the user to comment on the review.
    * A button in a dark grey colour turns light-blue, following the colour theme of the site, when the user hovers over, to allow the user to post the comment for approval by the admin of the site.

![Image of the comments section](static/media/comments.png)

* Registration Form
    * The registration form is displayed in the main colour theme of the site.
    * The user is requred to choose a username and password to sign up.
    * Email is an optionaly field.
    * A link to the login page is also available to users already signed up.
    * The login page is similar in aesthetic to the sign-up page.

![Image of registration form](static/media/register.png)

## Data Storage

The tables below show the datat structures used for creating reviews and commenting on the reviews. For comments the post, name, email and created_date are automatically updated based on the user logged in and the post that is being viewed.

### Review Table

| Title            | Key In Database | Form Validation | Data Type |
|------------------|-----------------|-----------------|-----------|
| Author       |      author        |  no validation  | ForeignKey  |
| Title       |   title   | max length 200 | CharField |
| image       |  featured_image   | no form validation | CloudinaryImage |
| content      |  content | no max length | TextField |
| created      | created_date | datetime.date.today | DateField |
| updated      | updated_date | datetime.date.today | DateField |
| likes        | likes | no form validation | ManyToManyField |
| status       | status | no form validation | IntegerField |
| slug(unique) | slug | no form validation | SlugField |
| rating       | rating | no form validation | IntegerField |
| youtube-trailer-link | yt_link | no form validation | TextField |

### Comments Table

| Title            | Key In Database | Form Validation | Data Type |
|------------------|-----------------|-----------------|-----------|
| Post       |      post        |  no form validation  | ForeignKey  |
| Name       |  name   | max length 80 | CharField |
| email       |  email   | must contain @ and .com etc | EmailField |
| Body      |  body | max length 300 | TextField |
| Created_date      | created_date | datetime.date.today | DateField |
| Approved      | apporved | no validation | BooleanField |

## Technology Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Tools

- [Heroku](https://www.heroku.com)
- [Git](https://git-scm.com/)
- [Postgres](https://www.postgresql.org/)

## Testing

No Automated testing was performed for the production of this site. Rigorous manual testing was performed through numerous user experiences.

- <strong>Implementation</strong>:
When designing the review list, movie review data is added to the database and can then be observed from the home page. To ensure that reviews loaded as expected and information was visible when the review was hovered over and review content was loading when clicked on, I manually tested this.

- <strong>Test</strong>:
To perform this test, I individually went through each test, loading the review content of each review, and attemted to change the urls to see whether each item loaded as expected.

- <strong>Result</strong>:
Each review loaded correctly with no information missing. When changing the urls to one that did not exist, a 404 error page was shown.

- <strong>Verdict</strong>:
The test passed and as the 404 error page is from the generic Django 404 error page, I design a custom 404 error page in the case that a user attempts to navigate from the page by changing the url.

---

- <strong>Implementation</strong>:
Users should not be able to comment on reviews unless they are authenticated. 

- <strong>Test</strong>:
To test this, I checked individually that each review, when user is not authenticated, does not show the comment box. I also copied the url when logged in, then logged out and siply pasted the url in to see if it would enable the comments.

- <strong>Result</strong>:
The comments box was not available on any of the review if the user was not authenticated. Even if the user changed the URL, the comments box was not available without authentication.

- <strong>Verdict</strong>:
The test passed and no amendments were necessary. 

---

- <strong>Implementation</strong>:
User are also unable to like/unlike reviews without authentication.

- <strong>Test</strong>:
To test this, I checked each review, attempting to like the review and then tried to change the url when logged in.

- <strong>Result</strong>:
When attempting to like the Review, I was unable to like the review without authentication.

- <strong>Verdict</strong>:
This test passed, and required no amendments.

---

- <strong>Implementation</strong>:
The user is required to register with only a username and password, and email is an aptional field. 

- <strong>Test</strong>:
To test this I attempted to create an account with only an email, or only a space in the CharField of the username.

- <strong>Result</strong>:
As expected, registration from this basis is not enabled. Although upon testing this, I discovered that when I registered a user with an email and username, after creating the user, I was sent to a 500 error page.

- <strong>Verdict</strong>:
Upon fixing this I changed the setting of Allauth authentication to fix this bug and also produced a custom 500 error page.


### Bugs

---
* <strong>Problem</strong>: Some card info was pushed outside of the cards.
* <strong>Cause</strong>: This was due to the movie title and excerpt being too long.
* <strong>Resolution</strong>: To tackle this, I made the CharField length of the excerpt smaller and also reduced font size.

---
* <strong>Problem</strong>: When user provides email in registration, user is sent to 500 error page.
* <strong>Cause</strong>: Allauth verified the users email after. Because of this, if user provided an incorrect email, user was sent to 500 error page.
* <strong>Resolution</strong>: Changed allauth settings to not verify users email, and provided a custom error page.
 
### Unresolved Bugs

No unresolved bugs to confirm to still be present in site.

## Deployment

This site was deployed using Heroku [Critiqal](https://critiqal.herokuapp.com/)

The following deployment instructions are to deploy a Django app to Heroku, assuming the necessary libraries have been installed, basic django application has been created, and PostgreSQL database is set up.

From this point, the four main steps dor deployment are as follows:

1. Create the Heroku App
2. Attach the database
3. Prepare our environment and settings.py file
4. Get our static and media files stored on Cloudinary

### Create the Heroku App

- Once logged into your personal Heroku account, In the top left corner is located an icon "New". Click this button and you will be provided with two options.
    - Click the option to create new app
- You can then choose a name for your application and your region.
- Then click Create app

- Then navigate to the Resources tab, and in the add-ons search bar, search and add "Heroku postgres".
    - click "Submit Order Form"
- In the settings tab, click Reveal Config vars and copy the CATABASE_URL.
- In your gitpod workspace for your new application create a new file called "env.py"
    - Import os library
    - Set up environment variables as the example demonstrates:
    os.environ['DATABASE_URL'] = 'postgres://...'
    os.environ['SECRET_KEY'] = 'Your Secret Key'
- Then add your SECRET_KEY to Config vars back in Heroku app settings
- In setting.py file for Django app
    - Reference env.py file
    - Remove insecure secret key and replace with links to SECRET_KEY from Heroku config vars
    - Comment out old Database section
    - Add new database section from DATABASE_URL as follows:
    "
    DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    "
- Save all the files and make migrations

### Setting up Cloudinary

- Copy CLOUDINARY_URL environment variable from dashboard
- Add ClOUDINARY_URL to env.py as shown:
    os.environ['CLOUDINARY_URL'] = 'cloudinary://...'
- Add CLOUDINARY_URL to Heroku config vars
- Add DISABLE_COLLECTSTATIC to Heroku Config Vars and set to 1
- Add Cloudinary Libraries to installed apps in settings
- Tell Django to use Cloudinary to store media and static files in settings.py
- Link file to the templates directory in Heroku
- Change the templates directory to TEMPLATES_DIR
- Add Heroku Hostname to ALLOWED_HOSTS as follows:
    ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
- On top level, creat the folders static, media and templates
- Create a Procfile
    - add "web: gunicorn PROJ_NAME.wsgi"
- Add, Commit and Push to GitHub
- And Deploy Content Manually through Heroku with "DEBUG = False" in settings.
    - To deploy click the deploy icon back in Heroku
    - Click "Connect to GitHub"
    - Then find the repo name of the app you created with Django
    - and manually deploy.


        
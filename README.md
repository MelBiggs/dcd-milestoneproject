![] Put link to gif here 

[Link to Deployed Website]( link )

# Code Institute Milestone Project 
## Recipe Blog 

The objective of this project was to build a MongoDB-backed Flask project for a recipe website. 

This project consists of a  

The Home page shows 

It leads on to the Recipes page which contain 

There is also a page to add a recipe and an About page. The user can log in or register also.

Social media links are included. 



## UX

The main goal in the design of this project 

I wanted to implement a colour palette which XXXX . 

With this dashboard, the target audience consists of all age groups who have an interest in cooking and food. 

[Here is a link to my UXD document] ()

### User Stories

* As an individual interested in cooking, 

* As a user who wishes to know what dishes are popular, 

* As a user who may be of an older demographic, I want a website which is easily navigated so that I can move through the webpage with ease.

* As a user who may be of a young demographic, I want the information to be laid out in a way that is understandable in order to make the most of the information present. 

* As a user I would prefer the option to reset the chosen filters to avoid having to individually remove each of the filters myself. 

## Wireframes

[Here is a link to my wireframe]( )


## Features
### Existing Features
My website consists of the following features: 

* **Navbar**: The navbar contains XXX

* **Search**: This feature allows the user to search for a particular recipe in the database. 

* **Recipe filter**: This feature allows the user to filter the data according to a specific artist.

* **Reset Button**: This feature that enables users to reset their selection.

* **Footer**: A footer at the end contains a link to the dataset and a link to Spotify’s main page. 

* **Responsive**: This dashboard has been made responsive so it allows the user to access this page through their mobile, tablet or desktop and have a pleasant user experience each time.

### Features Left to Implement

In the future, I would like to add more features to this website, such as:

XXXX 

### Another feature idea

XXXXX

## Technologies Used

### Programming Languages 

[HTML](https://en.wikipedia.org/wiki/HTML) -
HTML was used to control the layout and the structure of the dashboard.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) -
Cascading Style Sheets are used to describe the appearance of a website and I used it to make my website look appealing to the user.

[Javascript]( https://www.javascript.com/) - 
Javascript was used to introduce the interactive elements to the project. 

[Python]( https://www.python.org/) - 
XXXX

### Database

[MongoDB]( https://www.mongodb.com/) - 
XXXX

### Frameworks 

[Flask]( https://www.palletsprojects.com/p/flask/) - 
XXXX

[Bootstrap 4.0](https://getbootstrap.com/) - 
Bootstrap is a very useful CSS Framework. You can save time writing code by using the Bootstrap predefined design templates. It has a great grid system and is responsive to different screen resolutions.

### Libraries 

[JQuery](https://jquery.com/) - 
The project uses JQuery to simplify DOM manipulation.

[Gitpod](https://www.gitpod.io/) - 
Gitpod is the code editor I used to write the HTML and CSS.

[FontAwesome](https://fontawesome.com/) - 
Font Awesome is a great library of icons. I used this library for my link icons.

[Google Fonts](https://fonts.google.com/) - 
There is a great selection of fonts in the Google Fonts library, some of which I used in my project. 

### Also

[Gifox](https://gifox.io/) - 
I used Gifox to record the website demo for my README file. I recorded it off the website [Am I Responsive](http://ami.responsivedesign.is/?url=https%3A%2F%2Fmelbiggs.github.io%2Fifd-milestoneproject%2F#)

## Testing
* As an individual interested in popular music, I believe they will reach their intended goal. They can navigate the page and find out the audio features of their choice of the top 70 artists along with how many songs they have in the Top 100. They can follow the links for more information and read the comment card to have the charts explained. I manually tested each of the links to the band's social media accounts and each of these opened on a separate tab (due to using 'target="_blank"') to the correct destination.

* As a musician or producer who wishes to release music that has a better chance of generating attention or a user who wishes to know what makes up a Top 100 song, they can also see the energy, danceability, valence and genre that are prevalent in the Top 100. They can see what artist is most popular. They’ll see that the majority of the songs have high energy and danceability, they are relatively positive-sounding and that Hip-Hop/Rap and Pop are the most popular genres.

* As a user of an older age, I want it to be as easily navigated as possible and attractive on a desktop or tablet. Younger users may more regularly use their phone and while the dashboard is best on a larger screen size, I believe my project allows the user to achieve their goals in an easy, straightforward and pleasant way. On different screen sizes and browsers, the project looks good.

There was a bug with the valence, energy and danceability correlation chart. It would not respond to efforts to make it responsive. Using `< .useViewBoxResizing(true)>` didn’t throw an error but the chart would not appear in its card. That issue was resolved by adding `< #energy_to_danceability_to_valence{ height: 70%; width: 50%; }>` to the style sheet. It is now responsive and shrinks with the screen. 

### Code Validation

#### CSS
I validated my CSS code using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). This showed no errors.

#### HTML
I validated my CSS code using [W3C Markup Validation Service]( https://validator.w3.org/). This helped me to spot any small mistakes to the code and to clean it up. It warned me that my sections lack a heading but I have decided that it is appropriate to ignore this warning. 

#### JavaScript
The JavaScript code in my project was validated using [JSHint]( https://jshint.com/). This was really useful in identifying any extra semicolons that I may have missed and for cleaning my code. 

### Jasmine
When researching whether to test my code with Jasmine, I was told that it was not necessary as it is from the DC.js library. However I have three helper functions, `<millisToMinutesAndSeconds>`, `<transformKey>` and `<transformMode>`. I could use Jasmine to test these functions. 

I created tests for these which can be seen in `<graphSpec.js>` and run by previewing `<tests.html>` or on [Github](https://melbiggs.github.io/ifd-milestoneproject/tests.html). You may need to refresh the page a few times to see an accurate result.

### Responsiveness
I tested the responsiveness of the webpage on browsers such as Chrome, Microsoft Edge and Safari and on multiple mobile devices. The page is fully responsive and I am satisfied that it works well on all devices.

### Peer Code Review
I published my project on the Code Institute's 'Peer Code Review' channel. This channel allows other students to have a look at your code and offer suggestions and comments to improve your project. There wasn't a lot of traffic on the channel so I messaged a team lead for Interactive Frontend Development, **Derek Olson**, and he recommended centering my navbar title and moving my comments and explanations up closer to my charts. I took his advice. Instead of having one large card where I explained the terms, I explained them under each of their relevant charts. 

## Deployment

### Deployment onto GitHub
1. The git repository was initiated by inputting the command `<git init>` into the terminal 
2. I then used `<git add>` to add the files to the staging area before using the `<git commit -m "Description of work done">` command to commit the files.
3. I created a repository on GitHub and linked to it by using command `<git remote add origin https://github.com/MelBiggs/ifd-milestoneproject.git>`
4. I could then push my files into GitHub by using `<git push>`
5. To publish my site using GitHub Pages, I navigated to my GitHub Pages site's repository.
6. Under my repository name, I clicked Settings.
7. I scrolled down to the GitHub Pages section and used the Select source drop-down menu to select 'master' as my GitHub Pages publishing source.
8. Click save. 
To summarise, this site is hosted using GitHub pages, deployed directly from the master branch and the deployed site will update automatically upon new commits to the master branch. 
To run locally, you can clone this repository directly into the editor of your choice by pasting `<git clone https://github.com/MelBiggs/ifd-milestoneproject.git>` into your terminal. To cut ties with this GitHub repository, type `<git remote rm origin>` into the terminal.

## Credits

### Content
The dataset I used was downloaded from [Kaggle]( https://www.kaggle.com/janicejung/spotify-top-100-of-2018-with-genres).

### Media
The favicon I used was found on [favicon.io](https://favicon.io/emoji-favicons/)

### Acknowledgements
I received inspiration for the theme of this project from [Spotify]( https://www.spotify.com/ie/).  

I received tips on snippets of my code through [Stack Overflow](https://stackoverflow.com/), [CodePen]( https://codepen.io/) and [W3Schools](https://www.w3schools.com/).

I am very grateful to my mentor **Guido Cecilio** for his help and guidance throughout the project. I would also like to thank my mam and my friends for helping me test the responsiveness of the website. I would also like to thank the Code Institute Slack users for their helpful comments and suggestions on my project. 

[Link to Deployed Website](https://melbiggs.github.io/ifd-milestoneproject/)
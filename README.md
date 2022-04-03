# States 'N' Facts

States 'N' Facts is an interactive app designed to Provide user generated information about the various States that make up the U.S.
 

![App Screenshot](static/media/Screenshot1.png) 

## User Experience

### Goals

### User Goals
- As a user, I want to be able to easily navigate the site to find the information I need.
- As a user, I want to see a visually appealing and responsive site.
- As a user, I want to able to feel a sense of security.
- As a user, I want to be able to add , edit and delete information as needed.

### Owner Goals
- As the owner, I want my site to be easily navigated.
- As the owner, I want my users to be able to add and remove data without any issues.
- As the owner, I want the user to be able to log in as well as log out easily.

## Planning

### Wireframes

![App Screenshot](static/media/Screenshot2.jpeg)

![App Screenshot](static/media/Screenshot3.jpeg)


## Design

### Colour scheme
I went with a hot colour scheme with vibrant colours to evoke a sense adventure as each state comes with its own interesting information. Most of the colors are similar to red and are striking to the eye, and will grab ones attention as soon as the site is launched.
 
### Colours that were used

| Color             | rgb                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Persian green | rgb(42, 157, 143) |
| Maize crayola | rgb(233, 196, 106) |
| Sandy brown| rgb(244, 162, 97)|
| Burnt Sienna |rgb(231, 111, 81)  |


## Font

The font was largely unchanged in this project, as a design choice, as I struggled to find a font that would work better than the default font in displaying the information without compromising the look and feel of the site while also retaining a professional aesthetic.

## Features

- Responsive site that adapts to screen size

- Ability of the user to log in and out of the site

- Ability to add and remove information

- Site can be accessed across multiple devices and browsers

- Visually striking abd good looking site

## Technologies Used

- ### Html

- ### CSS

- ### Javascript

- ### Python

## Libraries/Frameworks used

- Materialize : Allowed me to create the collapsible elements in the project, as well as most other features in the html, that were mobile first in approach without compromising other devices.

## Programs used

- Git : Allowed me to push my changes to the repository

- Github : Stores my repository

- Gitpod : the editor where I write my code.

- MongoDB: served as the database to store information

- Heroku: Deployed the finished app

# Running Tests

 ## Validators used

The validators below were used to check my cide via URL to endure there were no errors with it.
Javascript however was checked locally.
 -  ## W3C Markup validator

Base.html : No errors were found 

fact.html : No errors were found

delfact.html : No errors were found

create.html : No errors were found

login.html : No errors were found

names.html : No errors were found

profile.html : No errors were found



 -  ## W3C CSS validator
 Style.css : No errors were found



 -  ## JSHint Javascript code quality checker
 Script.js : No errors were found 

 


 ## Testing against my User Goals

- ### As a user, I want to be able to easily navigate the site to find the information I need.
I added a very prominent navigation bar which inidicates clearly to the user where they need to go in order to add/remove information

- ### As a user, I want to see a visually appealing and responsive site.
he site uses bright and appealing colours that also more importantly do not get in the way of the purpose of the site

- ### As a user, I want to able to feel a sense of security.
Users are able to securely log in and log out 

- ### As a user, I want to be able to add , edit and delete information as needed.
Users are able to create accounts and log in, which allows them to be able to add or make changes to the facts that are attached to each state.

## Testing responsiveness on multiple screen sizes

The site was tested on a Samsung galsxy s21 as well as a regular pC, the site was responsive and had no issues present. The min browser used was Google Chrome.



## BUGS

- There was a bug where after inputing a fact into the input field, even if the wrong information had been entered (e.g a word that was not one of the 50 states), the statement "a new fact has been added" would be displayed which would cause confusion.
I fixed this by adding an extra condition wihin the code to ensure that the entry actually existed within mongodb amd to display an error if it did not.

- There was a bug where mongo db was unable to store information entered by user, and would come back as null in the database,I fixed this by converting the entries into a string before being fed to mongoDB.


# Deployment

This Project was deployed via Heroku

### Timeline
- Repository was located after logging in to github : https://github.com/NyHagan/Statesproject
- Launched Heroku
- Created a new App called States 'N' Facts
- Attached this app to github in order to deploy

### Cloning My Repository
- Locate My Repository via github : https://github.com/NyHagan/Statesproject
- Click on the green 'code' button to create a local clone

### Heroku

- Launch Heroku and create an account

- Click Create a new app and follow guidelines

- Name app and choose region

- Click Github and eter repository name and click connect

- scroll down and enter relevant config vars

- Deploy


## Future optimisation

- addiditon of a responsive dropdown for search functions

- animations

- larger array of photos

## Support

email nanaohagan@gmail for any support

## Author

Nana Hagan
- [@NyHagan](https://github.com/NyHagan)

## Acknowledgements

- My Mentor Spencer Barriball

- Code Institute

- The Learning People
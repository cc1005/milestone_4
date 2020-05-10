# Milestone Project 4

## Your Project's Name
**Irish Archive Database**
This project is designed to streamline access to important historical files on behalf of a (fictional) Irish historical archive. Most Irish archives require attendance in person to view documents, and most of these archives are located in Dublin, a clear inconvenience for any researchers located elsewhere. This website will provide unlimited access to digitised documents for a subscription fee, payable monthly. The files will be available to be read in browser. Free users will not require a user profile to browse the catalogue. 

The website will also function as an advertisement for the archive itself, with contact information and the location of the archive advertised on every page.

## UX
* See /READMEfiles/ for wireframe mockups from the early stage of the project.
This website is primarily for academic researchers who would benefit from remote access to important historical documents. It will have a broad age profile - primary researchers in Irish history (the likely primary customers) can vary from PhD students in their 20s to senior professors. Some of these users will have limited database experience, so the UX should be as streamlined and straightforward as possible. These researchers will want access to a large database of searchable records which this website will provide.

The colour palette was deliberately chosen to be muted to reflect the academic nature of the material presented to the user. The website is also reactive, with image icons representing the content of each document disappearing at smaller video sizes (as does the google map in the footer). 

Several elements of the website are designed to encourage users towards the premium membership. Firstly, a jumbotron will appear on the landing page of any user who does not have premium access advertising this service. The descriptor of the page will also highlight that the full records are not available to free users. Additionally, at the bottom of every record will be a prompt for non-premium users to register for premium access. Finally, the checkout process was designed to be as simple and streamlined as possible, with only a single subscription option available, to simplify the decision making process for prospective customers. 

The UX went through a couple of concepts. Originally, the landing page was divided in half, with the catalogue on the left and the documents presented to logged in subscribers on the right (see wireframe mock-up document). This design was changed to the simpler and cleaner catalogue presentation in the final version, primarily for simplicity of design to cater for less experienced users (given the wide user profile). 

User stories:
* User 1: *individual interested in viewing the catalogue of the Irish Archive Database*
    * This user will be able to see and search the entire catalogue of the Irish Archive without a user profile. These search results will show the title and a brief description of any records held by the Irish Archive. Prompts will be presented to the user to encourage them to purchase a full subscription to access the entire document at various stages.
* User 2: *individual looking to conduct comprehensive historical research on a particular topic*
    * This user will require a full subscription to gain access to the information they want. This user will be able to search the archive using key terms, and then view the entire document transcript in browser. 
* User 3: *individual interested in the Irish Archive itself*
    * This user will be served by a footer containing contact details, social media profiles and a map of where the archive itself is located. 

## Features

### Existing Features
* **Account creation and login:** This feature allows users to register for an account, login to that account, see details of that account and request new passwords. An account is required for users to purchase a subscription. Password resets can be emailed to users's email account. 
* **Checkout:** This app allows for users to purchase either a monthly subscription to the service. An account is required to access this feature which is processed by stripe (see acknowledgements for the Nick Walter course that heavily influenced this section of the website and in-line comments in checkout.html for more). _Note: the stripe functionality in this website is in test mode, so the card number 4242424242424242 should be used to pay for premium membership, as well as any future date and any 3 digit number_
* **Search** Users will be able to search the titles of the records held by the Archive using key word terms.
* **Javascript Map** On larger viewport settings, a map is available to users who wish to visit the archive in person (A fake address has been used, as the Irish Archive is not a real place). This map was designed using custom css & javascript, influenced by videos hosted by Traversy media. 
* **Connected databases of records** Several interconnected databases were created for this project. The link between the catalogue and full documents proved difficult to conceptualise in the catalogue app views & models, given the ForeignKey determined relationship from the catalogue to the full document, but the construction of separate tables for these datasets allowed for free customers and premium customers to have clearly demarcated access points to the content on the website.

### Features Left to Implement
* **Advanced Search** A more detailed and filtered search system would be useful for this project, which would be coupled with a second feature which would be very useful:
* **Categorisation of resources** A categorisation of resources would greatly assist in their readability for the project and would provide a better landing page for the user. 
* **Download records** An unforeseen difficulty when setting up my databases was reformatting the lengthy text that would be put into the full records. This, in the current instance of this site, is reproduced as a single block of text. Obviously, this is not ideal from a readability standpoint, and one potential workaround for this would be to offer a download of the full text document formatted appropriately, perhaps in PDF format. Alternatively, some preliminary research has suggested that storing the lengthy text as XML may allow for it to be reproduced in browser in a more readable format. 
* **Looking at other archives** As can be seen in some of the wireframe mockups, there was an ambition to link searches of other archives. For time reasons this feature was not implemented.

## Technologies Used
* The core of the project is based on python-django.
* Javascript is used to power the map at the bottom of base.html (See javascript file in static from the earlier renditions of the project on github).
* The project uses JQuery to simplify DOM manipulation.
* HTML & CSS (often through bootstrap) are used to format and style the content of the website.
* External dependencies are used to support the project, and the process of connecting with them can be seen in the section on "Hosting". The primary database was a postgresql database linked to the project through Heroku (the hosting platform), which AWS S3 allowed for the storage of images and other static files to be called in the project. 
* Travis CI was used in the testing process. 

## Testing
Note: early on in this project I decided to move from Gitpod to using my local machine to eradicate some of the complications that that IDE was presenting. I decided to used Visual Studio Code 3 (vscode), and before I set up Travis for dedicated bug/failure tracking, I made use of PyLint to help avoid simple errors (although Pylint had shortcomings when it came to recognising that certain classes had certain members). 
There were two main routes through which I tested my project, and several routes through which I tried to amend any errors found through this process:
* **User testing (running through test scenarios myself to ensure functionality):** This was the primary route through which I tested this product, and the two main methods I used were:
    * _Immediate tests of new functionality_: Whenever I incorporated a new feature or started to develop a new feature in my project, i always did so with DEBUG mode set to True to allow for any errors to be traced. After trialling any new view/model/style, I would immediately test it on a local server to ensure that it ran smoothly. Frequently I would test these implementations using test code specifically designed to produce obvious results (for a simple example, see the commented out "testing" css in static/css/custom.css).
    Often, these trials produced errors. The nature of these errors was used to then deconstruct the mistakes that led to this error. One example demonstrates a fairly standard error:
    After connecting my FullDocument Model to the Catalogue Model using a ForeignKey, I got an error when trying to iterate over it to ensure that the full text from the FullDocument model could be produced. This error informed me that FullDocument object was not iterable. After consulting with the slack channel and looking through StackOverflow, I eventually realised that my method of calling the FullDocument object (object.get) did not return a Queryset, meaning that it was not iterable. Testing the view code that produced this error shortly after its creation allowed me to catch this bug immediately, and made the second aspect of my testing somewhat easier:
    * _Running User stories_: The second main method I used to test my website functionality was running user test stories (see above). By trying to perform all the actions any one of those users would potentially do upon arriving on my website, i was able to routinely test the core loops that defined by User Experience. This process caught a very significant bug late in the development process, essentially preventing me from submitting the project without the core functionality. 
    Late in the project I decided to streamline my stripe functionality and use stripe checkout to process payments instead of a modified version of the payment system used by Nick Walter (see acknowledgements). Upon running through a user story on the live version of the project on Heroku, I discovered that this new payment method was not storing the user as a Customer (as was necessary for them to gain access to the premium aspects of the website), rendering their (test) payment functionally useless. Thankfully, I practiced extensive version control throughout the project, so was able to reference a Git Push from earlier in the day to revert back to the previous working code. 
    **1:** User 1: This user, upon reaching the website, can see all catalogue options laid out before them. They cannot access any of them, the only links available to them are to login or to register for an account (a prerequisite for purchasing a premium subscription, as made clear in the navbar). All titles and descriptions are available for them.
    **2:** User 2: This user will originally be faced with the same options as User 1, but will be presented with several prompts making it clear how to proceed. They will click to register, where they will be informed (if they had not already read on the navbar) that they need an account to subscribe for premium membership. After setting up their account, this user will be returned to the catalogue menu, where they will be presented in the jumbotron with the prompt to register for premium access. Following through this link, the user will be presented with a simple stripe payment system. Once they have inputted their payment data (which will register them as a customer and transfer the funds to my stripe account), they will be returned to a separate catalogue page with all the records unlocked. Instead of being prompted to register under each document, they will have a single link to access the full document. 
    **3:** This user will be able to scroll to the bottom of the page and, on medium and above browsers, see an interactive google map with the location of the archive pinned in it. The postal address and social media accounts of the archive will also be available to them. 

* **Travis CI continuous testing:** This proved to be a somewhat difficult process, as I was confronted with several errors trying to set up this testing process. Originally, I was consistently met with an error concerning parsing my database, which had already been moved onto Heroku postgres. The solution to this was to provide an if/else statement checking whether there was access to that database and if not to test on Travis as if a local Sqlite database was being used. This, coupled with syntactical problems with the version of Travis CI I was using, resulted in several failing builds on Travis throughout the bulk of the project. Whenever the problem of uploading to Travis was finally resolved through the help of student support and the slack channel, the original build ran without any errors.

## Deployment
Several platforms were used to deploy the project. 
Heroku: Heroku hosts the website from the master branch of my GitHub project. I already had a Heroku account so I did not need to set one up to host the project. All environmental variables are stored in Heroku's vars, which are called on by the relative coding of the website (os.environ.get(EXAMPLE)). 
Heroku also provides the database for the project, a Heroku Postgres database. About 2/3 of the way through production, I switched from using a local sqlite database to using the Heroku Postgres database.
All static files are hosted on AWS S3, with access provided through an AWS USER set up to allow use of the bucket. A custom bucket was set up to hold the files, and despite some early teething problems (specifically being unable to upload pre-stored static files for pre-existing catalogue records) it has worked well since. 
As previously mentioned, Travis CI was used to test the project, and one of the last things I did before finally deploying the project was made sure Travis CI ran the project with no errors.   

## Credits
### Content
Historical materials were taken from a selection of sources to provide variety:
* https://www.oireachtas.ie/en where all records of state debates are published online,
* Wikisource https://en.wikisource.org/wiki/Constitution_of_Ireland_%28original_text%29 for the Irish Constitution,
* Documents on Irish Foreign Policy https://www.difp.ie/docs/1922/Northern-Ireland/278.htm provided some of the letters used in the project.
* The letter from GBS to the British Times was taken from the website of the Institute for Historical Review http://www.ihr.org/jhr/v08/v08p509_Klett.html 
### Media
Icons were provided by https://uxwing.com/, a royalty free icon website which requires no attribution for the icons in its database.
Bootstrap was used to provide all non-custom styling.
### Acknowledgements
* The Code Institute Django lessons were very important for shaping the majority of this project, especially the accounts app, search functionality which is heavily based upon the app created in the Code Institute lectures on Django Accounts. 
* A Linkedin Training course by Nick Walter called "Building a paid membership site with Django" provided the concept and some of the base code for the stripe functionality and use of a subscription service. The tutorials can be found here (https://www.linkedin.com/learning/building-a-paid-membership-site-with-djang) behind a paywall. 
* Traversy media provided several lessons on Django and javascript which proved very helpful in developing aspects of this project. Their video on developing google maps in Javascript (https://www.youtube.com/watch?v=Zxf1mnP5zcw) and Udemy course on Django development ("Python Django Dev to Deployment", https://www.udemy.com/course/python-django-dev-to-deployment, behind a paywall) helped expand my understanding of Django and helped develop the map functionality in the footer.
* Corey Schafer's videos on Django on YouTube were used to help develop my understanding of Django (https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g). Similarly, The FreeCodeCamp course called "Python Django Web Framework - Full Course for Beginners" also helped develop my knowledge early in the project (https://www.youtube.com/watch?v=F5mRW0jo-U4).


[![Build Status](https://travis-ci.org/cc1005/milestone_4.svg?branch=master)](https://travis-ci.org/cc1005/milestone_4)
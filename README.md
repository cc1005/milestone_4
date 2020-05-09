# Milestone Project 4

## Your Project's Name
**Irish Archive Database**
This project is designed to streamline access to important historical files on behalf of a (fictional) Irish historical archive. Most Irish archives require attendance in person to view documents, and most of these archives are located in Dublin, a clear inconvenience for any researchers located elsewhere. This website will provide unlimited access to digitised documents for a subscription fee, payable monthly or yearly. The files will be available to be read in browser as well as to download in a .jpeg format. Free users will not requre a user profile to browse the catalogue. 

The website will also function as an advertisement for the archive itself, with contact information and the location of the archive advertised on every page.

## UX
This website is primarily for academic researchers who would benefit from remote access to important historical documents. It will have a broad age profile - primary researchers in Irish history (the likely primary customers) can vary from PhD students in their 20s to senior professors. Some of these users will have limited database experience, so the UX should be as streamlined and straightforward as possible. These researchers will want access to a large database of searchable records which this website will provide.

The UX went through a couple of concepts. Originally, the landing page was divided in half, with the catalogue on the left and the documents presented to logged in subscribers on the right (see wireframe mock-up document). This design was changed to the simpler and cleaner catalogue presentation in the final version, primarily for simplicity of design to cater for less experienced users (given the wide user profile). 

User stories:
* User 1: *individual interested in viewing the catalogue of the Irish Archive Database*
    * This user will be able to see and search the entire catalogue of the Irish Archive without a user profile. These search results will show the title and a brief description of any records held by the Irish Archive. A prompt will be presented to the user to encourage them to purchase a full subscription to access the entire document
* User 2: *individual looking to conduct comprehensive historical research on a particular topic*
    * This user will require a fully subscription to gain access to the information they want. This user will be able to search the archive using key terms, and then view the entire document transcript in browser or choose to download it. 
* User 3: *individual interested in the Irish Archive itself*
    * This user will be served by a footer containing contact details, social media profiles and a map of where the archive itself is located. 

## Features

### Existing Features
* **Account creation and login:** This feature allows users to register for an account, login to that account, request new passwords and delete their accounts. An account is required for users to purchase a subscription.
* **Checkout:** This app allows for users to purchase either a monthly or a yearly subscription to the service. An account is required to access this feature which is processed by stripe.
* **Search** Users will be able to search the records held by the Archive using key word terms.

### Features Left to Implement
* **Advanced Search** A more detailed and filtered search system would be useful for this project, which would be coupled with a second feature which would be very useful:
* **Categorisation of resources** A categorisation of resources would greatly assist in their readability for the project and would provide a better landing page for the user. 


## Technologies Used


## Testing

Early on in this project I decided to move from Gitpod to using my local machine to eradicate some of the complications that that IDE was presenting. I decided to used Visual Studio Code 3 (vscode), and before I set up Travis for dedicated bug/failure tracking, I made use of PyLint to help avoid simple errors (although Pylint had shotcomings when it came to recognising that certain classes had certain members). 

## Deployment


## Credits
### Content

### Media

### Acknowledgements

A Linkedin Training course by Nick Walter called "Building a paid membership site with Django" provided the concept and some of the base code for the stripe functionality and use of a subscription service. The tutorials can be found here (https://www.linkedin.com/learning/building-a-paid-membership-site-with-djang) behind a paywall. 
Icons were provided by https://uxwing.com/, a royalty free icon website which requires no attribution for the icons in its database.
Historical materials were taken from a selection of sources to provide variety:
* https://www.oireachtas.ie/en where all records of state debates are published online,
* Wikisource https://en.wikisource.org/wiki/Constitution_of_Ireland_%28original_text%29 for the Irish Constitution,
* Documents on Irish Foreign Policy https://www.difp.ie/docs/1922/Northern-Ireland/278.htm provided some of the letters used in the project.
* The letter from GBS to the British Times was taken from the website of the Institute for Historical Review http://www.ihr.org/jhr/v08/v08p509_Klett.html 


[![Build Status](https://travis-ci.org/cc1005/milestone_4.svg?branch=master)](https://travis-ci.org/cc1005/milestone_4)
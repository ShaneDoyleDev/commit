# Commit - Testing Documentation

Visit the deployed site: [Commit](https://news-bytes-f757f042ac64.herokuapp.com/)

## Table of Contents

- [Validator Testing](#validator-testing)

  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Javascript Validation](#javascript-validation)
  - [Python Validation](#python-validation)
  - [Accessibility](#accessibility)

- [Lighthouse Testing](#lighthouse-testing)

- [Device Testing](#device-testing)

  - [Devices](#devices)
  - [Browsers](#browsers)
  - [Responsiveness](#responsiveness)

- [Manual Testing](#manual-testing)

  - [User Stories Testing](#user-stories-testing)
  - [Feature Testing](#feature-testing)

- [Bugs](#bugs)

## Validator Testing

### HTML Validation

[W3C HTML Validation Service](https://validator.w3.org/) - After some refactoring some of the code across my templates, I successfully managed to ensure that all HTML code I authored passed validation.

- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2F) - pass

- [Signup Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Faccounts%2Fsignup%2F) - pass

- [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Faccounts%2Flogin%2F) - pass

- [Articles List Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2F) - pass

- [Articles Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Freact-and-the-virtual-dom%2F) - pass

- [User Articles Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fuser-posts%2F) - pass

- [Create Article Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fcreate%2F) - pass

- [Update Article Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fupdate%2F1%2F) - pass

- [Delete Article Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fdelete%2F1) - pass

- [Update Comment Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fcomment%2Fupdate%2F19%2F) - pass

- [Delete Comment Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fcomment%2Fdelete%2F19%2F) - pass

- [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fprofile%2F5) - pass

- [Update Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fprofile%2Fedit%2F5%2F) - pass

- 404 Page (Validator would not recognize URL for 404, so uploaded the html manually) - pass

404 page results:
</br>
<img src="./readme-images/testing/validation/html/404-html-validation.png" alt="html validation results for 404 page">

### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnews-bytes-f757f042ac64.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - Upon submission, I was pleased to see that all pages have passed the W3C CSS Validation Service with no errors.

- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2F) - pass

- [Signup Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Faccounts%2Fsignup%2F) - pass

- [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Faccounts%2Flogin%2F) - pass

- [Articles List Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2F) - pass

- [Articles Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Freact-and-the-virtual-dom%2F) - pass

- [User Articles Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fuser-posts%2F) - pass

- [Create Article Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fcreate%2F) - pass

- [Update Article Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fcreate%2F) - pass

- [Delete Article Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fposts%2Fdelete%2F37) - pass

- [Update Comment Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fcomment%2Fupdate%2F19%2F) - pass

- [Delete Comment Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fcomment%2Fdelete%2F19%2F) - pass

- [Profile Page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fprofile%2F5&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - pass

- [Update Profile Page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommit-blog-81c3ab6546fa.herokuapp.com%2Fprofile%2Fedit%2F5%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - pass

- 404 Page (Validator would not recognize URL for 404, so had to upload the stylesheet manually) - pass

404 page results:
</br>
<img src="./readme-images/testing/validation/css/404-css-validation.png" alt="css validation results for 404 page">

### Javascript Validation

[JSHint](https://jshint.com/) - Was used to validate my Javascript code. Each script passed with no error present in the validation.

#### navbar.js results

<img src="./readme-images/testing/validation/js/navbar.js.png" alt="navbar.js validation results">

#### category-menu.js results

<img src="./readme-images/testing/validation/js/category-menu.js.png" alt="category-menu.js validation results">

#### messages.js results

<img src="./readme-images/testing/validation/js/messages.js.png" alt="messages.js validation results">

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to review and validate each Python script, ensuring they met coding standards without errors. Initially, it highlighted that some lines in the scripts exceeded the character limit. This prompted a refactoring of the code to resolve these issues. As a result, all scripts have been revised and are now error-free.

#### manage.py results - pass

<img src="./readme-images/testing/validation/python/manage.py.png" alt="manage.py validation results">

#### commit/asgi.py results - pass

<img src="./readme-images/testing/validation/python/commit/commit-asgi.py.png" alt="commit/asgi.py validation results">

#### commit/settings.py results - pass

<img src="./readme-images/testing/validation/python/commit/commit-settings.py.png" alt="commit/settings.py validation results">

#### commit/urls.py results - pass

<img src="./readme-images/testing/validation/python/commit/urls.py.png" alt="commit/urls.py validation results">

#### commit/wsgi.py results - pass

<img src="./readme-images/testing/validation/python/commit/commit-wsgi.py.png" alt="commit/wsgi.py validation results">

#### blog/admin.py results - pass

<img src="./readme-images/testing/validation/python/blog/admin.py.png" alt="blog/admin.py validation results">

#### blog/apps.py results - pass

<img src="./readme-images/testing/validation/python/blog/apps.py.png" alt="blog/apps.py validation results">

#### blog/comment_urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/comment_urls.py.png" alt="blog/comment_urls.py validation results">

#### blog/forms.py results - pass

<img src="./readme-images/testing/validation/python/blog/forms.py.png" alt="blog/forms.py validation results">

#### blog/models.py results - pass

<img src="./readme-images/testing/validation/python/blog/models.py.png" alt="blog/models.py validation results">

#### blog/post_urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/post_urls.py.png" alt="blog/post_urls.py validation results">

#### blog/profile_urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/blog-profile_urls.py.png" alt="blog/profile_urls.py validation results">

#### blog/tests.py results - pass

<img src="./readme-images/testing/validation/python/blog/blog-tests.py.png" alt="blog/tests.py validation results">

#### blog/urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/urls.py.png" alt="blog/tests.py validation results">

#### blog/comment_urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/comment_urls.py.png" alt="blog/comment_urls.py validation results">

#### blog/blog_filters.py results - pass

<img src="./readme-images/testing/validation/python/blog/blog_filters.py.png" alt="blog/blog_filters.py validation results">

#### blog/views.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/admin.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/apps.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/forms.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/models.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/tests.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/urls.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

#### accounts/views.py results - pass

<img src="./readme-images/testing/validation/python/blog/views.py.png" alt="blog/views.py validation results">

### Accessibility

Accessibility testing was conducted initially using Google Lighthouse which revealed good scores across all pages. However, in-depth analysis using the - [WAVE accessibility tool](https://wave.webaim.org/).

Testing revealed that I had missed assigning aria labels to some links and also I needed to enhance the contrast ratio of certain elements on the site. Once I had addressed these issues.

<img src="./readme-images/testing/validation/accessibility/wave-validation.png" alt="wave validation results">

## Lighthouse Testing

### Homepage

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-homepage-desktop.png" alt="Homepage Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-homepage-mobile.png" alt="Homepage Mobile">

### Signup Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-signup-desktop.png" alt="Signup Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-signup-mobile.png" alt="Signup Page Mobile">

### Login Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-login-desktop.png" alt="Login Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-login-mobile.png" alt="Login Page Mobile">

### Articles List Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-articles-page-desktop.png" alt="Articles List Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-articles-page-mobile.png" alt="Articles List Page Mobile">

### Articles Detail Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-article-detail-desktop.png" alt="Articles Detail Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-article-detail-mobile.png" alt="Articles Detail Page Mobile">

### User Articles Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-users-articles-desktop.png" alt="User Articles Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-users-articles-mobile.png" alt="User Articles Page Mobile">

### Create Article Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-create-article-desktop.png" alt="Create Article Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-create-article-mobile.png" alt="Create Article Page Mobile">

### Update Article Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-update-article-desktop.png" alt="Update Article Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-update-article-mobile.png" alt="Update Article Page Mobile">

### Delete Article Confirmation Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-delete-article-confirmation-desktop.png" alt="Delete Article Confirmation Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-delete-article-confirmation-mobile.png" alt="Delete Article Confirmation Page Mobile">

### Update Comment Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-update-comment-desktop.png" alt="Update Comment Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-update-comment-mobile.png" alt="Update Comment Page Mobile">

### Delete Comment Confirmation Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-delete-comment-confirmation-desktop.png" alt="Delete Comment Confirmation Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-delete-comment-confirmation-mobile.png" alt="Delete Comment Confirmation Page Mobile">

### Profile Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-profile-page-desktop.png" alt="Profile Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-profile-page-mobile.png" alt="Profile Page Mobile">

### Update Profile Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-profile-edit-desktop.png" alt="Update Profile Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-profile-edit-mobile.png" alt="Update Profile Page Mobile">

### About Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-about-desktop.png" alt="About Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-about-mobile.png" alt="About Page Mobile">

### 404 Page

- Desktop
  <img src="./readme-images/testing/lighthouse/lighthouse-404-page-desktop.png" alt="404 Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/lighthouse-404-page-mobile.png" alt="404 Page Mobile">

## Device Testing

#### Devices

These are the different devices I have tested my site on after deployment.
| Device | iPhone SE | iPhone X | iPhone 12 Pro | iPhone 13 Pro Max | iPhone 14 Pro Max | iPad | iPad Air | iPad Pro | Macbook Pro M1 |
| ------------------ | ----------- | ----------- | ------------- | ----------------- | ----------------- | ------------ | ------------ | ------------- | -------------- |
| **Resolution** | **375x667** | **375x812** | **390x844** | **414x76** | **414x896** | **768x1024** | **820x1180** | **1024x1366** | **1440x900** |
| Render | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Layout | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Functionality | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Links | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Images | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Portrait/Landscape | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |

#### Browsers

These are the different browsers I have tested my site on after deployment.

- Google Chrome
- Firefox
- Safari
- Samsung Internet

#### Responsiveness

- Responsiveness testing was performed using Chrome Developer Tools and ResponsivelyApp.

- Comprehensive testing of the website was carried out across various emulated devices including mobiles, tablets, and large-format screens, in both portrait and landscape modes.

### Homepage

<img src="./readme-images/testing/responsiveness/homepage-top.png" alt="Homepage Top">
<img src="./readme-images/testing/responsiveness/homepage-mid.png" alt="Homepage Middle">
<img src="./readme-images/testing/responsiveness/homepage-bottom.png" alt="Homepage Bottom">

### Signup Page

<img src="./readme-images/testing/responsiveness/signup-page.png" alt="Signup Page">

### Login Page

<img src="./readme-images/testing/responsiveness/login-page.png" alt="Login Page">

### Articles List Page

<img src="./readme-images/testing/responsiveness/articles-list-page.png" alt="Articles List Page">

### Articles Detail Page

<img src="./readme-images/testing/responsiveness/article-detail-page.png" alt="Article Detail Page">

### User Articles Page

<img src="./readme-images/testing/responsiveness/user-articles-page.png" alt="User Articles Page">

### Create Article Page

<img src="./readme-images/testing/responsiveness/create-article-page.png" alt="Create Article Page">

### Delete Article Page

<img src="./readme-images/testing/responsiveness/delete-article-page.png" alt="Delete Article Page">

### Update Comment Page

<img src="./readme-images/testing/responsiveness/update-comment-page.png" alt="Update Comment Page">

### Delete Comment Page

<img src="./readme-images/testing/responsiveness/delete-comment-page.png" alt="Delete Comment Page">

### Profile Page

<img src="./readme-images/testing/responsiveness/profile-page.png" alt="Profile Page">

### Update Profile Page

<img src="./readme-images/testing/responsiveness/update-profile-page.png" alt="Update Profile Page">

### About Page

<img src="./readme-images/testing/responsiveness/about-page.png" alt="About Page">

### 404 Page

<img src="./readme-images/testing/responsiveness/404-page.png" alt="404 Page">

## Manual testing

#### User Stories Testing

`Site Owner Goals`
| Site Owner Goals | How are they achieved? |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. As the site owner, I want to have an admin account that allows me to log in and out of the admin panel securely to access the site's administrative features. | The site owner has a superuser account that allows them access to the admin panel provided by Django. |
| 2. As the site owner, I want to be able to remove posts from the blog if they are not relevant to the content of the site or feature potentially malicious content. | From the Django admin panel, the site owner can read a blog post and remove if if is deemed inappropriate. |
| 3. As the site owner, I want to be able to remove comments from the blog if they are not relevant to the content of the site or feature potentially malicious content. | From the Django admin panel, the site owner can read a comments on all posts and remove any of them if deemed inappropriate. |
| 4. As the site owner, I want to be able to remove user accounts from the blog if they post content that is potentially offensive or not suitable for the blog. | From the Django admin panel, the site owner can delete any account if necessary. |
| 5. As the site owner, in addition to myself for admin reasons, I want only the authors of the posts be to update and delete them, along with their profile information. | Only the site owner or the blog author, when signed in, will see edit icons next to their posts and profile information. This allows them to update or delete their content as desired. |
| 6. As the site owner, I want to have a CTA section encouraging users to sign up for an account so they can contribute to the blog and grow the community. | The Call-to-Action (CTA) section, prominently displayed on the home page, boasts an engaging image accompanied by compelling text. It's designed to encourage visitors to register an account and begin contributing to the blog. |
| 7. As the site owner, I want the website design to have a modern look and be aesthetically pleasing and professional to make a good impression on visitors. | The website's UI design was meticulously crafted in Figma, with special attention paid to the overall layout, color scheme, typography, and imagery. This was done to create an aesthetically pleasing look and feel, befitting a modern tech blog.|
| 8. As the site owner, I want to have a footer showing copyright information and linking to my GitHub for exposure.| The footer is positioned at the bottom of every page on the site and features a link to my GitHub profile. This allows visitors to see and explore my other projects. |

`User Goals`
| User Goals | How are they achieved? |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. As a user, I want to be able to easily sign up with a unique username and password to create an account. | A 'Sign Up' button, conveniently located in the navigation bar, directs users to a registration page. Here, they can enter their credentials to successfully create an account. |
| 2. As a user, I want to be able to easily sign out of the site to keep my account secure. | When the user is signed in, a 'Logout' button will appear on the navigation bar. Upon clicking this button, the user will be securely signed out of their account. |
| 3. As a user, I want to be able to easily log in to the site with my username and password to view my account. | The login page provides a secure interface for users to sign in using their username and password. |
| 4. As a user, I want to receive notifications as feedback confirmation for important actions I perform on the site, including signup, sign in, sign out, and any submissions, updates, or deletions of content. | Whenever the user performs a CRUD operation, logs in, or logs out of their account, they will be notified via a pop-up toast notification at the bottom right of the screen. |
| 5. As a user, I want to have a profile section so other readers can get to know about me and connect. | Upon creating an account, users gain access to their personal profile section. This feature allows them to share information about themselves, including links to their social media platforms, with other users. |
| 6. As a user, I want to be able to upload my own profile picture to better showcase myself and make my profile more personal. | From their profile page, users have the option to upload a personal profile picture. This image will not only enhance their profile page but will also accompany any articles they author, further personalizing their contributions. |
| 7. As a user, I want to be able to write a short bio about myself to give others an idea of who I am. | The profile page features a section where users can write a short bio, providing them with an opportunity to share more about themselves if they wish. |
| 8. As a user, I want to be able to share links to my social media profiles to connect with others in the tech industry. | A section within the profile settings allows users to add and edit links to their social media profiles, helping build connections with peers within the tech industry. |
| 9. As a user, I want to be able to update my profile section to keep it up to date. | Users can access their profile settings at any time to update their bio, profile picture, social media links, and any other personal information, ensuring their profile remains current. |
| 10. As a user, I want to be able to write and post my own articles to share my thoughts and knowledge with the tech community. | A user-friendly editor is available on the site, allowing users to write, format, and publish articles they can share with others. |
| 11. As a user, I want to be able to edit my own articles to correct or add to them if I have accidentally made a mistake. | An 'Edit' option is available on articles authored by the user, enabling them to make modifications to their content at any time to correct errors or update information. |
| 12. As a user, I want to be able to delete my own articles if I decide I no longer want others to see them. | Users can delete their articles via a 'Delete' button, which is available on each of their published pieces, removing the content from public view after a confirmation prompt. |
| 13. As a user, I want to be able to comment and show my appreciation on posts I have read. | A comment section is enabled below each article, allowing users to leave feedback and appreciation. |
| 14. As a user, I want to be able to edit my comments if I have made a mistake or want to add something else. | Users have the ability to edit their comments after posting, providing an opportunity to correct errors or update their thoughts. |
| 15. As a user, I want to be able to delete my comments if I no longer want others to read them. | A 'Delete' option is available for users to remove their comments, giving them control over their contributions to discussions. |
| 16. As a user, I want to be able to easily navigate throughout the blog and reach the most important features from anywhere on the site. | The site features a fully responsive navigation bar at the top of everypage with links to key sections, ensuring that users can easily access important features from anywhere on the blog. |
| 17. As a user, I want to be able to filter articles by category so I can find articles more relevant to my interests. | A category filter feature is provided, allowing users to narrow down articles based on their interests, making it easier to find relevant content. |
| 18. As a user, I want articles to be color-coded to enhance site organization and facilitate easier navigation of content. | Articles are color-coded based on their category, helping users to quickly identify content of interest and enhancing the overall organization of the site. |
| 19. As a user, I want the site to be responsive and easy to use on smaller devices and screen sizes. | The website is designed with a responsive layout, ensuring a seamless user experience across various devices and screen sizes, from desktops to smartphones. |
| 20. As a user, I want to see the articles I have written in one place so I can keep track of them. | A dedicated section in the user's profile compiles all the articles they have written, allowing for easy access and management of their content. |
| 21. As a user, I want a pagination feature that allows me to click through groups of articles on a page, ensuring a more streamlined user experience. | The site includes a pagination system, breaking down articles into smaller groups per page to facilitate easier browsing and enhance user experience. |
| 22. As a user, I want an about page that clearly explains the site's purpose and conveys the brand's tone, enabling me to decide if it aligns with my interests. | An 'About' page is available, detailing the site's mission, values, and the community it serves, helping users understand the site's purpose and decide if it aligns with their interests. |

---

<br/>

#### Feature Testing

<br/>

`Navigation Bar (Desktop)`
<img src="./readme-images/features/navbar-desktop.png" alt="navigation bar on desktop">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------- | ------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------ | --------- |
| Navbar | Navbar left menu, logo, and right menu are displayed to the user | Load website | All navbar elements are shown | Pass ✅ |
| Navbar | The navbar reflects the logged-in state appropriately | Log into the site | Navbar updates to show the "My Articles" link, "Create Article" link, Profile and logout buttons | Pass ✅ |
| Navbar Left Menu | Hover animation plays on hover | Hover over each menu link | Hover animation correctly plays | Pass ✅ |
| Navbar Left Menu | Clicking each link takes the user to the correct area of the site | Click each menu link | User is taken to the correct page | Pass ✅ |
| Navbar Logo | Clicking the logo takes the user to the homepage | Click navbar logo | User is correctly taken to the homepage | Pass ✅ |
| Navbar Signup Button | Clicking the signup button takes the user to the signup page | Click signup button | User is correctly taken to the signup page | Pass ✅ |
| Navbar Login Button | Clicking the login button takes the user to the login page | Click login button | User is correctly taken to the login page | Pass ✅ |
| My Articles Link | Logging into the site shows a "My Articles" link to the user on the left navbar menu | Log into site | Link is correctly shown | Pass ✅ |
| My Articles Link | Clicking on the "My Articles" link takes the user to their articles page | Click link | User is correctly taken to their articles page | Pass ✅ |
| Create Article Button | Clicking on the "Create Article" link takes the user to the create article page | Click link | User is correctly taken to their create article page | Pass ✅ |
| Profile Button | Clicking on the "My Profile" link takes the user to the profile page | Click link | User is correctly taken to their profile page | Pass ✅ |
| Profile Button | User's profile image is shown | Upload profile picture | User's profile picture is correctly shown on the profile button | Pass ✅ |
| Navbar Logout Button | Clicking the logout button successfully logs the user out of the website | Click button | User is successfully logged out of the website | Pass ✅ |
| Navbar Logout Button | User is notified of a successful logout via a popup notification | Logout from site | Notification is correctly shown to the user after logging out | Pass ✅ |

<br />

`Navigation Bar (Mobile)`
<img src="./readme-images/features/navbar-dropdown.png" alt="navigation bar on mobile">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------------|---------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------|------------|
| Navbar | On mobile, elements disappear to reveal hamburger icon in the center | Resize viewport to mobile width | Hamburger appears and displays as intended | Pass ✅ |
| Navbar Hamburger Icon | When clicked, the dropdown navigation menu slides into view | Click icon | Dropdown menu slides into view as intended | Pass ✅ |
| Dropdown | The dropdown menu reflects the logged-in state appropriately | Log into the site | Navbar updates to show the "My Articles" link, "Create Article" link, Profile, and logout buttons | Pass ✅ |
| Dropdown | When user resizes the viewport to desktop width, the dropdown disappears | Resize viewport to desktop width | Dropdown menu disappears as intended | Pass ✅ |
| Dropdown Logo | Clicking the logo takes the user to the homepage | Click navbar logo | User is correctly taken to the homepage | Pass ✅ |
| Dropdown Menu Site Links | Clicking each link takes the user to the correct area of the site | Click each menu link | User is taken to the correct page | Pass ✅ |
| Dropdown Signup Button | Clicking the signup button takes the user to the signup page | Click signup button | User is correctly taken to the signup page | Pass ✅ |
| Dropdown Login Button | Clicking the login button takes the user to the login page | Click login button | User is correctly taken to the login page | Pass ✅ |
| Dropdown Menu Close Icon | Clicking the icon closes the dropdown menu | Click icon | Dropdown menu is closed | Pass ✅ |

<br />

`Hero Section`
<img src="./readme-images/features/hero-image.png" alt=" hero section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------- | ---------------------------------------------------------------- | ----------------- | ----------------------------- | --------- |
| Hero Section Background | Background image covers and remains centered over all section widths | Window resize | Background image remains centered and covers all widths | Pass ✅ |
| Hero Section Background | Background image is shown | Load website | Background image correctly loads | Pass ✅ |

<br />

`Category Menu`
<img src="./readme-images/features/category-menu.gif" alt="category menu">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------|-----------|
| Category Menu | Menu and all links are displayed to the user | Load website | Category Menu and all menu links are rendered and shown | Pass ✅ |
| Category Menu | Category menu is responsive to various screen widths | Resize viewport to different widths | Category Menu shrinks and expands to accommodate different screen widths | Pass ✅ |
| Category Menu Links | When user hovers over a menu link, the correct category name is shown | Hover over category link | Correct category name is shown | Pass ✅ |
| Category Menu Links | When user hovers over a menu link, the menu color changes to reflect the correct category color | Hover over category link | Category Menu changes to the correct category color | Pass ✅ |
| Category Menu Links (homepage) | On the homepage, when a user clicks a category link, they are directed to the articles list page and the matching articles are filtered and shown to the user | Click category link | User is taken to the articles list page and the articles of the correct category are filtered and shown | Pass ✅ |
| Category Menu Links (articles list page) | On the articles list page, when a user clicks a category link, the matching articles are filtered and shown to the user on the same page | Click category link | Articles of the correct category are filtered and shown to the user on the same page | Pass ✅ |

<br />

`Recent Articles Section`
<img src="./readme-images/features/recent-posts-section.png" alt="recent articles section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-------------------------|------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------|-----------|
| Recent Articles Section | When the user visits the homepage, the four most recent articles are shown to the user | Load website homepage | The four most recent articles are retrieved from the database and shown to the user | Pass ✅ |
| Recent Articles Section | The articles are rendered in a 2 X 2 grid on desktop | View section on desktop | Articles are correctly displayed in a 2 X 2 grid | Pass ✅ |
| Recent Articles Section | The articles are displayed in a single column layout on mobile | View section on mobile | Articles are correctly displayed in a single column layout on mobile | Pass ✅ |

<br />

`CTA Section`
<img src="./readme-images/features/cta-section-signed-out.png" alt="call-to-action section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------------------|----------------------------------------------------------------------------------------|---------------------------------|--------------------------------------------------------------------------|-----------|
| CTA Section | CTA image and text section are displayed next to each other on desktop width | View section on desktop | Image and text box are displayed correctly | Pass ✅ |
| CTA Section | CTA image and text box are displayed in a stacked layout on mobile width | View section on mobile | Image and text box are displayed correctly in a stacked layout | Pass ✅ |
| CTA Image | Image loads correctly | Load page | Image is correctly displayed when page is loaded | Pass ✅ |
| CTA Text Section (not signed in) | User signup text and link is correctly shown to the user | View section when not signed in | Correct text and link is shown to the user | Pass ✅ |
| CTA Text Section (not signed in) | Sign in button takes user to the sign in page when clicked | Click sign in button | User is correctly taken to the sign in page | Pass ✅ |
| CTA Text Section (signed in) | User is shown correct heading and create article link | View section when signed in | Content or actions relevant to the signed-in state are correctly displayed | Pass ✅ |
| CTA Text Section (signed in) | Sign in button takes user to the create article page when clicked | Click create article button | User is correctly taken to the create article page | Pass ✅ |

<br />

`Social Media Section`
<img src="./readme-images/features/social-media-section.png" alt="social media section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------------|----------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|-----------|
| Social Media Section | All social media icons are correctly loaded and displayed to the user | Load website | All social media icons are displayed | Pass ✅ |
| Social Media Section | Social Media Section is responsive to various screen widths | Resize viewport to different widths | Social Media Section contents shrink and expand to accommodate different screen widths | Pass ✅ |
| Social Media Section Icon Links | Clicking a link takes the user to that corresponding social media platform | Click icon link | User is taken to the correct social media platform for that link | Pass ✅ |

<br />

`Footer Section`
<img src="./readme-images/features/footer-section.png" alt="footer section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------|--------------------------------------------------------------|-------------------|--------------------------------------------|-----------|
| Top Border Image | Image loads correctly | Load website | Border image loads correctly | Pass ✅ |
| Back To Top Link | Link directs user to the top of the page | Click link | User smooth scrolls to the top of the page | Pass ✅ |
| Github Link | Link directs user to the GitHub page | Click link | User is taken to the GitHub page | Pass ✅ |
| Heart Icon | Heart icon is correctly rendered and shown inline with text | Load page | Heart icon is correctly rendered and shown | Pass ✅ |

<br />

`Article Card Component`
<img src="./readme-images/features/article-card.png" alt="post card component">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------|-----------|
| Article Card | Post card component is fully responsive to multiple screen widths | Resize viewport | Post card component is fully responsive and readable on all viewport widths | Pass ✅ |
| Article author buttons | Edit and delete buttons are shown for each comment belonging to the logged-in user | Login to account and submit comment | Only artciles belonging to the user have edit and delete buttons shown at the top right of the corresponding article card | Pass ✅ |
| Article update button | Clicking the update button takes the user to the update article page | Login to account and click update button | User is taken to the article update page | Pass ✅ |
| Article delete button | Clicking the delete button prompts the user before deleting the article | Login to account and click delete button | User is taken to a confirmation page before deleting the comment | Pass ✅ |
| Hero Image | Image for the correct blog post is loaded and shown at the top of the card | Fetch blog article | Correct image is fetched from the database and displayed for the blog post | Pass ✅ |
| Category Color | Correct color is shown on the card for the matching category | Fetch blog article | Color correctly matches the post category | Pass ✅ |
| Profile Image | Profile image of the post author is shown | Fetch blog article | Profile image correctly loads and matches the author | Pass ✅ |
| Title | Correct title for the blog post is shown | Fetch blog article | Post title correctly matches the blog post | Pass ✅ |
| Title | Clicking title takes to its corresponding post detail page | Click blog post title| User is taken to the corresponding blog post detail page | Pass ✅ |
| Author Name | Correct author name for the author is shown | Fetch blog article | Correct author name is shown | Pass ✅ |
| Author Name | Clicking author name takes the user to the corresponding profile page | Click author name | Correct profile page is shown | Pass ✅ |
| Post Date | Correct post date name for article is shown | Fetch blog article | Correct post date is shown | Pass ✅ |
| Excerpt Section | Short descriptive excerpt for the article is shown | Fetch blog article | Matching excerpt for the blog post is shown | Pass ✅ |
| Full Article Link| Clicking link takes to its corresponding post detail page | Click link post | User is taken to the corresponding blog post detail page | Pass ✅ |

`Article Detail Page`
<img src="./readme-images/features/article-detail.png" alt="post detail page">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------|---------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------|-----------|
| Post Detail Page | Page is fully responsive and readable on all screen widths | Resize viewport | Page and blog post content is responsive and readable on all device screen widths | Pass ✅ |
| Post Detail Page | if the user has logged in and is the author of the article then the delete and edit buttons will be shown on the top right of the page| login and gor to corresponding article page | edite and delete buttons are shown to the user | Pass ✅ |
| Article author buttons | Edit and delete buttons are shown for each comment belonging to the logged-in user | Login to account and submit comment | Only comments belonging to the user have edit and delete buttons shown at the top right of the page | Pass ✅ |
| Article update button | Clicking the update button takes the user to the update article page | Login to account and click update button | User is taken to the article update page | Pass ✅ |
| Article delete button | Clicking the delete button prompts the user before deleting the article | Login to account and click delete button | User is taken to a confirmation page before deleting the comment | Pass ✅ |
| Hero Image | Image for the correct blog post is loaded and shown at the top of the page | Fetch blog article | Correct image is fetched from the database and displayed for the blog post | Pass ✅ |
| Category Color | Correct color is shown on the card for the matching category | Fetch blog article | Color correctly matches the post category | Pass ✅ |
| Profile Image | Profile image of the post author is shown | Fetch blog article | Profile image correctly loads and matches the author | Pass ✅ |
| Title | Correct title for the blog post is shown | Fetch blog article | Post title correctly matches the blog post | Pass ✅ |
| Post Date | Correct post date for the article is shown | Fetch blog article | Correct post date is shown | Pass ✅ |
| Author Name | Correct author name for the author is shown | Fetch blog article | Correct author name is shown | Pass ✅ |
| Author Name | Clicking the author name takes the user to the corresponding profile page | Click author name | Correct profile page is shown | Pass ✅ |
| Article Content | Correct content for the article is shown to the user | Fetch blog article | Correct content for the article is shown | Pass ✅ |
| Article Drop Cap | Drop cap letter is rendered for the first letter of the article | Load page | Drop cap is rendered correctly | Pass ✅ |

<br />

`Article Comments Section`
<img src="./readme-images/features/comment-section.png" alt="article comments section">
| Victory Screen | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------------------|----------------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------------|-----------|
| Comment Counter | Correct number of comments on the article are displayed to the user | Fetch article comments | Correct number of comments are shown | Pass ✅ |
| Comment Form (signed out) | A sign-in link is presented to the user if they are signed out | Sign out of account | Sign-in link is shown to the user | Pass ✅ |
| Comment Form (signed in) | A comment form is presented to the user when they sign in | Sign into account | Correct comment form is presented | Pass ✅ |
| Comments Form | When a user submits a comment, it is uploaded to the database and added to the page | Submit comment | Comment is correctly added and shown to the user | Pass ✅ |
| Comments Form | When the user submits a comment, they are directed back to the same article page | Submit comment | User is directed back to the same article page | Pass ✅ |
| Popup Notification | When the user submits a comment, they are notified via a popup notification | Submit comment | User is notified of a successful submission via a popup notification | Pass ✅ |
| Comments List | All comments for the article are rendered in a list and displayed to the user | Fetch article comments | All corresponding article comments are fetched and rendered in a list | Pass ✅ |
| Single Comment | Each comment shows the author's name and also the date and time posted | Fetch article comments | Each comment has the correct author's name and date posted shown to the user | Pass ✅ |
| Comment author buttons | Edit and delete buttons are shown for each comment belonging to the logged-in user | Login to account and submit comment | Only comments belonging to the user have edit and delete buttons shown | Pass ✅ |
| Comment update button | Clicking the update button takes the user to the update comment page | Login to account and submit comment | User is taken to the correct page | Pass ✅ |
| Comment delete button | Clicking the delete button prompts the user before deleting the comment | Login to account and submit comment | User is prompted before deleting the comment and taken to the correct page if necessary | Pass ✅ |

<br />

`Comment Update Form`
<img src="./readme-images/features/update-comment-form.png" alt="comment update section">
| Features | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------------|----------------------------------------------------------------------------------|---------------------------------|---------------------------------------------------------------------------------|-----------|
| Page | Route is protected if user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless they have an account and are logged in | Pass ✅ |
| Comment Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Comment Form | Entered comment is used to update the correct comment in the database | Submit updated comment details | Correct comment is updated and shown to the user | Pass ✅ |
| Comment Form | User is directed back to the corresponding article detail page | Submit updated comment details | User is directed back to the correct article | Pass ✅ |
| Popup Notification | When a comment is successfully updated, the user is notified via a popup notification | Submit updated comment details | User is notified via popup notification on successful comment update | Pass ✅ |

<br />

`Comment Delete Confirmation Page`
<img src="./readme-images/features/delete-comment-confirmation.png" alt="article update section">
| Features | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------------------|----------------------------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------------|-----------|
| Page | Route is protected if user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless logged in as the owner of the comment | Pass ✅ |
| Delete Button | Correct number of comments on the article are displayed to the user | click button | Correct number of comments are shown | Pass ✅ |
| Delete Button | User is directed back to the correspoding article detail page when comment is deleted | click button | Cuser is directed back to the correct article page | Pass ✅ |
| Popup Notification | When comment is successfully deleted the user is notified via a pop notification | click delete comment button | user is notofied via popup notification on success commment update | Pass ✅ |

<br />

<br />

`Create Article Form`
<img src="./readme-images/features/create-article-form.png" alt="create articles section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------|-----------|
| Page | Route is protected if user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless they have an account and are logged in | Pass ✅ |
| Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Form | If the form is invalid, the user will be directed back to the form page and notified of the invalid fields | Submit invalid form | Form prevents article submission and redirects user back to article form page with notifications | Pass ✅ |
| Form | If the form is valid, the user will be directed back to the form page and notified of the invalid fields | Submit invalid form | Form prevents article submission and redirects user back to article form page with notifications | Pass ✅ |
| Title Field | The form remains invalid if the title field is empty | Submit without filling in the title field | User is notified of invalid title field and prevented from submitting | Pass ✅ |
| Post Image Field | If the user does not supply an image then a default placeholder image is used | Submit without selecting an image | Article is assigned a placeholder image | Pass ✅ |
| Post Image Field | If the user does not supply a valid image format, the form remains invalid | Submit an incorrect file format | User is notified of an invalid form | Pass ✅ |
| Category Select | The form remains invalid if no category is selected | Submit without selecting a category | User is notified of invalid category selection and prevented from submitting | Pass ✅ |
| Excerpt Field | The form remains invalid if the excerpt field is empty | Submit without filling in the excerpt field | User is notified of invalid excerpt field and prevented from submitting | Pass ✅ |
| Content Field | The form remains invalid if the content field is empty | Submit without filling in the content field | User is notified of invalid content field and prevented from submitting | Pass ✅ |
| Summernote | The text formatting features of Summernote are correctly applied when text is selected and edited using the interface in the content field | Apply Summernote text formatting features to text in the content field | Text is correctly formatted according to the Summernote formatting buttons | Pass ✅ |
| Form Field Labels | The corresponding field is focused when the user clicks a label for accessibility purposes | Click the label for each form field | The correct corresponding field is focused for the user | Pass ✅ |
| Popup Notification | If the article is invalid, the user is notified of the error via a popup notification | Submit form with invalid data | User is notified via popup notification if the form is invalid | Pass ✅ |
| Popup Notification | When the article is successfully submitted, the user is notified via a popup notification | Submit form with valid data | User is notified via popup notification on successful article submission | Pass ✅ |

<br />

`Update Article Form`
<img src="./readme-images/features/update-article-form.png" alt="create articles section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|----------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------|-----------|
| Page | Route is protected if a user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless logged in as the owner of the article | Pass ✅ |
| Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Form | When the user chooses to update an existing article, each field will be populated with the content of the article | Click the article edit button | Article update page is shown with the form fields already populated with the article content | Pass ✅ |
| Form | If the form is invalid, the user will be directed back to the form page and notified of the invalid fields | Submit invalid form | Form prevents article submission and redirects user back to the article form page with notifications | Pass ✅ |
| Title Field | The form remains invalid if the title field is empty | Submit without filling in the title field | User is notified of invalid title field and prevented from submitting | Pass ✅ |
| Post Image Field | If the user does not supply an image then a default placeholder image is used | Submit without selecting an image | Article is assigned a placeholder image | Pass ✅ |
| Post Image Field | If the user does not supply a valid image format, the form remains invalid | Submit an incorrect file format | User is notified of an invalid form | Pass ✅ |
| Category Select | The form remains invalid if no category is selected | Submit without selecting a category | User is notified of invalid category selection and prevented from submitting | Pass ✅ |
| Excerpt Field | The form remains invalid if the excerpt field is empty | Submit without filling in the excerpt field | User is notified of invalid excerpt field and prevented from submitting | Pass ✅ |
| Content Field | The form remains invalid if the content field is empty | Submit without filling in the content field | User is notified of invalid content field and prevented from submitting | Pass ✅ |
| Summernote | The text formatting features of Summernote are correctly applied when text is selected and edited using the interface in the content field | Apply Summernote text formatting features to text in the content field | Text is correctly formatted according to the Summernote formatting buttons | Pass ✅ |
| Form Field Labels | The corresponding field is focused when the user clicks a label for accessibility purposes | Click the label for each form field | The correct corresponding field is focused for the user | Pass ✅ |
| Popup Notification | If the article is invalid, the user is notified of the error via a popup notification | Submit form with invalid data | User is notified via popup notification if the form is invalid | Pass ✅ |
| Popup Notification | When the article is successfully updated, the user is notified via a popup notification | Submit form with valid data | User is notified via popup notification on successful article submission | Pass ✅ |

<br />

`Delete Article Confirmation Page`
<img src="./readme-images/features/article-delete-confirmation.png" alt="article delete section">
| Features | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------|---------------------------------------------------------------------------------------|--------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Page | Route is protected if user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless logged in as the owner of the article | Pass ✅ |
| Title | Correct article title is shown to the user | Click button to load article | Correct title of the article is shown | Pass ✅ |
| Delete Button | Article is removed from the database when delete button is clicked | Click delete button on article | Article is successfully deleted from the database | Pass ✅ |
| Delete Button | User is directed back to the homepage when the article is deleted | Click delete button on article | User is directed back to the homepage after deletion | Pass ✅ |
| Popup Notification | When the article is successfully deleted, the user is notified via a popup notification | Click delete button on article | User is notified via popup notification on successful article deletion | Pass ✅ |

<br />

`User Articles Section`
<img src="./readme-images/features/users-articles-section-empty.png" alt="user articles section when empty">
<img src="./readme-images/features/user-article-section-filled.png" alt="user articles section when filled">
| Victory Screen | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------------------------|------------------------------------------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------|-----------|
| Page | Route is protected if user tries to access it while not logged in | Enter URL in browser address bar while not signed in | User cannot access route unless they have an account and are logged in | Pass ✅ |
| User article page | Page is fully responsive and readable on all screen widths | Resize viewport | Page content is responsive and readable on all device screen widths | Pass ✅ |
| Title | The user's name is correctly shown in the title of the page | Sign in and load page | Correct author name is shown | Pass ✅ |
| User article page (no user articles) | Message and write post button are shown to the user | Sign in and load page with no articles | Message and button are shown | Pass ✅ |
| Write post button (no user articles) | Clicking button takes users to the create article page | Click button | Users are taken to the create articles page | Pass ✅ |
| User article page (with user articles) | All articles belonging to the user are fetched and displayed to the user | Sign in, write one or more articles, and load page | Articles are retrieved and shown to the user in a grid layout | Pass ✅ |

</br>

`Articles List Section`
<img src="./readme-images/features/articles-list-section.png" alt="articles list section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------|--------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-----------|
| Category Menu | Category menu is shown when the page loads | Load page | Category menu is shown | Pass ✅ |
| Category Menu | Clicking the chosen category renders only articles within that category | Click category link | Articles of the correct category are shown | Pass ✅ |
| Articles List | All articles, starting with the most recently posted, are fetched and shown to the user on initial page load | Load page | All articles are shown to the user in order of most recent | Pass ✅ |
| Articles List | All articles are rendered on a responsive grid layout that adapts to all screen widths | Resize viewport | Layout responsively adapts to multiple viewport widths | Pass ✅ |

</br>

`Pagination`
<img src="./readme-images/features/pagination.png" alt="pagination">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------|-------------------------------------------------------------------------------|------------------------------------|------------------------------------------------------------------------------------|-----------|
| Pagination | Maximum of six articles are rendered at any one time | Load articles list page | A max of 6 articles are shown to the user | Pass ✅ |
| Page Counter | When clicked, the page number accurately reflects which pagination cycle the user is on | Click the next and prev buttons to change the number | The number updates to correctly reflect which page cycle the user is on | Pass ✅ |
| Next Button | Clicking the next button advances to the next set of articles | Click the next button | The next set of articles are shown to the viewer | Pass ✅ |
| Next Button | On the last pagination cycle, the next button is not shown | Navigate to the last pagination cycle | The next button is not shown to the user | Pass ✅ |
| Prev Button | Clicking the prev button moves back to the previous set of articles | Click the prev button | The previous set of articles are shown to the viewer | Pass ✅ |
| Prev Button | On the first pagination cycle, the prev button is not shown | Navigate to the first pagination cycle | The prev button is not shown to the user | Pass ✅ |

</br>

`Profile Section`
<img src="./readme-images/features/profile-section.png" alt="profile section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-------------------|-----------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------|-----------|
| Profile Page | Profile page is fully responsive on smaller screen widths | Resize viewport | Layout is responsive and adapts to smaller screen widths | Pass ✅ |
| Update Profile Button Page | User is taken to the Update Profile Page | Click button | User is successfully taken to the Update Profile Page | Pass ✅ |
| Default Profile Image | Default placeholder image is shown to the user if they do not yet have a profile image | Load profile page without uploading a profile image | Default profile image is shown to the user | Pass ✅ |
| Profile Image | User's uploaded profile image is shown to the user when they upload a profile image | Load profile page | Profile image is shown to the user | Pass ✅ |
| Username Title | User's account username is shown on the profile page when they log in | Log in to user's account | Correct username is shown to the user | Pass ✅ |
| Profession Info | User's profession is shown to the user when they update their profile | Enter profession | User's profession is correctly shown | Pass ✅ |
| Country Info | User's country is shown to the user when they update their profile | Enter country | User's country is correctly shown | Pass ✅ |
| City Info | User's city is shown to the user when they update their profile | Enter city | User's city is correctly shown | Pass ✅ |
| Firstname Info | User's first name is shown to the user when they update their profile | Enter first name | User's first name is correctly shown | Pass ✅ |
| Lastname Info | User's last name is shown to the user when they update their profile | Enter last name | User's last name is correctly shown | Pass ✅ |
| Date of Birth Info| User's date of birth is shown to the user when they update their profile | Enter date of birth | User's date of birth is correctly shown | Pass ✅ |
| Bio Info | User's bio is shown to the user when they update their profile | Enter bio | User's bio is correctly shown | Pass ✅ |
| Website URL | User's website URL is shown to the user when they update their profile | Enter website URL | User's website URL is correctly shown | Pass ✅ |
| Github URL | User's GitHub URL is shown to the user when they update their profile | Enter GitHub URL | User's GitHub URL is correctly shown | Pass ✅ |
| LinkedIn URL | User's LinkedIn URL is shown to the user when they update their profile | Enter LinkedIn URL | User's LinkedIn URL is correctly shown | Pass ✅ |
| Medium URL | User's Medium URL is shown to the user when they update their profile | Enter Medium URL | User's Medium URL is correctly shown | Pass ✅ |
| Popup Notification | When the users profile is successfully updates, the user is notified via a popup notification | Click submit button on update profile page | User is notified via popup notification on successful profile update | Pass ✅ |

</br>

`Update Profile Section`
<img src="./readme-images/features/update-profile-form.png" alt="update profile form">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------------------|-------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------------------------------|-----------|
| Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Form Field Labels | The corresponding field is focused when the user clicks a label for accessibility purposes | Click the label for each form field | The correct corresponding field is focused for the user | Pass ✅ |
| Profile Picture Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Bio Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Date of Birth | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Date of Birth Validation | User cannot enter a date for a date in the future | Enter date value after current date | Form is invalid and user is notified of the error with correct message | Pass ✅ |
| Country Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| City Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Profession Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Social Media URL Validation | If user inputs an incorrect URL, the form is invalid | Enter social media link URL | Field is invalid if a valid URL is not entered | Pass ✅ |
| Website URL Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Github URL Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| LinkedIn URL Field | Allow blank field on submission | Submit form with blank field | Form allows submission with blank field | Pass ✅ |
| Medium URL Field | Allow blank field on submission (listed twice, may need removal of duplicate) | Submit form with blank field | Form allows submission with blank field | Pass ✅ |

</br>

`About Section`
<img src="./readme-images/features/about-section.png" alt="about section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------|---------------------------------------------------------------------------|-------------------|-------------------------------------------------------------|-----------|
| About Page | The page layout and typography are responsive and readable on multiple screen widths | Resize viewport | The page is responsive for multiple screen sizes | Pass ✅ |
| About Image | The about image is correctly shown to the user when the page loads | Load about page | The about image is correctly shown | Pass ✅ |
| Text Keywords | Each keyword in the text is rendered with its correct color | Load about page | Each keyword is correctly highlighted in the correct color | Pass ✅ |

</br>

`Signup Section`
<img src="./readme-images/features/signup-form.png" alt="signup section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------------|-------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------|-----------|
| Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Form Field Labels | The corresponding field is focused when the user clicks a label for accessibility purposes | Click the label for each form field | The correct corresponding field is focused for the user | Pass ✅ |
| Username Field | The form is invalid if the username field is blank | Submit form with blank username field | Form is invalid and user is notified of the missing field | Pass ✅ |
| Firstname Field | The form is invalid if the firstname field is blank | Submit form with blank firstname field | Form is invalid and user is notified of the missing field | Pass ✅ |
| Lastname Field | The form is invalid if the lastname field is blank | Submit form with blank lastname field | Form is invalid and user is notified of the missing field | Pass ✅ |
| Email Field | User is allowed to leave the email field blank as it is optional | Submit form with blank email field | Form is successfully submitted | Pass ✅ |
| Email Field Validation | The form is invalid if the user does not provide a correct email address | Submit form with invalid email address | Form is invalid and correctly notifies user of the error | Pass ✅ |
| Password Field | The form is invalid if the user does not provide a password | Submit form with empty password | Form is invalid and correctly notifies user of the error | Pass ✅ |
| Password Validation | The form is invalid if the user tries to use a password that is too common | Submit form with common password | Form is invalid and correctly notifies user of the error | Pass ✅ |
| Password Confirmation | The form is invalid if the user enters the password incorrectly a second time | Enter password incorrectly in the confirmation field | Form is invalid and correctly notifies user of the error | Pass ✅ |
| Login Link | The user is taken to the signup page when they click the link | Click link | User is correctly taken to the signup page | Pass ✅ |
| Popup Notification | When the user signs up for an account, they are notified via a popup notification | Sign up for an account | User is notified of a successful signup via a popup notification | Pass ✅ |

</br>

`Login Section`
<img src="./readme-images/features/login-form.png" alt="login section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------|-----------|
| Form | Form is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Form Field Labels | The corresponding field is focused when the user clicks a label for accessibility purposes | Click the label for each form field | The correct corresponding field is focused for the user | Pass ✅ |
| Username Field | The form is invalid and the user cannot login if the username field does not match the user's account credentials | Submit form with incorrect username field | Form is invalid and user is notified that the username is incorrect | Pass ✅ |
| Password Field | The form is invalid and the user cannot login if the password field does not match the user's account credentials | Submit form with incorrect password | Form is invalid and correctly notifies that the password is incorrect | Pass ✅ |
| Signup Link | The user is taken to the signup page when they click the link | Click link | User is correctly taken to the signup page | Pass ✅ |
| Popup Notification | When the user logs into the site, they are notified via a popup notification | Login to site | User is notified of a successful login via a popup notification | Pass ✅ |

</br>

`404 Page`
<img src="./readme-images/features/404-section.png" alt="404 page">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------------|-------------------------------------------------------------------------|------------------------|------------------------------------------------|-----------|
| 404 Page | 404 page is displayed if the user enters an incorrect URL | Enter incorrect URL | 404 page is correctly shown | Pass ✅ |
| Hero Image | Hero image is displayed in the center of the 404 page | Load 404 page | Hero image is correctly displayed | Pass ✅ |
| Homepage Link | Clicking the homepage link takes the user back to the homepage | Click homepage link | User is successfully taken back to the homepage | Pass ✅ |

</br>

## Bugs

#### 1. **Invalid Allowed Host (Solved)**

<img src="./readme-images/testing/bugs/1.invalid-allowed-host.png" alt="code solution for invalid allowed host" >

<br/>

Initially, when deploying my application to Heroku, I was immediately shown a 400 Bad Request response. After using Chrome Developer Tools to inspect the HTTP message and researching the error, I found that Django was rejecting the request because I had not added the correct domain to the ALLOWED_HOSTS field in my settings file. Adding the correct domain helped fix the issue. I learned that this is a security measure implemented by Django to prevent HTTP Host header attacks, where an attacker might send requests with a malicious host header to manipulate the site.

<br />

#### 2. **HTTP 500 Status Error On Deployment (Solved)**

<img src="./readme-images/testing/bugs/2.http-500-status-error.png" alt="code solution for http 500 error on deployment" >

<br/>

During the deployment process, I encountered a 500 Error which prompted further investigation. Upon reviewing the debugging output provided by Django while running my development server, I discovered that my application had been deployed with the DEBUG setting enabled in the configuration file. This particular setting, when active, prevents Django from serving static and media files directly. Without proper configuration for these files to be served by an external web server or cloud service, the site's functionality can be compromised. This oversight was likely contributing to the 500 errors, especially on pages that depended on the availability of these static and media resources.

I resolved this issue by creating an environment variable and configuring it to True for my production environment, while setting it to False for my Heroku deployment. I then implemented a conditional statement within the settings file, which dynamically adjusts this value based on the target environment. This ensures the variable is accurately set for the specific environment in use.

<br />

#### 3. **Static Files Not Loading: (Solved)**

<img src="./readme-images/testing/bugs/3.static-files-not-loading.png" alt="code solution for http 500 error on deployment" >

<br />

After a thorough debugging session, I successfully resolved the issue with serving static files in my Django project. The root cause was a misconfiguration of the `STATICFILES_DIRS` in my settings.py file. Specifically, my project structure includes a static folder at the root, which Django was previously unaware of. To rectify this, I added the static directory to `STATICFILES_DIRS` in my settings.py. This adjustment informed Django of the additional location to search for static files beyond the standard app-specific static folders. This change effectively solved the problem, highlighting the importance of accurate settings configuration in Django projects.

<br />

#### 4. **Cross-Site Request Forgery (CSRF) Error: (Solved)**

<img src="./readme-images/testing/bugs/4.csrf-error.png" alt="code solution for http 500 error on deployment" >

<br />

Encountered a CSRF verification failure error while trying to submit a form, which led to an unsuccessful post request. This was a critical security feature preventing cross-site request forgery attacks, but it also hindered the intended functionality of our forms.

The solution involved ensuring each form contained the necessary {% csrf_token %} template tag within the form in our Django templates. This tag generates a CSRF token that gets verified with the user's session on submission. Implementing this resolved the submission issue, allowing forms to be submitted securely and successfully.

<br />

#### 5. **Incorrect Date Of Birth Submission: (Solved)**

<img src="./readme-images/testing/bugs/5.incorrect-dob-submission.png" alt="code solution for incorrect date of birth submission" >

<br />

During testing of my application, I spotted an error in the profile update form that I had initially overlooked. I noticed that users were able to set their date of birth to a future date, which should not be possible. To rectify this issue, I added a `clean` method to the Blog model to include a validation that utilizes the timezone utility from Django to check if the value of the date of birth is greater than the current date and time provided by `timezone.now()`. If this condition is met, a validation error will be correctly raised and displayed to the user as an error message.

<br />

#### 6. **Non Responsive Summernote Widget: (Solved)**

<img src="./readme-images/testing/bugs/6.non-responsive-summernote-widget.png" alt="code solution for non responsive summernote widget" >

<br />

When initially integrating the Summernote widget into my Post form, I noticed the resulting WYSIWYG field for the post content was not responsive on smaller screens. To address this, I needed to override the generated article form to customize the widget, allowing me to apply custom styling. This customization ensured the width of the field was responsive and not fixed. I achieved this by adding a percentage width attribute to the Form through the widget property on the PostForm class.

<br/>

#### 7. **Missing Profile Form Fields: (Solved)**

<img src="./readme-images/testing/bugs/7.missing-profile-form-fields.png" alt="code solution for missing profile form fields" >

<br />

Upon reviewing the profile form, I observed that two fields within the social media section were not visible upon form rendering, despite the ProfileForm class inheriting from forms.ModelForm. Initially, I speculated that these fields might have been omitted during database migrations. However, this hypothesis was incorrect. Further investigation revealed that these two fields were not properly included in the 'fields' property of the form. Once I added them it resolved the issue.

<br />

#### 8. **Missing Default Placeholder Profile Image: (Solved)**

<img src="./readme-images/testing/bugs/8.missing-default-placeholder-image.png" alt="code solution for missing default placeholder image" >

<br />

I aimed to integrate a default placeholder image for user profiles upon account creation, which would remain until the user uploads a personalized image. Initially, my strategy involved fetching a default image from Cloudinary for this purpose. However, this approach consistently resulted in broken image links during implementation. To address this, I devised an alternative solution by introducing a custom method within my Post model. This method retrieves a default image from the static folder in the absence of a set profile image. Ultimately, this approach proved to be more efficient as it reduced the number of requests made to the Cloudinary API.

[Back to Top ^](#Commit---testing-documentation)

<h1 align="center">Commit 👨‍💻</h1>

<img src="readme-images/readme-banner.png" alt="a colorful abstract geometric design">

<h3 align="center"><a href="https://commit-blog-81c3ab6546fa.herokuapp.com/">➡️ View the live project here ⬅️</a></h3>

<br/>

<div align="center">

![GitHub language count](https://img.shields.io/github/languages/count/ShaneDoyleDev/Commit)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/ShaneDoyleDev/Commit)
![GitHub repo size](https://img.shields.io/github/repo-size/ShaneDoyleDev/Commit)

</div>

## Introduction

Commit is a contemporary, full-stack blog platform powered by Django that I created to empower myself and other technology enthusiasts to express our thoughts and discoveries in the realm of modern web and software development. I envisioned this blog as a nurturing environment for the tech community, striving to build bridges and foster engagement among individuals of diverse backgrounds within the industry. The goal of this blog is to create a dynamic platform for people in the tech industry to connect with each other and exchange ideas covering the latest in web technologies, development practices, and industry insights.

When users sign up and create an account, they can fill out their profile to share their information with others in the tech community and showcase their skills and knowledge. They are also encouraged to write their own articles on any tech topic they wish to contribute to the community and help others, as well as comment on individual posts by other authors to share their thoughts and appreciation. Users can also sort through articles by category to find areas of tech they are more interested in, making for a richer user experience.

<h3 align="center"><img src="./readme-images/website-preview.webp" alt="a preview of the website shown on a range of different devices"></h3>

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Components](#components)
  - [Wireframe](#figma-wireframe)
  - [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Agile Workflow](#agile-workflow)
  - [Epics And User Stories](#epics-user-stories-and-tasks)
  - [Github Project Boards](#github-project-boards)
  - [MoSCoW Prioritization](#moscow-prioritization)
  - [Story Points](#story-points-and-t-shirt-sizing)
  - [Project Milestones](#project-milestones)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Implementations](#future-implementations)
- [Technologies](#technologies)
  - [Programming Languages](#programming-languages)
  - [Applications and Libraries](#applications-and-libraries)
- [Local Development & Deployment](#deployment--local-development)
  - [Local Development](#local-development)
  - [Heroku Deployment](#heroku-deployment)
  - [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Credits](#credits)
  - [Code Used And Tutorials](#code-used-and-tutorials)
  - [Acknowledgments](#acknowledgments)

## User Experience (UX)

Commit was designed as a blog with the tech community at heart, specifically targeting developers and tech enthusiasts in the web and software development industry. It caters to individuals who are keen on staying abreast of the latest trends in technology, sharing best practices, and engaging in thoughtful discussions on the future of software development.

Users can range in skill level from seasoned developers with years of experience to eager newcomers in the industry who are willing to dive into the world of tech. The blog was designed first and forwmorst to be a welcoming platform to encourage useres of these broad skill levels to learn, share, and connect. It's for those who not only seek to expand their own knowledge but also contribute to the growth of others by sharing their own insights, experiences, and expertise.

### User stories

#### Site Owner Goals

1. As the **site owner**, I want to have an admin account that allows me to log in and out of the admin panel securely to access the site's administrative features.

2. As the **site owner**, I want to be able to remove posts from the blog if they are not relevant to the content of the site or feature potentially malicious content.

3. As the **site owner**, I want to be able to remove comments from the blog if they are not relevant to the content of the site or feature potentially malicious content.

4. As the **site owner**, I want to be able to remove user accounts from the blog if they post content that is potentially offensive or not suitable for the blog.

5. As the **site owner**, in addition to myself, I want only the account owners of the posts and profile information to be able to update and delete them.

6. As the **site owner**, I want to have a CTA section encouraging users to sign up for an account so they can contribute to the blog and grow the community.

7. As the **site owner**, I want the website design to have a modern look and be aesthetically pleasing and professional to make a good impression on visitors.

8. As the **site owner**, I want to have a footer showing copyright information and linking to my GitHub for exposure.

</br>

#### User Goals

1. As a **user**, I want to be able to easily sign up with a unique **user**name and password to create an account.

2. As a **user**, I want to be able to easily sign out of the site to keep my account secure.

3. As a **user**, I want to be able to easily log in to the site with my username and password to view my account.

4. As a **user**, I want to receive notifications as feedback confirmation for important actions I perform on the site, including signup, signin, signout, and any submissions, updates, or deletions of content.

5. As a **user**, I want to have a profile section so other readers can get to know about me and connect.

6. As a **user**, I want to be able to upload my own profile picture to better showcase myself and make my profile more personal.

7. As a **user**, I want to be able to write a short bio about myself to give others an idea of who I am.

8. As a **user**, I want to be able to share links to my social media profiles to connect with others in the tech industry.

9. As a **user**, I want to be able to update my profile section to keep it up to date.

10. As a **user**, I want to be able to write and post my own articles to share my thoughts and knowledge with the tech community.

11. As a **user**, I want to be able to edit my own articles to correct or add to them if I have accidentally made a mistake.

12. As a **user**, I want to be able to delete my own articles if I decide I no longer want others to see them.

13. As a **user**, I want to be able to comment and show my appreciation on posts I have read.

14. As a **user**, I want to be able to edit my comments if I have made a mistake or want to add something else.

15. As a **user**, I want to be able to delete my comments if I no longer want others to read them.

16. As a **user**, I want to be able to easily navigate throughout the blog and reach the most important features from anywhere on the site.

17. As a **user**, I want to be able to filter articles by category so I can find articles more relevant to my interests.

18. As a **user**, I want articles to be color-coded to enhance site organization and facilitate easier navigation of content.

19. As a **user**, I want the site to be responsive and easy to use on smaller devices and screen sizes.

20. As a **user**, I want to see the articles I have written in one place so I can keep track of them.

21. As a **user**, I want a pagination feature that allows me to click through groups of articles on a page, ensuring a more streamlined user experience.

22. As a **user**, I want an about page that clearly explains the site's purpose and conveys the brand's tone, enabling me to decide if it aligns with my interests.

</br>

## Design

- #### Colour Scheme

  ### <img src="./readme-images/design/colors.png" alt="color palette for the website">

The blog features a clean and spacious design, utilizing a white background with subtle off-black accents for text and UI elements. This simplicity is balanced with vibrant colors in the images, adding visual interest. For easy navigation, article categories are distinguished by unique colors, enhancing the user experience with a professional touch.

- #### Typography

  ### <img src="./readme-images/design//typography.png" alt="typography list for the website">

Playfair Display was selected as the primary font for the website, chosen for its elegant serif style that complements a modern, clean design. To create a contrast, Inter, a clean sans-serif font, was employed for button text, form validation messages, and popup notifications, ensuring what I feel is a nice blend of classical and contemporary aesthetics.

- #### Components

  ### <img src="./readme-images/design/components.png" alt="ui component list for the website">

I embraced a component-centric approach in my UI design, focusing on crafting reusable UI components that can be applied in various contexts. This strategy ensures a uniform and cohesive appearance throughout the user interface, significantly enhancing the user experience on my site.

- #### Figma Wireframe

### <img src="./readme-images/design/figma-wireframe.png" alt="figma ui wireframe">

Knowing that I aimed to personalize the appearance of the base template, I turned to Figma to craft a visual mockup. Upon completion, this would allow me to transition more efficently into coding the CSS.

- Desktop Wireframe - [View](https://www.figma.com/file/M4f9nxGB5wfdTWwcuhe4qr/Commit?type=design&node-id=75-443&mode=design&t=5DclE4hP0mEYeBHX-0)

- Tablet Wireframe - [View](https://www.figma.com/file/M4f9nxGB5wfdTWwcuhe4qr/Commit?type=design&node-id=72-4&mode=design&t=5DclE4hP0mEYeBHX-0)

- Mobile Wireframe - [View](https://www.figma.com/file/M4f9nxGB5wfdTWwcuhe4qr/Commit?type=design&node-id=75-444&mode=design&t=5DclE4hP0mEYeBHX-0)

- Design System - [View](https://www.figma.com/file/M4f9nxGB5wfdTWwcuhe4qr/Commit?type=design&node-id=57-2&mode=design&t=5DclE4hP0mEYeBHX-0)

- #### Entity-Relationship Diagram

### <img src="./readme-images/design/erd-diagram.png" alt="the entity-relationship diagram">

Leveraging DrawSQL, I crafted an Entity-Relationship Diagram (ERD) for my PostgreSQL database. This approach proved invaluable, enabling me to visually map out the schema of each entity. It offered a clear, coherent view of how each of the tables interconnected within the database, significantly enhancing my understanding and management of the data structure.

</br>

## Agile Workflow

### Epics, User Stories and Tasks

#### Epics

### <img src="./readme-images/agile/epics.png" alt="list of project epics on Github">

Using Agile methods, I started my blog project by setting clear goals and deciding what features it would have. I identified the main themes, or "epics," which were broad outlines of what I wanted to achieve. These epics were like the big-picture goals of my project, guiding me towards what I wanted to build.

#### User Stories

### <img src="./readme-images/agile/github-project-user-stories.png" alt="list of project user stories on Github">

After defining all project epics, I broke them down into user stories. These stories were more detailed and focused on the needs and problems of my potential users. They helped me stay on track with my project goals, making sure I was building something people would actually find useful. For each story, I created a GitHub issue, describing the feature from a user's perspective and listing what criteria it needed to meet to be considered done.

#### Tasks

### <img src="./readme-images/agile/tasks.png" alt="list of tasks on a user story card">

I then listed all the individual tasks needed to complete each user story, breaking down the work into small, manageable parts. I used a checklist to keep track of what had been done and what still needed attention. This helped me stay organized and focused on the small details, ensuring that I met all the criteria for my user stories throughout the project.

### Github Project Boards

#### Github Project - User Stores List

### <img src="./readme-images/agile/github-project-user-stories.png" alt="user stories project board">

With the aid of GitHub projects, I grouped and organized all my user stories together in a project list view. This enabled me to visually grasp the most crucial aspects of each user story, and visualizing the interconnectedness between user stories and their respective Epics provided invaluable insights into the project's overarching goals and objectives.

You can see the project board here - <a href="https://github.com/users/ShaneDoyleDev/projects/7/views/2">User stories list</a>

#### Github Project - Kanban Board

### <img src="./readme-images/agile/github-project-kanban-board.png" alt="user stories kanban board">

I also implemented a Kanban board as an effective information radiator throughout each project milestone. This strategic approach enabled me to monitor the progress of tasks—from the initial backlog to current work-in-progress, all the way to completion. By visually mapping out each step of the process, the Kanban board provided a clear, real-time overview of the project's status, ensuring seamless tracking and management of tasks at every stage.

You can see the project board here - <a href="https://github.com/users/ShaneDoyleDev/projects/7/views/1">Kanban board</a>

### MoSCoW Prioritization

### <img src="./readme-images/agile/moscow.png" alt="list of moscow labels on a Gihub project board">

I used MoSCoW prioritization technique to label each user story and prioritize tasks according to their significance to the project's objectives. This strategic approach enabled me to identify and focus on the most critical tasks first, ensuring the project remained on schedule. By optimizing my time management in this manner, I could concentrate on delivering the essential features required for the Minimum Viable Product (MVP) and other key deliverables, effectively steering the project towards its successful completion while aligning with the project's overarching goals.

- **Must have**: These are non-negotiable requirements that the project needs to be successful and meet the requirement scope of the Minimum Viable Product (MVP).
- **Should have**: Important but not vital requirements, which could be included if time and resources permit.
- **Could have**: Desirable but not necessary requirements. These are features that could be added as additional features and enhancements for the app in the future.

### Story Points and T-Shirt Sizing

### <img src="./readme-images/agile/t-shirt-sizing.png" alt="list of moscow t-shirt sizing values on a Gihub project board">

### <img src="./readme-images/agile/t-shirt-sizing-card.png" alt="list of moscow t-shirt sizing values on a Gihub project board">

T-shirt sizing is a popular method used in Agile to measure story points. This was what I employed as my chosen method to evaluate the effort required for completing each user story. User stories were compared against a benchmark task, with size categories — ranging from XS to XXL — assigned to represent the relative complexity and effort needed.

I learned about this agile estimation technique from these learning resources:

- <a href="https://activecollab.com/blog/project-management/t-shirt-sizing">T-Shirt Sizing - Agile Estimation Guide</a>
- <a href="https://asana.com/resources/t-shirt-sizing">How to Use T-Shirt Sizing to Estimate Projects</a>

### Project Milestones

The project timeline was strategically segmented into three key milestones, each representing a distinct sprint or unit of work: the **MVP (Minimum Viable Product) milestone**, the **Post-MVP milestone**, and the **Enhancements milestone**. This structure played a crucial role in the planning and development phases, enabling me to prioritize the development of the most critical features first.

By adopting this approach, I effectively minimized the risk of allocating time to features that were not essential to the app's core functionality, ensuring a more focused and efficient progression towards the project goals.

#### MVP Milestone

This milestone encompasses all essential functionalities that are critical to the project's initial release. It includes fundamental features that the product must have in order to operate effectively and meet the minimum viable product (MVP) criteria. These tasks must be completed for the product to go live.

You can see this project milestone here - <a href="https://github.com/ShaneDoyleDev/commit/milestone/1">MVP Milestone</a>

#### Post-MVP Milestone

The post-launch milestone is aimed at enhancing the user experience and adding important features that were not critical for the initial launch. While these features are important to the product's overall value, they are not necessary for the core functioning of the platform. Implementing these tasks will further refine the user experience, add additional utility, and likely increase user satisfaction and engagement.

You can see this project milestone here - <a href="https://github.com/ShaneDoyleDev/commit/milestone/2">Post-MVP Milestone</a>

#### Enhancement Milestone

This milestone is focused on further enriching the platform with desirable features that could improve user interaction, personalization, and visual appeal. These are considered nice-to-have features that are not essential to the platform's primary functions but can contribute to the competitive edge, user retention, and overall marketability of the product. These tasks are scheduled for implementation once the more critical launch and post-launch features have been successfully completed.

You can see this project milestone here - <a href="https://github.com/ShaneDoyleDev/commit/milestone/3">Enhancement Milestone</a>

</br>

## Features

### Existing Features

<h3 align="center">Navigation Bar</h3>

### <img src="./readme-images/features/navbar-desktop.png" alt="navbar on desktop screen width">

- The navigation bar is prominently placed at the top of every page on the site so that users can easily navigate to any section from wherever they are.

### <img src="./readme-images/features/navbar-signed-in.png" alt="navbar on desktop screen width">

- The content of the navbar changes when the user is logged in to provide access to user specific features.

### <img src="./readme-images/features/navbar-mobile.png" alt="navbar on smaller screen width">

- The navigation bar is fully responsive; on smaller screen widths, the navbar menu collapses into a single hamburger icon. This approach prevents the links from becoming too crowded together.

### <img src="./readme-images/features/navbar-dropdown.png" alt="navbar dropdown menu">

- Clicking the hamburger icon for the mobile version of the navbar reveals a dropdown menu featuring the navbar menu links. This provides a more suitable layout for the menu items, allowing users to easily click on each link to be directed to the corresponding section of the page.

<br />

---

<br />

<h3 align="center">Hero Section</h3>

### <div align="center"><img src="./readme-images/features/hero-image.png"  alt="website hero image"></div>

- The Hero Section of a website occupies the full width of the screen and is located at the top of the page, above the fold (i.e., the portion of the webpage visible without scrolling). Given its prime location, I wanted it to capture the visitor's attention and prompt them to engage further with the content or offerings of the website.

- I also ensured to position the imagery in a way that would look good across a range of different devices, from desktops to mobile.

<br />

---

<br />

<h3 align="center">Category Menu</h3>

### <img src="./readme-images/features/category-menu.gif" alt="category menu">

- The category menu is a custom-designed menu that I created to enable users to select and filter blog posts using five categories: front-end, backend, UI/UX design, DevOps, and thoughts and perspectives.

- When the user hovers over a category, a tooltip appears, showing the category name, and the color of the menu also changes to reflect the selected category.

- Upon clicking the chosen category, the articles are filtered according to the category and presented to the user, allowing them to view posts that are more relevant to their interests.

- The category menu is located on both the homepage below the hero image and at the top of the articles page. Clicking the menu links on the homepage will direct the user to the articles page.

<br />

---

<br />

<h3 align="center">Recent Posts Section</h3>

### <img src="./readme-images/features/recent-posts-section.png" alt="recent posts section">

- This section aids visitors in finding the latest content without searching through the entire blog, enhancing overall user experience and navigation. Four recent posts are showcased for selection.

- Positioned below the homepage's Hero image, this section is one of the first elements visitors see, highlighting the blog's active updates and fresh content. Its intentional placement encourages reader engagement and suggests a continuous stream of new content to explore.

<br />

---

<br />

<h3 align="center">Call To Action Section</h3>

### <img src="./readme-images/features/cta-section-signed-out.png" alt="call to action section when user is not signed in">

- The Call-To-Action (CTA) Section features compelling imagery alongside a message aimed at enticing users to sign up for an account. On desktops, the image and CTA are side by side; on smaller screens, they shift to a column layout for better usability.

### <img src="./readme-images/features/cta-section-signed-in.png" alt="call to action section when user is logged in">

- This section adapts based on the user's login status. If not logged in, it displays a sign-up link; if logged in, it offers a direct link to create a new article.

### <img src="./readme-images/features/cta-section-mobile.png" alt="mobile layout for call to action section">

-This section is fully responsive and changes orientation for a better layout on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Social Media Section</h3>

### <img src="./readme-images/features/social-media-section.png" alt="website social media section">

- This section features all of the social media links displayed as SVG icons so that users can connect with it through various channels to help increase engagement.

<br />

---

<br />

<h3 align="center">Footer Section</h3>

### <img src="./readme-images/features/footer-section.png" alt="website footer section">

- The footer section appears at the bottom of each page, serving as an endpoint for the content.

- It includes a link to my GitHub page, providing viewers with exposure to my other work if they are interested.

<br />

---

<br />

<h3 align="center">Article Card Component</h3>

### <img src="./readme-images/features/article-card.png" alt="article card component">

- The article card component is a reusable UI element designed to provide readers with an overview of the article's content.

- It prominently displays the article's hero image to capture the reader's attention and encourage further exploration.

- Each article is color-coded according to its category, enabling users to quickly identify the content's topic for improved organization and user experience.

- Featuring the author's profile image adds a personal touch to the content, allowing readers to connect with the individual behind the writing.

- The author's profile link and publication date are included, providing additional context for the reader.

- A brief excerpt is included to offer a summary of the article's content.

- Clicking the link at the bottom directs the reader to the full article page for uninterrupted reading.

- The card components are fully responsive, adapting to smaller devices for optimal viewing.

<br />

---

<br />

<h3 align="center">Article Detail Section</h3>

### <img src="./readme-images/features/article-detail.png" alt="article detail page">

- When a user selects a blog post, they are directed to the full article detail page.

- At the top of the page, a full-bleed banner image captures the viewer's attention.

- The article maintains consistent color coding as seen in the card components.

- The author's profile picture takes a prominent position on the page.

- Article content is presented at an appropriate width, optimizing readability by avoiding excessive words per line.

### <img src="./readme-images/features/article-detail-edit-buttons.png" alt="article edit buttons">

- If the user is logged in and is the author of the blog post, they will find delete and edit buttons to the right of the page, enabling them to update or delete their post as desired.

- The page is responsive, ensuring a seamless reading experience across various device sizes.

<br />

---

<br />

<h3 align="center">Comment Section</h3>

### <img src="./readme-images/features/comment-section.png" alt="article comment section">

- The comment section appears below each article on the site, displaying the number of comments the post has received.

- Each comment includes the username of the commenter along with the timestamp indicating when the comment was made.

- Users must be signed in to leave a comment. If not signed in or do not have an account, they will be directed to the sign-in page to create one.

- If the user has an account and is logged in, they will see update and delete buttons next to their comments, allowing them to edit or remove their comments as desired.

<br />

---

<br />

<h3 align="center">Comment Update Form</h3>

### <img src="./readme-images/features/update-comment-form.png" alt="update comment form">

- Clicking the comment edit button directs the user to the update comment form, which is pre-populated with the content of the comment for easy editing.

- After submitting the updated comment, users are redirected back to the post they commented on and receive a popup notification confirming the successful update.

<br />

---

<br />

<h3 align="center">Comment Delete Confirmation Page</h3>

### <img src="./readme-images/features/delete-comment-confirmation.png" alt="delete comment confirmation page">

- If the user clicks the delete icon next to their comment, they will be directed to a confirmation page to ensure they want to proceed with deleting their comment.

Clicking the delete comment button on the confirmation page will remove the comment from the database and redirect the user back to the post where the comment was made.

- After deletion, the user will receive a popup notification confirming the successful removal of the comment.

<br />

---

<br />

<h3 align="center">Pagination</h3>

### <img src="./readme-images/features/pagination.png" alt="pagination component">

- Pagination is implemented on the articles page to display a maximum of six blog posts at a time, reducing clutter and minimizing scrolling.

- Clicking the next button reveals the next set of six blog posts from the list. It becomes invisible at the end of the list cycle when no more blog posts remain.

- Clicking the previous button displays the previous six blog posts from the list. It becomes invisible at the beginning of the list cycle.

- A number is displayed in the middle of the two controls, indicating the user's current position in the list cycle.

<br />

---

<br />

<h3 align="center">About Section</h3>

### <img src="./readme-images/features/about-section.png" alt="about section of the website">

- The About section functions as a summary of the blog's purpose and content.

- A descriptive image is positioned alongside large, readable text to create a positive impact on the reader.

- Certain words are highlighted using the color palette of the site to reinforce the brand qualities of the blog to the reader.

- The page is responsive across all device sizes, ensuring comfortable readability.

<br />

---

<br />

<h3 align="center">Signup Form</h3>

### <img src="./readme-images/features/signup-form.png" alt="signup form">

- The signup form is accessed through the signup button on the right side of the navbar, allowing users to sign in and create an account.

- Users are required to enter their credentials, including a username, first name, last name, and password. The email field is optional.

- If a user leaves a field invalid, they are redirected back to the form, and an error validation message is displayed.

- Upon successful account creation, a new user is added to the database, and they receive a notification via a popup message.

- The form is fully responsive, ensuring ease of interaction on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Login Form</h3>

### <img src="./readme-images/features/login-form.png" alt="login form">

- The login form enables users to sign in with their username and password credentials.

- If a user leaves a field invalid, they are redirected back to the form, and an error validation message is displayed.

- Upon successful login, the user receives a notification via a popup message confirming their successful login.

- The form is fully responsive, ensuring ease of interaction on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Logout Button</h3>

### <img src="./readme-images/features/logout-button.png" alt="logout buttoon">

- When the user is logged in to their account, a logout button will be displayed on the right side of the navbar.

- Clicking the logout button will successfully log the user out of their account to ensure its security.

- Upon successful logout, the user receives a notification via a popup message confirming that they have successfully logged out of their account.

<br />

---

<br />

<h3 align="center">Toast Popup Notification</h3>

### <img src="./readme-images/features/popup-notification.png" alt="popup toast notification">

- A toast popup notification is displayed for important actions the user performs on the site, such as signup, signin, signout, and any submissions, updates, or deletions of content.

- The popup appears at the bottom right of the page and is fixed to the viewport, ensuring it remains visible regardless of where the user has scrolled on the page.

<br />

---

<br />

<h3 align="center">Profile Section</h3>

### <img src="./readme-images/features/profile-section.png" alt="user profile section">

- The profile section serves as a platform to display all information related to a blog author, allowing them to share more about themselves.

- When the user initially creates an account, these details will be left blank, allowing the user to fill in the information whenever they please. This gives users the flexibility to choose how much information they want to share.

- If the profile belongs to the currently logged in user, then they have the option to click and edit button and be taken to the update profile page.

- The top section of the profile page showcases the user's profile picture alongside their username, city, and profession.

- The middle section is dedicated to more personal information, including first name, last name, date of birth, email, and a short bio.

- The last section provides an opportunity for the author to share links to their social media profiles, allowing others to connect if desired.

- This page is rully responsive for smaller device sizes.

<br />

---

<br />

<h3 align="center">Profile Update Form</h3>

### <img src="./readme-images/features/update-profile-form.png" alt="update profile form">

- Clicking the profile edit button directs the user to the update profile form, wwhere they can fill in their details.

- All fields are optional so user have the flexibility to choose how much information they want to share.

- After submitting the updated profile, users are redirected back to their profile page and receive a popup notification confirming the profile update.

<br />

---

<br />

<h3 align="center">My Articles Section</h3>

### <img src="./readme-images/features/users-articles-section-empty.png" alt="empth user article section">

- When logged in, users will find a "My Articles" link on the navigation bar, providing direct access to a page displaying all articles authored by that user.

- This feature offers users a convenient space to review all their blog posts contributed to the site, enabling them to make changes or delete them if desired, all from one location.

### <img src="./readme-images/features/user-article-section-filled.png" alt="filled user articles section">

- If the user has no articles, they will be notified accordingly, along with a link to the create article page for convenience, should they wish to write one.

<br />

---

<br />

<h3 align="center">Create Article Form</h3>

### <img src="./readme-images/features/create-article-form.png" alt="article creation form">

- When logged in, users will see a "Create Article" link on the navigation bar, which leads directly to the article creation form.

- The form features the Summernote widget, which integrates a WYSIWYG editor directly into the form, making text formatting for blog posts visually straightforward and intuitive.

- If a submission is missing required fields, users are sent back to the form with an error message that highlights the missing information, ensuring a straightforward correction process.

- Upon submitting the article, it is added to the database. Users are then redirected back to the home page and receive a popup notification confirming the article submission.

<br />

---

<br />

<h3 align="center">Update Article Form</h3>

### <img src="./readme-images/features/update-article-form.png" alt="update article form">

- When logged in, users will notice an edit article button (displayed as a pencil) next to any article they own. This button will be visible on both the post card component and on the post detail page.

- Clicking the edit button will redirect users to the update article form.

- The form will be prepopulated with the content of the article, allowing users to make any necessary changes, such as fixing spelling or grammatical errors, or adding additional information.

- Upon submitting the updates, the user will be redirected back to the article and given a popup notification of successful update.

<br />

---

<br />

<h3 align="center">Delete Article Confirmation Page</h3>

### <img src="./readme-images/features/article-delete-confirmation.png" alt="delete article confirmation page">

- When logged in, users will notice a delete article button (displayed as a cross) next to any article they own. This button will be visible on both the post card component and on the post detail page.

- If the user clicks the delete icon next to their article, they will be directed to a confirmation page to ensure they want to proceed with deleting their article.

- Clicking the delete article button on the confirmation page will remove the article from the database and redirect the user back to the homepage.

- After deletion, the user will receive a popup notification confirming the successful removal of the article.

<br />

---

<br />

<h3 align="center">404 Page</h3>

### <img src="./readme-images/features/404-section.png" alt="website 404 page">

- The 404 Page showcases a relevant, colorful image that fits with the site's overall style, reassuring users they're still on the same website. It informs users about the missing page with a short explanation and provides a button to easily return to the homepage for a smoother experience.

<br />

---

### Future Implementations

These features are part of the enhancement milestone of my project and serve as additional functionalities that I could integrate into the blog at a later date.

1. **Light and Dark Theme Options**

   - Users can toggle between light and dark themes using a switch in the navbar, enhancing the reading experience based on ambient light levels and time of day.

   <br/>

2. **Post Like Interaction**

   - A like system could be introduced that allows individual users to express appreciation for posts.

   - Users can click a heart icon next to a post to increment a like counter, fostering engagement.

   <br/>

3. **Bookmarking Articles**

   - Users can bookmark articles they wish to revisit in the future.

   - A dedicated section on the blog to keep all bookmarked posts together for easy access.

   <br/>

4. **Social Media Integration**

   - This would enable users to share blog posts via social media links to help expand the blog's reach within the tech community.

   - A share button could be implemented under each blog post for various social media platforms, enabling users to easily share posts across their preferred platforms.

     <br/>

5. **Interactive Reader Polls**

   - Featuring interactive reader polls on the homepage to encourage user engagement and foster discussion.

   - Poll topics could be updated to change regularly based on recent industry news or updates.

</br>

## Technologies

### Programming Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

Here's the revised section with corrected grammar, flow, and accuracy in the descriptions. Markdown is ready for you to copy and paste:

### Applications and Libraries

1. [Django](https://www.djangoproject.com/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design. Used for building the main application structure and functionality.

2. [PostgreSQL](https://www.postgresql.org/) - An open-source, advanced object-relational database system used to store data for the application.

3. [Code Institute Database Maker](https://dbs.ci-dbs.net/) - An API utilized in the application, allowing up to 100 requests per day for free. It enables filtering the response by category and language.

4. [Visual Studio Code](https://code.visualstudio.com/) - A source-code editor developed by Microsoft for Windows, Linux, and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. Used as the preferred IDE for coding the HTML, CSS, and JavaScript, aiding in the development process and creation of markdown README files.

5. [Git](https://git-scm.com/) - A free and open-source distributed version control system used to handle the project's code versioning, enabling tracking of changes and collaboration.

6. [GitHub](https://github.com/) - A platform for hosting and sharing source code, utilizing Git for version control. It hosts the project remotely, making the source code accessible to others, and is used for deploying the site via GitHub Pages.

7. [GitKraken](https://www.gitkraken.com/) - A graphical user interface (GUI) Git client that facilitates managing git repositories through a visual interface, particularly useful for visualizing commit history and managing complex Git operations.

8. [Datagrip](https://www.jetbrains.com/datagrip/) - A database management environment developed by JetBrains, designed to provide a better workflow for managing databases with advanced code insights, efficient schema navigation, and running queries.

9. [Figma](https://www.figma.com/) - An interface design application that is used for UI/UX design, allowing for the experimentation with design elements such as colors and layouts to create visual mockups.

10. [Shields.io](https://shields.io/) - A service used to create badges for README files, enhancing the documentation with visual indicators of project status, license, and other metrics.

11. [TinyPNG](https://tinypng.com/) - An online service used for compressing PNG and JPEG images to reduce file size without losing much quality, optimizing web performance.

12. [Midjourney](https://www.midjourney.com/) - I utilized Midjourney to generate all the website images. By incorporating specific keywords, I ensured that the images were produced in a consistent art style for a cohesive visual design. With my paid account plan, I have the right to use these generated images for my project, in line with Midjourney's [terms of service](https://docs.midjourney.com/docs/terms-of-service).

13. [Heroku](https://heroku.com/) - A platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud, used for deploying the website.

14. [DrawSQL](https://drawsql.app/) - An online tool for designing and visualizing database schemas through Entity-Relationship Diagrams (ERD), helping to conceptualize and communicate the database structure.

15. [Gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX, used as a web server gateway interface that allows Django applications to communicate with the web servers.

16. [Whitenoise](http://whitenoise.evans.io/) - A package for serving static files directly from Django without the need for a separate web server, simplifying deployment and improving performance.

17. [Pillow](https://python-pillow.org/) - The Python Imaging Library adds image processing capabilities to your Python interpreter, enabling image opening, manipulation, and saving across a wide variety of formats.

18. [Python Dotenv](https://pypi.org/project/python-dotenv/) - A Python library for reading key-value pairs from a `.env` file and setting them as environment variables, making configuration management easier.

19. [Dj Database URL](https://pypi.org/project/dj-database-url/) - A Django utility that allows you to utilize the `DATABASE_URL` environment variable to configure your Django application's database settings, simplifying database configuration.

20. [Psycopg2](https://www.psycopg.org/) - A PostgreSQL database adapter for the Python programming language, facilitating connection and interaction with PostgreSQL from Python.

<br />

## Deployment & Local Development

#### Local Development

1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. (Optional): Set up a virtual environment in the project folder using `python3 -m venv [virtual_environment name]`
5. (Optional): To activate the virtual environment on Windows run `myvenv\Scripts\activate` and on macOS and Linux, run `source myvenv/bin/activate`
6. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
7. **Note**: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](#environment-variables) for more information.
8. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
9. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
10. (Optional):: Fixtures for Users and also the individual blog posts are included in the project in the `fixtures` directory. To add the pre-populated data to the database, run `python manage.py loaddata fixtures/[fixture_name].json`.
11. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

#### Heroku Deployment

1. Ensure the project repository has been uploaded to Github.
1. Login to the Heroku dashboard and create a new app.
1. Connect your GitHub repository to your Heroku app.
1. In the Settings tab, ensure that the Python Buildpack is added.
1. Set environment variables in the Config Vars section of the Settings tab.
1. In the Deploy tab, enable automatic deploys from your GitHub repository.
1. Click the "Deploy Branch" button to deploy the app.
1. Once the app has been deployed, click the "Open App" button to view the app.

#### Environment Variables

- For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file.

- **Note**: Ensure the .env file is included in the .gitignore file to exclude it from your GitHub repo to prevent the environment variables from being publicly exposed.

- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
- You need to define the following environment variables:

  - `SECRET_KEY`: The secret key for your Django project. This is a critical setting that's used for cryptographic signing, and should be kept secret at all times. It's used to provide cryptographic signing, and should be a long, random string of bytes.

  - `DEBUG`: A boolean that turns on/off debug mode. Set to `True` for development to enable detailed error pages and logging for debugging. Set to `False` in production to improve performance and security.

  - `DATABASE_URL`: The URL for your database. This should include the database engine, username, password, host, port, and database name. For a Postgres database, it typically looks like `postgres://USER:PASSWORD@HOST:PORT/DB_NAME`.

  - `CLOUDINARY_API_KEY`: Your Cloudinary account's API key. This key is used to authenticate requests to Cloudinary's services for uploading and managing images and other media assets.

  - `CLOUDINARY_API_SECRET`: Your Cloudinary account's API secret. This secret is used alongside the API key to securely sign requests to Cloudinary.

  - `CLOUDINARY_CLOUD_NAME`: Your Cloudinary account's cloud name. This is the unique name that identifies your cloud within Cloudinary. It's used in the URL structure for accessing uploaded resources.

<br />

## Testing

[Link to TESTING.md](TESTING.md)

## Credits

### Code Used And Tutorials

- [Code Institute: Developing With Django](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm) - This series from Code Institute served as a solid introduction to the Django framework by walking me through how to build and deploy a Django app to Heroku.

- [Udemy: Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide/) - This course helped me dive deeper into Django, covering many aspects of the framework in greater detail.

- [Very Academy: Learn Django Class-Based Views](https://www.youtube.com/watch?v=GxA2I-n8NR8&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT) - To gain a solid conceptual grasp of class-based views, working through this playlist series from Very Academy on YouTube helped me explore how each view works in detail through examples.

- [Django Documentation: Custom Template Tags And Filters](https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/) - For developing custom logic to assign category colors to each of my blog posts, I learned to implement custom filters from this section of the Django documentation.

- [Django Documentation: Data Fixtures](https://docs.djangoproject.com/en/4.2/howto/initial-data/) - To efficiently populate my database with data, I learned about fixtures, how they work, and how they can be loaded into a database from this section of the Django documentation.

- [Colt Steele's Git and GitHub Course](https://www.udemy.com/course/git-and-github-bootcamp/) - As my project grew, maintaining a clear and secure git history became paramount. Initially, I had inadvertently included my API keys along with me Django secret key in my Github repository via the settings file. To enhance security, I altered my earlier commit history to move these keys to a `.env` file. The chapter on using interactive rebase was instrumental in enabling me to refactor those previous commits, ensuring the complete removal of the API keys from the commit history and thus avoiding a potential security vulnerability.

### Content

The content for each blog post was created with help from [ChatGPT](https://chat.openai.com/), starting from titles I provided. After getting the initial drafts, I went through and fine-tuned them to make sure they were just right. Then, I saved these polished posts as picture files before uploading them to our database. This process combined the convenience of AI with a personal touch to ensure quality.

### Media

- [Phosphor Icons](https://phosphoricons.com/) - This was the icon set I used for all icons across the website.
- [Midjourney](https://www.midjourney.com/) - All images were generated with the usage of Midjourney.

### Acknowledgments

- My Mentor [Lauren-Nicole](https://github.com/CluelessBiker) - who offered excellent advice, provided solid feedback, and supported me during my work on this project.

- The Code Institute Community - Both my class and the community have been invaluable. Having access to a wonderful group of people who share my passion for coding has significantly aided my journey in coding thus far.

- To you, dear reader, for taking the time to read my documentation. Have a cookie! 🍪

<br/>

[Back to Top ^](#introduction)

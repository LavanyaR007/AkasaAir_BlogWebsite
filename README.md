# AkasaAir_BlogWebsite

FrontEnd : HTML,CSS,JS
BackEnd : Python,Django
Database : sqlite3


To Set Up Run Application
1.	Download the zip file from github and Download Blog.zip
2.	Open pycharm or visual studio code
3.	Open terminal and type in commane

  a.	pip install -r requirements.txt	
4.	After Installing Files – apply migrations

  a.	python manage.py makemigartions
  
  b.	python manage.py migrate
  
5.	After applying migrations we are good to run the server – cmd to run the server
   
  a.	python manage.py runserver


Features (Implemented):
1.	Login and SignUp Module
2.	Home Page (shows old blogs in slider and new blogs below slider)
3.	See Profile and Update Profile
4.	Add Post/Blog
   
    a.	Can choose from various category suitable for their blog (if category is not found, the user can also add category)
  	
    b.	Title
  	
    c.	Description (max 300 words)
  	
    d.	Content (rich text upload, the user is given an chance to design how their content should look)
  	
    e.	Image
  	
    f.	Multiple Images(if there for image slider)
  	
5.	Edit Post
   
6.	Delete
   
    a.	Delete the entire blog (or)
  	
    b.	Delete only the images from slider
  	
7.	Category Blogs
    
    a.	Can see posts of different category on click on category name
   	
8.	Search Blogs
    
    a.	Can search for a blog based and results are shown based on title of blog which matches
   	
9.	Comment on Blogs
    
    a.	The logged in user can add comments
   	
10.	As the user views the post, the count of views will be incremented by 1 and displayed as well.
11.	Displaying Messages at header on success and error on actions performed from user.

Features (If time given):
1.	Forgot Password(Email facility)
2.	View the profile of other users
3.	Reply to comment
4.	Like and Dislike of Blog
5.	Contact us page
6.	Dynamic setting up data of about us, contact us pages, title and icon of website,etc

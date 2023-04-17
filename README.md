# Djano-Query-ORM-Example-Practice 


##  Write a Query using Django ORM to fetch all the books objects from your database.
##  Write a Query using Django ORM to fetch title and published_date of all books from the database.
##  Fetch first name and last name of all the new authors ( Authors with popularity_score = 0 are new authors ).
##  Fetch first name and popularity score of all authors whose first name starts with A and popularity score is greater than or equal to 8.
##  Fetch first name of all the authors with aa case insensitive in their first name.
##  Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25].
##  Fetch list of all the publishers who joined after or in September 2012, output list should only contain first name and join date of publisher. Order by join date.
##  Fetch ordered list of first 10 last names of Publishers, list must not contain duplicates.
##  Get the signup date for the last joined Author and Publisher.
##  Get the first name, last name and join date of the last author who joined.
##  Fetch list of all authors who joined after or in year 2013
##  Fetch total price of all the books written by authors with popularity score 7 or higher.
##  Fetch list of titles of all books written by authors whose first name starts with ‘A’. The result should contain a list of the titles of every book. Not a list of tuples.
##  Get total price of all the books written by author with pk in list [1, 3, 4]
##  Produce a list of all the authors along with their recommender.
##  Produce list of all authors who published their book by publisher pk = 1, output list should be ordered by first name.
##  Create three new users and add in the followers of the author with pk = 1.
##  Set the followers list of the author with pk = 2, with only one user.
##  Add new users in followers of the author with pk = 1.
##  Remove one user from the followers of the author with pk = 1.
##  Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing Author.objects manager )
##  Fetch list of all authors who wrote a book with “tle” as part of Book Title.
##  Fetch the list of authors whose names start with ‘A’ case insensitive, and either their popularity score is greater than 5 or they have joined after 2014. with Q objects.
##  Retrieve a specific object with primary key= 1 from the Author table.
##  Retrieve the first N=10 records from an Author table.
##  Retrieve records from a table that match this condition, popularity score = 7. And get the first and last record of that list.
##  Retrieve all authors who joined after or in the year 2012, popularity score greater than or equal to 4, join date after or with date 12, and first name starts with ‘a’ (case insensitive) without using Q objects.
##  Retrieve all authors who did not join in 2012.
##  Retrieve Oldest author, Newest author, Average popularity score of authors, sum of price of all books in database.
##  Retrieve all authors who have no recommender, recommended by field is null.
##  Retrieve the books that do not have any authors, where the author is null. Also, retrieve the books whose authors are present, but do not have a recommender, where the author is not null and the author’s recommender is null. (Note that if the condition for the author not being null is not specified and only the condition for the recommender being null is mentioned, all books with both author null and author’s recommender null will be retrieved.)
##  Total price of books written by author with primary key = 1. ( Aggregation over related model ), oldest book written by author with pk = 1, latest book written by author with pk = 1.
##  Among the publishers in the Publishers table what is the oldest book any publisher has published.
##  Average price of all the books in the database.
##  Maximum popularity score of publisher among all the publishers who published a book for the author with pk = 1. (Reverse Foreign Key hop)
##  Count the number of authors who have written a book which contains the phrase ‘ab’ case insensitive.
##  Get all the authors with followers more than 216.
##  Get average popularity score of all the authors who joined after 20 September 2014.
##  Generate a list of books whose author has written more than 10 books.
##  Get the list of books with duplicate titles.

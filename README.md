# CNNwebscrapper2023
A python script that reads and stores relevant data from CNN articles released in 2023

*I strongly advise compiling and running this on the terminal, as it takes quite a while to generate and in my experiences Pycharm was very slow*

This code was written as part of my University's Scientific Initiation program, which in my case focuses on machine learning and prediction algorithms

Kaggle link to the dataset generated: https://www.kaggle.com/datasets/pedroaribe/4000-cnn-articles-as-of-1062023

This was my first time writing in python and I did not care much for optimizing the code, so long as I was satisfied with the results, I also usually don't comment my code so any strange phrasings can be blamed on that

This code is heavily based on information from this tutorial: https://brightdata.com/blog/how-tos/web-scraping-with-python

Further detailed explanation is commented in the code but the general explanation is as follows:

1. The program will collect all the news and aggregator ((an aggregator in this case is any subsection which in itself houses links to more articles such as world or bussiness)) links in cnn's main page
2. For each aggregator it will collect every available link to other articles
3. For each article it will collect and store the title, description, article body, keywords, theme and article link
4. For each article it will also collect every link to other articles and store them so they can be read later in the loop
5. Once every single link has been read, a .csv file named news will be generated

Considerations:

Not every article will have keywords, but that is not a problem

Some links lead to posts and articles that do not have a body, that is a problem, therefore those are not stored

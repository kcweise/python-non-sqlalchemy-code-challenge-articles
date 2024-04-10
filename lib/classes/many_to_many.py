from lib.classes.string_validation import val_string 

class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        #Cleanup: adding sting validation
        # if isinstance(title, str) and 5<=len(title)<=50:
        #     self._title = title
        # else:
        #     raise Exception("Title must be a string with number of characters between 5 and 50")
        val_string("Title", title, 5, 50)
        self._title = title     
        
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        #Recognize this could also be a good candidate for a helper method.
        if hasattr(self, "_title"):
            raise Exception("Title already exists in Article class and cannot be changed.")
        else:
            self._title = title
        
class Author:
    def __init__(self, name):
        #Cleanup: adding sting validation
        # if isinstance(name, str) and len(name)>0:
        #     self._name = name
        # else:
        #     raise Exception("Name must be a string with more than 0 characters")
        val_string("Name", name, 1)
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        #Recognize this could also be a good candidate for a helper method.
        if hasattr(self, "_name"):
            raise Exception("Name already exists in Author class, and cannot be changed.")
        else:
            self._name = name

    def articles(self):
        return[article for article in Article.all if article.author == self]

    def magazines(self):
        #Clean up
        #unique_mags = {article.magazine for article in self.articles()}
        #return list(unique_mags)
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        #Clean up
        #new_article = Article(author = self, magazine = magazine, title = title)
        #return new_article
        return Article(author = self, magazine = magazine, title = title)
        
    def topic_areas(self):
        unique_topics = list(set(article.magazine.category for article in self.articles()))
        # if len(unique_topics) == 0:
        #     return None
        # else:
        #     return list(unique_topics)
        return unique_topics if unique_topics else None

class Magazine:
    
    all_mags = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all_mags.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # if isinstance(name, str) and 2<=len(name)<=16:
        #     self._name = name
        # else:
        #     raise Exception("Name must be a string with between 2 and 16 characters")
        val_string("Name", name, 2, 16)
        self._name = name 
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        # if isinstance(category, str) and len(category)>0:
        #     self._category = category
        # else:
        #     raise Exception("Category must be a string with more than 0 characters")
        val_string("Category", category, 5, 50)
        self._category = category 
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # unique_auth = {article.author for article in self.articles()}
        # return list(unique_auth)
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        mag_titles = [article.title for article in self.articles()]
        
        # if len(mag_titles) >0:
        #     return mag_titles
        # else:
        #     return None
        return mag_titles if mag_titles else None 

    def contributing_authors(self):
        auth_art_count = {}
        for article in self.articles():
            author = article.author
            if author in auth_art_count:
                auth_art_count[author] += 1
            else:
                auth_art_count[author] = 1
                
        contribs = [author for author, count in auth_art_count.items() if count > 2]
        
        # if len(contribs)>0:
        #     return contribs
        # else:
        #     return None
        
        return contribs if contribs else None  
    
    @classmethod
    def top_publisher(cls):
        if not cls.all_mags or not Article.all:
            return None
        
        #Create a dict {mag: number of articles in mag}
        #iterates over mags in all_mags passes mag to key, 
        # and sets that mag value by getting the len of what method articles() produces for that mag.
        mag_art_counts = {}
        for mag in cls.all_mags:
            mag_art_counts[mag] = len(mag.articles())
        
        #when mag_art_counts is not empty it return the key associated with the maximum value, 
        #or None when empty
        if mag_art_counts:
            top_pub = max(mag_art_counts, key = mag_art_counts.get)
            return top_pub
        else:
            return None
        
        
        
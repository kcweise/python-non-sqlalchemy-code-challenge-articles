class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title, str) and 5<=len(title)<=50:
            self._title = title
        else:
            raise Exception("Title must be a string with number of characters between 5 and 50")
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Title already exists in Article class and cannot be changed.")
        else:
            self._title = title
        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name)>0:
            self._name = name
        else:
            raise Exception("Name must be a string with more than 0 characters")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Name already exists in Author class, and cannot be changed.")
        else:
            self._name = name

    def articles(self):
        return[article for article in Article.all if article.author == self]

    def magazines(self):
        unique_mags = {article.magazine for article in self.articles()}
        return list(unique_mags)

    def add_article(self, magazine, title):
        new_article = Article(author = self, magazine = magazine, title = title)
        return new_article
        
    def topic_areas(self):
        unique_topics = {article.magazine.category for article in self.articles()}
        if len(unique_topics) == 0:
            return None
        else:
            return list(unique_topics)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<=len(name)<=16:
            self._name = name
        else:
            raise Exception("Name must be a string with between 2 and 16 characters")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category)>0:
            self._category = category
        else:
            raise Exception("Category must be a string with more than 0 characters")
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_auth = {article.author for article in self.articles()}
        return list(unique_auth)

    def article_titles(self):
        mag_titles = [article.title for article in self.articles()]
        
        if len(mag_titles) >0:
            return mag_titles
        else:
            return None

    def contributing_authors(self):
        auth_art_count = {}
        for article in self.articles():
            author = article.author
            if author in auth_art_count:
                auth_art_count[author] += 1
            else:
                auth_art_count[author] = 1
                
        contribs = [author for author, count in auth_art_count.items() if count > 2]
        
        if len(contribs)>0:
            return contribs
        else:
            return None   
            
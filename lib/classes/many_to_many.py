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
        if hasattr(self, "title"):
            raise Exception("Title already exists in Article class and cannot be changed.")
        else:
            self._title = title
        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name)>0:
            self._name = name
        else:
            raise Exception("Name must be a string with number of characters between 2 and 16")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("Name already exists in Author class, and cannot be changed.")
        else:
            self._name = name

    def articles(self):
        return[article for article in Article.all if article.author == self]

    def magazines(self):
        unique_mags = {article.magazine for article in self.articles()}
        return list(unique_mags)

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
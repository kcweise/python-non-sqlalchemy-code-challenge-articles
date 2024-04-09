class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title, str) and 5<=len(title)<=50:
            self._title = title
        else:
            raise Exception("Title must be a string with number of characters between 5 and 50")
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception("Title cannot change.")
        else:
            self._title = title
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

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
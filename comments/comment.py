'''Module representing the comments'''
from datetime import datetime

class Comment:
    '''Defintions for the comment entity'''
    COMMENTS = []

    def __init__(self, author, message):
        self.comment_id = len(Comment.COMMENTS) + 1
        self.author = author
        self.message = message
        self.created_at = str(datetime.now())

    def save(self):
        '''Save a comment to the comments list'''
        comment = {
            'comment_id': self.comment_id,
            'author': self.author,
            'message': self.message,
            'created_at': self.created_at
        }
        Comment.COMMENTS.append(comment)

    @staticmethod
    def find_comment_by_author(author):
        '''Find a comment by author'''
        comments_list = Comment.COMMENTS
        comment = {}
        for index, _ in enumerate(comments_list):
            if comments_list[index].get(author) == author:
                comment = comments_list[index]
        return comment

    def comment_to_dict(self):
        '''Return a dictionary of the comments object'''
        return {
            'author': self.author,
            'message': self.message,
            'created_at': self.created_at
        }

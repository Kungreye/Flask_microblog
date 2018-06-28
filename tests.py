#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
# TESTING is for application to determin if it is running under unit tests or not.
# Override default db in Config to use in-memory SQLite for unit tests.


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()     # Flask pushes an application text.
        db.create_all()
    # db needs to know the db config from app instance. SO, which app instance to use?
    # The current_app variable looks for an active application context in the current thread, 
    # if application context is found, the app instance is got from it. 
    # If there is no context, then no way to know what app is active,
    # and current_app raises an exception.

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        digest = 'd4c74594d841139328695756648b6bd6'
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/{}?d=identicon&s=128'.format(digest)))
        # from hashlib import md5
        # digest = md5('john@example.com'.encode('utf-8')).hexdigest()

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan',email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body='post from john', author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body='post from susan', author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(body='post from mary', author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body='post from david', author=u4, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])    # p2, p3, p4, p1  (desc in time)     
        db.session.commit()

        # setup the followers
        u1.follow(u2)   # john follows susan
        u1.follow(u4)   # john follows david
        u2.follow(u3)   # susan follows mary
        u3.follow(u4)   # mary follows david
        db.session.commit()

        # check the followed posts for each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
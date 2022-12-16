import pymysql
import os

class CommentResource:
    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "root"
        pw = "84443295412lx."
        h = "localhost"
        # h = "db6156.c4qfxod7s5ol.us-east-1.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_comments_by_blogID(blog_id):
        sql = "SELECT * FROM commentdb.comments WHERE blog_id=%s"
        user_sql = "SELECT profile_img FROM users.users WHERE username=%s"
        conn = CommentResource._get_connection()
        cur = conn.cursor()

        try:
            cur.execute(sql, blog_id)
        except:
            return None
        
        result = cur.fetchall()
        for each_comment in result:
            user = each_comment['owner_id']
            cur.execute(user_sql, user)
            user_image = cur.fetchone()['profile_img']
            each_comment['profile_img'] = user_image
            
        return result


    @staticmethod
    def get_comments_number(blog_id):
        sql = "SELECT COUNT(*) FROM commentdb.comments WHERE blog_id=%s"
        conn = CommentResource._get_connection()
        cur = conn.cursor()

        try:
            cur.execute(sql, blog_id)
        except:
            return None
        
        result = cur.fetchone()
        result = result["COUNT(*)"]
        return result
        
        
    @staticmethod
    def get_commentsnum_by_username(username):
        sql = "SELECT COUNT(*) FROM commentdb.comments WHERE owner_id=%s"
        conn = CommentResource._get_connection()
        cur = conn.cursor()

        try:
            cur.execute(sql, username)
        except:
            return None
        
        result = cur.fetchone()
        result = result["COUNT(*)"]
        return result
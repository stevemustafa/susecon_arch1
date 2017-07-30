import random
import string
import redis

class Shortener(object):
    db = redis.Redis(decode_responses=True, host='localhost', port=6379)

    def shorten(self, url):
        """ returns an 8 ASCII char 'representation' of the provided url - this is the key to which the lookup from the
        DB must be used """
        key = self.generate_key()



    def confirm_not_in_db(self, key):
        """ confirm whether the provided key is in the database or not"""
        return self.db.exists(key)

    def generate_key(self):
        key = ""
        for i in range(8):
            key += random.choice(string.ascii_letters)

        return key





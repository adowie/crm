from datetime import datetime
from Crypto.Cipher import AES
import config
import time
import os
import md5
import base64
import random
import logging

def year():
	return datetime.now().strftime("%Y")

def now_time():
	return time.strftime("%H:%M")

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def today():
    return time.strftime("%Y-%m-%d")


def boolInts(int_):
	if int_ == 1:
		return True
	else:
		return False

def datetimeToTime(dt):
    return dt.strftime('%H:%M:%S')

def datetimeToDate(dt):
    day = dt.strftime('%Y-%m-%d')
    
    return day
   

def convertDateTime(dt):
    # date = datetime(dt)
    return datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')

def barCoder(code):
    if code and code != "":
        c = md5.new()
        c.update(code)
        return c.digest()
    else:
        return None

def save_uploaded_file (file_, upload_dir):
    # This saves a file uploaded by an HTML form.
    #    The form_field is the name of the file input field from the form.
    #    For example, the following form_field would be "file_1":
    #        <input name="file_1" type="file">
    #    The upload_dir is the directory where the file will be written.
    #    If no file was uploaded or if the field does not exist then
    #    this does nothing.
    
    fileitem = file_

    filename = upload_dir + "default.png";

    if fileitem:
        if fileitem.filename:
            extension = os.path.splitext(fileitem.filename)[1][1:].strip()
            fn = str(md5.new(fileitem.filename).hexdigest())+"."+extension
            filename = upload_dir + fn 

            fout = file (os.path.join(upload_dir, fn), 'wb')
           
            while 1:
                chunk = fileitem.read(100000)
                if not chunk: break
                fout.write (chunk)
            fout.close()
    
    supd = filename.split("/")
    realPath = "/".join(supd[2:])

    return str(realPath)


def trim(str_):
    return str_.replace(" ","")

def encrypt_decrypt(ed,enc_str):
    if ed == "d":
        cipher = AES.new(config.SECRET_KEY,AES.MODE_ECB)
        return cipher.decrypt(base64.b64decode(enc_str)).strip()
    elif ed == "e":
        cipher = AES.new(config.SECRET_KEY,AES.MODE_ECB) # never use ECB in strong systems obviously
        return base64.b64encode(cipher.encrypt(enc_str.rjust(32)))
    else:
        return 0


def randomString(_len):
    # encrt_str = trim("%s%s"%(now(),seed))[:16]
    # return md5.new(encrypt_decrypt("e",encrt_str)).hexdigest()[16:32] #TODO : make real random string
    id_ = "";
    cypher_ = [];
    cypher = "0123456789?@#$!%&ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    for i in range((len(cypher) - 1)):
        cypher_.append(cypher[i])

    for i in range(_len):
        id_ += cypher_[ int(round(random.randint(0,(len(cypher_)-1)))) ]

    return id_


# make dictionary key,value referenceable by dot '.' notation
class Map(dict):
     # Usage: arr = Map(dict)
     # keyvalue = arr.key
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]



def logger():
    LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
    logging.basicConfig(filename = "../logs.log",level = logging.DEBUG,format = LOG_FORMAT)
    logger = logging.getLogger()



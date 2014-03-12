import json
import urllib2
import tempfile
import PIL.Image as Image
import time
import sys
import subprocess

from os import getenv

apicall = 'http://api.tumblr.com/v2/tagged?tag={0}&api_key={1}'
cons_key = None

def loadKey(path='apikey'):
    global cons_key
    keydata = json.load(open(path))
    cons_key = keydata['Consumer Key']

def display(img,face=0,rotation=0):
    subprocess.call("./cube-image",stdin=img.tostring())
    pass

def showTopics(topics):
    for topic in topics:
        a = json.load(urllib2.urlopen(apicall.format(topic,cons_key)))
        for elem in [x for x in a['response'] if x['type']=='photo']:
            url = elem['photos'][0]['alt_sizes'][-2]['url']
            tf=tempfile.TemporaryFile()
            print("Loading image from {0}.".format(url))
            tf.write(urllib2.urlopen(url).read())
            tf.seek(0)
            i = Image.open(tf)
            i2 = i.resize((32,32),Image.ANTIALIAS)
            ts = elem['timestamp']
            display(i2)
            tf.close()
            time.sleep(3.5)


if __name__ == '__main__':
    loadKey()
    topics = sys.argv[1:]
    if len(topics) == 0:
        pass
    showTopics(topics)


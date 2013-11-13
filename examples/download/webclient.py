#!/usr/bin/python

from http import client
from urllib.parse import urlparse

class WebClient:

  def __init__(self, factory):
    self.pbf = factory

  def get(self, url):
    u = urlparse(url)
    #host = '{:s}://{:s}'.format(u.scheme, u.netloc)
    host = u.netloc
    path = u.path
    print(host + " " + path)

    file_name = u.path.split('/')[-1]
    print(file_name)

    connection = client.HTTPConnection(host)
    connection.request('GET', u.path)
    response = connection.getresponse()
    size = int(response.getheader("Content-Length"))

    target = open(file_name, "wb")
    bar = self.pbf.create_default(size)
    current = 0
    block_size = 8192
    while True:
      buffer = response.read(block_size)
      if not buffer:
        break;

      target.write(buffer)
      current += len(buffer)
      bar.update(current)
      bar.render()

    connection.close()

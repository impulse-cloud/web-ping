import requests
import time
import traceback
import sys

print "Web Ping running..."
print "All connection exceptions will be output to stdout."

while True:

    time.sleep(5)
    try:
        r = requests.get('http://web/')
    except:
        print "Exception in request:"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60


'''run.py'''

import bottle

from detectem.settings import DEBUG
from detectem.ws import do_detection


def main():
    '''Run bottle server.'''
    bottle.debug(DEBUG)
    bottle.run(host='0.0.0.0', port=8080, server='gunicorn', workers=20)


# Execute main

if __name__ == '__main__':
    main()

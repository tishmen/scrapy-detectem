import bottle

from bottle import run
from detectem.settings import DEBUG
from detectem.ws import do_detection


def main():
    bottle.debug(DEBUG)
    run(host='0.0.0.0', port=5723)


if __name__ == '__main__':
    main()

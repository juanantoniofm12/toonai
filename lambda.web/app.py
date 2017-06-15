
# -*- coding: utf-8 -*-

import sys
from toonapp import app

if __name__ == '__main__':
    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler, StreamHandler
        file_handler = TimedRotatingFileHandler(
            "lambdastuff.log",
            when="D",
            backupCount=10
            )
        file_handler.setLevel(logging.WARNING)
        #TODO: Maybe for a lambda is better to just log  stuff to stdout
        if app.config["ONLINE"]:
            stdout_handler = logging.StreamHandler(sys.stdout)
            app.logger.addHandler(stdout_handler)
        else:
            app.logger.addHandler(file_handler)

    app.debug = app.config['DEBUG']
    app.secret_key = 'super secret key'
    app.run()

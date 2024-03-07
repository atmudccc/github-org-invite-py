#!/bin/sh
gunicorn -w 4 -b 0.0.0.0:18989 main:app

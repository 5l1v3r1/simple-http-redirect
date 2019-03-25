#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Simple Http Redirect
Author: K4YT3X
Date Created: March 25, 2019
Last Modified: March 25, 2019

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2018-2019 K4YT3X
"""

from avalon_framework import Avalon
import argparse
import http.server
import json
import socketserver


def process_arguments():
    """Processes CLI arguments
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # video options
    general_options = parser.add_argument_group('General Options')
    general_options.add_argument('-p', '--port', help='port number to listen on', action='store', type=int, default=8080)
    general_options.add_argument('-b', '--bind', help='IP or host to bind to', action='store', default='0.0.0.0')
    general_options.add_argument('-r', '--redirect_table', help='file to read redirect table from', action='store', default='redirect_table.json')

    # parse arguments
    return parser.parse_args()


class request_handler(http.server.SimpleHTTPRequestHandler):
    """ handler to handle http requests

    Extends:
        http.server.SimpleHTTPRequestHandler
    """

    def do_GET(self):
        """ When a GET request is received
        """
        Avalon.debug_info(self.path)

        try:
            # try to find a matched rule in the redirect table
            redirect_location = redirect_table[self.path]

            # send 301 redirect
            self.send_response(301)
            self.send_header('Location', redirect_location)
            self.end_headers()

        # if rule doesn't exist, send 404
        except KeyError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))


def read_redirect_table(path):
    """ read redirect table content into dictionary

    Arguments:
        path {string} -- path to redirect table

    Returns:
        dictionary -- dictionary of redirecting rules
    """
    with open(path, 'r') as redirect_table:
        return json.loads(redirect_table.read())


# parse command line arguments
args = process_arguments()

# load redirecting rules
redirect_table = read_redirect_table(args.redirect_table)

# setup socketserver
socketserver.TCPServer.allow_reuse_address = True
handler = socketserver.TCPServer((args.bind, args.port), request_handler)

# start socket server
Avalon.info('Starting HTTP server')
handler.serve_forever()

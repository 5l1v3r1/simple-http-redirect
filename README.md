# Simple HTTP Redirect

## Description

This is a short and simple Python HTTP redirect server. It reads the redirect table stored in a JSON file and redirect incoming requests according to the redirect table.

## Quick Start

```bash
$ python3 simple_http_redirect.py -p 8080 -b 0.0.0.0 -r redirect_table.json
```

## Full Usage

### -p PORT, --port PORT
    port number to listen on (default: 8080)
### -b BIND, --bind BIND
    IP or host to bind to (default: 0.0.0.0)
### -r REDIRECT_TABLE, --redirect_table REDIRECT_TABLE
    file to read redirect table from (default:redirect_table.json)
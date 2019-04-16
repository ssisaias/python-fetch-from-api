## Building and Usage

#### Running on Windows:

 - Use Python 3.6
 
```bash
Scripts\activate.bat

pip3 install requests

py src\dumpPageViews.py
```

The script will create one list for each request and append to the file, you should replace '][' for ',' to get a single list.
also watch out for }{ without the comma.

We can use this to pretty much store any large, multi paged api requests, like comments, etc.
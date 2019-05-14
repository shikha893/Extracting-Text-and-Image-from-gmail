# Extracting-Text-and-Image-from-gmail

 Set up the conda envrionment "google-api":

        $ conda env create -f environment.yml 

* Follow these instructions to allow python to access your gmail account 
    https://developers.google.com/gmail/api/quickstart/python

* After the set up you will download a file called `credentials.json`. Be sure to update the variable `GMAIL_CREDENTIALS_PATH` path to this file in `example.py`. Also update the `GMAIL_TOKEN_PATH` to be a file called `*-token.json` in the same directory

    e.g:
    ```
    example.py 

    GMAIL_CREDENTIALS_PATH = "credentials.json"
    GMAIL_TOKEN_PATH = "token.json"
    ...
    ``



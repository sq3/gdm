GDM - Google Drive Migration
============================

GDM will help you to migrate your Google Drive documents from a personal Google Account (e.g your.name@gmail.com) to a GoogleApps domain.


# Requirements


+ google-api-python-client==1.2
+ httplib2==0.8
+ pyOpenSSL==0.13.1
+ python-dateutil==2.2


# Usage

Before you start you have to create a project on https://console.developers.google.com/ and 
setup OAuth Authentication. For your personal account you need an Client ID and for the GoogleApps
account use a service account to access all accounts in your domain. Also don't forget to actiavte 
the GoogleDrive API for both accoutns.


## install requirements:

```
$ pip install -r requirements.txt
```


## Run the migration script to start the emails migrations:

```
$ python gdm.py /path/to/email_mapping_list.csv <condition number>
```

email_mapping_list.csv (2 columns: src - old domain email address, dest - new domain email address):

| src                     | dest                    |
| ----------------------- | ----------------------- |
| username1@olddomain.com | username1@newdomain.com |
| username2@olddomain.com | username2@newdomain.com |
| username3@olddomain.com | username3@newdomain.com |


Condition number: all posible numbers are: 

0,1,2,3,4,5,6,7,8,9 or 'all'


# Troubleshooting

+ [Cannot use SignedJwtAssertionCredentials?](http://iambusychangingtheworld.blogspot.com/2013/12/google-drive-api-to-use.html)
+ Error When installing PyOpenSSL:
  + ["openssl/ssl.h: No such file or directory"](http://iambusychangingtheworld.blogspot.com/2013/12/fix-error-opensslsslh-no-such-file-or.html)
  + ["fatal error: Python.h: No such file or directory"](http://iambusychangingtheworld.blogspot.com/2013/12/fix-error-fatal-error-pythonh-no-such.html)
+ [The official guide for setting up Google Drive Domain-wide Service Account didn't work?](http://iambusychangingtheworld.blogspot.com/2013/12/google-drive-api-how-work-with-domain.html)
+ [_csv.Error: Could not determine delimiter](http://iambusychangingtheworld.blogspot.com/2013/12/python-csv-error-when-read-data-from.html)


# References


* [*https://developers.google.com/drive/quickstart-python*](https://developers.google.com/drive/quickstart-python)
* [*https://developers.google.com/drive/v2/reference/*](https://developers.google.com/drive/v2/reference/)


# Contact 

Email: mail@mschnitzius.com
Twitter: [@marcschnitzius](https://twitter.com/marcschnitzius)


This is a fork of https://github.com/dangtrinh. Thanks for your job :)
+ Email: dangtrinhnt[at]gmail[dot]com - Trinh Nguyen

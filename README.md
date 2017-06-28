# OSX-Keychain-Internet-Password-Importer
A Python script that imports a CSV into Mac OSX Keychain

Some assumptions here,

You have Python 3 installed<br>
You're running Mac OS 10.12.5 +<br>
You can use the terminal<br>
Your data is in the format laid out in **example_password_list.csv**<br>
Your passwords are not encrypted<br>
These passwords don't exist in your keychain, **IF THEY DO, THEY'LL BE UPDATED**

<Br><br><br>

**`If the password exists it will be UPDATED, you've been warned`**


<br><br><br>

**Chrome users**

You need to enable the _Password import and export_ flag in _chrome://flags_ once that's done you can export your none encrypted passwords by going to _chrome://settings-frame/passwords_ and pressing the export button.

<br><br>

Once that's done you can go ahead and run the google_import.py script.
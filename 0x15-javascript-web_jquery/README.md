# 0x15. JavaScript - Web jQuery
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

## Resources

**Read or watch**:

-   [What is JavaScript?](https://intranet.hbtn.io/rltoken/FBd59d6M-Bal5PiSJbhw9g "What is JavaScript?")
-   [Selector](https://intranet.hbtn.io/rltoken/RtFB5Ycdvvk5OYv79zgr6A "Selector")
-   [Get and set content](https://intranet.hbtn.io/rltoken/JAC2vdSj1pbH6y_9OwQrAw "Get and set content")
-   [Manipulate CSS classes](https://intranet.hbtn.io/rltoken/Pvl_U4kdmxtHrZAHoFh_qw "Manipulate CSS classes")
-   [Manipulate DOM elements](https://intranet.hbtn.io/rltoken/fA1R3S7dNUX4lj68z6qMyw "Manipulate DOM elements")
-   [API](https://intranet.hbtn.io/rltoken/w_Y67Y3UlGQ6nluZx9KJyQ "API")
-   [Introduction](https://intranet.hbtn.io/rltoken/LOMQvsml-4ttg2Y2TVNbqQ "Introduction")
-   [GET & POST request](https://intranet.hbtn.io/rltoken/xN81Z76ZeNgB42tyJOgXjA "GET & POST request")
-   [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.hbtn.io/rltoken/Rq2Ob5rhN-N458YBxxaRXQ "JQuery Ajax Tutorial #1 - Using AJAX & API's")
-   [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/ZpjZXl5AxHmurQFuxQfB4A "What went wrong? Troubleshooting JavaScript")
-   [JQuery](https://intranet.hbtn.io/rltoken/L5nA7F44DBhrCAdlEvxrqQ "JQuery")
-   [JQuery API](https://intranet.hbtn.io/rltoken/U3XGm3WaMxON5c-NkBFS6Q "JQuery API")
-   [JQuery Ajax](https://intranet.hbtn.io/rltoken/pZmSwUxd65dxIrX7D4n1pg "JQuery Ajax")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/AsDSdFtLBtgOAoSNFE7QIQ "explain to anyone"),  **without the help of Google**:

### General

-   Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
-   How to select HTML elements in JavaScript
-   How to select HTML elements with JQuery
-   What are differences between  `ID`,  `class`  and  `tag name`  selectors
-   How to modify an HTML element style
-   How to get and update an HTML element content
-   How to modify the DOM
-   How to make a  `GET`  request with JQuery Ajax
-   How to make a  `POST`  request with JQuery Ajax
-   How to listen/bind to DOM events
-   How to listen/bind to user events

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Chrome (version 57.0)
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be  `semistandard`  compliant with the flag  `--global $`:  `semistandard *.js --global $`
-   You must use JQuery version 3.x
-   You are not allowed to use  `var`
-   HTML should not reload for each action: DOM manipulation, update values, fetch data…

## More Info

### Import JQuery

```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

```

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

### Manual QA Review

**It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

## Quiz questions

Show

## Tasks

### 0. No JQuery

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You must use  `document.querySelector`  to select the HTML tag
-   You can’t use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `0-script.js`


### 1. With JQuery


Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `1-script.js`

### 2. Click and turn red

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`) when the user clicks on the tag  `DIV#red_header`:

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `2-script.js`

### 3. Add `.red` class

Write a JavaScript script that adds the class  `red`  to the  `<header>`  element when the user clicks on the tag  `DIV#red_header`

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `3-script.js`

### 4. Toggle classes


Write a JavaScript script that toggles the class of the  `<header>`  element when the user clicks on the tag  `DIV#toggle_header`:

-   The  `<header>`  element must always have one class:  `red`  or  `green`, never both in the same time and never empty.
-   If the current class is  `red`, when the user click on  `DIV#toggle_header`, the class must be updated to  `green`  ; and the reverse.
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `4-script.js`

### 5. List of elements


Write a JavaScript script that adds a  `<li>`  element to a list when the user clicks on the tag  `DIV#add_item`:

-   The new element must be:  `<li>Item</li>`
-   The new element must be added to  `UL.my_list`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `5-script.js`

### 6. Change the text

Write a JavaScript script that updates the text of the  `<header>`  element to  `New Header!!!`  when the user clicks on  `DIV#update_header`

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `6-script.js`

### 7. Star wars character

Write a JavaScript script that fetches the character  `name`  from this URL:  `https://swapi-api.hbtn.io/api/people/5/?format=json`

-   The name must be displayed in the HTML tag  `DIV#character`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `7-script.js`


### 8. Star Wars movies


Write a JavaScript script that fetches and lists the  `title`  for all movies by using this URL:  `https://swapi-api.hbtn.io/api/films/?format=json`

-   All movie titles must be list in the HTML tag  `UL#list_movies`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `8-script.js`

### 9. Say Hello!

Write a JavaScript script that fetches from  `https://fourtonfish.com/hellosalut/?lang=fr`  and displays the value of  `hello`  from that fetch in the HTML tag  `DIV#hello`.

-   The translation of “hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   Your script must work when it is imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `9-script.js`


### 10. No jQuery - document loaded

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You must use  `document.querySelector`  to select the HTML tag
-   You can’t use the jQuery API
-   Note: Your script must be imported from the  `<head>`  tag, not at the end of the HTML

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `100-script.js`


### 11. List, add, remove

Write a JavaScript script that adds, removes and clears  `LI`  elements from a list when the user clicks:

-   The new element must be:  `<li>Item</li>`
-   The new element must be added to  `UL.my_list`
-   When the user clicks on  `DIV#add_item`: a new element is added to the list
-   When the user clicks on  `DIV#remove_item`: the last element is removed from the list
-   When the user clicks on  `DIV#clear_list`: all elements of the list are removed
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when it imported from the  `HEAD`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `101-script.js`

### 12. Say hello to everybody!

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service:  `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag  `INPUT#language_code`  (ex:  `es`,  `fr`,  `en`  etc.)
-   The translation must be fetched when the user clicks on  `INPUT#btn_translate`
-   The translation of “Hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `102-script.js`

### 13. And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service:  `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag  `INPUT#language_code`  (ex:  `es`,  `fr`,  `en`  etc.)
-   The translation must be fetched when the user clicks on  `INPUT#btn_translate`  OR presses  `ENTER`  when the focus is on  `INPUT#language_code`
-   The translation of “Hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

-   File:  `103-script.js`

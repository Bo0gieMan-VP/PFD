<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server">
    <img src="images/logo.png" alt="Logo" width="600" height="auto">
  </a>

<h3 align="center">Pink Floyd Discography Server</h3>

  <p align="center">
    Studential Project of Pink Floyd's Discography
    <br />
    <br />
    <a href="https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server">View Demo</a>
    ·
    <a href="https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/issues">Report Bug</a>
    ·
    <a href="https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#commands">Commands</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
  <img src="images/client-screen.jpg" alt="Screenshot of the program">

Socket based project, Server-side that can give information about Pink Floyd <br />
On the Client-side the client can use commands to get the information from the server<br />
</div>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
* [LyricsGenius](https://pypi.org/project/lyricsgenius/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### STEP 1
When running the server for the first time the server will start building it's database<br />
This will take some time

<img src="images/step-1.jpg">

### STEP 2
When the server is done building it's database it will notify

<img src="images/step-2.jpg">

### STEP 3
Start the client's window and insert the server's IP address.<br />
_if the server running on the same PC you can use `my_ip`_

<img src="images/step-3.jpg">

### STEP 4
Now that you can see the welcome screen you're good to go!<br />
_remember, if you don't know what you do you can always type `HELP`_

<img src="images/step-4.jpg">

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- COMMANDS -->
## Commands

### User Commands
| Command   |   Argument   |   Description   |
|:----------|:------------:|:----------------|
| **GETALBUMS** |  None| Get a list of Pink Floyd's albums|
| **FINDALBUM** | Name of Album | Find whether an album is Pink Floyd's |
| **ALBUMDUR** | Name of Album | Get the total length of an album |
| **LISTSONGS** | Name of Album | Get a list of all the songs in the album |
| **FINDSONG** | Name of Song | Find whether a song is Pink Floyd's, if yes, you'll see it's album |
| **HOWLONG** | Name of Song | Get the song's length |
| **GETLYRICS** | Name of Song | Get the song's lyrics |
| **FINDLYRICS** | Lyrics | Find songs containing the specified lyrics (can be more than one word) |
| **GOADMIN** | Password | Get Administrator Privileges |


### Admin Commands
| Command   |   Description   |
|:----------|:----------------|
| **UPDATE** | Update the server's database |
| **SHUTDOWN** | Shut the server down |
| **SCLEAR** | Clear the server's window |
| **GOUSER** | Get User Privileges |


### Utility Commands
| Command   |   Description   |
|:----------|:----------------|
| **CLEAR** | Clear the client's window |
| **QUIT** | Kill the connection and exit the program |

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Benny Kerido - kerido112@gmail.com

Project Link: [https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server](https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Bo0gieMan-VP/Pink_Floyd_Discography_Server.svg?style=for-the-badge
[contributors-url]: https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Bo0gieMan-VP/Pink_Floyd_Discography_Server.svg?style=for-the-badge
[forks-url]: https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/network/members
[stars-shield]: https://img.shields.io/github/stars/Bo0gieMan-VP/Pink_Floyd_Discography_Server.svg?style=for-the-badge
[stars-url]: https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/stargazers
[issues-shield]: https://img.shields.io/github/issues/Bo0gieMan-VP/Pink_Floyd_Discography_Server.svg?style=for-the-badge
[issues-url]: https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/issues
[license-shield]: https://img.shields.io/github/license/Bo0gieMan-VP/Pink_Floyd_Discography_Server.svg?style=for-the-badge
[license-url]: https://github.com/Bo0gieMan-VP/Pink_Floyd_Discography_Server/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/bennykerido/
[product-screenshot]: images/client-screen.jpg

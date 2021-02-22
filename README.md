<!--

*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![GitHub forks](https://img.shields.io/github/forks/EconoBen/headsdown)](https://github.com/EconoBen/headsdown/network)
[![GitHub stars](https://img.shields.io/github/stars/EconoBen/headsdown)](https://github.com/EconoBen/headsdown/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/EconoBen/headsdown)](https://github.com/EconoBen/headsdown/issues)
[![GitHub license](https://img.shields.io/github/license/EconoBen/headsdown)](https://github.com/EconoBen/headsdown/blob/main/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://www.twitter.com/EconoBen)
[![LinkedIn](https://img.shields.io/linkedin/url?style=social)](https://www.linkedin.com/in/benjamin-labaschin)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="images/logo.png" title="Logo">
  <h3 align="center">Heads Down</h3>

  <p align="center">
    A Mac app that lives in your ribbon—with a click of the mouse, temporarily block distracting websites and applications to encourage "heads down" time.
    <br />
    <br />
    <a href="https://github.com/EconoBen/headsdown/issues">Report Bug</a>
    ·
    <a href="https://github.com/EconoBen/headsdown/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
  <p align="left">
  This project was inspired by a tweet.
  <br />
  <p align="left">
  The person in question had a simple request: how can I block distracting apps and websites when I'm trying to work?
  <br />
  <p align="left">
  With Heads Down, you can easily block and unblock websites and apps with a click of the mouse.
  <br />

### Built With

* [rumps](https://github.com/jaredks/rumps)
* [py2app](https://pypi.org/project/py2app/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* git
* pip
* python

### Installation

1. Clone the repo
    ```sh
    https://github.com/EconoBen/headsdown.git
    ```
2. Change the directory
    ```sh
    cd headsdown/
    ```
3. Install the required libraries
    ```sh
    pip install -r requirements.txt
    ```
4. Install Heads Down
    ```sh
    python setup.py py2app --iconfile images/icon.icns
    ```
5. Move the Heads Down app to your Applications folder
    ```sh
    mv dist/headsdown.app /Applications
    ```

<!-- USAGE EXAMPLES -->
## Usage

![](images/Heads_Down.gif)

<p align="left">
Heads down comes with a list of predefined social media websites to block (see
<a href="https://github.com/EconoBen/headsdown/blob/main/block_sites.csv">block_sites.csv</a>). To add to the block list, simply select the "block sites" button and a popup window in which to add websites will appear.
<br />
<p align="left">
To begin a work session, simply cick on the "Heads Down" button. When you're done, select "Heads Up". It's that easy.
<br />


<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EconoBen/headsdown/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@econoben](https://twitter.com/econoben) - benjaminlabaschin@gmail.com

Project Link: [https://github.com/EconoBen/headsdown](https://github.com/EconoBen/headsdown)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


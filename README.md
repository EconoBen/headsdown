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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
    ![](images/icon.png)
  <h3 align="center">Heads Down</h3>

  <p align="center">
    A Mac app that lives in your ribbon—with a click of the mouse, temporarily block distracting websites and applications to encourage "heads down" time.
    <br />
    <a href="https://github.com/EconoBen/headsdown"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EconoBen/headsdown">View Demo</a>
    ·
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

![](Heads_Down.gif)

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
[contributors-shield]: https://img.shields.io/github/contributors/EconoBen/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/EconoBen/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EconoBen/repo.svg?style=for-the-badge
[forks-url]: https://github.com/EconoBen/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/EconoBen/repo.svg?style=for-the-badge
[stars-url]: https://github.com/EconoBen/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/EconoBen/repo.svg?style=for-the-badge
[issues-url]: https://github.com/EconoBen/repo/issues
[license-shield]: https://img.shields.io/github/license/EconoBen/repo.svg?style=for-the-badge
[license-url]: https://github.com/EconoBen/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/EconoBen
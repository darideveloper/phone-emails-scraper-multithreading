<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".****
*** Don't forget to give the project a star!****
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Fiverr][fiverr-shield]][fiverr-url]
[![Gmail][gmail-shield]][gmail-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darideveloper/europeanstartups_scraper">
    <img src="imgs/logo.png" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">Phone Emails Scraper Multithreading</h3>

  <p align="center">
    Project for extract emails and phones from a list of web pages, with multithreading, using requests, bs4, regex and selenium for get more data.
    <br />
    <a href="https://github.com/darideveloper/europeanstartups_scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/darideveloper/europeanstartups_scraper/issues">Request Feature</a>
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

This project is for extract emails and phones from a list of web pages, with multithreading, using requests, bs4, regex and selenium for get more data.

The script extract emails and phones from the web pages in the `input .txt` file, and save the output in the `output.csv` file.

The script use multithreading for extract data from the web pages faster.

The script use selenium (google chrome) for get more data from the web pages, because some web pages use javascript to show the data. You can use or not it (see the `USE_SELENIUM` variable in the `.env` file).

You can setup the number of threads in the `.env` file (see the `THREADS` variable).

### Built With


<div>
<a href="https://www.python.org/">
  <img src="https://cdn.svgporn.com/logos/python.svg" width="50" alt="python" title="python">
</a>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/europeanstartups_scraper.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. Set your option in the file `.env`
2. Put the web pages in the `input.csv` file
3. Run the project folder with python: 
    ```sh
    python .
    ```
4. Wait until the script finish, and check the `output.csv` file in the project folder

<!-- ROADMAP -->
## Roadmap

- [x] Extract email and phone using requests and bs4
- [x] Extract email and phone using regex
- [x] Extract email and phone using selenium
- [x] Multithreading
- [x] `.env` file fro options

See the [open issues](https://github.com/darideveloper/europeanstartups_scraper/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

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

Darideveloper - [@developerdari](https://twitter.com/developerdari) - darideveloper@gmail.com.com

Project Link: [https://github.com/darideveloper/europeanstartups_scraper](https://github.com/darideveloper/europeanstartups_scraper)


<!-- MARKDOWN LINKS & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/darideveloper/europeanstartups_scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[forks-url]: https://github.com/darideveloper/europeanstartups_scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[stars-url]: https://github.com/darideveloper/europeanstartups_scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[issues-url]: https://github.com/darideveloper/europeanstartups_scraper/issues
[license-shield]: https://img.shields.io/github/license/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[license-url]: https://github.com/darideveloper/europeanstartups_scraper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/
[product-screenshot]: ./imgs/screenshot.gif
[gmail-url]: mailto:darideveloper@gmail.com
[fiverr-url]: https://www.fiverr.com/darideveloper
[gmail-shield]: https://img.shields.io/badge/-gmail-black.svg?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[fiverr-shield]: https://img.shields.io/badge/-fiverr-black.svg?style=for-the-badge&logo=fiverr&colorB=555&logoColor=white

<span>Last code update: <time datetime="2022-11-29" class="last-update">2023-01-06</time>

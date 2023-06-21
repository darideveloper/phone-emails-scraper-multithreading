<div><a href='https://github.com/darideveloper/phone-emails-scraper-multithreading/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/phone-emails-scraper-multithreading.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/phone-emails-scraper-multithreading/raw/master/imgs/logo.png' alt='Phone Emails Scraper Multithreading' height='80px'/>

# Phone Emails Scraper Multithreading

Project for extract emails and phones from a list of web pages, with multithreading, using requests, bs4, regex and selenium for get more data.

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a><a href='https://www.crummy.com/software/BeautifulSoup/' target='_blank'> <img src='https://github.com/darideveloper/darideveloper/blob/main/imgs/logo%20bs4.png?raw=true' alt='BeautifulSoup4' title='BeautifulSoup4' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

This project is for extract emails and phones from a list of web pages, with multithreading, using requests, bs4, regex and selenium for get more data.

The script extract emails and phones from the web pages in the `input .txt` file, and save the output in the `output.csv` file.

The script use multithreading for extract data from the web pages faster.

The script use selenium (google chrome) for get more data from the web pages, because some web pages use javascript to show the data. You can use or not it (see the `USE_SELENIUM` variable in the `.env` file).

You can setup the number of threads in the `.env` file (see the `THREADS` variable).

# Install

## Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/phone-emails-scraper-multithreading
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```

# Settings

1. Set your option in the file `.env`
2. Put the web pages in the `input.csv` file

# Run

1. Run the project folder with python: 
    ```sh
    python .
    ```
2. Wait until the script finish, and check the `output.csv` file in the project folder

# Roadmap

- [x] Extract email and phone using requests and bs4
- [x] Extract email and phone using regex
- [x] Extract email and phone using selenium
- [x] Multithreading
- [x] `.env` file for options


**MyEntergy-API**
================

Open Source API for MyEntergy Advanced Meters to pull there "live" usage.

**Table of Contents**
-----------------

* [Getting Started](#getting-started)
* [Usage](#usage)
* [Requirements](#requirements)
* [Installation](#installation)
* [Troubleshooting](#troubleshooting)

**Getting Started**
---------------

This project is designed to pull "live" usage data from MyEntergy Advanced Meters From There Webui. To get started, follow these steps:

### Step 1: Clone the repository

```bash
git clone https://github.com/Cloud-121/MyEntergy-API
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

**Usage**
-----

To use the script, simply run the following command:

```bash
python main.py <username> <password>
```
or provide a json file named login.json with the following structure:

```json
{
    "username": ""
    "password": ""
}
```

**Requirements**
------------

* Python 3
* Selenium
* selenium_recaptcha_solver
* Firefox (for geckodriver)

**Installation**
------------

To install the required dependencies, You can use pip to install them from the requirements.txt file:

```bash
pip install -r requirements.txt
```

**Troubleshooting**
----------------

If you encounter any issues while using this project, please make a gitub issue or contact me at [https://github.com/Cloud-121](https://github.com/Cloud-121).

**Contributing**
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. I will be happy to have help in fixing this horrible code :3

**License**
-------

This project is licensed under the [GPL-3.0 license](LICENSE.md).
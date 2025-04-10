# Quoternator

**Quoternator** is an open-source project that retrieves a new quote each day and amends [QUOTE.md](QUOTE.md) with the new quote, author and a time stamp. You can see an example of this, by heading to the file within this repo, the quote updates each day at midnight.

## Features

- Randomised Quote each day.
- Workflow automation.

## Requirements

- Python 3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azio0/Quoternator.git
   cd Quoternator
   ```
2. Install Python and PIP:
   ```bash
   sudo apt-get install python3
   sudo apt-get install python3-pip
   ```
4. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can directly generate a new quote by running ```app.py``` from within the ```source``` folder, or fork this repository and have the workflow automatically do it for you. 

For workflow automation to function on your repository, you must create an ```actions secret``` named ```PAT``` with the value of a personal access token that has write permissions on the repository.

## Configuration

There is a ```config.yml``` file that contains the URL from where these quotes are generated, you are able to change this however, please note if the json return differs from the original source, then the project's codebase will need to be updated to ensure usability.

## Contributing

This is an open-source project, and contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

## Donations

This project is intended to be open-source and free from cost to use. I love coding, setting a target and accomplishing it, sometimes by using pre-existing technology or creating an original approach to a problem. It excites me and gives me a sense of purpose, but it is not always easy to find the time or motivation to keep pushing forward. Donations are welcome if you wish to give something towards the work I do, but it is completely optional and is certainly not a requirement.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/azio0)

# HoneypotFTP

HoneypotFTP is a python based application that acts as an FTP server - except that it's fake. It let's clients to connect to its open service, can provide file listing - everything that a basic FTP server can do. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- [ ] **Simple installation**: Configure a simple JSON file, or use the reasonable defaults
- [ ] **Detailed logging**: Creates a separate log file for each connection, and logs every command provided by the connection
- [ ] **Reporting capabilities**: Based on the log files, most known report formats(XML,JSON,CSv) are available
- [ ] **Fake file structure**: dynamic folder structure creation, based on the configuration options
- [ ] **Username restriction**: Can be configured to accept every connection(even anonymous login), or restrict to some username-password pairs

## Installation

### Prerequisites

Before installing HoneypotFTP, make sure you have the following installed:

- **Python3** (3.12 or higher)
- **Open port for data and communication** HoneypotFTP recommends open ports if the given ports are closed.

### Step-by-Step Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tiborscholtz/HoneypotFTP
    ```

2. Navigate to the project directory:

    ```bash
    cd HoneypotFTP
    ```

3. Install the required environment plugins, using the following command:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the application, using the following command:

    ```bash
    python3 .
    ```

That's it! HoneypotFTP should now be running, and ready to accept connection!.

## Usage

Once HoneypotFTP is running, it waits for incoming connections, and gives readable output on the terminal about the current activies, like: login, file download request, file listing.

### Commands & Options

Coming soon!

## Configuration

Coming soon!

## Contributing

We welcome contributions to HoneypotFTP! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and write tests (if necessary).
4. Submit a pull request.

Before contributing, please ensure that your changes adhere to the existing code style and pass all tests.

### Reporting Issues

If you encounter any bugs or issues, please open an issue on the GitHub repository. Include detailed information about the problem, including:

- Your operating system version
- Python version
- Steps to reproduce the issue
- Any error messages or logs

## License

HoneypotFTP is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contact

- **Author**: [tiborscholtz](https://github.com/tiborscholtz)
- **GitHub**: [https://github.com/tiborscholtz/HoneypotFTP](https://github.com/tiborscholtz/HoneypotFTP)

---
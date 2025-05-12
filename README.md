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

- [x] **Simple installation**: Configure a simple JSON file, or use the reasonable defaults
- [x] **Detailed logging**: Creates a separate log file for each connection, and logs every command provided by the connection
- [x] **Fake file structure**: dynamic folder structure creation, based on the configuration options
- [ ] **Reporting capabilities**: Based on the log files, most known report formats(XML,JSON,CSV) are available
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

3. Start the application, using the following command:

    ```bash
    python3 .
    ```

That's it! HoneypotFTP should now be running, and ready to accept connection!.

## Usage

Once HoneypotFTP is running, it waits for incoming connections, and gives readable output on the terminal about the current activies, like: login, file download request, file listing.

### Commands & Options

Coming soon!

## Configuration

The server relies on a valid json file, which looks like this:

```json
{
    "server_type":"default",
    "command_port":8892,
    "filesystem_depth":3,
    "average_entity_per_directory":10,
    "file_ratio":0.8,
    "directory_ratio":0.2,
    "logging":true,
    "allowed_users":50,
    "extended_log_on_disconnect":true,
    "modification_minutes_from":20,
    "modification_minutes_to":500,
    "file_byte_size_min":1000,
    "file_byte_size_max":50000,
    "different_structure_per_client":false
}
```

**server_type**  

It gives the option to change from one server response type to another. Currently, only `default` is supported.

**command_port**  

The default port used to exchange commands between the client and the server.

**filesystem_depth**:  

Indicates that how deep should be the fake file structure. An example with a filesystem_depth of 3:

```md
/ (root)
├── documents/
│   ├── Project_Phoenix_Blueprints.pdf
│   ├── Secret_Meeting_Notes.docx
│   ├── ToDo_List_2025.txt
├── media/
│   ├── photos/
│   │   ├── Launch_Event_2024.jpg
│   │   ├── Prototype_SneakPeek.png
│   ├── videos/
│   │   ├── Drone_Footage_TestRun.mp4
│   │   ├── Hologram_Demo_Reveal.mov
├── archives/
│   ├── Old_Projects/
│   │   ├── SkyNet_v1.0.zip
│   │   ├── OceanX_MissionLogs.tar.gz
│   ├── Legal/
│   │   ├── NDA_Clients_Confidential.pdf
│   │   ├── Lawsuit_Documents_2023.docx
├── system/
│   ├── config/
│   │   ├── server_settings_backup.json
│   │   ├── user_roles_legacy.ini
│   ├── logs/
│   │   ├── auth_failures.log
│   │   ├── backup_success_04252025.log
├── README_FIRST.txt
├── hidden/.flag_secret_hidden.txt
```

**average_entity_per_directory**:  

The application generates fake files under each directory. The variables defines that how many directory/file should exists inside one directory.

**file_ratio**:  

The valid range of this value is between 0 and 1. It represents the percentage of files inside one directory.

**directory_ratio**:  

The valid range of this valud is between 0 and 1. It represensts the percentage of directories inside one directory.

**logging**:  

If it is set to `true`, the application creates a log file for each connection, and logs the client's activities.

**allowed_users**(work in progress):  

The amount of connected users allowed at one time.

**extended_log_on_disconnect**:  

When set to true, after the client disconnects, the server creates log files on most known(CSV,JSON,XML) file formats, with the same file name.

**modification_minutes_from** and **modification_minutes_to**:  

Since this server does not serve real files, at the start of each session, the server grabs the current time. You can create fake modification time based on the current time. For example, if the current time is `2025-04-26 17:00:00`, `modification_minutes_from` has the value of 2, and `modification_minutes_to` has the value of 10, one file's modification time can range from `2025-04-26 16:50:00` to `2025-04-26 16:58:00`.

**file_byte_size_min** and **file_byte_size_max**:  

Since this server does not serve real files, at the start of each session the server calculates sime made-up size for each file. You can control the amount of bytes written to each file with these parameters.

**different_structure_per_client**:  

If set to `True`, the server creates a different file structure for each connected client. Otherwise, it uses the same for every client.


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
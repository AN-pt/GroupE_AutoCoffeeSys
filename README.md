# AutoCafé

AutoCafé is a cafe management application that aims to bring efficiency and convenience to privately-owned coffee shops, especially the smaller ones. With this automation in place, coffee shops can bid farewell to paper-based chaos and manual order management.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [External Dependencies](#external-dependencies)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

The Cafe Management application has the following features:

- Customer authentication using face recognition (still working on this)
- Real-time item management for coffee shop resources
- Create, manage and export order records from selling products and receipts from buying ingredients into Excel (still working on this)
- Generate reports on sales, inventory and other metrics.

## Getting Started

### Prerequisites

Before running this project, you need to have the following installed:

- Python 3 (Version 3.11 or higher)
- MySQL Community Server (Version 8.0 or higher)

*Note: having basic knowledge of MySQL and Python will make running this project much easier. If you are unfamiliar with either, YouTube is a good resource to get practice first.

### Installation

To install the Cafe Management application, follow these steps:

1. Clone the repository to your local machine **(VSCode highly recommended)**.
        ```
        git clone https://github.com/quangduy201/cafe-application.git
        ```

2. Open a terminal at the project folder and run `python setup.py`.

3. Install the required dependencies:
        ```
        pip install -r requirements.txt
        ```

4. Create a MySQL database schema named `cafe_management` and run the SQL file located at `cafe_application/database/cafe_db.sql`.

5. Configure the MySQL class located at `cafe_application/src/DAL/MySQL.py` to connect to your MySQL database.

6. Build the project and run the `CafeManagement` class located at `cafe_application/src/main/CafeApplication.py`.

## Usage

To use the Cafe Management application, follow these steps:

1. Log in with a default account: `username='admin'`, `password='admin'`.

2. Use the GUI to manage items, orders, and receipts.

### Disclaimer: This function is still under development.
3.	Click the "DETECTION" button to try out the face recognition for customer authentication. 
   
## Contributors

The following people have contributed to the AutoCafé:

- Amani Nelson (developed the database and system from translating the original Vietnamese)
- Vitou Prim (developed UI for the app)
- Menghengleap Chhin (created user and system documentation)

## External Dependencies

To see the dependencies required by this project, refer to the `requirements.txt` file.

## Acknowledgements

We would like to acknowledge the Vietnamese developers who originally created the foundation for this project. Their work was instrumental in making this project possible.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

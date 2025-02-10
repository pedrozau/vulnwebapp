# Vulnerable Applications Showcase

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents
- Introduction
- Features
- Getting Started
- Usage
- Available Applications
- Technologies Used
- Contributing
- License
- Contact

## Introduction

This project showcases a collection of intentionally vulnerable web applications. It's designed for educational purposes, allowing security professionals and enthusiasts to practice and improve their penetration testing skills.

## Features

- Multiple Vulnerable Apps: A variety of applications with different vulnerabilities (e.g., SQL Injection, XSS, CSRF).
- Docker Setup: Easy deployment using Docker, allowing quick setup and teardown of environments.
- User-Friendly Interface: A Flask-based web application to access and manage these vulnerable apps.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Docker installed on your machine.
- Basic knowledge of Docker and web security concepts.

### Installation

1. Clone the repository:

   git clone https://github.com/pedrozau/vulnwebapp.git

2. Navigate to the project directory:

   cd vulnerable-apps

3. Start the applications:

   docker-compose up

## Usage

Once the applications are running, visit the following URLs to access each vulnerable app:

- DVWA: http://localhost:8081
- Juice Shop: http://localhost:8082
- Mutillidae: http://localhost:8083
- WebGoat: http://localhost:8084
- bWAPP: http://localhost:8085
- Hackazon: http://localhost:8086
- XVWA: http://localhost:8087

## Available Applications

| Application  | Description                   | Port   |
|--------------|-------------------------------|--------|
| DVWA         | Damn Vulnerable Web App       | 8081   |
| Juice Shop   | An OWASP project for web apps | 8082   |
| Mutillidae   | Another vulnerable web app     | 8083   |
| WebGoat      | Teaching web application security| 8084   |
| bWAPP        | Buggy Web Application          | 8085   |
| Hackazon     | A vulnerable e-commerce site   | 8086   |
| XVWA         | Xtreme Vulnerable Web App      | 8087   |

## Technologies Used

- Flask for the web interface
- Docker for containerization
- Various vulnerable web applications

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

## License

Distributed under the MIT License. See LICENSE for more information.

## Contact

Your Name - pedrozau28@gmail.com

Project Link: https://github.com/pedrozau/vulnwebapp/

Sub-Domain Reconnaissance Tool
This Python script is designed to perform reconnaissance on a given domain name that includes retrieving sub-domains, IP addresses, open ports, web page titles, web server versions, web-framework versions, and programming language versions for each identified sub-domain.

## Installation
Before running this script on your system, you need to ensure that you have the required libraries and tools installed.

## Prerequisites
The following libraries/tools must be installed for the script to work:

```
* Python3
* Python3-pip
* dns.resolver
* requests
* numpy
* urllib3
* Beautiful Soup 4
* whatweb 0.5.1 version
* nmap
```

# Debian/Ubuntu
On Debian-based systems, you can install the required libraries/tools using the following commands:

```
* sudo apt update
* sudo apt install python3 python3-pip
* sudo python3 -m pip install numpy requests urllib3 bs4
* sudo snap install whatweb
* sudo apt install nmap
```

# Red Hat
On Red Hat-based systems, you can install the required libraries/tools using the following commands:

```
* sudo yum install python3 python3-pip
* sudo python3 -m pip install numpy requests urllib3 bs4
* sudo dnf install whatweb
* sudo yum install nmap
```

# Usage
Once you have installed the required libraries and tools, you can run the script using the following command:

```
python3 sub-recon.py
```

The script will prompt you to enter the domain name for which you want to perform reconnaissance. Once you enter the domain name, the script will automatically retrieve sub-domains, IP addresses, open ports, web page titles, web server versions, web-framework versions, and programming language versions for each identified sub-domain.

Note: It's important to obtain necessary authorizations before using it against any domain.

# Contribution
```
OpenAvijeh welcomes everyone who is interested in improving the tool to contribute. For any issues, suggestions or contribution, feel free to open an issue or pull request in the repository.
```

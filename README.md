# rwc-python-api

This is python library to control RWC5020x LoRa Tester remotely through either serial
(RS232) or ethernet port.

## Requirements

- [Python3.*](https://www.python.org/downloads/)
- [PySerial](https://pypi.org/project/pyserial/)

## API Setup

![Python API Setup](doc/build/html/_images/API_Setup.jpg)

- To access RWC5020x tester using Python Library, please follow the setup shown in the diagram.

## How to install the package

1.  clone the repository from [github](https://github.com/mcci-catena/rwc-python-api)
2.  Open terminal in PC
3.  Go to /[path_to_repository]/rwc-python-api/
4.  To install, enter the command `python setup.py install`

## How to use the package

Create a python file and import the class library from package:

     from rwclib.cRWC5020x import RWCTesterApi

Create a class object and pass serial port or ethernet port & ip address as constructor parameter

     #Serial Communication
     ob = RWCTesterApi('COM5') #windows
     (or)
     ob = RWCTesterApi('/dev/ttyUSB0') #Linux
     (or)
     #Ethernet Communication
     ob = RWCTesterApi('5001', '192.168.0.33')
     
Access the class methods using instantiated object

     ob.query_identification()
     
To know more about class methods, please see the **code documentation** in the following location in cloned repository:

*/[path_to_repository]/rwc-python-api/doc/build/html/index.html*

Example scripts to access the library has been placed [here](https://github.com/mcci-catena/rwc-python-api/tree/master/examples) for your reference.

## Support

Python library supports RWC5020A firmware software from v1.150 to latest version.
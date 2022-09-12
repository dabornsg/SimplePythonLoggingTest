# Simple Python Logging Test

Small repository for testing Python's logging module. Run textstack.py for a command-line program to add strings to stack. Logs various errors to a .log file.

## Installing

Clone the repository and run `textstack.py` with Python3.0 or later. No additional modules are needed to run.

## How to use

Run `textstack.py` with Python in any folder where you have write permissions. It will need this to create the `.log` file. It'll run as a console application.

When running `textstack.py`, information will be logged in `textstack.log`. Only INFO and ERROR messages are expected to appear in log.

Running `textstack_test.py` will run a small unit test on the `TextStack` class defined in `textstack.py`. Errors and info will be logged on `textstack_test.log`. On a normal run, 6 errors are expected to be found (No items available for getting shortest/longest string, input variable is not a string, tried to push an empty string, invalid index for current TextStack: 15, and Couldn't use one or both of the following indexes: 15, 23). They are expected and the lack of these means that the class is not correctly catching some errors.

## Contributing

Feel free to send Pull Requests of whatever you feel is lacking or any bugs you may find. However, make sure the following applies to the request:

1. Your request is up-to-date with the latest commit.
2. The request's description clearly states what is being changed or added.
3. Changes to the base class should pass the unit test without any extra errors.
4. New features to the base class should have a test associated with them.


## License
- - -
MIT License

Copyright (c) [2022] [Daniel Bornscheuer]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

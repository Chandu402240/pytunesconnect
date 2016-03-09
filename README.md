# pytunesconnect

pytunesconnect is some Python code (not quite a library) that enables programatic access to *Sales and Trends* and *App Analytics* data from Apple's iTunes Connect platform.

Although independent work, it was significantly helped along by [node-itunesconnect](https://github.com/stoprocent/node-itunesconnect), which does the same (and more) for node.js (much kudos to those who worked on that). Also worth mentioning is [Spaceship](https://spaceship.airforce/), which is the same (and more) for Ruby (see also their [GitHub repo](https://github.com/fastlane/fastlane/tree/master/spaceship)).
## Why?

* iTunes Connect doesn't provide all of the querying functionality that a developer might like (that's not a criticism of iTunes Connect - it can't be all things to all men)
* Downloading data to CSV before it can be mashed with other data sources is time-consuming
* Dashboards that combine multiple data sources
* Organizations should own their own data, and intermediaries such as Apple *should* provide a full API (which is fully documented)

## What you need

An iTunes Connect account (email & password), with access to the modules that you want to access, such as *App Analytics*, *Sales and Trends* and *Payments and Financial Reports*.

To access earnings reports you also need a *contentProviderId* and *vendornumber*. The vendor number can be found in the *Payments and Financial Reports* web interface to iTunes Connect. Both the contentProviderId and vendornumber can be obtained programmatically through pytunesconnect.

And Python.

## Setup

1. Install Python
2. Install dependencies (requests, lxml):
   ```pip install requests```
   ```pip install lxml```
3. Download the code
4. Open `examples.py` in your Python interpreter
5. Point it to your credentials file*
6. Run some of the examples and see what you get

\* `examples.py` is set up to use a `.json` file with the following contents:

```json
{
  "accounts": [
    {
      "accountName": "<your email>",
      "password": "<your password",
      "contentProviderId": "<your contentProviderId",
      "vendornumber": "<your vendor number>",
      "adamIds": [
        "<adamid>"
      ]
    }
  ]
}
```




## Other notes

- adamIds are not prefixed 'id' as in iTunes on the web

## To do

* Docstrings
* Test cases
* More documentation
* Error handling
* PEP8 compliance
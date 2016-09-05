## HackerEvents

[![Build Status](https://travis-ci.org/frankrousseau/hackerevents.svg?branch=master)](https://travis-ci.org/frankrousseau/hackerevents)

### Goals

The aim of this project is to provide:

* A list of upcoming events about software.
* A quick access to Call For Presentation pages.
* An ical feed of events for each country.

I started this project because I was tired to visit many websites to have basic
information about the event I was interested in. I hope it will be useful to
you. My goal is to make it a website maintained by a community, so feel free to
participate!

### How to contribute

#### Add an event

Feel free to add your events to the website. For that you just have to add a file in the folder corresponding to the event country and open a PR accordingly.

The file format is pretty simple, see an example:

```yaml
name: FOSDEM' 17
start: 2017-02-04-10:00:00
end: 2017-02-05-18:00:00
place: ULB
address: Avenue Franklin Roosevelt 50 1050 Bruxelles
link: https://fosdem.org/
cfp: https://fosdem.org/2017/news/2016-07-20-call-for-participation/
```

To name the file simply follow this convention: `*YYYYMMDD*-*event-name*.yml`

Example: `20170204-fosdem.yml`

The file is located at `events/belgium`.

Once your event added, the website will be rebuilt. 

#### Test your changes

You can test your changes by building the website and open the generated index
file:

    python build.py
    firefox build/index.html


### Contributors

#### Code

* Nicolas (@nikaro)

#### Events

* Bryan (@chreekat)
* Shaiou (@Shaiou)
* Pierre (@pierrevdk)

### Image credits

Logo made by LSE Design: https://www.iconfinder.com/lsedesigns

# UB Hacking Website

This repository holds all of the code for the *UB Hacking* website. Its goal is
to provide a clean and consistent structure to managing and deploying the website,
and to make the lives of those involved to be that much easier!

## Development

Now, **HOPEFULLY** you aren't going to start from scratch, but are actually going
to use what we made to help you. If so, then its pretty easy to start developing!
You will just need the following involved before you begin.

#### Needed Dependencies
* `virtualenv`: Python virtual environment to containerize our code.
* `npm`: Handles most of our frontend compiling.
* `make`: To handle `Makefile`...most likely this is already installed if on Unix.

### Before You Begin

Before you can start developing, you will need to run the command below.

```bash
$ make setup
```

This will create the virtual environment, install the Python dependencies inside
of it, and then install the node dependencies. **You should never run this more
than once**.

### Handy Makefile

.select2-results__option {
  color: black;
}

.select2-container {
  margin-left: 1em;
}

.select2-selection {
  padding: 0.41667rem !important;
  background-color: rgba(254, 254, 254, 0.7) !important;

  &:hover {
    background-color: white !important;
  }
}

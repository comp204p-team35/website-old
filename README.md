COMP204P Systems Engineering
============================
The project website for UCL COMP204P Team 35.

Team Members
------------
- Ben Hadfield
- Julien Nahum
- Sim Zi Jian

Getting Started
---------------
Clone the repo to your computer and then run
```
$ gem install jekyll bundler
$ cd <path/to/cloned/repo>
$ bundle exec jekyll serve
```
This starts a lightweight server. Navigate to `http://localhost:4000` to view the site.

Editing Pages
-------------
To edit a page, open the `.md` file corresponding to that page. So to edit the testing page open `testing.md`.  

Notice that all `.md` files start with some [YAML](https://en.wikipedia.org/wiki/YAML) code surrounded by three dashes.
This gives Jekyll some information on how to render the page.  

After the YAML section, we can write the content we want to appear on the page.
This is written using the [markdown](https://guides.github.com/features/mastering-markdown/) syntax and the [Liquid Templating Language](https://jekyllrb.com/docs/templates/).  

Changes you make should be automatically detected whilst the Jekyll server is running. If, however, this doesn't work then try running
```
$ jekyll build
```
date: 2015-09-30 20:00:00+00:00
slug: wallabag-v2-alpha-finally
title: wallabag 2.0.0-alpha, finally
tags: v2, website
Status: draft

**wallabag is a read-it-later application**. Its main advantage it's open source. You know what we do with your data: nothing!

We created it in 2013, with some PHP classes.
Quickly, we saw that wallabag was technically limited (no API, database fields missing, etc.).

We decided to rewrite it from scratch, using a framework. We started this v2 many times. But we missed time.

In 2014, Jérémy Benoist ([aka @j0k3r](https://github.com/j0k3r)) joined us. He is a Symfony lead developer, so it was a great news for us.
He does a very good job. ~~~~

We think it's time to release a first version of wallabag v2. All the features from the v1 are still not developed, but we need to test it in order to continue the development.

I'm very happy with this new big step in wallabag's life: the first release of wallabag v2.

## Features already implemented

Here are the main features already implemented:

* a REST API ([you can have a look to the documentation](http://demo.wallabag.org/api/doc))
* authorization via oAuth2
* a new default theme, called `material`
* save an article, read it, favorite it, archive it. Hopefully.
* you can edit the articles title
* RSS feeds (with a limit parameter)
* create a new account from config page
* recover your password from login page (you have to fill your email on config page)

There are less features in this alpha version than in the 1.9. But we still have lot of work to do.

## Test wallabag 2.0.0-alpha

We published this alpha on our demo website: [http://v2.wallabag.org](http://v2.wallabag.org) (login wallabag, password wallabag)

Try it, and try it again. And again. There are bugs, so tell us if you found one of them (have a look [at the existing issues](https://github.com/wallabag/wallabag/issues) and [create a new one](https://github.com/wallabag/wallabag/issues/new) if necessary).

## Install wallabag 2.0.0-alpha

Keep in mind it's an **instable** branch, everything can be broken. Please don't use in production.

wallabag v2 uses [Symfony2 framework](http://symfony.com), one of the main reference in PHP development.

### via composer

```
git clone https://github.com/wallabag/wallabag.git -b v2
cd wallabag
composer install
php app/console wallabag:install
php app/console server:run
```

### via docker

### via Vagrant

## Develop third-apps by using wallabag API

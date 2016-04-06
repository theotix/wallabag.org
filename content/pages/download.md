Title: Download wallabag
Menulabel: Downloads
sortorder: 30

 * Last version: **2.0.0** (2016/04/03).
 * [Blog post about this version]({filename}/20160403-wallabag-v2.md)
 * [Need help about installation?]({filename}support.md)
 * [<i class="fa fa-github fa-lg"></i> Source code](https://github.com/wallabag/wallabag)

## Installation on a dedicated web server (recommended way)

If you don't have it yet, please [install composer](https://getcomposer.org/download/) and git.  
Then you can install wallabag by executing the following commands:

```
git clone https://github.com/wallabag/wallabag.git
cd wallabag
git checkout 2.0.0
SYMFONY_ENV=prod composer install --no-dev -o --prefer-dist
php bin/console wallabag:install --env=prod
```
[Read this documentation to create your virtual host](http://doc.wallabag.org/en/v2/user/installation.html#installing-on-apache).

## Installation on a shared hosting

We provide you a package with all dependancies inside.  
The default configuration uses SQLite for the database. If you want to change these settings, please edit `app/config/parameters.yml`.

We already created a user: login and password are `wallabag`.

<div class="alert alert-warning" markdown="1">
  <p>With this package, wallabag don't check mandatory extensions used in the application (theses checks are made during `composer install` when you have a dedicated web server, see above).  
  **[Please read our installation documentation to see requirements](http://doc.wallabag.org/en/v2/user/installation.html)**.</p>
</div>

Execute this command to download and extract the latest package: 

```
wget http://wllbg.org/latest-v2-package && tar xvf latest-v2-package
```

<small>(md5 hash of the package: `62c629d1803a159282dd3065deea9f3a`)</small>

[Read this documentation to create your virtual host](http://doc.wallabag.org/en/v2/user/installation.html#installing-on-apache).  
If you changed the database configuration to use MySQL or PostgreSQL, you need to create a user via this command `php bin/console wallabag:install --env=prod`.

## wallabag 1

  * Last version: **1.9.1** (2015/08/03).
  * [Blog post about this version]({filename}/20150803-wallabag-v1.9.1-released.md)
  * [Need help about installation?]({filename}support.md)
 * [<i class="fa fa-github fa-lg"></i> Source code](https://github.com/wallabag/wallabag/tree/master)

```
wget http://wllbg.org/latest && unzip latest
```

<small>(md5 hash of the package: `79269248d038569a49677366dae5eb77`)</small>

## Third-party applications

<div class="col-lg-12" markdown="1">
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-firefox fa-lg"></i> <strong>[Firefox](https://addons.mozilla.org/firefox/addon/wallabag-v2/)</strong>  
          <small>for wallabag v2 only</small>
        </div>
        <div class="panel-footer">Developed by Thibaud Dauce.  
        *[source code](https://github.com/ThibaudDauce/wallabag-firefox)*</div>
      </div>
  </div>
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-firefox fa-lg"></i> <strong>[Firefox](https://addons.mozilla.org/firefox/addon/wallabag/)</strong>  
          <small>for wallabag v1 only</small>
        </div>
        <div class="panel-footer">Developed by Jonathan Gaulupeau.  
        *[source code](https://github.com/wallabag/firefox-ext)*</div>
      </div>
  </div>
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-chrome fa-lg"></i> <strong>[Chrome](https://chrome.google.com/webstore/detail/wallabag/bepdcjnnkglfjehplaogpoonpffbdcdj)</strong>
        </div>
        <div class="panel-footer">Developed by Jonathan Gaulupeau.  
        *[source code](https://github.com/wallabag/chrome-ext)*</div>
      </div>
  </div>
</div>

<div class="col-lg-12" markdown="1">
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-firefox fa-lg"></i> <strong>[Firefox OS](https://github.com/wallabag/wallabag-fxos)</strong>
        </div>
        <div class="panel-footer">Developed by freddyb.  
        *[source code](https://github.com/wallabag/wallabag-fxos)*</div>
      </div>
  </div>
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-android fa-lg"></i> <strong>Android</strong>  
  		  <small>[Google Play Store](https://play.google.com/store/apps/details?id=fr.gaulupeau.apps.InThePoche) or [F-droid](https://f-droid.org/app/fr.gaulupeau.apps.InThePoche)</small>
        </div>
        <div class="panel-footer">Developed by Jonathan Gaulupeau.  
        *[source code](https://github.com/wallabag/android-app)*</div>
      </div>
  </div>
  <div class="col-lg-4">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-windows fa-lg"></i> <strong>[Windows Phone](http://apps.microsoft.com/windows/app/wallabag/f551b9c4-7346-4509-ae46-c6167c705a30)</strong>  
          <small>for wallabag v2 only</small>
        </div>
        <div class="panel-footer">Developed by Julian Oster.  
        *[source code](https://github.com/wallabag/windows-app)*</div>
      </div>
  </div>
</div>

<div class="col-lg-12" markdown="1">
  <div class="col-lg-6">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-windows fa-lg"></i> <strong>[Windows Phone](http://apps.microsoft.com/windows/app/wallabag/f551b9c4-7346-4509-ae46-c6167c705a30)</strong>  
          <small>for wallabag v1 only</small>
        </div>
        <div class="panel-footer">Developed by Julian Oster.  
        *[source code](https://github.com/wallabag/windows-app/tree/master)*</div>
      </div>
  </div>
  <div class="col-lg-6">
      <div class="panel panel-default">
        <div class="panel-body">
          <i class="fa fa-apple fa-lg"></i> <strong>[iPhone](https://itunes.apple.com/app/wallabag/id828331015?mt=8)</strong>  
        </div>
        <div class="panel-footer">Developed by Kevin Meyer.  
        *[source code](https://github.com/wallabag/ios-app)*</div>
      </div>
  </div>
</div>

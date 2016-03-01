Title: Download wallabag
Menulabel: Downloads
sortorder: 30

## wallabag 2.0.0 (beta version)

 * Last version: **2.0.0-beta.1** (2016/03/01).
 * [Blog post about this version]({filename}/20160301-wallabag-public-beta1.md)
 * [Need help about installation?]({filename}support.md)

  <a class="btn btn-info btn-lg" href="http://wllbg.org/latest-v2">Download wallabag 2.0.0-beta.1 for dedicated web server</a><br />
  (md5 hash: `eacc13770eb37f5d5006c1d1fa984dd8`)
  
    <a class="btn btn-info btn-lg" href="http://wllbg.org/latest-v2-package">Download wallabag 2.0.0-beta.1 for shared hosting</a><br />
  (md5 hash: `fdc51587f5b56c926f5dd3ef9b35daf1`)
  
### Installation

Keep in mind it's a **beta** branch, don't use it in production. 

### On a dedicated web server

If you don't have it yet, please [install composer](https://getcomposer.org/download/). Then you can install wallabag by executing the following commands:

```
SYMFONY_ENV=prod composer create-project wallabag/wallabag wallabag "2.0.0-beta.1" --no-dev
php bin/console wallabag:install --env=prod
php bin/console server:run --env=prod
```

### On a shared hosting

We provide you a package, `wallabag-2.0.0-beta.1.tar.gz`, with all dependancies inside.

The default configuration uses SQLite for the database. If you want to change these settings, please edit `app/config/parameters.yml`.

**Warning:** With this package, wallabag don't check mandatory extensions used in the application (theses checks are made during `composer create-project` when you have a dedicated web server, see above).  
**[Please read our installation documentation to see requirements](http://doc.wallabag.org/en/v2/user/installation.html)**.

* Download this file here: 
* Extract it (`tar xvf wallabag-2.0.0-beta.1.tar.gz`)
* In your wallabag folder, run `php bin/console wallabag:install --env=prod`
* Run `php bin/console server:run --env=prod`

## wallabag 1.9 (stable branch)

  * Last version: **1.9.1** (2015/08/03).
  * [Blog post about this version]({filename}/20150803-wallabag-v1.9.1-released.md)
  * [Need help about installation?]({filename}support.md)

   <a class="btn btn-info btn-lg" href="http://wllbg.org/latest">Download wallabag 1.9.1</a><br />
   (md5 hash: 79269248d038569a49677366dae5eb77)

## Third-party applications

* [extension for Firefox](https://addons.mozilla.org/firefox/addon/wallabag/) – developed by Jonathan Gaulupeau.
You have to add wallabag in your toolbar. Then, just click on this icon to save a new link.  
*[source code](https://github.com/wallabag/firefox-ext)*
* [extension for Chrome](https://chrome.google.com/webstore/detail/wallabag/bepdcjnnkglfjehplaogpoonpffbdcdj) – developed by Jonathan Gaulupeau.
You have to add wallabag in your toolbar. Then, just click on this icon to wallabag a new link.  
*[source code](https://github.com/wallabag/chrome-ext)*
* application for FirefoxOS – developed by freddyb.  
*[source code](https://github.com/wallabag/wallabag-fxos)*
* application for Android ([f-droid](https://f-droid.org/app/fr.gaulupeau.apps.InThePoche) and [google play](https://play.google.com/store/apps/details?id=fr.gaulupeau.apps.InThePoche)) – developed by Jonathan Gaulupeau.
This extension adds a wallabag icon in the share menu.  
*[source code](https://github.com/wallabag/android-app)*
* application for [Windows (8+)](http://apps.microsoft.com/windows/app/wallabag/f551b9c4-7346-4509-ae46-c6167c705a30) and [Windows Phone](http://www.windowsphone.com/s?appid=d5226cf1-f422-4e00-996c-88e9c5233332) – developed by Julian Oster.
*[source code](https://github.com/wallabag/windows-app)*
* [application for iOS](https://itunes.apple.com/app/wallabag/id828331015?mt=8) – developed by Kevin Meyer.  
*[source code](https://github.com/wallabag/ios-app)*

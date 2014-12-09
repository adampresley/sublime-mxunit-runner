Sublime Text MXUnit Test Runner
===============================

MXUnit Test Runner is a Sublime Text 2 and 3 plugin for running all unit tests for the current open test component. When you have a test CFC open and are exercising all that TDD goodness, you can simply right-click and select *Run MXUnit Tests in the Browser*. This command is also available in the Sublime command palette.

## Installation
To install this plugin you need to use git to clone the repository into your sublime packages directory.  The easiest way to find that directory is to go into sublime and select  Prefences -> Browse Packages.  That will open the directory where your packages are installed.  Then go to your shell (cmd, terminal, etc) and git clone this repository.
Once the repo is downloaded this plugin will be automatically activated.  However, you'll need to configure things on a per-project level to get it to actually work for you.  If you aren't currently using the Sublime Project feature for the project you're working on simply select the Project Menu then "Save Project As".  Once you've saved your project you'll get two new files {projectname}.sublime-project and {project-name}.sublime-workspace.

## Configuration
To use this plugin you must make use of Sublime's **Project** feature. Each project has a project file where you can setup things like what folders are in your project, as well as settings. MXUnit Test Runner makes use of the project file and expects you to have the following information configured.

```javascript
"mxunit-runner": {
    "urlPrefix": "http://localhost:8080/unittests",
    "testsDirectory": "C:\\code\\coldfusion\\myapp\\unittests",
    "additionalUrlParameters": "stuff=abc&fluff=123&"
}
```

The settings demonstrated above must go into a **settings** key in your project file. To edit your projet file simply click on the menu item named **Edit Project** found in the *Project* menu. Put it all together and it may look something like this.

```javascript
{
    "folders":
    [
        {
            "follow_symlinks": true,
            "path": "C:\\code\\coldfusion\\myapp"
        }
    ],
    "settings": {
        "mxunit-runner": {
            "urlPrefix": "http://localhost:8080/unittests",
            "testsDirectory": "C:\\code\\coldfusion\\myapp\\unittests",
            "additionalUrlParameters": "stuff=abc&fluff=123&"
        }
    }
}
```

* **urlPrefix** - This should be the base URL path where you run MXUnit tests
* **testsDirectory** - This should be the base path to where your unit tests live
* **additionalUrlParameters** - Add any additional URL-encoded parameters to be appended to the final URL. This is not usually needed


## History
* 2014-10-13
    - Created


## License
The MIT License (MIT)

Copyright (c) 2014 Adam Presley

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



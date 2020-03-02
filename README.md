# belc-dlk-api-log-archetype
This belcorp library aims to centralize api log connectors and useful functions knowledges.

#### Installation :
In this section we could download binary python executable compatible with pip, this binary is just a test library
the official library will be hosted in a official beclorp bucket. 

        python3 -m pip install belc_log --find-link=https://repository-python-archetype.s3.us-east-2.amazonaws.com/belc_log.html --no-cache-dir
        or
        pip3 install belc_log --find-link=https://repository-pythofn-archetype.s3.us-east-2.amazonaws.com/belc_log.html --no-cache-dir

#### How to Uninstall :
        python3 -m pip uninstall belc_log -y

#### Validation :
        python3 -m pip freeze
        or
        pip3 freeze

### Use Case :
In this section we are going to make an example of how to instantiate a session object. 
        
        
        from belc_log.logging_bdi import BdiService
        
        session = BdiService(env='qas',
                             app_name='arp',
                             service='product-ordering',
                             country='CL',
                             type_execution='Automatica')
                    
        session.create_session()
        session.update_session()
        session.done_session()
        session.failed_session(
             message="java.lang.javax caused by :Memory is Overhead")
        session.add_event("debug","evento_prueba",
         datetime.strptime("21/11/06 16:30","%d/%m/%y %H:%M"),
          datetime.strptime("21/11/07 16:30", "%d/%m/%y %H:%M"), DEBUG")
        
#### Test
This test was done in EMR cluster.

    >>> from belc_log.logging_bdi import LoggingBDI
    >>> a = LoggingBDI(env='qas', app_name='arp', service='product-ordering', country='CL', type_execution='Automatica')
    >>> a.create_session()
    Success!
    >>> a.update_session()
    Success!
    >>> a.done_session()
    Success!

#### Api Log connector Functions
All result of this functions is shown in BDI dashboard, each time that you execute create_session it has 
a unique identifier and its delivering to each functions like : update_session, done_session, add_event,
 failed_session.  
* **create_session** - Create session in status pending for BDI Dashboard
* **udpate_session** - Update the same session that your have previously already created and it is set as initiated.
* **done_session** - Update the same session object and put it in Terminated status.
* **add_event** - This function create events in a determinated status, it could be: initiated, terminated, pending, etc.
* **failed_session** - This function update the same session object and put it in Failed status.


Advantages of use and maintain this artifact:

* This library centralize connector functions for BDI dashboards to avoid replicate code.
* It helps us to standardize belcorp technologies.
* Reduce Development time.
* This project use concepts of clean architecture that helps the scalability and the maintenance of the project.

![alt text](http://xurxodev.com/content/images/2016/07/CleanArchitecture-8b00a9d7e2543fa9ca76b81b05066629.jpg)

* Good practices, clean code and Solid principle also helps the scalability and maintain of the project.

![alt text](http://xtendedview.com/wp-content/uploads/2019/08/Android-Development.jpg)

### Complete guide of how to generate .wheel binary executable python project
https://packaging.python.org/guides/distributing-packages-using-setuptools/
### Fast introduction about Setup.py arguments

**name :** is the distribution name of your package. This can be any name as long as only contains letters, numbers, _ , and -. It also must not already be taken on pypi.org. Be sure to update this with your username, as this ensures you won’t try to upload a package with the same name as one which already exists when you upload the package.

**version :** is the package version see PEP 440 for more details on versions.

**author :** and author_email are used to identify the author of the package.

**description :** is a short, one-sentence summary of the package.

**long_description:** is a detailed description of the package. This is shown on the package detail package on the Python Package Index. In this case, the long description is loaded from README.md which is a common pattern.

**long_description_content_type :** tells the index what type of markup is used for the long description. In this case, it’s Markdown.

**url :** is the URL for the homepage of the project. For many projects, this will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting service.

**packages :** is a list of all Python import packages that should be included in the distribution package. Instead of listing each package manually, we can use find_packages() to automatically discover all packages and subpackages. In this case, the list of packages will be example_pkg as that’s the only package present.

**classifiers :** gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/.

**install_requires :** in this sections all dependencies that we put will be installed before install our project.

**python_requires :** gives the scope of the python versions for example : 3.* <= x <= 4.



###  Steps to Install in local mode belc-dlk-api-log-archetype :
First of all, I recommend to use docker container to develop any changes in the project because exist some automations that helps us to be more efficiently.
 
 * **Pull Amazon Linux Docker Image** - Download an official docker image so then we deploy a container with many features installed like : aws-cli, python3, aws-sdk.
 then we have to mount our window memory into our linux container to access to all window files, however if you are using linux distribution you dont have to mount memory,
 perhaps only create a volume to assure our container storage.
 
        docker pull amazonlinux
 
 ![alt text](http://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png)
 
 * **Install Extra Bash dependencies** - Install zip, and make command.
 
        apt-get update
        apt-get install zip
        apt-get install --reinstall make
          
    <img src="http://blog.minabta.com/wp-content/uploads/2018/10/gnu_logo_white-e1539089802374.png" width="150" height="150">
 * **Configure Git credentials** - request credentials for the git project.  
        
        ssh-keygen -t rsa
        cat /root/.ssh/id_rsa.pub.
        
 * **Make help** - this sections gives us a description of all existent automations.
 
        make help
        
   output:
   
        push - clean wheel refresh git_wheel
        clean - remove all build, test, coverage and Python artifacts
        develop - clean wheel refresh
        wheel - Execute Generate .wheel binary python application
        refresh - remove last version installed and install the newest
        clean-build - remove wrapped file
        clean-pyc - remove not important generated python files
        git - commit and push passing commit message
        git-push - commit and push passing commit message and default commit message
        test - run unit tests
        install - Install Python requirements to install for the first time in any enviroment
        aws - Configure Access-key and Secret Key
   
        
 * **Make aws** - We just have to set our Access-key and Secret-Key to start our development.
 
        make aws

 * **Make install** - We just need to execute this command into our container, so it would install python dependencies 
 that our project need.
 
        make install
        
 * **Make pep8** - This evaluate your code with good practices created in PEP8.
 
        make pep8

### Steps to Deploy new Features
We must have to consider that each release have to modify some important files like :
**env.sh** and **belc_log.html** these files are stored in a s3 belcorp bucket that it works like pypi.org hub, where all .wheel 
files are stored with their specific version and name.   

* For example if i list aws s3 ls "belcorp bucket" :

        2019-12-16 20:52:46   24.2 KiB belc_log-0.0.1-py3-none-any.whl
        2019-12-16 20:52:46    7.8 KiB belc_log-0.0.1.tar.gz
        2019-12-16 20:52:42  232 Bytes belc_log.html

* Environment variables are set in env.sh

        PROJECT_TAG ?= 0.0.1
        PROJECT_ADDRESS ?= ${PROJECT_NAME}:${PROJECT_TAG}
        BRANCH_NAME ?= master
        PROJECT_NAME ?= belc_log
        BUCKET_NAME ?= repository-python-archetype 
        
* BUCKET_NAME : the bucket name where the .wheel file are stored.
* PROJECT_TAG : the version of the project, it is update when new changes are deployed.
* PROJECT_NAME : the name of the project this name also are set in in setup.py in the argument "name",
also the html file it should be named like this variable.
* BRANCH_NAME : This have to be your development branch

* Html file are used to link with the .wheel file that are stored in the S3 bucket,
 therefore when the process execute :
 
        pip install belc_log --find-link="https:file.html"
         
it will download .wheel file to be executed.

* We have to be careful of set up the correct name, these arguments name are generated by the process :
        
        python3 setup.py sdist bdist_wheel
        
output :

        ll ${project}/dist
        20:52 belc_log-0.0.1-py3-none-any.whl
        20:52 belc_log-0.0.1.tar.gz
         
* these files are uploaded to the Belcorp bucket and this names files have to be set in the file called ${project}.html 
        <!-- belc_log.html -->
         
        <html>
          <body>
            <a href="belc_log-0.0.1.tar.gz">
              belc_log-0.0.1.tar.gz
            </a>
            <a href="belc_log-0.0.1-py3-none-any.whl">
              belc_log-0.0.1-py3-none-any.whl
            </a>
          </body>
        </html>

     ![alt text](https://upload.wikimedia.org/wikipedia/commons/3/34/Belcorp.jpg)
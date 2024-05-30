<h1>Tests for automated testing of the <i>rabota.by</i> website</h1>

---

<p align="center">
    <img width="200" height="200" src="final_project/models/img/logo.jpg">
</p>

<h2><img width="40" align="center" src="final_project/models/img/description.png"> Description</h2>
<li><a href="#tools">Tools</a></li>
<li><a href="#tests">Tests</a></li>
<li><a href="#run-tests">Run tests</a></li>
<li><a href="#test-example">Example of passing test</a></li>
<li><a href="#telegram-notification">Telegram notifications</a></li>

---

<h2 id="tools"><img width="40" align="center" src="final_project/models/img/tools.png"> Tools</h2>
<div align="center">
    <img title="Pytest" width="40" src="final_project/models/img/pytest.png">
    <img title="Python" width="40" src="final_project/models/img/python.png">
    <img title="Selenium" width="40" src="final_project/models/img/selenium.png">
    <img title="Selene" width="40" src="final_project/models/img/selene.png">
    <img title="PyCharm" width="40" src="final_project/models/img/pycharm.png">
    <img title="Jenkins" width="40" height="40" src="final_project/models/img/jenkins.png">
    <img title="Selenoid" width="40" src="final_project/models/img/selenoid.png">
    <img title="Allure" width="40" src="final_project/models/img/allure.png">
    <img title="Github" width="40" src="final_project/models/img/github.png">
    <img title="Appium" width="40" src="final_project/models/img/appium.png">
    <img title="Pydantic" width="40" src="final_project/models/img/pydantic.png">
    <img title="Telegram" width="40" src="final_project/models/img/telegram.png">
</div>
<p>Autotests are written in <b>Python</b> using <b>Selenide</b> for <i>UI tests</i>, <b>Browserstack</b>, <b>emulator or real device</b> for <i>mobile tests</i></p>
<p>Tests are run from <b>Jenkins</b></p>
<p><b>Selenoid and Browserstack</b> are used to launch the browser</p>
<p><b>Allure report</b> is generated and sent to telegram</p>

---

<h2 id="tests"><img width="40" align="center" src="final_project/models/img/tests.png"> Tests</h2>

<p><b>UI tests:</b></p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Successfully login</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Unsuccessfully login</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Search company</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Advanced search</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Open resume page</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Save search without registering</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Choose city</p>
<p><b>API tests:</b></p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Login with correct data</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Login with incorrect data</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Search vacancy</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Add vacancy to favorite without registered</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Enter phone number for get otp</p>
<p><b>Mobile tests:</b></p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> Login page</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> New user page</p>
<p><img width="20" align="center" src="final_project/models/img/checkbox.png" alt="checkbox"> User profile</p>
---

<h2 id="run-tests"><img width="40" align="center" src="final_project/models/img/run-tests.png" alt="run"> Run tests</h2>

<pre>
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest . --browser_version=${BROWSER_VERSION}
</pre>
<p><b>Parameters</b>: 
    <li>BROWSER_VERSION - browser version in which the tests will be run</li>
</p>

---

<p>To run tests in Jenkins you need to click on <b>Build with Parameters</b> button</p>
<img src="final_project/models/img/build.png" alt="build">
<p>Сhoose parameters (<i>BROWSER_VERSION, ENVIRONMENT, COMMENT</i>) and click on <b>"Build"</b> button</p>
<img src="final_project/models/img/parameters.png" alt="parameters">
<p>After passing the tests report will be generated, you can see it by clicking on the <b>Allure report</b></p>
<img src="final_project/models/img/allure-report.png" alt="allure-report">
<img src="final_project/models/img/allure-result.png" alt="allure-result">

---

<h2 id="test-example"><img width="40" align="center" src="final_project/models/img/example.png" alt="exapmle">Example of passing search of company test</h2>
<img src="final_project/models/img/test-example.gif" alt="test">

---

<h2 id="telegram-notification"><img width="40" align="center" src="final_project/models/img/notification.png" alt="exapmle">Telegram notifications</h2>
<img src="final_project/models/img/report-telegram.png" alt="report-telegram">

<h1>Tests for automated testing of the <i>rabota.by</i> website</h1>

---

<p align="center">
    <img width="600" height="300" src="resources/main-page.png">
</p>

<h2><img width="40" align="center" src="resources/description.png"> Description</h2>
<li><a href="#tools">Tools</a></li>
<li><a href="#tests">Tests</a></li>
<li><a href="#run-tests">Run tests</a></li>
<li><a href="#test-example">Example of passing test</a></li>
<li><a href="#telegram-notification">Telegram notifications</a></li>

---

<h2 id="tools"><img width="40" align="center" src="resources/tools.png"> Tools</h2>
<div align="center">
    <img title="Pytest" width="40" src="resources/pytest.png">
    <img title="Python" width="40" src="resources/python.png">
    <img title="Selenium" width="40" src="resources/selenium.png">
    <img title="Selene" width="40" src="resources/selene.png">
    <img title="PyCharm" width="40" src="resources/pycharm.png">
    <img title="Jenkins" width="40" height="40" src="resources/jenkins.png">
    <img title="Selenoid" width="40" src="resources/selenoid.png">
    <img title="Allure" width="40" src="resources/allure.png">
    <img title="Github" width="40" src="resources/github.png">
    <img title="Appium" width="40" src="resources/appium.png">
    <img title="Pydantic" width="40" src="resources/pydantic.png">
    <img title="Telegram" width="40" src="resources/telegram.png">
</div>
<p>Autotests are written in <b>Python</b> using <b>Selenide</b> for <i>UI tests</i>, <b>Browserstack</b>, <b>emulator or real device</b> for <i>mobile tests</i></p>
<p>Tests are run from <b>Jenkins</b></p>
<p><b>Selenoid and Browserstack</b> are used to launch the browser</p>
<p><b>Allure report</b> is generated and sent to telegram</p>

---

<h2 id="tests"><img width="40" align="center" src="resources/tests.png"> Tests</h2>

<p><b>UI tests:</b></p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Successfully login</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Unsuccessfully login</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Search company</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Advanced search</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Open resume page</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Save search without registering</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Choose city</p>
<p><b>API tests:</b></p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Login with correct data</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Login with incorrect data</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Search vacancy</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Add vacancy to favorite without registered</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Enter phone number for get otp</p>
<p><b>Mobile tests:</b></p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> Login page</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> New user page</p>
<p><img width="20" align="center" src="resources/checkbox.png" alt="checkbox"> User profile</p>
---

<h2 id="run-tests"><img width="40" align="center" src="resources/run-tests.png" alt="run"> Run tests</h2>
<p><b>For web tests:</b></p>
<pre>
    pytest tests/web
</pre>
<p><b>For API tests:</b></p>
<pre>
    pytest tests/api
</pre>
<p><b>For mobile tests on emulator:</b></p>
<pre>
    pytest tests/api --context=local_emulator
</pre>
<p><b>For mobile tests on real device:</b></p>
<pre>
    pytest tests/api --context=real_local
</pre>
<p><b>For mobile tests on bstack:</b></p>
<pre>
    pytest tests/api --context=bstack
</pre>


---

<p>To run tests in Jenkins you need to click on <b>Build with Parameters</b> button</p>
<img src="resources/build.png" alt="build">
<p>Сhoose parameters (<i>BROWSER_VERSION, ENVIRONMENT, COMMENT</i>) and click on <b>"Build"</b> button</p>
<img src="resources/parameters.png" alt="parameters">
<p>After passing the tests report will be generated, you can see it by clicking on the <b>Allure report</b> and <b>Allure TestOps</b></p>
<p><a href="https://allure.autotests.cloud/launch/39345">TestOps</a></p>
<img src="resources/allure-report.png" alt="allure-report">
<img src="resources/allure-result.png" alt="allure-result">
<img src="resources/testOps.png" alt="allure-testOps">
<img src="resources/testOps-tests.png" alt="allure-testOps-tests">


---

<h2 id="test-example"><img width="40" align="center" src="resources/example.png" alt="exapmle">Example of passing search of company test</h2>
<img src="resources/test-example.gif" alt="test">

---

<h2 id="telegram-notification"><img width="40" align="center" src="resources/notification.png" alt="exapmle">Telegram notifications</h2>
<img src="resources/report-telegram.png" alt="report-telegram">

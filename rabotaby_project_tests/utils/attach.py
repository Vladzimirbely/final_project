import json
import logging
import allure
from allure_commons.types import AttachmentType
import requests
from requests import Response
from selene import browser


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')


def bstack_video(session_id):
    from config import config as app_config
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(app_config.userName, app_config.accessKey)
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML
    )


def page_source_xml():
    allure.attach(
        browser.driver.page_source,
        name='page_source_xml',
        attachment_type=allure.attachment_type.XML
    )


def screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )

def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    allure.attach(
        body=str(response.status_code),
        name='response status code',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    allure.attach(
        body=response.text,
        name='response text',
        attachment_type=AttachmentType.TEXT,
        extension='.txt'
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(str(response.request.body)),
            name="request body",
            attachment_type=AttachmentType.JSON,
            extension=".json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="response",
            attachment_type=AttachmentType.JSON,
            extension=".json",
        )

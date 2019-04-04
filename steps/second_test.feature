Feature: Second test
Scenario: Test regions lists

Given get token "http://discovery-preprod.ertelecom.ru/er/misc/domains"
Then pass correct token
Then pass incorrect token
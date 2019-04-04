Feature: First test
Scenario: Test authorization

Given website "http://discovery-preprod.ertelecom.ru/api/token/device"
Then check authorization success
Then pass incorrect client_id
Then pass one parametr
Then pass incorrect parameters
Then pass two parameters
Then pass time float
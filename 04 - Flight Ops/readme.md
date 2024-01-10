# Flight Ops

## Challenge Stats

Category: Web
Difficulty: Easy
Skillsets: BurpSuite, ClientSide Validation
Flag: EspionageCTF{cl13nt_s1d3_val1dat10n_st1ll_3x1sts}

## Description

I seem to have found this maintenance dashboard for some airline or something... but I cannot seem to login as admin. They must be doing some kind of checks or input sanitizaiton. Can you?

## Start Up Instructions

1. `sudo docker build -t webac .`
2. `sudo docker run -p <port>:80 -t webac`

## Solution 1

1. Right click on the website to "view source", and notice that the Javascript function invoked upon form submit is replacing the username "admin" with "noflag"
2. Using Firefox
    1. Using the network devtools function on firefox, submit the form.
    2. Right click the network traffic and select "Edit and Resend"
    3. Edit the request data to change the username sent back to admin
    4. Recieve the flag as a response
3. Using Burpsuite
    1. Open the webpage using Burpsuite and turn intercept on.
    2. Submit the form with anything as the username.
    3. Before forwarding the request, change username back to admin, then forward.
    4. Recieve the flag as a response
4. Directly interact with the API
    1. Using Postman, or some kind of programming library like python requests, make a POST request to /api/check_user
    2. Ensure the data sent is json and looks like the following `{"username" : "admin"}`
    3. Recieve the flag as a response
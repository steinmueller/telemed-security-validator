# Telemedicine-Cloud-Validation
This repository is part of a validation procedure of cybersecurity requirements
within the master thesis with the topic "Requirements on Secure Cloud Design
for Telemedicine Applications" by Sebastian Steinmüller.

The code described here implements a basic tele-emergency-doctor
application that could allow emergency services to remotely get in
contact with a doctor via a video call.
The implementation follows the requirements that have been defined in
the thesis. With this project, a set the defined requirements will be
tested for practicality and implementability.

## Installation
The final application can be accessed at http://telemed-validation.azurewebsites.net/

## Usage
The following users have been added: 

doc@tna.de
XETUg9DxdNAFov362ZRTaHwy2cAAWgJV

emt@tna.de
vkrmcGjuJHjuLDREn89rTT24xFGyMtd7

The admin access won't be published.
The following credentials can be used for the video conferencing functionality

User 1:
ID: 8:acs:8e6931ed-a106-4851-98a9-ca241069218c_00000019-97e3-3f4a-f4f3-ad3a0d000378
Token: eyJhbGciOiJSUzI1NiIsImtpZCI6IjVFODQ4MjE0Qzc3MDczQUU1QzJCREU1Q0NENTQ0ODlEREYyQzRDODQiLCJ4NXQiOiJYb1NDRk1kd2M2NWNLOTVjelZSSW5kOHNUSVEiLCJ0eXAiOiJKV1QifQ.eyJza3lwZWlkIjoiYWNzOjhlNjkzMWVkLWExMDYtNDg1MS05OGE5LWNhMjQxMDY5MjE4Y18wMDAwMDAxOS05N2UzLTNmNGEtZjRmMy1hZDNhMGQwMDAzNzgiLCJzY3AiOjE3OTIsImNzaSI6IjE2ODc3ODgwMzQiLCJleHAiOjE2ODc4NzQ0MzQsInJnbiI6ImRlIiwiYWNzU2NvcGUiOiJ2b2lwIiwicmVzb3VyY2VJZCI6IjhlNjkzMWVkLWExMDYtNDg1MS05OGE5LWNhMjQxMDY5MjE4YyIsInJlc291cmNlTG9jYXRpb24iOiJnZXJtYW55IiwiaWF0IjoxNjg3Nzg4MDM0fQ.kpPLO-eeLGpgVXhEwI9HYDNgG-TX0a02lIgTBb9EKQSy-RmbGLOHCh76IFZ3fLH8-8QfOjVuuoCgIRmZHVrEpfsbx6m95uVx7f_c44EB5M3aS4FGum7ZuqLlz7LMYmU3C0QzCH2mIwlUKFM9AZvc57PV5yFapu7rdRj9eSoSPLaV4mY3TlsuGxfhH7oKVagcd_NX1CpkxZJ7qrF3YqmmFHtxn0Ynf4eSoADVidQf7C5gQSB2pnHb5V3snkPozPtlApp_9mKaOCzdl84a99pb_Z4B9DN_mFn9dhs_xHJyVAdV6_SrHCAjB_0Hyf1zA-TkEvEQ2yd1m3A2_eAL7MAR0Q

User 2:
ID: 8:acs:8e6931ed-a106-4851-98a9-ca241069218c_00000019-9808-4a53-34fa-ad3a0d000cd4
Token: eyJhbGciOiJSUzI1NiIsImtpZCI6IjVFODQ4MjE0Qzc3MDczQUU1QzJCREU1Q0NENTQ0ODlEREYyQzRDODQiLCJ4NXQiOiJYb1NDRk1kd2M2NWNLOTVjelZSSW5kOHNUSVEiLCJ0eXAiOiJKV1QifQ.eyJza3lwZWlkIjoiYWNzOjhlNjkzMWVkLWExMDYtNDg1MS05OGE5LWNhMjQxMDY5MjE4Y18wMDAwMDAxOS05ODA4LTRhNTMtMzRmYS1hZDNhMGQwMDBjZDQiLCJzY3AiOjE3OTIsImNzaSI6IjE2ODc3OTA0NjIiLCJleHAiOjE2ODc4NzY4NjIsInJnbiI6ImRlIiwiYWNzU2NvcGUiOiJ2b2lwIiwicmVzb3VyY2VJZCI6IjhlNjkzMWVkLWExMDYtNDg1MS05OGE5LWNhMjQxMDY5MjE4YyIsInJlc291cmNlTG9jYXRpb24iOiJnZXJtYW55IiwiaWF0IjoxNjg3NzkwNDYyfQ.jxoUl4kTre3wQxPGhaGCnHPnA1rQwA3fEPKgR5Dy1LE7zc-KSR8Xz8LB0YzU4DpK7tDOjOdh1_ql2oT0aVsjHkM0E5MV9LeHwa0ofrWEXldVHvYILyKkySWyfcAXjGSERcTxzCtV16TGmuoX5P7XVVuq0FfX8-SuKwb2PvpzziB3f3Fi4dD0gG0j6OPjfL2l-ZD8ekTbGuKJfWqCqSfvWGtQpD_itajJjoAPakGyyMr9raY_UMARs2iPSxlrKZkYFuQB0hHQTRxVI1fBjfqK07RQMrRc2bE25V1FLQTAUc8iklOhwJ01uBAXebmQff13ls9QkwTz0hu09WvkxWkFlw

## Roadmap
The idea was to show the implementability of the functionalities in the
infrastructure of a cloud hyperscaler. To deploy an actual application,
this web app was created. Therefore the development will not continue

## Contributing
As this is part of a final thesis for a masters degree, contribution is
not possible. But feel free to fork or read more about the topic in the
thesis.

## Acknowledgements
This project is based on the following resources by Microsoft under MIT License:

https://github.com/Azure-Samples/msdocs-flask-postgresql-sample-app
https://github.com/Azure-Samples/communication-services-javascript-quickstarts/tree/main/add-1-on-1-video-calling

## License
Copyright (C) 2023 by Sebastian Steinmüller s.steinmueller@tum.de

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

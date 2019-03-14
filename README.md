python-2c2p
===========

A simple python class to assist connecting to 2c2p.com redirect API.

Example:

```
tctp = twoctwop_redirectapi('JT04', 'QnmrnH6QE23N', 'https://demo2.2c2p.com/2C2PFrontEnd/RedirectV3/payment')
tctp.set_value('amount', 100000)
tctp.set_value('currency', 'THB')
tctp.set_value('default_lang', 'en')
tctp.set_value('order_id', '000001')  # optional, if you do not specify this it will default to use a milliseconds timestamp
tctp.set_value('payment_description', 'First attempt using demo2.2c2p.com')
tctp.set_value('result_url_1', 'http://localhost/payment-complete/')
html = tctp.request()

print(html)
```
from alipay import AliPay
def Pay(order_id,money):
    alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1GC/Ls99rvzS2WeB7Limav4g3kTc4HtQ23xOy0LuCBVQaorubkUIm9IrSne0gZMA1UtsmdRc4IgjIwZetR0eMLClgosKff2548dhYcGnodtqioNGMSbpxsp1/QJojJmKFHHGwyefHoTaA9bKjGIWB7aX6SFcRtQt3LPupRDxHy9R1C1EoB++j805+oSqeSj1fUAWqLTM7wD3QRbrNv+Q5zNga8ATgYx68gNPeeFiTMBk6EZR4g3dsKK0Hhm26gxaZ9EG/aMNWIEKj/+8+X61j8RfmCL4h/dMk1MyMUnUit8XbyAjrN7PwYaW3iXyQgMXwwrmZ0RYinz2foTteeFVkQIDAQAB
    -----END PUBLIC KEY-----"""
    app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEA1GC/Ls99rvzS2WeB7Limav4g3kTc4HtQ23xOy0LuCBVQaorubkUIm9IrSne0gZMA1UtsmdRc4IgjIwZetR0eMLClgosKff2548dhYcGnodtqioNGMSbpxsp1/QJojJmKFHHGwyefHoTaA9bKjGIWB7aX6SFcRtQt3LPupRDxHy9R1C1EoB++j805+oSqeSj1fUAWqLTM7wD3QRbrNv+Q5zNga8ATgYx68gNPeeFiTMBk6EZR4g3dsKK0Hhm26gxaZ9EG/aMNWIEKj/+8+X61j8RfmCL4h/dMk1MyMUnUit8XbyAjrN7PwYaW3iXyQgMXwwrmZ0RYinz2foTteeFVkQIDAQABAoIBAQCxTUeu08iwox+AIrrEHu/IWPqltUXVHv5FDsVVSj4gf3LQT8Z4RqfGNrKvi7olhs1mRH6Y+kLDrMPwxKuidnmy2naCwoNy5bUgJV72Vs8VAHI0yx15gWwf6vyPykfwQWqWYNo4KMbdmrnMBLC6fFS6AcVW+uPnudHD9G+iXL+AcOIty2u/O20mh5VCeoUs905xcyvgXE6xtKurekx+WdE6uj8L5ZsmF6i3YWKtw1B/6TMQAZM0QuPBUAXqe5ruDSzm6L6wOKMZiV2J0hgIrVRlOt6bqlPi8D9Gw4K+rDem4owQMJam5d517dUqDJOTUcHGaAovCHW2xdNj/AOwY93xAoGBAPMCMsimJZEyU6sxV0qqWl34bp8eMW0UyUE6+Cfk8VtAfbLOs8X9rkQYdeKziX/a84/Vonox8Ydp8rukr4eWVP9Fg2HRkPHTpEces1Qy69z67rkTQ9katclEZLbEyYnhoqrlFe5aRkKrLXTV3GT7cEGgKbqpuwEEENI1Nc31yFO9AoGBAN+7Vr3TOt8U5pVNqIt6nvGwL0TtHxXXLeSPZqop1DrXoXO76rLCh5H1Vx7fwmsodXUgBNO5wh4BiItrW1PF5q8ULxC92zUuqhNu55GpWN0u0DIP1kblskjD3oF6QLZf/Zq/926vNqf+BViqGxA+thxX4jrv8wR1Wd6gexyOmDxlAoGAb8PtE3fHA3bAIJZ67W5YTav7RNegJ+lNfuDeTYrwruWEan7DFCbOxabyYSft744GQ3sgVU8vJPbHmyHtUVEFGrsf6Bd4sKCEh+lI1UruTB5lOV3w8KNmRIFeSOlNQEs0g6EFazC969/K8leCHDfAs440YxO5XIhALE4oxudqEYkCgYALW5hQtKt1bbsy8ylOQ2BURqxvpFYCptTWmI0OsGbswcuZc327q3J0b28HyzY0eG5WDtUP5os7OLq00TNmslI+qxikke7R6VeK+wNYeq9fMyQwlms7WCfP19mw2wLz/zWBqKMoBE8TAitFUAVlsrlOAQwkD9BXdpmkWqNFVNvXnQKBgQCR5WCLtrxRTGd+RZ8x7fXo0k4+Pn5ZfzXSMfVZHh8ZB8qDYwoI6yC1KvVCWiR9BR3oSVFvio/ddJX2sHpB54i9gzzwpLhgJRT98iuJSUxORySoEFadomWOtE82wEaHzJLdpZOGZMy9ccFQ6jt/kFxiuT6FCNRWPDp++0THd8BDPw==
    -----END RSA PRIVATE KEY-----"""

    alipay = AliPay(
        appid="2016101500695725",
        app_notify_url="",
        app_private_key_string = app_private_key_string,
        alipay_public_key_string = alipay_public_key_string,
        sign_type="RSA2",
    )
    #发起支付
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(money),
        subject="商贸商城",
        return_url="http://127.0.0.1:8000/Buyer/pay_result/",
        notify_url="http://127.0.0.1:8000/Buyer/pay_result/"
    )

    return "https://openapi.alipaydev.com/gateway.do?" + order_string

if __name__ == '__main__':
    print(Pay("123456","10000"))
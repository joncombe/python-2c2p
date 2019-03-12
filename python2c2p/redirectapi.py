import hashlib
import hmac
import random
import time

class twoctwop_redirectapi:
    def __init__(self, merchant_id, secret_key, request_uri):
        self.request_uri = request_uri
        self.secret_key = secret_key
        self.data = {
            'merchant_id': merchant_id,
            'version': '7.5'
        }

    def request(self):
        # check manadatory values
        mandatory_fields = ['payment_description', 'order_id', 'amount']
        for f in mandatory_fields:
            if f not in self.data:
                raise Exception('Missing mandatory value: %s' % f)

        # generate hash
        self.data['hash_value'] = self._get_request_hash()

        # generate form id
        form_id = ''
        chars = 'bcdfghjklmnpqrstvwxyz'
        for i in range(0, 20):
            form_id = '%s%s' % (form_id, chars[random.randint(0, len(chars) - 1)])

        # generate html
        html = []
        html.append('<form id="%s" action="%s" method="post">' % (form_id, self.request_uri))
        for key in self.data:
            html.append('<input type="hidden" name="%s" value="%s" />' % (key, self.data[key]))
        html.append('<input type="submit" value="Pay now">')
        html.append('</form>')
        html.append('<script>document.forms.%s.submit()</script>' % fornm_id)
        return ''.join(html)

    def set_value(self, key, value):
        if key == 'amount':
            value = ('000000000000%s' % str(value))[-12:]
        if key == 'currency':
            value = self._get_currency_id_from_code(value)
        self.data[key] = value

    def _get_currency_id_from_code(self, code):
        return {
            'HKD': 344,
            'IDR': 360,
            'MMK': 104,
            'MYR': 458,
            'PHP': 608,
            'SGD': 702,
            'THB': 764,
        }[code.upper()]

    def _get_request_hash(self):
        fields = [
            'version', 'merchant_id', 'payment_description', 'order_id', 'invoice_no',
            'currency', 'amount', 'customer_email', 'pay_category_id', 'promotion',
            'user_defined_1', 'user_defined_2', 'user_defined_3', 'user_defined_4',
            'user_defined_5', 'result_url_1', 'result_url_2', 'enable_store_card',
            'stored_card_unique_id', 'request_3ds', 'recurring', 'order_prefix',
            'recurring_amount', 'allow_accumulate', 'max_accumulate_amount',
            'recurring_interval', 'recurring_count', 'charge_next_date',
            'charge_on_date', 'payment_option', 'ipp_interest_type', 'payment_expiry',
            'default_lang', 'statement_descriptor', 'use_storedcard_only',
            'tokenize_without_authorization', 'product', 'ipp_period_filter'
        ]

        # generate plain string
        hash_str = ''
        for f in fields:
            if f in self.data:
                hash_str = '%s%s' % (hash_str, self.data[f])

        # generate hash from secret key
        hash = hmac.new(
            bytes(self.secret_key, 'latin-1'),
            bytes(hash_str, 'latin-1'),
            hashlib.sha1
        ).hexdigest()

        return hash.upper()


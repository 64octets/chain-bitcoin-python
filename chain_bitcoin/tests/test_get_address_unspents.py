from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, Output, get_address_unspents
from .mock_http_adapter import *


def test_get_address_unspents():
    get_address_unspents(address_id, api_key_id=api_key_id,
                         http_adapter=http_adapter) \
        .should.equal(unspents)


def test_get_address_unspents_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_address_unspents(address_id).should.equal(unspents)


def test_get_address_unspents_without_api_key_id():
    (lambda: get_address_unspents(address_id, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


address_id = '1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/addresses/' \
      '1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb/unspents?api-key-id=DEMO-4a5e1e4'

response_body = """
[
    {
        "transaction_hash": "0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc",
        "output_index": 0,
        "value": 290000,
        "addresses": [
            "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
        ],
        "script": "OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG",
        "script_hex": "76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac",
        "script_type": "pubkeyhash",
        "required_signatures": 1,
        "spent": false,
        "confirmations": 8758
    },
    {
        "transaction_hash": "5ad2913b948c883b007b1bca39322c42d60ef465b9dc39bc0a53ffe8fe3faafd",
        "output_index": 0,
        "value": 10000,
        "addresses": [
            "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
        ],
        "script": "OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG",
        "script_hex": "76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac",
        "script_type": "pubkeyhash",
        "required_signatures": 1,
        "spent": false,
        "confirmations": 9074
    },
    {
        "transaction_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
        "output_index": 1,
        "value": 32000,
        "addresses": [
            "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
        ],
        "script": "OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG",
        "script_hex": "76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac",
        "script_type": "pubkeyhash",
        "required_signatures": 1,
        "spent": false,
        "confirmations": 8760
    }
]
"""

unspents = [
    Output(
        transaction_hash='0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc',
        output_index=0,
        value=290000,
        addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
        script='OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG',
        script_hex='76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac',
        script_type='pubkeyhash',
        required_signatures=1,
        spent=False,
        confirmations=8758,
    ),
    Output(
        transaction_hash='5ad2913b948c883b007b1bca39322c42d60ef465b9dc39bc0a53ffe8fe3faafd',
        output_index=0,
        value=10000,
        addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
        script='OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG',
        script_hex='76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac',
        script_type='pubkeyhash',
        required_signatures=1,
        spent=False,
        confirmations=9074,
    ),
    Output(
        transaction_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
        output_index=1,
        value=32000,
        addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
        script='OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG',
        script_hex='76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac',
        script_type='pubkeyhash',
        required_signatures=1,
        spent=False,
        confirmations=8760,
    ),
]

http_adapter = mock_get(url, response_body)

# -*coding: utf-8-*-

from datetime import datetime, date
from decimal import Decimal

from ...models.transfer import Transfer
from ...models.subaccount import Subaccount


def make_payment(d, subaccount_id, account_item_id, sum):
    """outgoing transfers creator
    """
    assert isinstance(d, (datetime, date)), \
        u'Datetime or Date instance expected'
    assert isinstance(sum, Decimal), u'Decimal expected'
    subaccount = Subaccount.get(subaccount_id)
    return [
        Transfer(
            subaccount_from_id=subaccount.id,
            account_item_id=account_item_id,
            sum=sum,
            date=d,
        ),
    ]
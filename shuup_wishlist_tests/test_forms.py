# -*- coding: utf-8 -*-
# This file is part of Shuup Wishlist.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from shuup_wishlist.forms import WishlistForm

from shuup.core.models import get_person_contact
from shuup.testing.factories import get_default_shop, create_product
from .fixtures import regular_user

regular_user = regular_user  # noqa


@pytest.mark.django_db
def test_form(admin_user, rf):
    shop = get_default_shop()
    customer = get_person_contact(admin_user)
    customer.save()
    product = create_product("test")

    form = WishlistForm(data={"name": "foo", "privacy": 0, "product_id": product.id}, shop=shop, customer=customer, product_id=product.id)
    form.full_clean()
    assert not form.errors
    assert form.is_bound
    form.is_valid()  # shouldn't raise

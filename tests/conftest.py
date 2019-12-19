# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime
import pytest
import pytz


import os
import random


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


# Set a fixed random seed so that tests are stable
random.seed(42)

parent = os.path.split(__file__)
FIXTURE_PATH = os.path.join(os.path.split(__file__)[0], "fixtures")

CFR_IDS = [
    "BOOKMARK_SYNC_CFR",
    "CRYPTOMINERS_PROTECTION",
    "CRYPTOMINERS_PROTECTION_71",
    "FACEBOOK_CONTAINER_3",
    "FACEBOOK_CONTAINER_3_72",
    "FINGERPRINTERS_PROTECTION",
    "FINGERPRINTERS_PROTECTION_71",
    "GOOGLE_TRANSLATE_3",
    "GOOGLE_TRANSLATE_3_72",
    "MILESTONE_MESSAGE",
    "PDF_URL_FFX_SEND",
    "PIN_TAB",
    "PIN_TAB_72",
    "SAVE_LOGIN",
    "SAVE_LOGIN_72",
    "SEND_RECIPE_TAB_CFR",
    "SEND_TAB_CFR",
    "SOCIAL_TRACKING_PROTECTION",
    "SOCIAL_TRACKING_PROTECTION_71",
    "WNP_MOMENTS_1",
    "WNP_MOMENTS_2",
    "WNP_MOMENTS_SYNC",
    "YOUTUBE_ENHANCE_3",
    "YOUTUBE_ENHANCE_3_72",
]


@pytest.fixture
def FIXTURE_JSON():
    return {
        "client_id": "5caa92ae-e078-4f18-bbaf-bd23094a4a1a",
        "addon_version": "2018.08.22.1219-93becf29",
        "source": "TOP_SITES",
        "session_id": "{8435349f-bf5d-41e5-b4df-cc94821db032}",
        "page": "about:newtab",
        "action_position": "13",
        "event": "CLICK",
        "receive_at": datetime.datetime(2018, 9, 30, 10, 51, 40, tzinfo=pytz.utc),
        "date": datetime.date(2018, 9, 30),
        "locale": "en-US",
        "country_code": "LV",
        "os": "Windows 7",
        "browser": "Firefox",
        "version": "62.0.2",
        "device": "Other",
        "user_prefs": 43,
        "release_channel": "release",
        "shield_id": "n/a",
        "sample_id": 63,
        "value": '{"card_type": "pinned", "icon_type": "screenshot_with_icon"}',
    }


@pytest.fixture
def WEIGHT_VECTOR():
    return {
        "CFR_ID_1": {
            "feature_1": {"p_given_cfr_acceptance": 0.7, "p_given_cfr_rejection": 0.5}
        },
        "CFR_ID_2": {
            "feature_1": {
                "p_given_cfr_acceptance": 0.49,
                "p_given_cfr_rejection": 0.25,
            },
            "feature_2": {
                "p_given_cfr_acceptance": 0.49,
                "p_given_cfr_rejection": 0.25,
            },
        },
        "CFR_ID_3": {
            "feature_1": {
                "p_given_cfr_acceptance": 0.343,
                "p_given_cfr_rejection": 0.125,
            },
            "feature_2": {
                "p_given_cfr_acceptance": 0.343,
                "p_given_cfr_rejection": 0.125,
            },
            "feature_3": {
                "p_given_cfr_acceptance": 0.343,
                "p_given_cfr_rejection": 0.125,
            },
        },
        "CFR_ID_4": {
            "feature_1": {
                "p_given_cfr_acceptance": 0.2401,
                "p_given_cfr_rejection": 0.0625,
            },
            "feature_2": {
                "p_given_cfr_acceptance": 0.2401,
                "p_given_cfr_rejection": 0.0625,
            },
            "feature_3": {
                "p_given_cfr_acceptance": 0.2401,
                "p_given_cfr_rejection": 0.0625,
            },
            "feature_4": {
                "p_given_cfr_acceptance": 0.2401,
                "p_given_cfr_rejection": 0.0625,
            },
        },
    }

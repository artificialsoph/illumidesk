import pytest

from tornado.web import HTTPError

from illumidesk.authenticators.authenticator import LTI11LaunchValidator
from tests.illumidesk.factory import factory_lti11_basic_launch_args


def test_basic_lti11_launch_request():
    """
    Does a standard launch request work?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    assert validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_nonce_key():
    """
    Does the launch request work with a missing oauth_nonce key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_nonce']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_nonce_value():
    """
    Does the launch request work with an empty or None oauth_nonce value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_nonce'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_nonce'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_timestamp_key():
    """
    Does the launch request work with a missing oauth_timestamp key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_timestamp']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_timestamp_value():
    """
    Does the launch request work with an empty or None oauth_timestamp value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_timestamp'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_timestamp'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_consumer_key_key():
    """
    Does the launch request work with a missing oauth_consumer_key key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_consumer_key']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_consumer_key_value():
    """
    Does the launch request work with an empty or None oauth_consumer_key value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_consumer_key'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_consumer_key'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_fake_oauth_consumer_key_value():
    """
    Does the launch request work when the consumer_key isn't correct?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_consumer_key'] = [b'fake_consumer_key'][0].decode('utf-8')
        assert validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_signature_method_key():
    """
    Does the launch request work with a missing oauth_signature_method key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret)

    del args['oauth_signature_method']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_signature_method_value():
    """
    Does the launch request work with an empty or None oauth_signature_method value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_signature_method'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_signature_method'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_callback_key():
    """
    Does the launch request work with a missing oauth_callback key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_callback']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_callback_value():
    """
    Does the launch request work with an empty or None oauth_callback value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_callback'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_callback'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_version_key():
    """
    Does the launch request work with a missing oauth_version key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_version']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_version_value():
    """
    Does the launch request work with an empty or None oauth_version value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_version'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_version'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_oauth_signature_key():
    """
    Does the launch request work with a missing oauth_signature key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['oauth_signature']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_oauth_signature_value():
    """
    Does the launch request work with an empty or None oauth_signature value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_signature'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['oauth_signature'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_unregistered_consumer_key():
    """
    Does the launch request work with a consumer key that does not match?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    args['oauth_consumer_key'] = 'fake_consumer_key'

    with pytest.raises(HTTPError):
        assert validator.validate_launch_request(launch_url, headers, args)


def test_unregistered_shared_secret():
    """
    Does the launch request work with a shared secret that does not match?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: 'my_other_shared_secret'})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_lti_message_type():
    """
    Does the launch request work with a missing lti_message_type argument?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['lti_message_type']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_lti_message_type():
    """
    Does the launch request work with an empty or None lti_message_type value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['lti_message_type'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['lti_message_type'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_lti_version():
    """
    Does the launch request work with a missing oauth_signature key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['lti_version']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_lti_version():
    """
    Does the launch request work with an empty or None oauth_signature value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['lti_version'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['lti_version'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_resource_link_id():
    """
    Does the launch request work with a missing resource_link_id key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['resource_link_id']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_resource_link_id():
    """
    Does the launch request work with an empty or None resource_link_id value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['resource_link_id'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['resource_link_id'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_missing_user_id_key():
    """
    Does the launch request work with a missing user_id key?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    del args['user_id']

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_none_or_empty_user_id_value():
    """
    Does the launch request work with an empty or None user_id value?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['user_id'] = None
        validator.validate_launch_request(launch_url, headers, args)

    with pytest.raises(HTTPError):
        args['user_id'] = ''
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_same_oauth_timestamp_different_oauth_nonce():
    """
    Does the launch request pass with when using a different nonce with the
    same timestamp?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret,)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_nonce'] = 'fake_nonce'
        validator.validate_launch_request(launch_url, headers, args)


def test_launch_with_same_oauth_nonce_different_oauth_timestamp():
    """
    Does the launch request pass with when using a different timestamp with the
    same nonce?
    """
    oauth_consumer_key = 'my_consumer_key'
    oauth_consumer_secret = 'my_shared_secret'
    launch_url = 'http://jupyterhub/hub/lti/launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    args = factory_lti11_basic_launch_args(oauth_consumer_key, oauth_consumer_secret)

    validator = LTI11LaunchValidator({oauth_consumer_key: oauth_consumer_secret})

    with pytest.raises(HTTPError):
        args['oauth_timestamp'] = '0123456789'
        validator.validate_launch_request(launch_url, headers, args)

# -*- coding: utf-8 -*-

"""Test cases for the 'delete_volume' helper function."""

# ======================================================================================================================
# Imports
# ======================================================================================================================
import os
import json
import pytest
import pytest_rpc.helpers
import testinfra.host
import testinfra.backend.base


# ======================================================================================================================
# Tests
# ======================================================================================================================
def test_successful_deletion(mocker):
    """Verify delete_volume returns None when OpenStack volume has been
    successfully deleted."""

    fake_backend = mocker.Mock(spec=testinfra.backend.base.BaseBackend)
    myhost = testinfra.host.Host(fake_backend)
    cr1 = mocker.Mock(spec=testinfra.backend.base.CommandResult)
    cr2 = mocker.Mock(spec=testinfra.backend.base.CommandResult)
    mocker.patch('testinfra.host.Host.run', side_effect=[cr1, cr2, cr2])

    server = {'ID': 'foo', 'Name': 'myvolume'}
    cr1.rc = cr2.rc = 0
    cr1.stdout = json.dumps(server)
    cr2.stdout = '[]'

    assert not pytest_rpc.helpers.delete_volume('myvolume', myhost)


@pytest.mark.skipif('SKIP_LONG_RUNNING_TESTS' in os.environ, reason='Impatient developer is impatient')
def test_failed_deletion(mocker):
    """Verify delete_volume raises an AssertionError when OpenStack volume has
    failed to successfully be deleted."""

    fake_backend = mocker.Mock(spec=testinfra.backend.base.BaseBackend)
    myhost = testinfra.host.Host(fake_backend)
    cr = mocker.Mock(spec=testinfra.backend.base.CommandResult)
    mocker.patch('testinfra.host.Host.run', return_value=cr)

    server = [{'ID': 'foo', 'Name': 'myvolume'}]
    cr.rc = 0
    cr.stdout = json.dumps(server)

    with pytest.raises(AssertionError):
        pytest_rpc.helpers.delete_volume('myvolume', myhost)

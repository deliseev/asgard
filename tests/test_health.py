from unittest import mock

import pytest

from asgard.main import app


@pytest.mark.asyncio
async def test_health():
    send_mock = mock.AsyncMock()
    _ = await app({'type': 'http'}, None, send_mock)

    assert send_mock.call_count == 2


def test_version():
    from asgard import version

    assert getattr(version, 'VERSION') is not None

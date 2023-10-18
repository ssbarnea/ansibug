# Copyright (c) 2023 Jordan Borean
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import collections.abc
import pathlib
import sys
import typing as t

import pytest

import ansibug.dap as dap

sys.path.append(str(pathlib.Path(__file__).parent / "utils"))

from dap_client import DAPClient


@pytest.fixture(scope="function")
def dap_client() -> collections.abc.Iterator[DAPClient]:
    with DAPClient() as client:
        client.send(
            dap.InitializeRequest(
                adapter_id="ansibug",
                client_id="ansibug",
                client_name="Ansibug Conftest",
                locale="en",
                supports_variable_type=True,
                supports_run_in_terminal_request=True,
            ),
            dap.InitializeResponse,
        )

        yield client

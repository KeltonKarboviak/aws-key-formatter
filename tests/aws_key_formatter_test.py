# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner

from aws_key_formatter import aws_key_formatter, cli


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string]


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    # TODO: Need to mock out the AWS Config file so we can
    # run some tests on the actual execution
    # result = runner.invoke(cli.main)
    # assert result.exit_code == 0
    # assert 'ACCESS_KEY_ID' in result.output
    # assert 'SECRET_ACCESS_KEY' in result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "aws_key_formatter" in help_result.output

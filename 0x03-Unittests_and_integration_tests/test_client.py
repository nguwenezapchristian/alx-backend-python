#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method."""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), {})
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Test _public_repos_url method."""
        payload = {"repos_url": "http://example.com/repos"}
        with patch.object(GithubOrgClient, 'org', return_value=payload):
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url,
                             "http://example.com/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method."""
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
                return_value="http://example.com/repos"):
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class((
    'org_payload',
    'repos_payload',
    'expected_repos',
    'apache2_repos'), [
    ({"name": "org_name"}, [{"name": "repo1", "license": {
     "key": "apache-2.0"}}, {"name": "repo2"}], ["repo1", "repo2"], ["repo1"])
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down test class."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method."""
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload]
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license parameter."""
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload]
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()

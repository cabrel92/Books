import os
import unittest
from unittest.mock import patch, mock_open, call
from generate_docker import DockerConfigGenerator  # Assuming your script is named docker_config_generator.py

class TestDockerConfigGenerator(unittest.TestCase):

    def setUp(self):
        self.template_dir = 'templates'
        self.generator = DockerConfigGenerator(template_dir=self.template_dir)
        self.context_file = 'config.json'
        self.target_dir = 'test'

    @patch('builtins.open', new_callable=mock_open, read_data='{"service_name": "my_service"}')
    def test_get_service_name(self, mock_file):
        service_name = self.generator.get_service_name(self.context_file)
        self.assertEqual(service_name, 'my_service')
        mock_file.assert_called_once_with(self.context_file, 'r')

    @patch('os.makedirs')
    @patch('generate_docker.DockerConfigGenerator.generate_file')
    @patch('generate_docker.DockerConfigGenerator.load_context_from_file')
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_all(self, mock_open, mock_load_context, mock_generate_file, mock_makedirs):
        mock_context = {
            "service_name": "my_service",
            "base_image": "python:3.9-slim",
            "copy_files": [
                {"src": "env_vars.txt", "dest": "/usr/src/app/env_vars.txt"},
                {"src": "export_env_vars.sh", "dest": "/usr/src/app/export_env_vars.sh"}
            ],
            "run_commands": [
                "chmod +x /usr/src/app/export_env_vars.sh",
                "./export_env_vars.sh"
            ],
            "env_vars": [
                {"name": "ENV_VAR1", "value": "value1"},
                {"name": "ENV_VAR2", "value": "value2"}
            ],
            "arguments": [
                "--arg1=value1",
                "--arg2=value2"
            ]
        }

        mock_load_context.return_value = mock_context

        self.generator.generate_all(self.context_file, self.target_dir)

        mock_makedirs.assert_called_once_with(self.target_dir, exist_ok=True)
        calls = [
            call('Dockerfile.j2', mock_context, os.path.join(self.target_dir, 'my_service_Dockerfile')),
            call('build.sh.j2', mock_context, os.path.join(self.target_dir, 'my_service_build.sh')),
            call('entrypoint.sh.j2', mock_context, os.path.join(self.target_dir, 'my_service_entrypoint.sh'))
        ]
        mock_generate_file.assert_has_calls(calls, any_order=True)

        # Check that files are being opened and written to
        expected_file_paths = [
            os.path.join(self.target_dir, 'my_service_Dockerfile'),
            os.path.join(self.target_dir, 'my_service_build.sh'),
            os.path.join(self.target_dir, 'my_service_entrypoint.sh')
        ]
        mock_open.assert_has_calls([call(path, 'w') for path in expected_file_paths], any_order=True)

if __name__ == '__main__':
    unittest.main()

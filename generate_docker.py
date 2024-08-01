import os
import json
from jinja2 import Environment, FileSystemLoader

class DockerConfigGenerator:
    def __init__(self, template_dir=None):
        if template_dir is None:
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate_file(self, template_name, context, output_path):
        template = self.env.get_template(template_name)
        content = template.render(context)
        with open(output_path, 'w') as file:
            file.write(content)
        print(f"{os.path.basename(output_path)} generated at {output_path}")

    def generate_dockerfile(self, context, output_path='Dockerfile'):
        self.generate_file('Dockerfile.j2', context, output_path)

    def generate_build_sh(self, context, output_path='build.sh'):
        self.generate_file('build.sh.j2', context, output_path)
        os.chmod(output_path, 0o755)  # Make the build script executable

    def generate_entrypoint_sh(self, context, output_path='entrypoint.sh'):
        self.generate_file('entrypoint.sh.j2', context, output_path)
        os.chmod(output_path, 0o755)  # Make the entrypoint script executable

    def load_context_from_file(self, context_file):
        with open(context_file, 'r') as file:
            context = json.load(file)
        return context

    def get_service_name(self, context_file):
        context = self.load_context_from_file(context_file)
        return context.get('service_name', 'default_service')

    def generate_all(self, context_file, target_dir):
        context = self.load_context_from_file(context_file)
        service_name = self.get_service_name(context_file)
        context['service_name'] = service_name  # Ensure service_name is in the context for Jinja2 templates

        os.makedirs(target_dir, exist_ok=True)
        self.generate_dockerfile(context, os.path.join(target_dir, f'{service_name}_Dockerfile'))
        self.generate_build_sh(context, os.path.join(target_dir, f'{service_name}_build.sh'))
        self.generate_entrypoint_sh(context, os.path.join(target_dir, f'{service_name}_entrypoint.sh'))

# Example usage
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 your_script_name.py config.json /app/dir/")
        sys.exit(1)

    context_file = sys.argv[1]
    target_dir = sys.argv[2]

    generator = DockerConfigGenerator()
    generator.generate_all(context_file, target_dir)

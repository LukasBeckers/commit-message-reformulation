# Commit Message Reformulation Server

This project provides a service that reformulates Git commit messages to follow the GitHub semantic commit messages convention using OpenAI's API. The service is Dockerized for easy deployment and can be accessed via a git hook from any repository.

## Features

- Reformulates commit messages to follow the GitHub semantic commit messages convention.
- Prompts the user to accept or reject the reformulated commit message.
- Dockerized for easy deployment and configuration using Docker Compose.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- OpenAI API Key

### Setup

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/commit-message-reformulation-server.git
   cd commit-message-reformulation-server
   ```

2. Set your OpenAI API key, your prefered model and the port in the docker-compose.yaml:

   ```
   -OPENAI_API_KEY="your_openai_api_key"
   -MODEL="gpt-4o-mini"
   -PORT=5000
   ```

3. Run the setup script:

   ```
   chmod +x ./setup.sh
   ./setup.sh
   ```

This script will:

- Move the git hook script to the `.git/hooks` directory.
- Make the git hook script executable.
- Build and start the Docker container.

### Usage

After running the setup script, the server will be running and accessible. To use the commit message reformulation service in another repository:

1. Copy the `prepare-commit-msg` hook script from the `.git/hooks` directory of this repository to the `.git/hooks` directory of your target repository:

   ```
   cp /path/to/this/repo/.git/hooks/prepare-commit-msg /path/to/your/other/repo/.git/hooks/
   chmod +x /path/to/your/other/repo/.git/hooks/prepare-commit-msg
   ```

2. Ensure the server is running and accessible from the target repository.

### License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

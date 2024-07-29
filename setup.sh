
#!/bin/bash

# Define variables
GIT_HOOKS_DIR=".git/hooks"
HOOK_SCRIPT="prepare-commit-msg"
HOOK_SOURCE="./prepare-commit-msg"
DOCKER_COMPOSE_FILE="docker-compose.yaml"
SERVER_DIR="commit_message_server"

# Check if the script is run from a git repository
if [ ! -d "$GIT_HOOKS_DIR" ]; then
  echo "This script must be run from the root of a git repository."
  exit 1
fi

# Move the git hook to the correct directory
if [ -f "$HOOK_SOURCE" ]; then
  cp "$HOOK_SOURCE" "$GIT_HOOKS_DIR/$HOOK_SCRIPT"
  chmod +x "$GIT_HOOKS_DIR/$HOOK_SCRIPT"
  echo "Git hook moved to $GIT_HOOKS_DIR and made executable."
else
  echo "Hook script $HOOK_SOURCE not found."
  exit 1
fi

cd $SERVER_DIR

# Start the server using Docker Compose
if [ -f "$DOCKER_COMPOSE_FILE" ]; then
  docker compose up -d --build
else
  echo "Docker Compose file $DOCKER_COMPOSE_FILE not found."
  exit 1
fi

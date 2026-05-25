#!/usr/bin/env bash

#------------------------------------------------------------------------------
# @file
# Builds a Hugo site hosted on a Cloudflare Worker.
#
# The Cloudflare Worker automatically installs Node.js dependencies.
#------------------------------------------------------------------------------

main() {

  DART_SASS_VERSION=1.93.2
  GO_VERSION=1.25.3
  HUGO_VERSION=0.152.2
  NODE_VERSION=22.20.0

  export TZ=Europe/Oslo
  INSTALL_ROOT="${HOME}/.local"

  BASE_URL="${HUGO_BASE_URL:-}"
  if [ -z "${BASE_URL}" ] && [ -f CNAME ]; then
    BASE_URL="https://$(tr -d '\n' < CNAME)"
  fi

  mkdir -p "${INSTALL_ROOT}"

  # Install Dart Sass
  echo "Installing Dart Sass ${DART_SASS_VERSION}..."
  curl -sLJO "https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
  rm -rf "${INSTALL_ROOT}/dart-sass"
  tar -C "${INSTALL_ROOT}" -xf "dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
  rm "dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
  export PATH="${INSTALL_ROOT}/dart-sass:${PATH}"

  # Install Go
  echo "Installing Go ${GO_VERSION}..."
  curl -sLJO "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz"
  rm -rf "${INSTALL_ROOT}/go"
  tar -C "${INSTALL_ROOT}" -xf "go${GO_VERSION}.linux-amd64.tar.gz"
  rm "go${GO_VERSION}.linux-amd64.tar.gz"
  export PATH="${INSTALL_ROOT}/go/bin:${PATH}"

  # Install Hugo
  echo "Installing Hugo ${HUGO_VERSION}..."
  curl -sLJO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
  rm -rf "${INSTALL_ROOT}/hugo"
  mkdir -p "${INSTALL_ROOT}/hugo"
  tar -C "${INSTALL_ROOT}/hugo" -xf "hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
  rm "hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
  export PATH="${INSTALL_ROOT}/hugo:${PATH}"

  # Install Node.js
  echo "Installing Node.js ${NODE_VERSION}..."
  curl -sLJO "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz"
  rm -rf "${INSTALL_ROOT}/node-v${NODE_VERSION}-linux-x64"
  tar -C "${INSTALL_ROOT}" -xf "node-v${NODE_VERSION}-linux-x64.tar.xz"
  rm "node-v${NODE_VERSION}-linux-x64.tar.xz"
  export PATH="${INSTALL_ROOT}/node-v${NODE_VERSION}-linux-x64/bin:${PATH}"

  # Verify installations
  echo "Verifying installations..."
  echo Dart Sass: "$(sass --version)"
  echo Go: "$(go version)"
  echo Hugo: "$(hugo version)"
  echo Node.js: "$(node --version)"

  # Configure Git
  echo "Configuring Git..."
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git config core.quotepath false
    if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
      git fetch --unshallow
    fi
  else
    echo "Skipping Git configuration because the build context is not a Git worktree."
  fi

  # Build the site
  echo "Building the site..."
  if [ -n "${BASE_URL}" ]; then
    echo "Using base URL: ${BASE_URL}"
    hugo --gc --minify --baseURL "${BASE_URL}"
  else
    hugo --gc --minify
  fi

}

set -euo pipefail
main "$@"

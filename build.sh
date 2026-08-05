#!/usr/bin/env bash

set -euo pipefail

HUGO_VERSION=0.152.2
INSTALL_ROOT="${HOME}/.local"
HUGO_ROOT="${INSTALL_ROOT}/hugo"
HUGO_TARBALL="hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"


resolve_base_url() {
  local base_url="${HUGO_BASE_URL:-}"

  if [ -z "${base_url}" ] && [ -f CNAME ]; then
    base_url="https://$(tr -d '\n' < CNAME)"
  fi

  printf '%s' "${base_url}"
}


install_hugo() {
  mkdir -p "${INSTALL_ROOT}"

  echo "Installing Hugo ${HUGO_VERSION}..."
  curl -fsSL -o "${HUGO_TARBALL}" \
    "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TARBALL}"
  rm -rf "${HUGO_ROOT}"
  mkdir -p "${HUGO_ROOT}"
  tar -C "${HUGO_ROOT}" -xf "${HUGO_TARBALL}"
  rm -f "${HUGO_TARBALL}"
  export PATH="${HUGO_ROOT}:${PATH}"
}


configure_git() {
  echo "Configuring Git..."
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "Skipping Git configuration because the build context is not a Git worktree."
    return
  fi

  git config core.quotepath false
  if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git -c fetch.recurseSubmodules=false fetch --unshallow
  fi
}


build_site() {
  local base_url

  base_url="$(resolve_base_url)"

  echo "Verifying Hugo installation..."
  echo "Hugo: $(hugo version)"

  configure_git

  echo "Building the site..."
  if [ -n "${base_url}" ]; then
    echo "Using base URL: ${base_url}"
    hugo --gc --minify --cleanDestinationDir --baseURL "${base_url}"
    return
  fi

  hugo --gc --minify --cleanDestinationDir
}


main() {
  install_hugo
  build_site
}


main "$@"

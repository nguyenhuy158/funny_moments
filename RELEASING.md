# Releasing

## Release Tag Naming

Release tags must follow semantic versioning with a `v` prefix:

- Stable release: `v1.2.3`
- Pre-release: `v1.2.3-rc.1`
- Pre-release: `v1.2.3-beta.2`

Accepted pattern:

```text
^vMAJOR.MINOR.PATCH(-SUFFIX)?$
```

Rules:

- `MAJOR`, `MINOR`, and `PATCH` are non-negative integers.
- `SUFFIX` is optional and is used for pre-releases such as `rc.1`, `beta.2`, or `alpha.1`.
- Tags that do not start with `v` are rejected by release CI.

## Release CI

The release workflow lives in `.github/workflows/release.yml`.

It runs when:

- A Git tag matching `v*` is pushed
- The workflow is triggered manually with `workflow_dispatch`

The workflow will:

1. Validate the tag format
2. Build the Hugo site in production mode
3. Copy `CNAME` into the built site when present
4. Package `public/` as `funny-moments-<tag>.tar.gz`
5. Create a GitHub Release and upload the artifact

## Create a Release

Create and push a stable release tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Create and push a pre-release tag:

```bash
git tag v1.1.0-rc.1
git push origin v1.1.0-rc.1
```

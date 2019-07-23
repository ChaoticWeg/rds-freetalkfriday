#!/usr/bin/env bash
thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pushd "${thisdir}" >/dev/null 2>&1

python create.py

popd >/dev/null 2>&1


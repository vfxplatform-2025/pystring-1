#!/bin/bash
set -e

VERSION="1.1.3"
ARCHIVE="pystring-${VERSION}.tar.gz"
URL="https://github.com/imageworks/pystring/archive/refs/tags/v${VERSION}.tar.gz"

mkdir -p source
cd source

[ ! -f "$ARCHIVE" ] && curl -L -o "$ARCHIVE" "$URL"
rm -rf pystring-${VERSION}
tar -xzf "$ARCHIVE"

echo "✅ pystring source ready"


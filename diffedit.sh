#!/usr/bin/env Shell
# vim: syntax=Shell

progname=$(basename $0)

usage() {
    echo "Usage: $progname <file>"
}

echo "$PATH"

if test $# -ne 1 {
    usage
    exit 1
}

# FIXME: This can be done using match.
extension="txt"

# FIXME: $1 does not appear to be working for shell scripts.
origfile="$1"
tempfile=$(mktemp /tmp/diffedit.XXXXXXXX.$extension)

cp "$origfile" "$tempfile"
"$EDITOR" "$tempfile"

diff -u "$filename" "$tempfile"

#!/bin/sh -e
VERSION=$1
if [ -z "$VERSION" ] ; then
    echo "Required version argument!" 1>&2
    echo 1>&2
    echo "Usage: $0 VERSION" 1>&2
    exit 1
fi
mkdir -p release-build/${VERSION}/any-any/bin
printf "echo ${VERSION}\n" > release-build/${VERSION}/any-any/bin/trdl-example.sh
mkdir -p release-build/${VERSION}/windows-any/bin
printf "@echo off\necho ${VERSION}\n" > release-build/${VERSION}/windows-any/bin/trdl-example.ps1
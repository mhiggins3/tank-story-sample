#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
pushd $script_dir
echo $script_dir
mkdir -p $script_dir/build
cp -r * build
cd build
for i in `cat ../Modules`
do
    pip3 install $i -t ./
done
chmod -R 755 .
zip -r build.zip ./
popd

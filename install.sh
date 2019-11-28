apt-get install -y libboost-graph-dev libboost-iostreams-dev libgmp3-dev zlib1g-dev liblzma-dev libjemalloc-dev cmake cmake-data
mkdir build ; cd build ; cmake .. ; make install
mv /usr/local/bin/toulbar2 /usr/local/share/pracmln/toulbar2
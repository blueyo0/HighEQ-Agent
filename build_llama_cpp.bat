cd thirdparty/llama.cpp
if not exist build (
    mkdir build
) 
cd build
cmake ..
cmake --build . --config Release
cd ../../..
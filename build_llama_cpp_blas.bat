cd thirdparty/llama.cpp
if not exist build_blas (
    mkdir build_blas
) 
cd build_blas
cmake .. -DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=Intel10_64lp -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx
cmake --build . --config Release
cd ../../..
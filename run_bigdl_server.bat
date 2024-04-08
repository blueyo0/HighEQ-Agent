echo using %1
cd /d %~dp0

@REM start thirdparty\llama.cpp\build_blas\bin\Release\server.exe -m models\internlm2-chat-7b.Q4_K_M.gguf -c 1024 --port 8040 --log-disable --chat-template chatml &
@REM start thirdparty\llama.cpp\build_blas\bin\Release\server.exe -m models\Qwen-7B-Chat.Q4_K_M.gguf -c 1024 --port 8030 --log-disable --chat-template chatml  &
@REM start thirdparty\llama.cpp\build_blas\bin\Release\server.exe -m models\qwen1_5-4b-chat-q3_k_m.gguf -c 1024 --port 8031 --log-disable --chat-template chatml  &
start bigdl\server.exe -m D:\Public\High_EQ_Trainer-main\models\7B-chat\Qwen-7B-Chat.Q4_K_M.gguf -t 8 -ngl 33 --port 8030 --log-disable --chat-template chatml &
echo start all bigdl server
echo using %1
cd /d %~dp0

set http_proxy=http://proxy-prc.intel.com:913/
set https_proxy=http://proxy-prc.intel.com:913/
set no_proxy=localhost,127.0.0.*

echo ====current proxy：
echo %http_proxy%
echo %https_proxy%
echo %no_proxy%

python demo.py

rm testfile.dat
touch testfile.dat 
rm testfilefixed.dat 
touch testfilefixed.dat 

set -x

testcase="concurrenttest"

curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" 

sleep 10

curl --url "http://localhost:5000/${testcase}" 


testcase="concurrenttestfixed"

curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" & 
curl --url "http://localhost:5000/${testcase}" 

sleep 10

curl --url "http://localhost:5000/${testcase}" 


URL=http://127.0.0.1:8000

curl --request POST -H "Content-Type: application/octet-stream" --data-binary @DE0_TOP.sof $URL/sof

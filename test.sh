while true
do
    wget --no-check-certificate --quiet \
  --method GET \
  --timeout=0 \
  --header '' \
   'http://192.168.254.17/drcom/login?callback=dr1635488822195&DDDDD=｛账号｝@｛运营商｝&upass=｛密码｝'
    echo "ok"
    sleep 1h
    cd /
    rm login*
done
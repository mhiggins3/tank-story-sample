#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
do
curl -d "{\"date\":\"2019-02-$i 16:43:40\",\"measure\":\"199\",\"out_temp\":\"44\",\"house_temp\":\"67\",\"tank_temp\":\"53\",\"burner_state\":\"on\"}" -H "Content-Type: application/json" -X POST https://475lrvm7v7.execute-api.us-east-1.amazonaws.com/production/sample/d2f702a1-36f8-11e9-8305-acde48001122
done


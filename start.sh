#!/bin/bash
# Simple start script for lottopy designed by Matteo DiBiagio 
# www.wvlotterypredictor.xyz
# MIT License
# Edit to your need

echo "Powerball" && 
python lottopy_pb.py && 
echo "MegaMillions" && 
python megamil.py && 
echo "Lotto America" && 
python lotto_america.py &&
echo "Daily3" && 
python daily3.py && 
echo "Daily4" && 
python daily4.py &&
echo "Cash25" && 
python cash25.py

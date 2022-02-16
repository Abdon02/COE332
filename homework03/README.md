# README.md file concerns the files: 'hw03_part2.py' and 'test_hw03_part3.py'

  Before I start talking about 'hw03_part2.py' and 'test_hw03_part3.py' it is important that we download the JSON
  file that contains the water data. This data will be used in to find the turbidity and the time it will take
  for the water to be in the "safe" level for water consumption.

  To download the JSOPN file, follow these steps
  1.- Go to the directory where you want this file to be
  2.- copy and paste this into your terminal: 
      wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
  *The data get updated every day, so the results may vary when it is time to make calculations*

  The purpose of 'hw03_part2.py' is to calculate the average Turbidity of the water from the last 5 recent 
  recordings. To calculate the Turbidity, you use this formula, T= a0 * I90, where T is Turbidity,
  a0 is Calibration Constant, I90 is the Ninety degree dectector.  
  There is a turbidity threshold, meaning that if the turbidity that was calculated is over the threshold it is
  not safe to drink that water. If the turbidity is less than or equal to the Turbidity Threshold, then it is 
  safe to consume. 
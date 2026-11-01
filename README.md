## [Sieve_Analysis.py](https://github.com/shreyanspeaking-arch/Sieve-Analysis/blob/main/Sieve_Analysis.py)

**🧰 Prerequisites**

- **Software**
  - Python 3
  - `pandas`
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `openpyxl`
  - Install the packages with `pip install pandas numpy scipy matplotlib openpyxl`
- **Choices you will be asked to make** (type the value shown)
  - Input method: `1` read a CSV or Excel file, `2` type the values in
  - Plot the % finer against sieve size: `Yes` or `No`
  - Look up the particle size at a percentile (such as D10, D30 or D60): press Enter for yes, or `No` to skip
- **Data to have ready**
  - The sieve sizes with units (`mm` or `µm`) and the weight retained (g) on each, plus the weight retained on the pan
  - For a file: the file name with its extension (`.csv` or `.xlsx`), and the names of the columns holding each value
  - The actual total weight of the sample (g)
  - The maximum allowed percentage error
  - A name for the output Excel file, typed without `.xlsx`

1. This program performs the sieve analysis of a soil or aggregate sample, computing the percentage of the sample retained on and passing through each sieve, and plotting the particle size distribution curve of % finer against sieve size. It works for only one material at a time.
2. The user either reads the sieve sizes and weights retained from a CSV or Excel file, or enters them manually sieve by sieve along with the weight retained on the pan. Sieve sizes are entered with their unit, in mm or µm, and weights in g. If the file does not contain columns named Sieve Size and Weight Retained (in g), the user is shown the available columns and asked which ones to use, and a last row named Pan is taken as the weight retained on the pan.
3. The program adds up the weights retained on all sieves and the pan, shows this total, and asks for the actual total weight of the sample and the maximum allowed percentage error, so that the total from the table can be checked against the weight of the sample.
4. For each sieve the program computes the % weight retained, the cumulative % weight retained and the cumulative % weight passing (% finer), and exports this table to an Excel file.
5. If the user wants, the program plots % finer against sieve size on a logarithmic scale, with a smooth curve fitted through the points using PCHIP interpolation.
6. The user can then find the sieve size corresponding to any percentile of % finer from this curve, such as D10, D30 or D60, repeated for as many percentiles as desired.

`Soil Lab Graph.png` is a sample % finer vs sieve size graph created using this program.

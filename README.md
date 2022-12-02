# ROXBASE Scripts

Collections of the scripts that I used to automate data generation for ROXBASE and other useful scripts

## How to use
1. Extract `TextAssets` and  `Sprites` from the APK, the simplest method is to use [AssetsStudio](https://github.com/Perfare/AssetStudio)
2. Run the `./src/clean_text.py` on the folder where the assets located, when being run successfully, you should be able to see the results like the files under the `./input/` folder
3. To parse the data, you can open `ROXBASE_Automatic_Data_Parser_v1_0_5.ipynb` using Jupyter Notebook (I usually use Google Colab, as its free and super fast) or you can convert the `.ipynb` file to `.py` if you want to run it from the command line, successful ran will give you the tabular data located in the `./output/` folder

PS: Pardon the noodley codes, hadn't had the time to comment it properly but each header on the `.ipynb` should be self-explanatory
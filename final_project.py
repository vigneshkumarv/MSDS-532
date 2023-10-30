"""
Final Project Topic 2: Analysis of carAd data set to determine the most influencial attributes when predicting vehicles price.
October 18, 2023
Vignesh Kumar Venkateshwar
"""

"""
Note: This code was initially written in Jupyter Notebook and then imported here.
      This version has most print statements removed, only essential ones have been retained.
"""

# Imports
import pyreadr as pyr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.inspection import permutation_importance

# Read dataset followed by data frame
carAd_file = pyr.read_r('E:/UC/Fall_2023/MSDS532/car_ads_fp.RData')
carAd = carAd_file["carAd"]
carAd = pd.DataFrame(carAd)
carAd.reset_index(drop = True, inplace = True)

# Determine car models to keep for analysis
models_to_keep = ['L200', 'Q3', 'CX-5', 'XC90']
carAd_model = carAd.loc[carAd['Genmodel'].isin(models_to_keep)]

# Determine fuel types to keep for analysis
fuel_types_to_keep = ['Diesel', 'Petrol']
carAd_model_fuel = carAd_model.loc[carAd_model['Fuel_type'].isin(fuel_types_to_keep)]

# Determine car body types to keep for analysis
Bodytypes_to_keep = ['SUV', 'Pickup']
carAd_model_fuel_body_type = carAd_model_fuel.loc[carAd_model_fuel['Bodytype'].isin(Bodytypes_to_keep)]

# Determine car colors to keep for analysis
color_frequency = carAd_model_fuel_body_type['Color'].value_counts()

colors_to_keep = ['Black', 'White', 'Grey', 'Silver', 'Blue', 'Red']
carAd_filtered = carAd_model_fuel_body_type.loc[carAd_model_fuel_body_type['Color'].isin(colors_to_keep)]

# Drop columns not required for analysis
columns_to_drop = ['Maker', 'Genmodel_ID', 'Adv_ID', 'Adv_month', 'Engin_size', 'Gearbox', 'Seat_num', 'Door_num']
carAd_filtered = carAd_filtered.drop(columns_to_drop, axis=1)

# Convert datatypes of 'Runned_Miles' and 'Price' from object to numeric
carAd_filtered['Runned_Miles'] = pd.to_numeric(carAd_filtered['Runned_Miles'], errors='coerce')
carAd_filtered['Price'] = pd.to_numeric(carAd_filtered['Price'], errors='coerce')

# Identify fields requiring encoding
objs = carAd_filtered.select_dtypes(include = np.object_).columns.tolist()

# Instantiate encoder and model
ohe = OneHotEncoder()
cTrans = make_column_transformer((ohe, objs), remainder = "passthrough")
etr = ExtraTreesRegressor(random_state = 75, max_features = None, verbose = 1)

# Fit Encoder
cTrans.fit(carAd_filtered)

# Establish Pipeline
pipe = Pipeline(steps = [('ctrf', cTrans), ('model', etr)])

# Define the target variable
target_col = 'Price'
X = carAd_filtered.drop(target_col, axis = 1)
Y = carAd_filtered[target_col]

# Split data for training and testing
x, testX, y, testY = train_test_split(X, Y, test_size = .3, random_state = 1 )

# Train model
pipe.fit(x, y)
trPr = pipe.predict(x)

# Test model
pred = pipe.predict(testX)

# Visualization of predicted vs actual values
fig, ax = plt.subplots()
ax.scatter(pred, testY, edgecolors = (0,0,1))
ax.plot([testY.min(), testY.max()],
        [testY.min(), testY.max()],
         'r--', lw = 3)
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Actual Values')
plt.show(block = True)

imps = pipe.named_steps["model"].feature_importances_

one_hot_cat = pipe.named_steps["ctrf"].named_transformers_["onehotencoder"].categories_
indeps = carAd_filtered.iloc[:, carAd_filtered.columns != "Price"].columns.tolist()

# List to house the lables that were used in the model
features = []
for each in indeps:
    if each in objs:
        spot = objs.index(each)
        # For each one hot label, prefix column name and underscore to label
        one_hot_mess = [each + "_" + str(what) for what in one_hot_cat[spot]]
        features.extend(one_hot_mess)          # Extend a list with another iterable
    else:
        features.append(each)                  # Append item to the list

influencers = pd.DataFrame({"Features" : features,
                            "Importance" : imps}).sort_values(by = "Importance", ascending = False)
print(influencers)

# Collect permutation
perm_imps = permutation_importance(pipe, x, y, n_repeats = 5, random_state = 1)
perm_sorts = perm_imps.importances_mean.argsort()    # Create an array for sorting

# Create an offset index for plotting
indices = np.arange(0, len(imps)) + .5

# Get features order for permutation
perms_df = pd.DataFrame({"Features" : indeps,
                        "Permutation": perm_imps.importances_mean}).sort_values(by = "Permutation", ascending = False)
print(perms_df)

# Visualize differences between importance measures
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 8))

# Convert influencers into a list and reverse it
label_list = influencers["Features"].tolist()
reversed_list = label_list[::-1]
# Horizontal bar graph of original importance values
ax1.barh(indices, imps[np.argsort(imps)], height = .7)
ax1.set_yticks(indices)
ax1.set_yticklabels(reversed_list)
ax1.set_ylim((0, len(imps)))

# Box plot showing permutation importance across n_repeats
ax2.boxplot(perm_imps.importances[perm_sorts].T,
            vert = False, labels = perms_df["Features"].tolist(),
            patch_artist = True,
            boxprops = {'color':'black', 'edgecolor': "black"})
fig.tight_layout()
plt.show(block = True)
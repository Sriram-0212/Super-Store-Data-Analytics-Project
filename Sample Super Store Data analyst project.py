import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

#Data Exploration:
# Reading CSV file into a Data Frame
df = pd.read_csv('C:/Users/DELL/Downloads/SampleSuperstore.csv')

#Exploring Shape:
print("Strucure of Data Frame : ",df.shape)

#Exploring all datatypes.
print("Each columns Data Types : ",df.dtypes)

#Exploring Information about data set.
print("Describing Data Frame : ",df.describe())
print("Information about Data Frame : ",df.info())

#Exploring Columns and some rows.
print("All Columns : ",df.columns)
print("First 5 rows : ",df.head())
print("last 5 rows : ",df.tail())
print("row 50 to 60 : ",df.loc[50:60])

# Unique of all Categories.
print('Category Categories : ',df['Category'].unique())
print('Sub-Categories : ',df['Sub-Category'].unique())
print('Ship Mode Categories : ',df['Ship Mode'].unique())
print('Segment Categories : ',df['Segment'].unique())
print('City Categories : ',df['City'].unique())
print('State Categories : ',df['State'].unique())

#Value Counts of Categorical columns
print(df['Category'].value_counts())
print(df['Sub-Category'].value_counts())
print(df['City'].value_counts())
print(df['State'].value_counts())
print(df['Segment'].value_counts())

#Checking for null values
print(df.isna().sum())

#Checking for Duplicated Values.
print(df.duplicated().sum())

#Data Cleaning:

#Changing Data Types of postal code and Quantity.

df['Postal Code'] = df['Postal Code'].astype(object)
df['Quantity'] = df['Quantity'].astype(float)

#Removing Duplicates.

df = df.drop_duplicates()

#Descriptive Statistics:
#Total_Sales.

Total_sales = df['Sales'].sum()
print("Total_Sales :" , Total_sales)

#Average Order value.

Avg_ord_val = df['Sales'].mean()
print("Average_Order_value : ", Avg_ord_val)

#Total Quantity.

Total_Quantity = df['Quantity'].sum()
print("Total_Quantity : ",Total_Quantity)

#Total Discount.

Total_Discount = df['Discount'].sum()
print("Total_Discount : ", Total_Discount)

#Total_Proit.

Total_Profit = df['Profit'].sum()
print("Total_Profit : ", Total_Profit)

#Visualizing Distribution of Sales,Order Quantity and relevent Metrics:
#Distribution of Sales.
plt.figure(figsize=(10,6))
plt.hist(df['Sales'],bins=100,color='red')
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Distribution of Sales")
plt.show()

#Distribution of Order Quantity.
plt.figure(figsize=(10,6))
plt.hist(df['Quantity'],bins=100)
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.title("Distribution of Quantity")
plt.show()

#Distribution of Profit.
plt.figure(figsize=(10,6))
plt.hist(df['Profit'],bins=100,color='green')
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.title("Distribution of Profit")
plt.show()

#Distribution of Discount.
plt.figure(figsize=(10,6))
plt.hist(df['Discount'],bins=100,color='orange')
plt.xlabel("Discount")
plt.ylabel("Frequency")
plt.title("Distribution of Discount")
plt.show()

#Customer Segmentation:


#Calculating total sales for each Segment.

Total_Sales_Per_Segment = df.groupby('Segment')['Sales'].sum()

#Calculating total orders for each Segment.

Total_orders_per_segment = df.groupby('Segment').size()

# Calculate average order value for each Segment.
average_order_value_per_customer = df.groupby('Segment')['Sales'].mean()

#Segment Customers Based on purchasing Behaviour.
Segment_Customers = pd.DataFrame({'Total_Sales' : Total_Sales_Per_Segment,
                                  'Total_orders' : Total_orders_per_segment,
                                  'Average_order_value' : average_order_value_per_customer})
print(Segment_Customers)

#Analyze the characteristics of each customer segment.

# Calculate total sales for each customer segment
Total_sales_per_segment = df.groupby('Segment')['Sales'].sum()

# Calculate total profit for each customer segment
Total_profit_per_segment = df.groupby('Segment')['Profit'].sum()

# Calculate average discount for each customer segment
Average_discount_per_segment = df.groupby('Segment')['Discount'].mean()

# Calculate average quantity sold for each customer segment
Average_quantity_per_segment = df.groupby('Segment')['Quantity'].mean()
     

# Analyzing characteristics of each customer segment.

Segment_characteristics = pd.DataFrame({
    'Total Sales': Total_sales_per_segment,
    'Total Profit': Total_profit_per_segment,
    'Average Discount': Average_discount_per_segment,
    'Average Quantity': Average_quantity_per_segment
})

print("Characteristics of Each Customer Segment:")
print(Segment_characteristics)

#Product Analysis:
#Identifying the top-selling products and categories.

Total_sales_per_product = df.groupby('Sub-Category')['Sales'].sum()

# Identifying top-selling products

Top_selling_products = Total_sales_per_product.sort_values(ascending=False).head(10)

# Printing the top-selling products

print("Top Selling Products:")
print(Top_selling_products)

# Calculating total sales for each category.

Total_sales_per_category = df.groupby('Category')['Sales'].sum()

# Identifying top-selling categories.

Top_selling_categories = Total_sales_per_category.sort_values(ascending=False)

# Printing the top-selling categories

print("Top Selling Categories:")
print(Top_selling_categories)

#Analyzing the performance of products over time:
# Assuming 'Sales' and 'Profit' columns are available in the dataset as there is no date column in data
# Aggregating data by product category and calculate total sales and profit
Product_performance = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Sort the data by total sales in descending order
Product_performance = Product_performance.sort_values(by='Sales', ascending=False)

# Print the top performing products based on total sales and profit
print(Product_performance)

#Visualizing Product Performance.
colors = ['skyblue', 'pink']
Product_performance.plot(x='Category', y=['Sales', 'Profit'], kind='bar',color=colors)
plt.title('Product Performance by Sales and Profit')
plt.xlabel('Product Category')
plt.ylabel('Amount')
plt.show()

#Time Series Analysis:
print("Time Series Analysis : ")
print("""The dataset 'Superstore Sales' does not include a date column, which means that time series analysis is not possible.
and also it' not possible to Examine sales trends over different time periods""")

#Visualization:

# Distribution of sales by category

plt.figure(figsize=(10, 6))
sns.barplot(x="Category", y="Sales", data=df, color='skyblue')
plt.title("Distribution of Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#Distribution of Sales by Region.
plt.figure(figsize=(10, 6))
sales_by_region = df.groupby('Region')['Sales'].sum()
sales = sales_by_region.values
categories = sales_by_region.index
plt.pie(x=sales,labels=categories,autopct='%1.1f%%')
plt.legend(title='Sales by Region')
plt.show()

#  Distribution of Profit by region

plt.figure(figsize=(10, 6))
sns.boxplot(x="Region", y="Profit", data=df)
plt.title("Distribution of Profit by region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()


# Histogram of Sales

plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=20, kde=True)
plt.title('Histogram of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

#kde plot of distribution of sales.
plt.figure(figsize=(10, 6))
sns.kdeplot( x = df['Sales'])
plt.title("kde plot of distribution of sales")
plt.show()

# Ship Mode counts.

plt.figure(figsize=(10, 6))
sns.countplot(x='Ship Mode', data=df, color="violet")
plt.title('Count of Ship Modes')
plt.xlabel('Ship Mode')
plt.ylabel('Count')
plt.show()

# Scatter plot of Sales vs Segment

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Segment', data=df, hue='Category')
plt.title('Sales vs Segment')
plt.xlabel('Sales')
plt.ylabel('Segment')
plt.show()



#Correlation of Numeric_Columns.
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.title("Correlation of Numeric Columns")
plt.show()

#Pairplot of Dataframe.

columns = ['Sales', 'Quantity', 'Discount', 'Profit','Region']
sns.pairplot(df[columns], hue='Region', palette='Set2')
plt.show()

# Sub-Category Counts.

plt.figure(figsize=(10, 6))
plt.rcParams['font.size'] = 5
sns.countplot(x='Sub-Category', data=df,palette='muted')
plt.title('Count of Sub_Category')
plt.xlabel('Ship Mode')
plt.ylabel('Count')
plt.show()




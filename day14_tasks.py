import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder for plots
os.makedirs("plots", exist_ok=True)

# Load and clean data
df = pd.read_csv('sales.csv')
df.dropna(inplace=True)

# Line Chart: Monthly Revenue
plt.figure(figsize=(10, 5))
sns.lineplot(x='Month', y='Revenue', data=df)
plt.title('Monthly Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/Line_Chart.png")
plt.close()

# Bar Chart: Product Sales
product_sales = df.groupby('Product')['Sales'].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='Product', y='Sales', data=product_sales)
plt.title('Product Sales')
plt.tight_layout()
plt.savefig("plots/Bar_Chart.png")
plt.close()

# Pie Chart: Market Share
market_share = df['Region'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(market_share, labels=market_share.index, autopct='%1.1f%%')
plt.title('Market Share by Region')
plt.savefig("plots/Pie_Chart.png")
plt.close()

# Heatmap: Correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("plots/Heatmap.png")
plt.close()

# Summary Report
with open("plots/Summary_Report.txt", "w") as f:
    f.write("Summary:\n")
    f.write(df.describe().to_string())

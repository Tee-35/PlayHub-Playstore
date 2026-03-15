<a name="top"></a>
## 🎮  Playhub - Gamestore - Project Background

***Monthly Sales Performance Report – Finance Analysis Summary***

Play Hub is an online retailer specialising in gaming consoles and IT equipment, offering products such as PlayStation 5 consoles, AirPods, and Google Pixel devices. This analysis was done using Python with Pandas, NumPy & Google Looker to uncover purchasing trends and operational insights. The review demonstrates how data-driven insights can support stronger business performance.  

The review will provide recommdations the following key areas:  

-  **[Key Findings](#Key-Findings)**  
-  **[Commercial Impact, Geographical Insights & Fraud Risk Highlights](#Commercial-impact-geographical-insights--fraud-risk-highlights)**
-  **[Next Analytical Steps](#Next-Analytical-Steps)**  
-  **[Recommended Business Focus Areas](#Recommended-Business-Focus-Areas)**  

The Python code used in Pandas to clean the data is [here](Dataset/syntax.md).   
The dataset csv file used to for the project is [here](Dataset).   

---


### Overview of Key KPIs  

The latest monthly sales dashboard indicates strong commercial performance with total **revenue reaching £2.30m across 5,000 orders**. **Website orders** account for **56% of total transactions**, highlighting the continued importance of digital channels in overall revenue generation. Month-on-month revenue growth stands at **25%**, demonstrating significant momentum in sales performance and suggesting successful marketing and demand generation strategies during the reporting period.
The **most ordered product is the Xbox Series X**, confirming strong consumer demand for high-value gaming products. Payment retry rates remain relatively low at **3% of total orders**, suggesting that the majority of transactions are successfully processed on first attempt, though retry activity should still be monitored due to potential operational or fraud implications.

Click [here](dashboard.jpg) to view the dashboard.  

### Key Findings
Revenue distribution across cities reveals that **Manchester generated the highest revenue (£608k)**, followed by **London (£492k)** and **Glasgow (£368k)**. Order volumes follow a similar pattern, with **Manchester recording the highest number of orders (1,209)**. While London ranks second in order volume (996), its revenue per order appears relatively high, suggesting a higher proportion of premium product purchases.  

Marketing channel analysis shows revenue is **fairly evenly distributed across acquisition channels**, with search, social, affiliate, direct, and email each contributing between approximately **£433k and £458k**. This balanced distribution indicates diversified customer acquisition, reducing dependency on a single marketing source. Orders by channel also remain consistent (around 900–950 orders each), reinforcing the effectiveness of the multi-channel marketing strategy.  

[⬆ Back to top](#top) 

### Commercial Impact, Geographical Insights & Fraud Risk Highlights  

From a commercial perspective, **Manchester and London remain the key revenue-driving markets**, together contributing a significant share of total sales. Manchester leads in order volume, suggesting strong demand and effective customer acquisition in that region. However, **London’s relatively high revenue compared with its order volume suggests higher-value purchases**, likely driven by premium electronics products. 

Reattempted order analysis highlights potential operational or fraud-related considerations. **London shows the highest number of reattempted orders (105)**, significantly exceeding other cities such as Manchester (18) and Glasgow (9). This may indicate payment friction, system retries, or potential fraudulent activity requiring further investigation.  

Platform analysis reveals that **mobile app transactions account for the majority of reattempted orders (120)** compared with **30 from the website**. This suggests that mobile payment flows may require further review to identify technical issues or customer authentication challenges.  

From a product perspective, **high-value electronics products dominate reattempted transactions**, with the Xbox Series X showing notable retry activity. High-value goods often attract higher fraud attempts, meaning monitoring and fraud controls should remain a priority. 

[⬆ Back to top](#top)  

### Next Analytical Steps

To strengthen commercial performance and risk monitoring, the following analytical steps are recommended:  

- **Monitor high-value product sales in London**, particularly gaming consoles and electronics, to ensure strong revenue growth while maintaining fraud safeguards.  
- **Analyse mobile app payment flows** , given the high concentration of payment retries on the mobile platform, to identify potential technical or user experience issues.  
- **Conduct deeper fraud risk analysis on reattempted orders** , focusing on London and high-ticket products where abnormal retry behaviour may indicate fraud attempts.  
- **Evaluate marketing channel ROI**, ensuring that channels delivering strong order volume continue to generate profitable customer acquisition.

[⬆ Back to top](#top)

### Recommended Business Focus Areas

Strategically, the business should prioritise:

- 	**London**  for high-value product sales optimisation and fraud monitoring. 
- 	**Manchester**  for continued order volume growth and customer acquisition.  
- 	**Mobile app platform**  improvements to reduce payment retry rates.  
- 	**High-value product categories,**  particularly gaming consoles and electronics.
  
Overall, the business demonstrates strong revenue growth and balanced marketing performance, with targeted improvements in payment monitoring and platform optimisation expected to further strengthen profitability and operational resilience.

[⬆ Back to top](#top)  






# Books
Starting point 
[24/06 à 07:53] Cabrel N'gako: ### CPU and Memory Utilization Analysis with Prometheus

#### Introduction
The aim of this analysis is to evaluate the average CPU and memory resource usage of our Spark nodes over periods of one week and one month. The aim is to understand resource consumption trends, identify peak usage periods and propose recommendations for optimal resource management.

#### Methodology

##### Data source
The data used in this analysis comes from Prometheus, a time-series database collecting metrics from Spark nodes. The specific metrics analyzed are:
- `node_memory_MemAvailable_bytes`
- node_memory_MemTotal_bytes
- `node_cpu_seconds_total` (idle mode)

##### Calculation formula
To calculate average resource usage, we use the following formulas:

###### Memory
\[ \text{Average_Memory}(T) = \left(1 - \frac{\text{avg\_over\_time}(\text{node_memory\_MemAvailable\_bytes}[T])}{\text{avg\_over\_time}(\text{node_memory\_MemTotal\_bytes}[T])}\right) \times 100 \]

###### CPU
\times = \left(1 - \text{avg\_over\_time}(\text{rate}(\text{node\_cpu\_seconds_total}\{mode="idle"\}[1m])[T])}right) \times 1
00 \]

### Results

Translated with DeepL.com (free version)
[24/06 à 07:54] Cabrel N'gako: #### Week period

##### Memory usage
For a one-week period, the formula is :
\[ \text{Average_Memory}(1 \text{week}) = \left(1 - \frac{\text{avg\_over\_time}(\text{node_memory\_MemAvailable_bytes}[7d])}{\text{avg\_over\_time}(\text{node_memory\_MemTotal\_bytes}[7d])}\right) \times 100 \]

The results show that the average memory usage over a week is **X%**. There are noticeable variations during working hours and periods of low activity. Peak usage corresponds to times when workloads are highest.

##### CPU utilization
For a one-week period, the formula is :
\text{Average_CPU}(1 \text{week}) = \left(1 - \text{avg\_over\_time}(\text{rate}(\text{node\_cpu\_seconds\_total}{mode="idle"\}[1m])[7d])\right) \times 100 \]

The results show that average CPU usage over a week is **Y%**. Peaks in utilization are mainly observed at the beginning of the week, corresponding to the start-up of data processing tasks.

#### Monthly period


Translated with DeepL.com (free version)
[24/06 à 07:54] Cabrel N'gako: ##### Memory usage
For a period of one month, the formula is:
\[ \text{Average_Memory}(1 \text{month}) = \left(1 - \frac{\text{avg\_over\_time}(\text{node_memory\_MemAvailable_bytes}[30d])}{\text{avg\_over\_time}(\text{node_memory\_MemTotal\_bytes}[30d])}\right) \times 100 \]

The results show that average memory usage over one month is **Z%**. There is an upward trend in memory usage towards the end of the month, which could be linked to data accumulation or long processes.

##### CPU usage
For a one-month period, the formula is :
\text{Average_CPU}(1 \text{month}) = \left(1 - \text{avg\_over\_time}(\text{rate}(\text{node\_cpu\_seconds\_total}\{mode="idle"\}[1m])[30d])\right) \times 100 \]

The results show that average CPU usage over a month is **W%**. There is a relatively stable utilization with some sporadic peaks, probably due to specific resource-intensive tasks.

### Analysis and Interpretation

#### Memory usage
Analysis of the data over one week and one month reveals that memory usage is generally stable, but spikes can occur depending on data processing tasks. The upward trend over a month could indicate a growing need for memory, perhaps requiring task optimization or an increase in memory capacity.


Translated with DeepL.com (free version)
[24/06 à 07:55] Cabrel N'gako: #### CPU utilization
CPU utilization is equally stable over both periods, with peaks corresponding to peak hours and the start of the week. These observations suggest that the nodes are well balanced, but that there may be times when additional resources would be beneficial.

### Conclusions and Recommendations

#### Summary of Conclusions
CPU and memory resource utilization is relatively stable over one-week and one-month periods, with expected variations due to workloads. However, the upward trend in long-term memory usage requires particular attention.

#### Recommendations
1. **Continuous monitoring**: Continue to monitor resources for emerging trends and anomalies.
2. **Task Optimization**: Review data processing tasks to optimize memory use.
3. **Additional Capacity**: Consider adding memory and CPU resources during identified peak periods to avoid bottlenecks.
4. **Capacity Planning**: Use historical data to plan future capacity and guarantee optimum performance.

### Appendices

#### Charts and Data Tables
Include Grafana-generated graphs and data tables detailing resource utilization over the specified peri
specified periods.
[24/06 à 07:56] Cabrel N'gako: **Example graphics:**

1. Graph of memory usage over one week.
2. Graph of CPU usage over one week.
3. Graph of memory usage over a month.
4. Graph of CPU usage over one month.

By following this structure, you can draw up a complete and detailed analysis of CPU and memory usage using the data collected by Prometheus
https://medium.com/cuddle-ai/async-architecture-with-fastapi-celery-and-rabbitmq-c7d029030377

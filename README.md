# Data Science: Mapping income inequality to the ECI

Data Science project that researchs the relationship between economic complexity, income-inequality and recession-recovery performance across OECD member countries

## Datasets used 

Three datasets will be used in this research:

1. The economic-complexity index is published by the "Atlas of Economic Complexity" which is part of the <a href="https://atlas.cid.harvard.edu/growth-lab">Growth Lab at Harvard University</a>.The index data can be downloaded as <b>a CSV file</b> from the official website: https://atlas.cid.harvard.edu/rankings
2. The "average OECD relative poverty rate by country" data is extracted from the OECD's "society at a glance 2019 report". This research will use <b>one CSV file</b> that contains the total percentage of people in relative poverty by country. The CSV file was downloaded from the official website: https://www.oecd-ilibrary.org/sites/8483c82f-en/index.html?itemId=/content/component/8483c82f-en
3. Given that the GDP per capita in purchasing power parity (PPP) terms data is provided by both the IMF and the World Bank, this work will consider both sources, compare them and then choose one of them to test the hypotheses.<br/>The World Bank data is included in <b>a CSV file</b> downloaded from the official website: https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv

## Data scraping

The IMF data will be <b>web scraped</b> from the official website using the Python package "Beautiful Soup"

## Installation

To run this project, you will need the following:

- Jupyter Notebooks
- Python and Pip

## Dependencies

```bash
pip install -r requirements.txt
```

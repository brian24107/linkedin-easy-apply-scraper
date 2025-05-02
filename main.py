from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Step 1: Open Chrome browser
driver = webdriver.Chrome()  # Make sure chromedriver.exe is in the same folder

# Step 2: Go to LinkedIn job search page
search_url = "https://www.linkedin.com/jobs/search/?f_AL=true&keywords=cybersecurity"
driver.get(search_url)

# Wait 5 seconds for the page to load
time.sleep(5)

# Step 3: Find all job cards
jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')

# Step 4: Create a list to store the job info
job_data = []

for job in jobs:
    try:
        title = job.find_element(By.CLASS_NAME, 'job-card-list__title').text
        company = job.find_element(By.CLASS_NAME, 'job-card-container__company-name').text
        location = job.find_element(By.CLASS_NAME, 'job-card-container__metadata-item').text
        link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')

        job_data.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Link': link
        })
    except:
        pass

# Step 5: Save job info to a CSV file
df = pd.DataFrame(job_data)
df.to_csv('jobs.csv', index=False)

# Step 6: Close the browser
driver.quit()

print("🎉 Done! Check the 'jobs.csv' file in your folder.")

# AI-Powered Job Market Intelligence System

## Dataset Inspection – Day 1

### Dataset Details
- scraped_jobs.json: 2,500 job records
- gold_labels.json: 108 gold label records

### Job Dataset Columns
id, title, company, location, description, seniority_level, employment_type, job_function, industry, url, posted_at, scraped_at, role_family_hint, domain_hint, experience_years_hint, remote_hint.

### Gold Label Columns
pair_id, skills, seniority, domain, location, composite, overqualified, reasoning.

### Gold Label Matching
- Total labels: 108
- Matched labels: 106
- Unmatched labels: 2
- Unmatched IDs: 21_job_20, 111_job_14

### Initial Gold Label Statistics
- Minimum composite score: 58
- Maximum composite score: 96
- Mean: 76.08
- Median: 76
- Overqualified True: 13
- Overqualified False: 95

### First Job Record
- Company: Cisco
- Title: Software Engineer - Development
- Location: Bengaluru, Karnataka, India
- Industry: Software Development
- Employment: Full-time
- Role family hint: fullstack

### Next Session – Day 2
1. Missing values count
2. Missing-value percentage
3. Duplicate records
4. Categorical analysis
5. Job market EDA

## Day 2 – Missing Values Analysis

### Dataset
- Total job records: 2,500

### Missing Values Results

| Column | Missing Values | Percentage |
|---|---:|---:|
| id | 0 | 0% |
| title | 0 | 0% |
| company | 0 | 0% |
| location | 1 | 0.04% |
| description | 0 | 0% |
| seniority_level | 0 | 0% |
| employment_type | 0 | 0% |
| job_function | 7 | 0.28% |
| industry | 0 | 0% |
| url | 0 | 0% |
| posted_at | 2500 | 100% |
| scraped_at | 0 | 0% |
| role_family_hint | 0 | 0% |
| domain_hint | 2500 | 100% |
| experience_years_hint | 2500 | 100% |
| remote_hint | 0 | 0% |

### Key Observations
1. Most columns have no missing values.
2. Location has 1 missing value (0.04%).
3. Job function has 7 missing values (0.28%).
4. posted_at, domain_hint and experience_years_hint have 100% missing values.
5. No missing-value treatment has been performed yet.

## SDuplicate Analysis:
- Total job records: 2500
- Unique duplicate IDs: 29
- Records with duplicate IDs: 58
- Exact duplicate rows: 29
- First duplicate ID verification: 2 records, 1 unique record.

## Missing Values Analysis:
- Total records: 2471
- location: 1 missing (0.04%)
- job_function: 7 missing (0.28%)
- posted_at: 2471 missing (100%)
- domain_hint: 2471 missing (100%)
- experience_years_hint: 2471 missing (100%)

## Observation:
Three columns have 100% missing values.
Location and job_function have very few missing values.

- posted_at, domain_hint and experience_years_hint
  contain 100% missing values.
- These columns are preserved without guessing values.
- They may be excluded from model features later.
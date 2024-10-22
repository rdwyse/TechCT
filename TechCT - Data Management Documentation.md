2024.10.21
# TechPT Data Management Documentation


# Table of Contents
1. [Introduction to the Data Management Documentation](#introduction-to-the-data-management-documentation)
2. [Data Cleanup Process Documentation](#data-cleanup-process-documentation)
   - [Date: 2024.09.13](#date-20240913)
      - [Following Solution C Procedures](#following-solution-c-procedures)
      - [Backing Up the Original Data](#backing-up-the-original-data)
      - [Configuring Excel Worksheet](#configuring-excel-worksheet)
      - [Sorting and Filtering, and Removing Testing Data](#sorting-and-filtering-and-removing-testing-data)
   - [Date: 2024.09.15](#date-20240915)
      - [Transfer SelfMonitoring6 to ConfMonitoring6](#transfer-selfmonitoring6-to-confmonitoring6)
      - [Cleaning Confederate Guide End of Session Entries](#cleaning-confederate-guide-end-of-session-entries)
      - [Additional Test Data Removal](#additional-test-data-removal)
   - [Date: 2024.09.16](#date-20240916)
      - [Set CaregiverID to Case Assignment](#set-caregiverid-to-case-assignment)
      - [Cleaning CaregiverID During Simulated Child Session](#cleaning-caregiverid-during-simulated-child-session)
      - [Adjusting Records for Caregiver Entry Due to Guide Reset](#adjusting-records-for-caregiver-entry-due-to-guide-reset)
         - [Edit 1](#edit-1)
         - [Edit 2](#edit-2)
      - [Investigate Confederate Note Indicating Caregiver Guide Issue](#investigate-confederate-note-indicating-caregiver-guide-issue)
      - [Adjusting Records for Confederate Compliance Based on Trial Notes](#adjusting-records-for-confederate-compliance-based-on-trial-notes)
      - [Adjusting Confederate Interaction Based on Trial Notes](#adjusting-confederate-interaction-based-on-trial-notes)
      - [Correcting CaregiverID for Confederate Guide Based on Research Notes](#correcting-caregiverid-for-confederate-guide-based-on-research-notes)
      - [Review of Confederate Guide Entry - No Action Required](#review-of-confederate-guide-entry---no-action-required)
      - [Correcting Study Phase and CaregiverID Based on Research and Session Notes](#correcting-study-phase-and-caregiverid-based-on-research-and-session-notes)
      - [Mastery Criteria Review Based on 8029hmvgjh Note](#mastery-criteria-review-based-on-8029hmvgjh-note)
      - [Missing TrialDirection Recordings During Training Sessions](#missing-trialdirection-recordings-during-training-sessions)
3. [Data Preparation](#data-preparation)
   - [Workflow Summary](#workflow-summary)
   - [Data Preparation in Excel for Confederate Monitoring Analysis](#data-preparation-in-excel-for-confederate-monitoring-analysis)
      - [Introduction](#introduction)
      - [Loading the Master Table](#loading-the-master-table)
      - [Using Power Query for Data Filtering and Transformation](#using-power-query-for-data-filtering-and-transformation)
      - [Processing Simulated Child (SC) Sessions](#processing-simulated-child-sc-sessions)
      - [Processing Actual Child (AC) Sessions](#processing-actual-child-ac-sessions)
      - [Combining SC and AC Data](#combining-sc-and-ac-data)
      - [Conclusion](#conclusion)
4. [Prism Design Considerations](#prism-design-considerations)
   - [Table Format: XY Data in GraphPad Prism](#table-format-xy-data-in-graphpad-prism)
      1. [Entering Multiple Sets of Data That Don’t Share X Values](#entering-multiple-sets-of-data-that-dont-share-x-values)
      2. [Example Table Structure for a Single Participant](#example-table-structure-for-a-single-participant)
5. [Documentation for Data Transfer and Plotting in GraphPad Prism](#documentation-for-data-transfer-and-plotting-in-graphpad-prism)
   - [Steps for Manual Data Transfer and Plotting in GraphPad Prism](#steps-for-manual-data-transfer-and-plotting-in-graphpad-prism)
      - [Merging Data Tables](#merging-data-tables)
      - [Creating Data Tables for Additional Series](#creating-data-tables-for-additional-series)
      - [Verifying Data Alignment](#verifying-data-alignment)
6. [Steps for Python Script to Automate Data Transfer to Prism](#steps-for-python-script-to-automate-data-transfer-to-prism)
   - [Introduction](#introduction)
   - [Processing Session Data](#processing-session-data)
   - [Main Loop: Generating Columns for Each Session](#main-loop-generating-columns-for-each-session)
   - [Output Formatting](#output-formatting)
7. [Interobserver Agreement (IOA) and Confederate Data Merge Documentation](#interobserver-agreement-ioa-and-confederate-data-merge-documentation)
   - [Date: 2024.10.16](#date-20241016)
      - [Following Solution C Procedures](#following-solution-c-procedures-1)
      - [IOA Table Generation](#ioa-table-generation)
   - [Date: 2024.10.17](#date-20241017)
      - [Master Table for IOA Merge](#master-table-for-ioa-merge)
      - [IOA Data Changes](#ioa-data-changes)
      - [Irregularities](#irregularities)
   - [Date: 2024.10.18](#date-20241018)
      - [Caregiver x Confederate Data Merger Documentation](#caregiver-x-confederate-data-merger-documentation)
8. [Script Documentation for IOA and Confederate Kappa Data Prep](#script-documentation-for-ioa-and-confederate-kappa-data-prep)
   - [CSV Dataset Overview](#csv-dataset-overview)
   - [Key Steps](#key-steps)
      - [Loading the Updated Spreadsheet](#loading-the-updated-spreadsheet)
      - [Loading and Preparing Data](#loading-and-preparing-data)
      - [Separate IOA and Confederate Data](#separate-ioa-and-confederate-data)
      - [Merge IOA and Confederate Data](#merge-ioa-and-confederate-data)
      - [Generate Key](#generate-key)
      - [Merge Keys Back to Original Dataset](#merge-keys-back-to-original-dataset)
      - [Export the Final Dataset](#export-the-final-dataset)
9. [Script Documentation for IOAxCONFxCARE Kappa Data Prep](#script-documentation-for-ioaxconfxcare-kappa-data-prep)
   - [Key Features and Changes from Original Script](#key-features-and-changes-from-original-script)
   - [Key Steps](#key-steps-ioaxconfxcare)
10. [Script Documentation for Fully Keyed Data Merge](#script-documentation-for-fully-keyed-data-merge)
   - [Key Steps](#key-steps-for-fully-keyed-data-merge)
11. [Flattening Process for IOA and Confederate Data](#flattening-process-for-ioa-and-confederate-data)
   - [Key Steps](#key-steps-ioa-and-confederate-flattening)
12. [Kappa Calculation for IOA and Confederate Data](#kappa-calculation-for-ioa-and-confederate-data)
   - [Confusion Matrix Breakdown](#confusion-matrix-breakdown)
   - [Confusion Matrix Summary](#confusion-matrix-summary)
   - [Overall Metrics](#overall-metrics)
13. [IOAxCONFxCARE Fully Keyed Data Prep](#ioaxconfxcare-fully-keyed-data-prep)
   - [Purpose](#purpose)
   - [CSV Dataset](#csv-dataset)
   - [Key Steps](#key-steps)
      - [1. Loading and Preparing the Dataset](#1-loading-and-preparing-the-dataset)
      - [2. Ensuring Column Consistency](#2-ensuring-column-consistency)
      - [3. Iterative Key Resolution](#3-iterative-key-resolution)
      - [4. Exporting the Final Dataset](#4-exporting-the-final-dataset)
   - [Summary](#summary)

14. [Flattening Process for IOA and Confederate Data](#flattening-process-for-ioa-and-confederate-data)
   - [Overview](#overview)
   - [Input File](#input-file)
   - [Output](#output)
   - [Script Details](#script-details)
   - [Purpose and Benefits](#purpose-and-benefits)
   - [Notes](#notes)

15. [IOAxCONF Kappa Prep Script Documentation](#ioa-conf-kappa-prep-script-documentation)
   - [Overview](#overview)
   - [Confusion Matrix Breakdown](#confusion-matrix-breakdown)
   - [Confusion Matrix Summary](#confusion-matrix-summary)
   - [Matrix Calculations](#matrix-calculations)
   - [Overall Metrics](#overall-metrics)
   - [Purpose of Confusion Matrix in Kappa Calculation](#purpose-of-confusion-matrix-in-kappa-calculation)
   - [How the Script Processes Data](#how-the-script-processes-data)

16. [Documentation for TechPT - 2024.10.18 - Script - IOAxCONF Kappa Calculator V2.py](#documentation-for-techpt---20241018---script---ioa-conf-kappa-calculator-v2)
   - [Overview](#overview)
   - [Key Features](#key-features)

17. [IOAxCONF - sklearn Kappa Script Documentation](#ioaxconf-sklearn-kappa-script-documentation)
   - [Overview](#overview)
   - [Key Changes from Previous Version](#key-changes-from-previous-version)
   - [Key Features](#key-features)
   - [Example Output](#example-output)
   - [New Advantages](#new-advantages)
   - [Output File](#output-file)

18. [Self-Monitoring Data Analysis](#self-monitoring-data-analysis)
   - [Task Overview](#task-overview)
   - [Step-by-Step Workflow](#step-by-step-workflow)
      - [Step 1: Initial Data Extraction and Cleaning](#step-1-initial-data-extraction-and-cleaning)
      - [Step 2: InstanceID Splitting and Sorting](#step-2-instanceid-splitting-and-sorting)
      - [Step 3: Dataset Cleanup and Metadata Handling](#step-3-dataset-cleanup-and-metadata-handling)
      - [Step 4: Kappa Calculation and Analysis](#step-4-kappa-calculation-and-analysis)

19. [SelfMonitoring - Omnibus.py Script Documentation](#selfmonitoring---omnibuspy-script-documentation)
   - [Overview](#overview)
   - [Purpose](#purpose)
   - [Steps of Analysis](#steps-of-analysis)
      - [1. Data Loading](#1-data-loading)
      - [2. Defining Columns for Comparison](#2-defining-columns-for-comparison)
      - [3. Metric Calculation Function](#3-metric-calculation-function)
      - [4. Iterative Calculation for Monitoring Pairs](#4-iterative-calculation-for-monitoring-pairs)
      - [5. Pooled Data Analysis](#5-pooled-data-analysis)
      - [6. Saving Results to CSV](#6-saving-results-to-csv)
   - [Metrics Calculated](#metrics-calculated)
   - [Example Use Case](#example-use-case)
   - [Summary](#summary)

# Introduction to the Data Management Documentation

The data management documentation for the "TechPT" project serves as a comprehensive guide detailing the organization, extraction, processing, and validation of all data collected during the study. This study examines the functional relationship between caregiver participation in a technology-assisted training program and the effectiveness of direction delivery to children. To ensure the accuracy and integrity of the collected data, meticulous records have been maintained throughout each phase of the research, from initial data capture to final analysis. 

This documentation outlines the methods used for data handling, focusing on the following key areas:
1. Data Extraction and Filtering: Specific techniques and procedures used to extract relevant data subsets from the master table, based on unique identifiers such as caregiver IDs, session types, or phases of the study. This ensures that only the necessary data is extracted for analysis while maintaining the integrity of the original dataset.
2. Table Structures and Comparison Methods: An explanation of how the raw data is organized into structured tables for different analyses, including comparisons between self-monitoring and confederate monitoring, session duration calculations, and compliance rates.
3. Formula and Script Documentation: A detailed breakdown of the formulas and scripts (both in Excel and Python) used to process the data, calculate session durations, and generate compliance scores.
4. Validation and Integrity Checks: Steps taken to verify the completeness and accuracy of the data, ensuring any anomalies are identified and corrected.
5. Preparation for GraphPad Prism: Final preparation of the datasets for statistical analysis and visualization, including specific formatting techniques required for smooth import into GraphPad Prism.

This documentation ensures that the data processes are transparent, replicable, and accurate, supporting the study's findings and contributing to the scientific rigor of the project.

# Data Cleanup Process Documentation

## Date: 2024.09.13

### Following Solution C Procedures
- Action: Followed Solution C procedures for manual extraction of the JSON data and converting it to a structured format.
  - See Solution C documentation for details within the qualtics guide (https://github.com/rdwyse/TechPT/blob/main/2023-247%20TechPT%20-%20Qualtrics%20Documentation.md#solution-c-data-extraction-procedure).

### Backing Up the Original Data
- Action: Saved a copy of the original raw data table as a separate document (`TechPT - 2024.09.13 - RAW Qualtrics Data transformed to CSV - Original Unedited.CSV`).
  
- Reason: To preserve the original data in its unaltered form for reference or reprocessing if necessary.

### Configuring Excel Worksheet
- Action: Duplicated the `TechPT - 2024.09.13 - RAW Qualtrics Data transformed to CSV - Original Unedited.CSV` into a new Excel worksheet.
  - New Worksheet Name: `TechPT - Master Table`.
  
- Reason: The `Master Table` will serve as the primary working copy for all data cleaning operations. The original cleaned data is preserved for comparison.

### Sorting and Filtering, and Removing Testing Data
- Action: 
  - Sorted the `CGID` (Caregiver ID) column in ascending order to easily identify test records.
  - Deleted the rows containing recorded activity from testing, identified by testing CGID.
    - Rows Removed: 791 - 871.
  
- Reason: 
  - These rows were identified as test data and should not be included in the final analysis.


## Date: 2024.09.15

### Transfer SelfMonitoring6 to ConfMonitoring6
- Action: 
  - Custom sorted by **Respondent** to isolate `0_CONF` entries, then sorted by **Date** to isolate the beginning of data collection where the error occurred.
  - **Range T407:T612** (SelfMonitoring6) was cut and pasted into **Range AD407:AD612** (ConfMonitoring6).
  - Subsequent rows already had the confederate response correctly documented in **ConfMonitoring6**.

- Reason: 
  - The confederate's monitoring data was mistakenly recorded under **SelfMonitoring6** instead of **ConfMonitoring6** due to a programming error.
  - No data duplication or overwriting occurred because the confederate guide only used the SelfMonitoring indices to maintain the `AggregateData` structure.
  - The error was identified during sessions on **2024-08-08** and resolved before the next day’s sessions by updating the header script (see **EventRecorder** function documentation).

- Observation on Redundancy:
  - **ConfResponse** and **ConfMonitoring6** fields are redundant:
    - **ConfResponse** is coded as `0 = Comply`, `1 = NoComply`.
    - **ConfMonitoring6** is coded as `0 = NoComply`, `1 = Comply`.


### Cleaning Confederate Guide End of Session Entries

- Action:
  - Sorted the **EventNote** column in ascending order to identify instances of `4.0_End_of_Session`.
  - Located **Rows 744 - 789** where `4.0_End_of_Session` was present.
  - Deleted the cell contents for **Range X744:X789** (ConfResponse) and **Range AD744:AD789** (ConfMonitoring6).

- Reason:
  - Due to a design flaw in the confederate guide, **ConfResponse** and **ConfMonitoring6** values were not cleared when a session was ended prematurely (i.e., before a trial was executed).
  - The confederate response values were pre-loaded before trials but weren’t properly nulled upon early session termination. This led to incorrect data being carried over.

- Outcome:
  - By deleting the pre-loaded data in **ConfResponse** and **ConfMonitoring6**, the dataset now accurately reflects the absence of trials during sessions that were ended before execution.


### Additional test data removal

- Action: 
  - Sorted the **EventNote** column in ascending order to identify instances of `4.0_End_of_Session`.
  - Deleted the row containing recorded activity from testing, .
    - Row Removed: 790.

- Reason:
  - identified by IOAVideo Name `Test3205_1_BL_1.MOV`

  -Action:
  - Sorted the **Respondent** column in ascending order, then DateTimeStamp in ascending order.
  - Deleted the row containing recorded activity from testing, .
    - **Row Removed:** 789.

- Reason:
  - identified by IOAVideo Name `Test3205_1_BL_1.MOV`

  ## Date: 2024.09.16

  ### Set CaregiverID to Case Assignment

- Action:
  - Utilized Excel Find and replace function to replace all `CGID` values with the corresponding `CaseAssignment` values.

- Reason:
  - The `CGID` values were used for randomization and identification during the study, but are now removed to mitigate risk of CaregiverID being linked back to private health information.

  ### Cleaning CaregiverID during simulated child session

- Action:
  - Sorted the **DateTimeStamp** column in ascending order.
  - Replaced CaregiverID for both caregiver and confederate entries during identified session
    - **CaregiverID** was misrecorded as `Case2` and replaced with `Case3`.
    - Replaced 28 entries E591:E618 with `Case3`.
    - Updated Session Note with `**Addressed 2024.09.16**` to indicate the correction.

- Reason:
  - instanceiD `rfolltfbkr` note indicating "wrong caregiverid during simulated child"
  - Verified timestamps and sessions completed during the day to ensure correct replacement.

### Adjusting Records for Caregiver Entry Due to Guide Reset

**EDIT 1:**

- Action:
  - Custom sorted **Respondent** in ascending order, then sorted the **DateTimeStamp** column in ascending order.
  - Deleted the row containing instanceID `z82e5xapom`, which represented the survey start for the caregiver.
  - Updated the `TotalSessionTrials` and `SessionBlockCount` for the session following the guide reset:
    - Added 1 to `TotalSessionTrials` and 0.5 to `SessionBlockCount` for **Range J288:K294** (7 entries).
    - Updated the caregiver end-of-session instanceID `vbbxofr3i5` to match the standard format by replicating the previous trial count values.
  - Updated the confederate trial note with **Addressed 2024.09.16** to indicate the correction.

- Reason:
  - InstanceID `9tqvddipvs`: The confederate trial note indicated, "Participant accidentally advanced the trial without self-monitoring?" This was the first note recorded after the caregiver guide reset.
  - InstanceID `vmfqt8wmtu`: The previous entry was a caregiver trial, which occurred directly before the first opportunity to make a note.
  - InstanceID `z82e5xapom`: This was a `0_SurveyStart` for the caregiver.
  - The guide reset also reset the `TotalSessionTrials` and `SessionBlockCount`.
  - Only one trial had occurred prior to the reset, so 1 was added to `TotalSessionTrials` and 0.5 to `SessionBlockCount` following the guide reset.

**EDIT 2:**

- Action:
  - Custom sorted **Respondent** in ascending order, then sorted the **DateTimeStamp** column in ascending order.
  - Deleted the row containing instanceID `gog0nhhfcf`, which represented the survey start for the caregiver.
  - Updated the `TotalSessionTrials` and `SessionBlockCount` for the session following the guide reset:
    - Added 4 to `TotalSessionTrials` and 2 to `SessionBlockCount` for **Range J170:K183** (14 entries).
    - Updated the caregiver end-of-session instanceID `vbbxofr3i5` to match the standard format by replicating the previous trial count values.
  - Updated the confederate trial note with **Addressed 2024.09.16** to indicate the correction.

- Reason:
  - InstanceID `2ihhrtz5xp`: The confederate trial note indicated, "Had to restart caregiver guide." This was the first note recorded after the caregiver guide was reset.
  - InstanceID `o37jreo054`: The previous entry was a caregiver trial, which occurred directly before the first opportunity to make a note.
  - InstanceID `gog0nhhfcf`: This was a `0_SurveyStart` for the caregiver.
  - The guide reset also reset the `TotalSessionTrials` and `SessionBlockCount` for the caregiver
  - Four trials had occurred prior to the reset, so 4 was added to `TotalSessionTrials` and 2 to `SessionBlockCount` following the guide reset.
    -Upon review of the timestamps, it was identified that the caregiver guide did not record `totalsessionTrial` 4. 

- Observation:
  - There is now a missing piece of caregivermonitoring data for this trial.


### Investigate Confederate note indicating caregiver guide issue

- Action:
  - updated confederate trial note with **Addressed 2024.09.16** to indicate the investigation.

- Observation:
  - Confederate guide note InstanceID `0kaipj5v5x` indicated, "Caregiver guide was interupted and reset"
  - No erranious entry was found within the data set. 
  

### Adjusting Records for Confederate Compliance Based on Trial Notes

- Action:
  - Sorted by **ConfTrialNote** in ascending order to identify instances where trial notes indicated an error in confederate compliance.
  - Updated **ConfMonitoring6** to reflect the correct compliance status as indicated in the trial notes for the following instanceIDs:
    - `g1p4exdh69`
    - `ylwmempocs`
    - `fezz3o4qcl`
    - `sv1ln9v67n`
  - Updated the confederate trial note with **Addressed 2024.09.16** to indicate the correction.

- Reason:
  - The trial notes for these instances indicated errors in confederate compliance that were not accurately reflected in **ConfMonitoring6**.
  - Adjustments were made to ensure that **ConfMonitoring6** accurately represents the confederate's behavior as described in the notes.

### Adjusting Confederate Interaction Based on Trial Notes

- Action:
  - Identified instanceID `v6pz5ir50l`, where the trial note stated, "No interaction last trial."
  - Located the previous confederate trial response, instanceID `sr093zo0zh`.
  - Updated **ConfederateInteraction** for `sr093zo0zh` from `1` to `0` to accurately reflect the lack of interaction in the last trial as noted.
  - Updated the confederate trial note with **Addressed 2024.09.16** to indicate the correction.

- Reason:
  - The trial note indicated that no interaction occurred during the previous confederate trial, but **ConfederateInteraction** was marked as `1`.
  - This adjustment ensures that **ConfederateInteraction** accurately represents the trial behavior based on the note.

### Correcting CaregiverID for Confederate Guide Based on Research Notes

- Action:
    - Reviewed external research notes on an alternative platform for **Case2**, which indicated, "I used the wrong CaregiverID during the first few," with a session of the same date.
  - Sorted the data in ascending order by **Date** and identified the corresponding timestamps for the session mentioned in the research note.
    - **Start of session:** instanceID `yd6f1txm6f` (Row 59).
    - **End of session:** instanceID `heh1nahvk3` (Row 137).
  - The discrepancy began with the first trial of the confederate guide and persisted until the second actual child trial (requiring opening and closing the confederate guide).
    - Identified the confederate guide resolution of discrepancy at **Row 95** (instanceID `budjp46u8w`).
  - Updated the **CaregiverID** in **Cells E60:E94** (18 entries) to reflect **Case2**.

- Reason:
  - Based on the research notes, the wrong **CaregiverID** was used during the first few trials, requiring updates to the confederate guide entries.
  - Verification of the timestamps and session notes confirmed the correct entries for the **CaregiverID** correction.

- Observation:
  - No further complications are expected as a result of this correction.

### Review of Confederate Guide Entry - No Action Required

- Action:
  - Marked the trial note with **Addressed 2024.09.16** to indicate that the review was completed.

- Review:
  - Identified instanceID `vws0jd4py3`, where the trial note stated, "Sent wrong guide."
  - Only two confederate guide records prior to note within session, both marked as `0_Survey_start` approximately 12 minutes apart.
  - No other anomalies were identified during the session, and no relevant entries were found in research notes notes.

- Reason:
  - Although the trial note mentioned sending the wrong guide, no discrepancies or issues were found in the logs or research notes. As a result, no changes were made.

### Correcting Study Phase and CaregiverID Based on Research and Session Notes **See error adjustment below**

- Action:
  - Identified instanceID `ihaltfgu1j`, where the session note stated: "Had the phase set to baseline in my guide, should be T2, check caregiver too. I assumed Mastery."
  - Reviewed research notes, which indicated: "Used the wrong CGID for XXX [Case 3] at 9 AM, used XXX [Case2]." **See error adjustment below**
  - Identified session start at instanceID `aayf1gemmr` and session stop at instanceID `hfvedav993`.
  - Updated **StudyPhase** from `0_BL` to `2_t2` for **Cells G430:G464** (17 entries).
  - Updated **CaregiverID** from `Case2` to `Case3` for **Cells E430:E465** (36 entries).
  - Marked the trial note with **Addressed 2024.09.16** to indicate the review was completed.

- Reason:
  - The session was incorrectly recorded with **StudyPhase** set to baseline (`0_BL`) when it should have been set to `2_t2`.
  - Additionally, the wrong **CaregiverID** was used for the session, necessitating the update to **Case3**.

- Observation:
  - This correction will need to be noted in the methods section and graphically represented.
  - Mastery criteria were actually met a few trial blocks before the session was concluded.
  - The directions delivered by the caregiver would have been different if the correct phase was set. Although, there is overlap in the directions delivered by both caregivers.

  #### 2024.09.16 Error Addendum

  While tabulating date for Case2, it was identified that there were no 2_t2 trials for Case2. Upon review of the previous edit an error was made while reviewing the research notes. The date of the research note was for the 2024.08.14 session, not the current 2024.08.09 Session. The note referenced 9 AM and the current session was at 9 AM as well in combination of the reference to "check caregiver" the note was misinterpreted.

  - Action: 
    - Sort by timedatestamp and searched for `hfvedav993`
    - Identified session start at instanceID `aayf1gemmr` and session stop at instanceID `hfvedav993`.
    - REVERTED **CaregiverID** from `Case3` to `Case2` for **Cells E430:E465** (36 entries).

### Mastery Criteria Review Based on 8029hmvgjh Note
- Action:  
  - Updated the trial note for instanceID `8029hmvgjh` with **Addressed 2024.09.16** to indicate that the note had been reviewed and documented

- Reason:  
  - Reviewed the confederate guide note for instanceID `8029hmvgjh`, which stated: "Not sure if Mastery criteria included all items or just this phase." 
  - The confederate note raised concerns about whether the correct mastery items were being used for the session's phase. Upon review of mastery criteria within , the criteria had been incorrectly tailored for each phase.
   - Checked the mastery criteria applied during this session and identified to ensure that only the relevant items for the current phase (T1, T2, or T3) were being evaluated.
  - Verified that the mastery criteria for each phase had been correctly updated based on previous changes (see **Mastery Criteria Update** section of Qualtrics documentation). 
  
- Outcome:  
  - Confederate Guide logic was updated upon the identification of this error.
  - This will require discussion within the manuscript and graphical representation.
  - Marked the note as resolved in the session data, and no additional discrepancies were found.

### Missing TrialDirection Recordings During Training Sessions

- Observation:  
  - The `TrialDirection` field in the caregiver guide was only recorded during Baseline and Actual Child sessions. No `TrialDirection` data was recorded during training sessions.

- Suspected Cause:  
  - It is likely that a variable for recording `TrialDirection` was missed within the qualtrics question specific javascript api window within caregiver training.

- Erroneous Recordings:  
  - In some cases, `TrialDirection` was erroneously recorded during caregiver `4.0_End_of_Session` events, these do not reflect actual training session data as it is a pre-cached entry for the following trial.
  
- Validation of Caregiver Guide Function:  
  - Despite the absence of `TrialDirection` recordings during training sessions, caregiver-delivered directions were observed and functioned correctly, indicating that the `CaregiverDirection` pool and function were working properly throughout the study.

- Action:  
  - Documented this oversight for future reference without attempting to correct javascript for future studies.

## Date: 2024.09.20

  ### Readjusting CaregiverID for Case 2
  See  `#### 2024.09.16 Error Addendum`

  ### Adjusting Records for Caregiver Entry Due to Incorrect Phase Selection

- **Action**:  
  - Custom sorted the data by `DateTimeStamp` in ascending order.
  - Identified the instance with `InstanceID: 0mor6ievy3`, which was the last trial of the simulated child session.
  - Duplicated the row with `InstanceID: 0mor6ievy3` and assigned the duplicated row `InstanceID: 0mor6ievy3-duplicate`.
  - Added the following trial note:  
    `**Post-Hoc duplication of trial see # Data Cleanup Process Documentation ## Date: 2024.09.20.`

- **Reason**:  
  - The wrong phase selection (`0_BL` instead of `2_T2`) caused the caregiver to deliver incorrect directions. While mastery was determined in-session by the experimenter, it was not reflected in the programmatic calculations, leading to an extra 9 trials being completed.
  - These extra trials resulted in an odd number of trials, which would cause issues in the trial block parsing. By duplicating the last trial, we ensured an even number of trials without impacting the score, as duplicating or keeping a single trial results in the same trial block score.

- **Outcome**:  
  - The duplicated trial allowed the data to be properly parsed with an even number of trials, ensuring accurate trial block formation without discarding any trials.
  - This will need to be noted in the methods section and graphically represented.

  ### Adjusting CaregiverID for Incorrect Case Assignment

- **Action**:  
  - Sorted data by `DateTimeStamp` to identify the relevant session start and end points.
  - Identified InstanceID: `ycmd3jnuj5` as the confederate guide survey start and InstanceID: `embw4dvrws` as the session end.
  - Sorted the data by `Respondent`, then by `DateTimeStamp`, to ensure the correct sequence of events was captured.
  - Replaced 8 cells from `Case3` to `Case2` in `E541:E548`, between InstanceID: `ycmd3jnuj5` to `to8bfqsufjxg`.

- **Reason**:  
  - While tabulating Case 2 data, it was identified that the `Simulated Child 1_T1` data was missing. Upon review of the Master Table, it was discovered that Case 3’s `CaregiverID` had been incorrectly assigned during the confederate guide session for Case 2.
  - This error occurred during the session immediately following the identification of the mastery criteria issue in Case 3 and its subsequent adjustment, which likely contributed to the confusion in the confederate guide.
  - The Caregiver Guide for Session 2 correctly utilized `Case 2` during the session, ensuring that only the confederate guide had this discrepancy.
  - Additionally, the `0_AC` trials following `1_T1` and `1_SC` correctly used the `CaregiverID` for `Case 2`.

- **Outcome**:  
  - Corrected the CaregiverID for the confederate guide during Case 2 sessions, ensuring that all relevant data is properly associated with the correct case.
  - This adjustment ensures accurate data tabulation for Case 2 and prevents any further discrepancies between the Caregiver and Confederate guides.
  - No impact on direction delivery due to the correct CaregiverID being used in the Caregiver Guide.


# Data Preparation

## Workflow Summary 

This workflow combines the strengths of **Excel** and **Power Query** for data management and **GraphPad Prism** for visualization. The goal is to efficiently organize data and produce high-quality graphs without performing complex statistical analysis.

### 1. **Data Preparation in Excel**:
   - **Data Import**: The master table is loaded into Excel and processed using **Power Query**.
   - **Power Query for Filtering and Transformation**: Power Query is used to filter and transform the dataset (e.g., extracting data for specific cases, respondents, or sessions). Filters are applied to select relevant columns and rows, such as extracting all **Actual Child (AC)** trials for **Case 1** with **Confederate (CONF)** as the respondent.
   - **Automated Updates**: The query results are loaded back into Excel. Any changes made to the master table are reflected in the query results when refreshed.

### 2. **Exporting Data to GraphPad Prism**:
   - Once the data is cleaned and organized in Excel, it is exported as a **CSV file** for use in GraphPad Prism.
   - This file will contain the relevant variables for generating  visualizations.
   
### 3. **Visualization in GraphPad Prism**:
   - **Data Import**: The cleaned CSV file is imported into GraphPad Prism.
   - **Graph Creation**: Prism is used to create publication-quality graphs, focusing on visual comparisons such as **SelfMonitoring vs. ConfMonitoring** or phase-by-phase analyses.
   - **No Complex Statistics**: Since complex statistical analysis is not needed, Prism is used mainly for its graphing capabilities.

### Key Points:
- **Excel** is used for **data management** and **real-time calculations**.
- **Power Query** allows for dynamic filtering and automated updates from the master table.
- **GraphPad Prism** is used solely for generating high-quality visualizations, without conducting complex statistical tests.
- **Exporting** data from Excel to Prism as a **CSV** ensures smooth transitions between data preparation and visualization.


## Table Naming Convention:

```plaintext
<SessionType>_<StudyPhase>_<CaregiverID>_<Respondent>_<Additional Details>_<Version>
```

### Components Breakdown:
1. **SessionType**: 
   - **AC**: Actual Child trials.
   - **SC**: Simulated Child trials.
   
2. **StudyPhase**:
   - **BL**: Baseline.
   - **T1**, **T2**, **T3**: Training Phases 1 to 3.
   - **RTB**: Reversal to Baseline.

3. **CaregiverID or GroupDescription**: 
   - Either a specific case ID (e.g., **Case1**, **Case2**) or a group descriptor (e.g., **AllCases**, **BaselineGroup**).

4. **Respondent**:
   - **CARE**: Caregiver.
   - **CONF**: Confederate.
   - **IOA**: Interobserver Agreement.

5. **Additional Details**: 
   - Any additional descriptors for the dataset, such as **TrialType**, **ChildTrials**, **Monitoring**, etc., to differentiate between datasets if needed.
   
6. **Version**: 
   - **V1**, **V2**, etc., for different versions of the table.

### Example Table Names:

1. **All Actual Child Trials for Case 1 (Caregiver as Respondent)**:
   - `AC_T1_Case1_CARE_ChildTrials_V1`: All actual child trials for **Case 1**, in **T1**, with **Caregiver (CARE)** as the respondent, version 1.

2. **Simulated Child Trials for Training Phase 2 (T2) for Case 1 (Confederate as Respondent)**:
   - `SC_T2_Case1_CONF_ChildTrials_V1`: Simulated child trials for **Case 1**, in **T2**, with **Confederate (CONF)** as the respondent, version 1.

3. **All Trials for Baseline Phase (BL) for Case 1 (Interobserver Agreement as Respondent)**:
   - `AC_BL_Case1_IOA_AllTrials_V1`: All trials during the **Baseline phase (BL)** for **Case 1**, with **IOA** as the respondent, version 1.

4. **Actual Child Trials for All Cases in Training Phases**:
   - `AC_T1_AllCases_AllRespondents_ChildTrials_V1`: Aggregated table of **all actual child trials** for all cases, during **T1**, across all respondents, version 1.

5. **Simulated Child Trials for Reversal to Baseline Phase (RTB) for IOA Respondent**:
   - `SC_RTB_Case1_IOA_ChildTrials_V1`: Simulated child trials during the **Reversal to Baseline (RTB)** phase for **Case 1**, with **IOA** as the respondent, version 1.

### Broader Aggregated Examples:
1. **All Actual Child Trials for All Cases Across All Phases**:
   - `AC_ALL_AllCases_AllRespondents_ChildTrials_V1`: All actual child trials for all cases, across all phases and respondents, version 1.

2. **All Records for Case 1 Across All Phases and Respondents**:
   - `AC_ALL_Case1_AllRespondents_AllTrials_V1`: Aggregated table of all records for **Case 1**, across all phases and respondents, version 1.

 

## Data Preparation in Excel for Confederate Monitoring Analysis

### 1. **Introduction**
   - This sections outlines the steps to clean, filter, and organize  Monitoring data for analysis and visualization in GraphPad Prism. 
   - The goal is to process data from both Simulated Child (SC) and Actual Child (AC) sessions, calculating trial block scores, averages, and counts for each session.
   - The Power Query language service for VS Code Available in the Visual Studio Code Marketplace. Provides a language service for the Power Query / M formula language in Visual Studio Code. This extensions provides syntax highlighting, auto-suggestions, and other editing features for M code files. It also provides syntax debugging and error highlighting features making the development of Power Query code easier.

### 2. **Loading the Master Table**
   - **Step 1**: Import the master table into Excel from a CSV file.
     - Navigate to the **Data** tab in Excel.
     - Select **Get Data** → **From File** → **From CSV** and choose the master table.
   - **Step 2**: Format the imported data as a table in Excel.
     - Select the table and choose **Format as Table** to enable easier filtering and querying.

### 3. **Using Power Query for Data Filtering and Transformation**
   - **Step 1**: Load the master table into Power Query.
     - Go to the **Data** tab in Excel and click **Get Data** → **From Table/Range** to open the table in Power Query.
   - **Step 2**: Define key parameters in Power Query: ALL_ALL_Case1_CONF_TrialBlockScoring_v1
     - Parameters for filtering the data dynamically are set at the start of the script. These include `CaregiverID`, `Respondent`, `SessionType`, and `EventNote`.
   
   ```powerquery
   let
       CaregiverID = "Case1",  // Parameter: Case1, Case2, Case3
       Respondent = "1_CONF",  // Parameter: 1_CONF, 2_IOA, CARE
       EventNote_Prefix = "3.0_Conf",  // Match the first 8 characters of EventNote
       SessionType_SC = "1_SC",  // Simulated Child session type
       SessionType_AC = "0_AC"   // Actual Child session type
   ```

   ### 4. **Processing Simulated Child (SC) Sessions**

   #### **Filtering and Sorting SC Sessions**
   - **Step 1**: Filter for SC sessions based on the parameters.
     - The script filters rows that match the selected `CaregiverID`, `Respondent`, `EventNote_Prefix`, and **Simulated Child** sessions.

     ```powerquery
     #"Filtered Rows_SC" = Table.SelectRows(#"Changed Type", each 
         ([CaregiverID] = CaregiverID) and 
         ([Respondent] = Respondent) and
         (Text.Start([EventNote], 8) = EventNote_Prefix) and
         ([SessionType] = SessionType_SC)
     )
     ```
   - **Step 2**: Sort SC sessions chronologically by `DateTimeStamp`.
     ```powerquery
     #"Sorted Rows_SC" = Table.Sort(#"Filtered Rows_SC", {{"DateTimeStamp", Order.Ascending}})
     ```

   #### **Creating Trial Blocks for SC Sessions**
   - **Step 3**: Add an index column to uniquely identify each trial.
     ```powerquery
     #"Added Index_SC" = Table.AddIndexColumn(#"Sorted Rows_SC", "Index", 1, 1, Int64.Type)
     ```
   - **Step 4**: Create `TrialBlockGroup` by grouping trials into pairs.
     - Each pair of trials is treated as a block, and trial block scores will be computed for each pair.
     ```powerquery
     #"Added TrialBlockGroup_SC" = Table.AddColumn(#"Added Index_SC", "TrialBlockGroup", each Number.IntegerDivide([Index] - 1, 2) + 1)
     ```

   #### **Computing Trial Block Scores for SC**
   - **Step 5**: Calculate the trial block scores for SC sessions based on Confederate Monitoring variables (**ConfMonitoring1-6a_3**).
     - For each trial block, a score of `1` is assigned if both trials have a value of `1` for a given variable, otherwise, the score is `0`.

     ```powerquery
     #"Added Custom_SC" = Table.AddColumn(#"GroupedTBRows_SC", "TrialBlockScore_SC", each
         let
             TrialRows = [ComputedTrialBlockSubTable],
             Trial1 = if Table.RowCount(TrialRows) > 0 then TrialRows{0} else null,
             Trial2 = if Table.RowCount(TrialRows) > 1 then TrialRows{1} else null,
             // Extract fields from Trial2
             SessionNumber = if Trial2 <> null then Trial2[SessionCount] else null,
             StudyPhase = if Trial2 <> null then Trial2[StudyPhase] else null,
             TB_ConfMonitoring1 = if (Trial1[ConfMonitoring1] = 1 and Trial2[ConfMonitoring1] = 1) then 1 else 0,
             TB_ConfMonitoring2 = if (Trial1[ConfMonitoring2] = 1 and Trial2[ConfMonitoring2] = 1) then 1 else 0,
             // Continue for all other ConfMonitoring variables
         in
         [
             SessionNumber = SessionNumber,
             StudyPhase = StudyPhase,
             TB_ConfMonitoring1 = TB_ConfMonitoring1,
             TB_ConfMonitoring2 = TB_ConfMonitoring2
             // Include other ConfMonitoring variables
         ]
     )
     ```

   #### **Calculating Averages and Counts for SC**
   - **Step 6**: Compute averages and counts for Confederate Monitoring variables across all trial blocks.
     - **T1** includes variables 1, 2, and 6a_1-6a_3.
     - **T2** includes variables 3, 4, and 5.

     ```powerquery
     #"Added SC_T1_Count" = Table.AddColumn(#"Expanded TrialBlockScore_SC", "SC_T1_Count", each 
         [TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3]
     ),
     #"Added SC_T1_Average" = Table.AddColumn(#"Added SC_T1_Count", "SC_T1_Average", each 
         [SC_T1_Count] / 5
     ),
     #"Added SC_T2_Average" = Table.AddColumn(#"Added SC_T1_Average", "SC_T2_Average", each 
         [SC_T2_Count] / 3
     ),
     ```

### 5. **Processing Actual Child (AC) Sessions**

#### **Filtering and Processing AC Sessions**
   - **Step 1**: Filter for AC sessions based on the selected parameters.
     ```powerquery
     #"Filtered Rows_AC" = Table.SelectRows(#"Changed Type", each 
         ([CaregiverID] = CaregiverID) and
         ([Respondent] = Respondent) and
         (Text.Start([EventNote], 8) = EventNote_Prefix) and
         ([SessionType] = SessionType_AC)
     )
     ```
   - **Step 2**: Adjust the columns for AC trials, ensuring they align with SC structure.
     ```powerquery
     #"Selected Columns_AC" = Table.SelectColumns(#"Filtered Rows_AC", {"DateTimeStamp", "CaregiverID", "SessionCount", "StudyPhase", 
         "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", 
         "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3"}),
     #"Renamed Columns_AC" = Table.RenameColumns(#"Selected Columns_AC", {{"SessionCount", "SessionNumber"}})
     ```

#### **Calculating Averages and Counts for AC**
   - **Step 3**: Compute averages and counts for Confederate Monitoring variables for the AC trials, similar to the SC calculations.
     ```powerquery
     #"Added AC_T1_Count" = Table.AddColumn(#"Added TrialBlockGroup_AC", "AC_T1_Count", each 
         [ConfMonitoring1] + [ConfMonitoring2] + [ConfMonitoring6a_1] + [ConfMonitoring6a_2] + [ConfMonitoring6a_3]
     ),
     #"Added AC_T1_Average" = Table.AddColumn(#"Added AC_T1_Count", "AC_T1_Average", each 
         [AC_T1_Count] / 5
     ),
     #"Added AC_AllConfMonitoring_Average" = Table.AddColumn(#"Added AC_T1_Average", "AC_AllConfMonitoring_Average", each 
         [AC_AllConfMonitoring_Count] / 8
     )
     ```

### 6. **Combining SC and AC Data**

   - **Step 1**: Ensure the SC and AC tables have the same columns and structure.
     - If a column is missing in either table, it's added with `null` values.
     ```powerquery
     #"Adjusted SC Table" = Table.SelectColumns(#"Added SC_AllConfMonitoring_Average", AllColumns, MissingField.UseNull),
     #"Adjusted AC Table" = Table.SelectColumns(#"Added AC_AllConfMonitoring_Average", AllColumns, MissingField.UseNull)
     ```

   - **Step 2**: Combine the SC and AC tables into a single dataset.
     ```powerquery
     #"Combined AC_SC Results" = Table.Combine({#"Adjusted SC Table",

### `ALL_ALL_Case1_CONF_TrialBlockScoring_v1` Power Query Code:



```powerquery
let
    // Define parameters (Case1, Case2, Case3)
    CaregiverID = "Case1",  // Select the relevant participant ID
    Respondent = "1_CONF",  // Parameter: 1_CONF, 2_IOA, CARE (Confederate, IOA, Caregiver)

    EventNote_Prefix = "3.0_Conf",  // Match the first 8 characters of EventNote
    SessionType_SC = "1_SC",   // Set session type for Simulated Child
    SessionType_AC = "0_AC",   // Set session type for Actual Child

    // Load the data from Excel table
    Source = Excel.CurrentWorkbook(){[Name="Table2"]}[Content],

    // Ensure consistent data types
    #"Changed Type" = Table.TransformColumnTypes(Source, {
        {"InstanceID", type text}, {"EventNote", type text}, {"DateTimeStamp", type datetimezone}, 
        {"ResponseIDx", type text}, {"CaregiverID", type text}, {"Respondent", type text}, 
        {"StudyPhase", type text}, {"SessionType", type text}, {"SessionCount", Int64.Type}, 
        {"ConfMonitoring1", Int64.Type}, {"ConfMonitoring2", Int64.Type}, {"ConfMonitoring3", Int64.Type}, 
        {"ConfMonitoring4", Int64.Type}, {"ConfMonitoring5", Int64.Type}, {"ConfMonitoring6a_1", Int64.Type}, 
        {"ConfMonitoring6a_2", Int64.Type}, {"ConfMonitoring6a_3", Int64.Type}
    }),

    // 1. Handle SC Trials

    // Filter for SC sessions
    #"Filtered Rows_SC" = Table.SelectRows(#"Changed Type", each 
        ([CaregiverID] = CaregiverID) and 
        ([Respondent] = Respondent) and
        (Text.Start([EventNote], 8) = EventNote_Prefix) and  // Match the first 8 characters of EventNote
        ([SessionType] = SessionType_SC)
    ),

    // Sort the table by DateTimeStamp to ensure the rows are in chronological order
    #"Sorted Rows_SC" = Table.Sort(#"Filtered Rows_SC", {{"DateTimeStamp", Order.Ascending}}),

    // Add an index column starting from 1
    #"Added Index_SC" = Table.AddIndexColumn(#"Sorted Rows_SC", "Index", 1, 1, Int64.Type),

    // Create TrialBlockGroup column by dividing the Index by 2 and adding 1 (pairs of two trials per group)
    #"Added TrialBlockGroup_SC" = Table.AddColumn(#"Added Index_SC", "TrialBlockGroup", each Number.IntegerDivide([Index] - 1, 2) + 1),

    // Group by TrialBlockGroup (which uniquely identifies each block of two trials)
    #"GroupedTBRows_SC" = Table.Group(#"Added TrialBlockGroup_SC", {"TrialBlockGroup"}, {
        {"ComputedTrialBlockSubTable", each _, type table}
    }),

    // Compute the trial block scores for SC ConfMonitoring variables and extract additional fields from Trial 2
    #"Added Custom_SC" = Table.AddColumn(#"GroupedTBRows_SC", "TrialBlockScore_SC", each
        let 
            TrialRows = [ComputedTrialBlockSubTable],  // set to the sub-table of trials within each trial block
            Trial1 = if Table.RowCount(TrialRows) > 0 then TrialRows{0} else null, // First trial in the block
            Trial2 = if Table.RowCount(TrialRows) > 1 then TrialRows{1} else null, // Second trial in the block
            
            // Extract additional fields from Trial2 (if it exists)
            SessionNumber = if Trial2 <> null then Trial2[SessionCount] else null,
            StudyPhase = if Trial2 <> null then Trial2[StudyPhase] else null,
            CaregiverID = if Trial2 <> null then Trial2[CaregiverID] else null,
            DateTimeStamp = if Trial2 <> null then Trial2[DateTimeStamp] else null,

            // Compute scores for ConfMonitoring
            TB_ConfMonitoring1 = if (Trial1[ConfMonitoring1] = 1 and Trial2[ConfMonitoring1] = 1) then 1 else 0,
            TB_ConfMonitoring2 = if (Trial1[ConfMonitoring2] = 1 and Trial2[ConfMonitoring2] = 1) then 1 else 0,
            TB_ConfMonitoring3 = if (Trial1[ConfMonitoring3] = 1 and Trial2[ConfMonitoring3] = 1) then 1 else 0,
            TB_ConfMonitoring4 = if (Trial1[ConfMonitoring4] = 1 and Trial2[ConfMonitoring4] = 1) then 1 else 0,
            TB_ConfMonitoring5 = if (Trial1[ConfMonitoring5] = 1 and Trial2[ConfMonitoring5] = 1) then 1 else 0,
            TB_ConfMonitoring6a_1 = if (Trial1[ConfMonitoring6a_1] = 1 and Trial2[ConfMonitoring6a_1] = 1) then 1 else 0,
            TB_ConfMonitoring6a_2 = if (Trial1[ConfMonitoring6a_2] = 1 and Trial2[ConfMonitoring6a_2] = 1) then 1 else 0,
            TB_ConfMonitoring6a_3 = if (Trial1[ConfMonitoring6a_3] = 1 and Trial2[ConfMonitoring6a_3] = 1) then 1 else 0
        in
        [
            SessionNumber = SessionNumber,
            StudyPhase = StudyPhase,
            CaregiverID = CaregiverID,
            DateTimeStamp = DateTimeStamp,
            // Removed TrialBlockGroup to avoid duplicate column
            TB_ConfMonitoring1 = TB_ConfMonitoring1,
            TB_ConfMonitoring2 = TB_ConfMonitoring2,
            TB_ConfMonitoring3 = TB_ConfMonitoring3,
            TB_ConfMonitoring4 = TB_ConfMonitoring4,
            TB_ConfMonitoring5 = TB_ConfMonitoring5,
            TB_ConfMonitoring6a_1 = TB_ConfMonitoring6a_1,
            TB_ConfMonitoring6a_2 = TB_ConfMonitoring6a_2,
            TB_ConfMonitoring6a_3 = TB_ConfMonitoring6a_3
        ]
    ),

    // Expand the TrialBlockScore record into separate columns for SC
    #"Expanded TrialBlockScore_SC" = Table.ExpandRecordColumn(#"Added Custom_SC", "TrialBlockScore_SC", 
    {"SessionNumber", "StudyPhase", "CaregiverID", "DateTimeStamp", 
    "TB_ConfMonitoring1", "TB_ConfMonitoring2", "TB_ConfMonitoring3", "TB_ConfMonitoring4", 
    "TB_ConfMonitoring5", "TB_ConfMonitoring6a_1", "TB_ConfMonitoring6a_2", "TB_ConfMonitoring6a_3"}),

    // Add custom SC calculations for counts and averages
    #"Added SC_T1_Count" = Table.AddColumn(#"Expanded TrialBlockScore_SC", "SC_T1_Count", each 
        [TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3]
    ),
    #"Added SC_T2_Count" = Table.AddColumn(#"Added SC_T1_Count", "SC_T2_Count", each 
        [TB_ConfMonitoring3] + [TB_ConfMonitoring4] + [TB_ConfMonitoring5]
    ),
    #"Added SC_AllConfMonitoring_Count" = Table.AddColumn(#"Added SC_T2_Count", "SC_AllConfMonitoring_Count", each 
        [SC_T1_Count] + [SC_T2_Count]
    ),
    #"Added SC_T1_Average" = Table.AddColumn(#"Added SC_AllConfMonitoring_Count", "SC_T1_Average", each 
        [SC_T1_Count] / 5
    ),
    #"Added SC_T2_Average" = Table.AddColumn(#"Added SC_T1_Average", "SC_T2_Average", each 
        [SC_T2_Count] / 3
    ),
    #"Added SC_AllConfMonitoring_Average" = Table.AddColumn(#"Added SC_T2_Average", "SC_AllConfMonitoring_Average", each 
        [SC_AllConfMonitoring_Count] / 8
    ),

    // 2. Handle AC Trials

    // Filter for AC sessions
    #"Filtered Rows_AC" = Table.SelectRows(#"Changed Type", each 
        ([CaregiverID] = CaregiverID) and 
        ([Respondent] = Respondent) and
        (Text.Start([EventNote], 8) = EventNote_Prefix) and  // Match the first 8 characters of EventNote
        ([SessionType] = SessionType_AC)
    ),

    // Select necessary columns and rename SessionCount to SessionNumber
    #"Selected Columns_AC" = Table.SelectColumns(#"Filtered Rows_AC", {"DateTimeStamp", "CaregiverID", "SessionCount", "StudyPhase", 
        "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", 
        "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3"}),
    #"Renamed Columns_AC" = Table.RenameColumns(#"Selected Columns_AC", {{"SessionCount", "SessionNumber"}}),

    // Add TrialBlockGroup column, set to null (or any appropriate value)
    #"Added TrialBlockGroup_AC" = Table.AddColumn(#"Renamed Columns_AC", "TrialBlockGroup", each null),

    // Add custom AC calculations for counts and averages
    #"Added AC_T1_Count" = Table.AddColumn(#"Added TrialBlockGroup_AC", "AC_T1_Count", each 
        [ConfMonitoring1] + [ConfMonitoring2] + [ConfMonitoring6a_1] + [ConfMonitoring6a_2] + [ConfMonitoring6a_3]
    ),
    #"Added AC_T2_Count" = Table.AddColumn(#"Added AC_T1_Count", "AC_T2_Count", each 
        [ConfMonitoring3] + [ConfMonitoring4] + [ConfMonitoring5]
    ),
    #"Added AC_AllConfMonitoring_Count" = Table.AddColumn(#"Added AC_T2_Count", "AC_AllConfMonitoring_Count", each 
        [AC_T1_Count] + [AC_T2_Count]
    ),
    #"Added AC_T1_Average" = Table.AddColumn(#"Added AC_AllConfMonitoring_Count", "AC_T1_Average", each 
        [AC_T1_Count] / 5
    ),
    #"Added AC_T2_Average" = Table.AddColumn(#"Added AC_T1_Average", "AC_T2_Average", each 
        [AC_T2_Count] / 3
    ),
    #"Added AC_AllConfMonitoring_Average" = Table.AddColumn(#"Added AC_T2_Average", "AC_AllConfMonitoring_Average", each 
        [AC_AllConfMonitoring_Count] / 8
    ),

    // 3. Define the list of all required columns
    AllColumns = {
        "DateTimeStamp", "CaregiverID", "SessionNumber", "TrialBlockGroup", "StudyPhase",
        "TB_ConfMonitoring1", "TB_ConfMonitoring2", "TB_ConfMonitoring3", "TB_ConfMonitoring4",
        "TB_ConfMonitoring5", "TB_ConfMonitoring6a_1", "TB_ConfMonitoring6a_2", "TB_ConfMonitoring6a_3",
        "SC_T1_Average", "SC_T2_Average", "SC_AllConfMonitoring_Average", "SC_T1_Count", "SC_T2_Count", "SC_AllConfMonitoring_Count",
        "AC_T1_Average", "AC_T2_Average", "AC_AllConfMonitoring_Average", "AC_T1_Count", "AC_T2_Count", "AC_AllConfMonitoring_Count"
    },

    // 4. Adjust SC table to have all required columns
    #"Adjusted SC Table" = Table.SelectColumns(#"Added SC_AllConfMonitoring_Average", AllColumns, MissingField.UseNull),

    // 5. Adjust AC table to have all required columns
    #"Adjusted AC Table" = Table.SelectColumns(#"Added AC_AllConfMonitoring_Average", AllColumns, MissingField.UseNull),

    // 6. Combine the adjusted SC and AC tables
    #"Combined AC_SC Results" = Table.Combine({#"Adjusted SC Table", #"Adjusted AC Table"}),

    // 7. Reorder the columns as needed
    #"Reordered Columns" = Table.ReorderColumns(#"Combined AC_SC Results", AllColumns),
    #"Sorted Rows" = Table.Sort(#"Reordered Columns",{{"DateTimeStamp", Order.Ascending}})
in
    #"Sorted Rows"
```

###  Key Differences and Explanation of `ALL_ALL_ALL_CONF_X_V1`

The **`ALL_ALL_ALL_CONF_X_V1`** query extends upon `ALL_ALL_CASE1_Conf_TrialBlockScoring_v1` to handle **multiple caregivers dynamically**, allowing for greater scalability and flexibility. This is achieved through the use of a helper function and dynamic application across all caregivers in the dataset.

#### Key Improvement #5: Dynamic Caregiver Processing

In **`ALL_ALL_ALL_CONF_X_V1`**, a helper function `ProcessCaregiver` is used to process each caregiver’s data for both **Simulated Child (SC)** and **Actual Child (AC)** sessions. This avoids the need to manually write the same logic for each caregiver.

##### Explanation of Key Logic

1. **Helper Function to Process Each Caregiver:**

   The `ProcessCaregiver` function accepts a **`CaregiverID`** as a parameter and filters the dataset for that caregiver’s SC and AC sessions. It processes the filtered data by calculating trial block scores, averages, and counts for each session. This modular function can be applied to any caregiver, ensuring that the logic is reusable and does not need to be rewritten for each individual case.

   ```powerquery
   ProcessCaregiver = (CaregiverID as text) => 
   let
       // Filter and process SC sessions
       // Filter and process AC sessions
       // Combine SC and AC results for this caregiver
   in
       Combined_SC_AC
   ```

2. **Retrieving Unique Caregivers and Applying the Function:**

   After defining the `ProcessCaregiver` function, the query automatically **retrieves all unique caregivers** from the dataset using `List.Distinct`. This ensures that every caregiver present in the data is processed. 

   The **`List.Transform`** function is then used to apply the `ProcessCaregiver` function to each unique `CaregiverID`. This means the processing logic is applied dynamically to all caregivers in the dataset, regardless of how many caregivers there are.

   ```powerquery
   CaregiverIDs = List.Distinct(#"Changed Type"[CaregiverID]), // Get unique caregivers
   AllResults = List.Transform(CaregiverIDs, each ProcessCaregiver(_)), // Apply the helper function to each caregiver
   ```

3. **Combining Results for All Caregivers:**

   Once the `ProcessCaregiver` function has been applied to all caregivers, the results are combined into a single table using `Table.Combine`. This final step merges the processed data for all caregivers into a unified dataset, making it ready for further analysis.

   ```powerquery
   FinalResult = Table.Combine(AllResults) // Combine results for all caregivers into one table
   ```

### Summary

The key improvement in **`ALL_ALL_ALL_CONF_X_V1`** is its ability to dynamically process data for multiple caregivers. By defining a helper function (`ProcessCaregiver`) and applying it to each unique caregiver, the query becomes scalable and reusable. This approach significantly reduces the manual effort needed to process each caregiver's data, ensuring that the logic is applied consistently and efficiently across the entire dataset.

### Conclusion:
This script provides a clean, processed dataset that groups trials into blocks, computes monitoring scores, and calculates averages. It ensures that each trial block is scored based on the performance of both trials in the block and includes additional relevant metadata for further analysis.





## **Prism Design Considerations**

This section outlines the design considerations for setting up data for GraphPad Prism using trial blocks as the X-axis for individual participants. The goal is to visualize different phases of a study, such as baseline, training, and return to baseline, for a single participant, while allowing flexibility in the structure for trials that do not share the same X values across phases. Information is summarized from Prism Manual.

### **Table Format: XY Data in GraphPad Prism**

In GraphPad Prism, an **XY data table** is structured so that each point is defined by an **X** and **Y** value. The table can accommodate different phases or data series, even if they do not share the same X values. This format is ideal for analyzing time-based data or trial blocks across different phases for a participant.

#### **Key Characteristics of an XY Table:**
- **X Column**: Represents the independent variable (in this case, trial blocks).
- **Y Columns**: Represent the dependent variable (EDC performance). You can have multiple Y columns for each phase of the study.
- **Staggered Data**: If trials within a phase do not start at the same X value, you can stagger the data entry by leaving rows blank and starting the data at the correct X point for each phase.


#### **Entering Multiple Sets of Data That Don’t Share X Values**

 Each XY data table in Prism has a single X column for up to 104 sets of Y values (i.e., phases or variables). If different phases or data series do not share the same X values (e.g., if trial blocks begin at different points within the study), you can handle this by **staggering the data entry**. This means leaving blank rows where needed and only entering values where the X value corresponds to the start of that phase.

#### **Best Practice for Staggering Data**:
1. **Start Entering Data at the Correct X Value**: You don’t need to start entering data in the first row. If one phase begins at a later trial block, simply start that phase’s data in a later row, leaving previous X values blank.
2. **Separate Phases into Different Y Columns**: For each phase (e.g., Baseline, Training 1, Training 2), use separate Y columns to keep the data organized.


## **Example Table Structure for a Single Participant**

For a participant, the data can be structured as follows:

| X (Trial Block) | Baseline (Y1) | Training 1 (Y2) | Training 2 (Y3) | Maintenance (Y4) |
|-----------------|---------------|-----------------|-----------------|------------------|
| 1               | 85            |                 |                 |                  |
| 2               | 87            |                 |                 |                  |
| 3               | 89            |                 |                 |                  |
| 4               |               | 70              |                 |                  |
| 5               |               | 72              |                 |                  |
| 6               |               | 75              |                 |                  |
| 7               |               |                 | 80              |                  |
| 8               |               |                 | 83              |                  |
| 9               |               |                 | 85              |                  |
| 10              |               |                 |                 | 88               |
| 11              |               |                 |                 | 90               |

#### **Explanation**:
- **X (Trial Block)**: Represents the trial block number.
- **Baseline (Y1)**: This participant's data during the baseline phase.
- **Training 1 (Y2)**: Data for the first training phase, which starts later than the baseline.
- **Training 2 (Y3)**: Data for the second training phase, starting even later.
- **Maintenance (Y4)**: Data for the maintenance phase, which begins after the training phases.


#### **Considerations for Graphing in Prism**:
- **Error Bars**: If you have replicate values for each trial block, Prism allows you to add error bars by using subcolumns. For each replicate, you can enter the corresponding Y value in the subcolumns.
- **Annotations**: Use Prism’s annotation feature to mark key points, such as the transition from one phase to another or significant changes in performance.
- **Handling Missing Data**: Blank cells will be automatically ignored by Prism, and no lines will be drawn through them, allowing for clear representation of the different start points of phases.



### Documentation for Data Transfer and Plotting in GraphPad Prism

#### **Steps for Manual Data Transfer and Plotting in GraphPad Prism**:

##### 1. **Y-Axis Group Labels in Prism**:
   - Each Y-axis group within **Prism** was named according to the study phase and session type.
   - **Example Y-axis group labels**:
     - `BL_AC` (Group A)
     - `BL_SC` (Group B)
     - `T1_SC` (Group F)
     - `T2_SC_1` (Group H)
     - `RTB_AC` (Group N)

##### 2. **Merging Data Tables**:
   - The **AC_ALL_Case1_CONF_X_V1** table (15 entries) was merged into the **ALL_ALL_Case1_CONF_TrialBlockScoring_v1** table (41 entries).
   - This resulted in a combined dataset with **56 entries**. The `TrialBlockGroup` column was updated as follows:
     - **X.5**: Assigned to baseline entries.
     - **X.25, X.5, X.75**: Assigned to the remaining AC sets (entries from the merged table).

   This merged dataset was then transferred to GraphPad Prism for further visualization.

##### 3. **Transferring Data Series to Prism**:

1. **Starting with `AllConfMonitoring_Average` Values**:
   - The first step was to copy the **`AllConfMonitoring_Average`** values from the combined dataset in Excel and paste them into Prism.
   - Initially, the values were pasted into the **Group A (`BL_AC`)** column within Prism.

2. **Cut and Paste to the Correct Y-Axis Groups**:
   - After pasting all the `AllConfMonitoring_Average` values into Group A, each subset of data was moved (cut and pasted) to the correct Y-axis group based on the session and phase.
   - For instance:
     - **Group A** (`BL_AC`) received the corresponding baseline values.
     - **Group B** (`BL_SC`) received its respective values.
     - **Group C** (`BL_AC`) was populated, and so on for each group.

   This ensured that the correct Y-axis group contained the appropriate data for each phase or session.

##### 4. **Creating Data Tables for Additional Series (`T1_Average`, `T2_Average`)**:
   - Once the `AllConfMonitoring_Average` data was organized in the correct Y-axis groups, the process was repeated for other series.
   - **For `T1_Average` and `T2_Average`**:
     - Separate data tables were created in Prism for the `T1_Average` and `T2_Average` series.
     - These values were copied from Excel and pasted into the appropriate Y-axis groups for each series.

   This resulted in three separate Prism data tables for:
   - **ALL_ALL_Case1_CONF_TrialBlockScoring_v1** (56 entries after the merge)
   - **ALL_T1_Case1_CONF__v1**
   - **ALL_T2_Case1_CONF__v1**

##### 5. **Verifying Data Alignment**:
   After each series was transferred to Prism, the data was cross-referenced for accuracy:
   
   1. **Check Row Configuration**:
      - After moving the data series into their corresponding Y-axis groups, the row configuration was verified to ensure that each row of data was correctly aligned with the corresponding Y-axis group.
      - This confirmed that the data points in each series were properly aligned between Excel and Prism.

   2. **Cross-Reference Check**:
      - For each series (`AllConfMonitoring_Average`, `T1_Average`, `T2_Average`), five random data points were selected and visually compared between the Excel source and Prism to ensure accuracy in the transfer.
      - This step provided assurance that the row order and data values matched perfectly.

#### **Conclusion**:
By carefully merging the **AC_ALL_Case1_CONF_X_V1** and **ALL_ALL_Case1_CONF_TrialBlockScoring_v1** tables into a combined set of 56 entries, and transferring each data series one at a time (starting with `AllConfMonitoring_Average`, followed by `T1_Average` and `T2_Average`), and assigning them to their corresponding Y-axis groups in Prism, the integrity and alignment of the data were maintained. This process ensured that the data was structured and ready for accurate visualization in GraphPad Prism.

### Steps for Python Script to Automate Data Transfer to Prism `TechPT - 2024.09.19 - Script - Translate Excel to Prism`


#### 1. **Introduction**
This section outlines the steps taken to dynamically process a CSV file containing session or trial data. The goal of the script is to dynamically select the last column in the dataset, generate new columns based on session and phase identifiers, for visualization in GraphPad Prism.

### 2. **Loading and Initial Setup**
- **Step 1**: Prepare CSV file with essential columns. The `TechPT - 2024.09.18 - Query - ALL_ALL_Case1_CONF_TrialBlockScoring_v1` query was used to generate the CSV file.
- **Step 2**: The script prompts the user to select a CSV file using a file dialog.
- **Step 3**: The script reads the selected CSV file into a pandas DataFrame (`df`), ensuring that essential columns are present. These include:
  - `DateTimeStamp`
  - `CaregiverID`
  - `SessionNumber`
  - `TrialBlockGroup`
  - `StudyPhase`
  - `SessionType`
  - Last column with the data to be visualized in Prism.

- **Step 3**: The last column of the CSV is identified dynamically, ensuring flexibility regardless of the column header names in the input file.

```python
last_column = df.columns[-1]
```

#### 3. **Processing Session Data**
#### **Step 1: Creating a Phase and Session Identifier**
- A new identifier, `Phase_Part`, is created by combining `StudyPhase` and `SessionType` for each row. This helps in organizing data by the session phase and type.

```python
def get_phase_part(row):
    study_phase = row['StudyPhase']
    session_type = row['SessionType']
    if study_phase == '5_RTB':
        phase_part = 'RTB'
    else:
        phase_part = study_phase.split('_')[-1]
    type_part = session_type.split('_')[-1]
    return f"{phase_part}_{type_part}"

df['Phase_Part'] = df.apply(get_phase_part, axis=1)
```

##### **Step 2: Assigning Row Index**
- Each row is indexed starting from 1 for easier tracking and reference.

```python
df['Row_Index'] = df.index + 1
```

#### 4. **Main Loop: Generating Columns for Each Session**
- The script iterates through the rows of the DataFrame, dynamically creating new columns based on `Phase_Part` and `SessionNumber`. The values from the dynamically identified last column are placed into these new columns. 

- **Loop Initialization**:
  - Each combination of `Phase_Part` and `SessionNumber` starts a new column.
  - Subsequent rows that match the same `Phase_Part` and `SessionNumber` are placed into the same column.

```python
while idx < len(df):
    row = df.iloc[idx]
    phase_part1 = row['Phase_Part']
    session_number1 = row['SessionNumber']
    last_column_value1 = row[last_column]  # Dynamically fetched last column

    column_count += 1
    column_name = f"{phase_part1}_{session_number1}_{column_count}"

    if column_name not in output_df.columns:
        output_df[column_name] = pd.NA

    output_df.at[idx, column_name] = last_column_value1

    # Nested loop for same phase and session
    idx += 1
    while idx < len(df):
        row2 = df.iloc[idx]
        phase_part2 = row2['Phase_Part']
        session_number2 = row2['SessionNumber']
        last_column_value2 = row2[last_column]

        if phase_part2 == phase_part1 and session_number2 == session_number1:
            output_df.at[idx, column_name] = last_column_value2
            idx += 1
        else:
            break
```

#### 5. **Output Formatting**
- Once the loop completes, the script organizes the new columns into a desired order and prompts the user to save the output as a CSV file.

```python
# Reorder columns
desired_columns_order = ['Trial Block Count'] + columns_order
output_df = output_df[desired_columns_order]

# Prompt user to save CSV
output_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV Files", "*.csv")],
                                           title="Save CSV as")
if output_file:
    output_df.to_csv(output_file, index=False)
    print(f"Data successfully exported to {output_file}")
```


### Script Documentation: **Translation of `ConfChildResponse` for Prism Graphing** TechPT - 2024.09.24 - Script - Translate Excel to Prism - Actual Child Compliance

#### Purpose:
This script is designed to transform a CSV dataset containing child behavior responses during sessions (Compliance, Omission, and Commission) into a format suitable for further analysis and graphing, specifically for GraphPad Prism.

#### Key Steps:

### 1. **Load CSV File**
The script begins by opening a file dialog to select the input CSV file. It expects the file to contain specific columns such as `DateTimeStamp`, `CaregiverID`, `SessionNumber`, `StudyPhase`, and `ConfChildResponse`.
The Data file is from `TechPT - 2024.09.23 - Query - AC_ALL_ALL_CONF_X_V1`

```python
# Import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Hide the root window for file dialogs
root = tk.Tk()
root.withdraw()

# Open file dialog to select input CSV file
csv_file = filedialog.askopenfilename(title="Select CSV File",
                                      filetypes=[("CSV Files", "*.csv")])
```

### 2. **Load and Convert Data**
The selected CSV file is loaded into a pandas DataFrame, and the `DateTimeStamp` column is converted from an Excel serial date format into a readable datetime format.

```python
# Load the CSV data with DateTimeStamp as object
df = pd.read_csv(csv_file, dtype={'DateTimeStamp': 'object'})

# Convert Excel serial date format to datetime
df['DateTimeStamp'] = pd.to_datetime(df['DateTimeStamp'].astype(float), origin='1899-12-30', unit='D', errors='coerce')
```

### 3. **Column Check**
This step ensures that all required columns (`DateTimeStamp`, `CaregiverID`, `SessionNumber`, `StudyPhase`, and `ConfChildResponse`) are present in the CSV file. If any required columns are missing, an error is raised, and the script displays the actual columns found in the file.

```python
# Ensure required columns are present
required_columns = ['DateTimeStamp', 'CaregiverID', 'SessionNumber', 'StudyPhase', 'ConfChildResponse']
if not all(col in df.columns for col in required_columns):
    print(f"Input CSV file is missing required columns. Expected columns: {required_columns}")
    print("Actual columns in the CSV file:", df.columns)
    raise ValueError("Input CSV file does not match the expected structure.")
```

### 4. **Translate `ConfChildResponse`**
In this step, the script translates the `ConfChildResponse` values into numerical values for compliance, omission, and commission:
- **0_CO (Compliance)** → 1
- **1_PO (Omission)** → -0.5
- **2_PC (Commission)** → -1

The translation is done by applying a function to each row, and new columns (`0_CO_Trans`, `1_PO_Trans`, and `2_PC_Trans`) are created to store the translated values.

```python
# Translate ConfChildResponse values to the needed transformation
def translate_conf_child_response(conf_child_response):
    if conf_child_response == '0_CO':  # Compliance
        return 1, 0, 0  # Compliance = 1, Omission = 0, Commission = 0
    elif conf_child_response == '1_PO':  # Omission
        return 0, -0.5, 0  # Compliance = 0, Omission = -0.5, Commission = 0
    elif conf_child_response == '2_PC':  # Commission
        return 0, 0, -1  # Compliance = 0, Omission = 0, Commission = -1
    else:
        return 0, 0, 0  # Default to zero if no match

# Create new columns for translated values
df['0_CO_Trans'], df['1_PO_Trans'], df['2_PC_Trans'] = zip(*df['ConfChildResponse'].apply(translate_conf_child_response))
```

### 5. **Export Transformed Data**
The processed data, including the translated values, is saved to a new CSV file. The user is prompted to choose the location and name of the output file via a file dialog.

```python
# Initialize the final DataFrame with the necessary columns
final_df = df[['DateTimeStamp', 'CaregiverID', 'SessionNumber', 'StudyPhase', '0_CO_Trans', '1_PO_Trans', '2_PC_Trans']]

# Open file dialog to save the output CSV file
output_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV Files", "*.csv")],
                                           title="Save CSV as")

# Export the formatted data to CSV
final_df.to_csv(output_file, index=False)
print(f"Data successfully exported to {output_file}")
```

## **IOA Data Preparation and Kappa Analysis**

### Overview
This document provides a summary of the entire workflow for analyzing the IOA (Interobserver Agreement) and Confederate data. Each step lists the script name, its purpose, and the corresponding CSV files used or generated.

### Step-by-Step Workflow

#### **Step 1: Initial Data Extraction and Cleaning**
- **Script**: *TechPT - 2024.10.16 - Solution C - IOA RAW Data Export*
  - **Purpose**: Follow Solution C procedures for manually extracting JSON data from Qualtrics and converting it to a structured format.
  - **CSV Output**: `TechPT - 2024.10.16 - IOA Table - RAW Data Export.xlsx`

#### **Step 2: IOA Table Generation**
- **Script**: Manual Cleaning and IOA Table Generation
  - **Purpose**: Cleaned the IOA table, removed empty rows, and created new columns for tracking session trials. This updated table was merged with the Master Table.
  - **CSV Output**: `TechPT - 2024.10.17 - Data - IOAxCONF merge.csv`

#### **Step 3: Master Table Updates**
- **Script**: *TechPT - 2024.10.17 - Master Table for IOA Merge*
  - **Purpose**: Updated specific trial counts, adjusted session information, and updated formulas for matching IOA and Confederate responses.
  - **CSV Output**: None (updates were made to existing master and merge tables).

#### **Step 4: Data Merge and Key Generation**
- **Script**: *TechPT - 2024.10.17 - Script - IOAxCONF - Kappa Prep.py*
  - **Purpose**: Prepared the CSV dataset for kappa analysis by matching IOA and Confederate responses and generating unique keys for each pair.
  - **CSV Output**: `TechPT - 2024.10.17 - IOAxCONF_keyed.csv`

#### **Step 5: Combined Keyed Dataset Preparation**
- **Script**: *TechPT - 2024.10.18 - Combine Keyed Tables based on Instance.py*
  - **Purpose**: Combined previously keyed tables from multiple respondents (IOA, Confederate, Caregiver) into a unified dataset, ensuring all rows were aligned for kappa analysis.
  - **CSV Output**: `resolved_merged_keyed_data.csv`

#### **Step 6: Data Flattening**
- **Script**: *TechPT - 2024.10.18 - Script - IOAxCONF - flatten Kappa prep.py*
  - **Purpose**: Flattened the combined IOA and Confederate dataset into a concise format by collapsing matched rows while retaining key data from each observer.
  - **CSV Output**: `TechPT - 2024.10.18 - Data - IOAxCONF_Keyed_flat.csv`

#### **Step 7: Merged Data Preparation for Full Kappa Analysis**
- **Script**: *TechPT - 2024.10.18 - Combine Keyed Tables based on Instance.py*
  - **Purpose**: Created a fully keyed and cleaned dataset for analyzing agreement across multiple combinations of observers.
  - **CSV Output**: `TechPT - 2024.10.18 - Data - IOAxCONFxCARE Fully Keyed and cleaned for Kappa v2.csv`

#### **Step 8: Kappa Calculation**
- **Script**: *TechPT - 2024.10.18 - Script - IOAxCONF Kappa Calculator V2.py*
  - **Purpose**: Compared IOA and Confederate ratings to create a confusion matrix, generating agreement metrics (e.g., true positive, true negative, false positive, false negative) to calculate observed agreement (`P_o`).
  - **CSV Output**: None (this step was mainly focused on calculating metrics and summary tables for kappa analysis). Many of these calculations were also completed in Excel for manual verification.



### IOA Data Entry modifications and procedures

### Date: 2024.10.16

#### Following Solution C Procedures
- **Action**: Followed Solution C procedures for manual extraction of the JSON data and converting it to a structured format.
  - Reference: [Solution C documentation](https://github.com/rdwyse/TechPT/blob/main/2023-247%20TechPT%20-%20Qualtrics%20Documentation.md#solution-c-data-extraction-procedure) in the Qualtrics guide.
  - Saved output: `TechPT - 2024.10.16 - Solution C - IOA RAW Data Export.txt`.

#### IOA Table Generation
- **Action**: Copied relevant rows (1–149) from Solution C cleaned output to a new Excel spreadsheet.
  - Spreadsheet name: `TechPT - 2024.10.16 - IOA Table - RAW Data Export.xlsx`.
  - Created a copy of the IOA table for cleaning.
  - Removed empty rows: 17, 18, 84, 140.
  - Replaced `CaregiverID` with `CaseAssignment`.
  - Generated a new column `IOA Trial` based on `SessionCount` (observer entered trial and session count).
  - Updated the `SessionCount` column to only contain session count data.
  - Deleted content in `TotalSessionTrials` and `SessionBlockCount` columns as these are only validly generated by caregiver and confederate guides.


### Date: 2024.10.17

#### Master Table for IOA Merge
- **Action**: Generated a copy of the Master Table for IOA merge.
  - Updated `ConfChildResponse` formula for simulated trials:  
    ```excel
    =IF(LEFT(B108,1)="3",IF(AD108=1,"0_CO", "1_PO"),"")
    ```
  - Matched `IOA Table` headers and `Master Table` headers.
  - Added columns: `CONF_TotalSessionTrials`, `IOA_TotalSessionTrials`, `Merge_TotalSessionTrials` to both tables.
  - Copied all rows of Master Table and merged into the IOA Table.
  - Resaved as `TechPT - 2024.10.17 - IOA and Confederate Merge.CSV`.
  
#### IOA Data Changes:
- **Baseline Trial Count**: Adjusted for CONF observations due to AC trials being included in the count.
- **Session Count Update**: 
  - Updated `IOA-TrackingSession4` for `Case 3, Trial 1_41` from session 1 to session 2.
  - Updated trial type for `IOA-TrackingSession4` for `Case 4, RTB` from SC to AC.
- **IOA Monitoring Updates**:
  - For all SC trials, merged IOA problems of omission and commission into compliance and non-compliance using:  
    ```excel
    =IF(AV2="0_CO",1,IF(AV2="","",0))
    ```

#### Irregularities:
- **f7ylw8pinh**: No match found. IOA trial count skips TrialCount 17.
- **jve0bc8gh8**: No match found. IOA trial count skips TrialCount 16.


### Date: 2024.10.18

#### Caregiver x Confederate Data Merger Documentation

During the **Caregiver x Confederate (CARE x CONF)** data merger, three orphaned entries were identified:

| InstanceID | EventNote                        | DateTimeStamp             | ResponseIDx        | Respondent | CaregiverID | StudyPhase | SessionType | SessionCount | Merge\_TotalSessionTrials |
| ---------- | -------------------------------- | ------------------------- | ------------------ | ---------- | ----------- | ---------- | ----------- | ------------ | ------------------------- |
| 1phcqur8wf | 3.0\_Conf\_TX\_SC\_TrialComplete | 2024-08-15T09:23:21-04:00 | R\_32Q0HaHaawwoVjr | 1\_CONF    | Case1       | 3\_T3      | 1\_SC       | 5            | 6                         |
| 3bw0gzxxfb | 3.0\_Conf\_TX\_SC\_TrialComplete | 2024-08-09T10:39:44-04:00 | R\_1tD6uMNpqoFo69y | 1\_CONF    | Case1       | 2\_T2      | 1\_SC       | 4            | 6                         |
| apxqoxnx71 | 3.0\_Conf\_TX\_SC\_TrialComplete | 2024-08-07T12:48:31-04:00 | R\_60MjqExxQsnR0oA | 1\_CONF    | Case1       | 1\_T1      | 1\_SC       | 2            | 4                         |

**Issue Summary**: The corresponding **Caregiver self-monitoring entries** for these orphaned Confederate trials were not initially identified in either the master table or the Qualtrics database. Upon further investigation, it was found that the entries for **3\_T3** and **2\_T2** were the last session trials where the caregiver did not advance at the end of the trial. The entry for **1\_T1** was due to a guide reset: "Had to restart caregiver guide \


It was considered to enter an estimated set of data for the Total Session Trials (6 for 3\_T3 and 2\_T2) specifically for visualization purposes. However, it was deemed unnecessary at this point, and it is reasonable to assume that all values would be 1. 

Orphaned enteries were deleted from the merged table.

**Impact**:
This will slightly affect the total number of trials in the session for IOA. 


## Script Documentation: **IOA and Confederate Kappa Data Prep**

###### - TechPT - 2024.10.17 - Script - IOAxCONF - Kappa Prep.py

### Purpose

This script processes a CSV dataset to match IOA (Interobserver Agreement) and Confederate responses, generating unique keys for each matched pair. The primary goal is to prepare the data for kappa analysis, with visualization as a secondary outcome.



### CSV Dataset

The CSV dataset used in this script contains observation data related to the IOA and Confederate responses. The columns in the dataset include the following:

- **CaregiverID**: Identifier for the caregiver associated with each observation.
- **Respondent**: Specifies whether the response is from an IOA (Interobserver Agreement) or a Confederate.
- **StudyPhase**: Indicates the phase of the study (e.g., baseline, training, etc.).
- **SessionType**: Specifies the type of session (e.g., Actual Child (AC), Simulated Child (SC)).
- **SessionCount**: Represents the session number.
- **Merge_TotalSessionTrials**: Indicates the total number of trials in the session, used for matching pairs between IOA and Confederate responses.
- **Additional Monitoring Columns**: The dataset may also include columns like `ConfMonitoring1`, `ConfMonitoring2`, etc., which capture specific monitoring data from each session.

### Key Steps 

#### 1. Loading the Updated Spreadsheet

The script begins by importing necessary libraries (`pandas`, `os`, `tkinter`) and prompting the user to load the updated spreadsheet. The user is asked to specify the input CSV file and output directory using file dialogs. The output filename is generated based on the input filename, appending '_IOAxCONF_keyed.csv'.

##### Libraries Used

- **pandas** (`import pandas as pd`):
  - pandas is used for loading, processing, and saving data in table format.
  - It helps read the CSV file into a DataFrame, manipulate the data, merge subsets, and write the final result to a new CSV.
  - A DataFrame can be thought of as a table with rows (Y-axis) representing observation records and columns (X-axis) representing attributes (`CaregiverID`, `Respondent`, `StudyPhase`, etc.).

- **os** (`import os`):
  - os is used to work with file paths.
  - It helps extract the filename and extension, modify filenames, and create full paths for saving the output file.

- **tkinter** (`from tkinter import filedialog, from tkinter import Tk`):
  - tkinter is used to create file dialog windows.
  - `filedialog.askopenfilename()` allows the user to select the input CSV file.
  - `filedialog.askdirectory()` allows the user to choose where to save the output.
  - `Tk().withdraw()` hides the tkinter main window, so only the dialog boxes are shown.

```python
# Import necessary libraries
import pandas as pd
import os
from tkinter import filedialog
from tkinter import Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input file
input_file_path = filedialog.askopenfilename(title="Select Input CSV File")

# Generate output file name based on the input file name
input_file_name = os.path.basename(input_file_path)
output_file_name = os.path.splitext(input_file_name)[0] + 'keyed.csv'

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")
output_file_path = os.path.join(output_dir, output_file_name)
```

#### 2. Load and Prepare Data

The selected CSV file is loaded into a pandas DataFrame.

- `pd.read_csv()`: This function reads the CSV file into a pandas DataFrame. It processes the CSV row by row and creates columns based on the headers in the CSV. Each row becomes an entry in the DataFrame, with data types inferred or specified.

By default, pandas will infer the data type of each column based on the values present in the data. For example, if a column contains only numeric values, pandas might infer it as an integer or float. However, you can also explicitly specify the data type of a column using the `dtype` parameter in functions like `pd.read_csv()`.

When managing data types, it's important to ensure consistency to prevent issues during operations like merging or calculations. Explicitly specifying data types can help avoid unexpected behavior caused by incorrect inferences, especially when dealing with categorical data or mixed types.

Relevant columns are converted to strings to ensure proper matching during the subsequent merge process in this script.

```python
# Load the dataset
# Read the CSV file into a DataFrame
updated_data = pd.read_csv(input_file_path)

# Convert relevant columns to strings to ensure proper matching
# Ensuring all relevant columns are strings to avoid type mismatch issues during merge
for col in ['Respondent', 'CaregiverID', 'StudyPhase', 'SessionType']:
    updated_data[col] = updated_data[col].astype(str)
```

#### 3. Separate IOA and Confederate Data

The dataset is separated into two subsets: IOA and Confederate rows, based on the 'Respondent' column. This separation creates two new DataFrames (`ioa_data` and `confederate_data`), which are necessary for matching related observations before merging them back into a unified dataset.

```python
# Separate the IOA and Confederate rows based on 'Respondent'
# Splitting the dataset into IOA and Confederate subsets for later matching
ioa_data = updated_data[updated_data['Respondent'] == '2_IOA']
confederate_data = updated_data[updated_data['Respondent'] == '1_CONF']
```

#### 4. Merge IOA and Confederate Data

IOA and Confederate data are matched based on common identifiers, including `CaregiverID`, `StudyPhase`, `SessionType`, `SessionCount`, and `Merge_TotalSessionTrials`. A unique key is generated for each matching pair.

The `pd.merge()` function is used to combine two pandas DataFrames based on common columns or index keys. In this script, `pd.merge()` is merging the `ioa_data` and `confederate_data` DataFrames based on the specified columns: `CaregiverID`, `StudyPhase`, `SessionType`, `SessionCount`, and `Merge_TotalSessionTrials`. Here’s how it works:

- **Identify Matching Columns**: The merge operation uses the values in the specified columns to identify corresponding rows between `ioa_data` and `confederate_data`.

- **Handling Duplicates**: If duplicates exist in both DataFrames for the merge columns, the result will be a Cartesian product, meaning each duplicate row from `ioa_data` is paired with each duplicate row from `confederate_data`, resulting in multiple rows for the same values in the merge columns.

##### Example:

**Before Merge (IOA DataFrame)**

| CaregiverID | StudyPhase | SessionType | SessionCount | Merge_TotalSessionTrials | IOAmonitor1 |
| ----------- | ---------- | ----------- | ------------ | ------------------------- | ----------- |
| 001         | 0_BL       | 0_AC        | 1            | 1                         | 0           |
| 001         | 0_BL       | 1_SC        | 1            | 3                         | 1           |

**Before Merge (Confederate DataFrame)**

| CaregiverID | StudyPhase | SessionType | SessionCount | Merge_TotalSessionTrials | CONFmonitor1 |
| ----------- | ---------- | ----------- | ------------ | ------------------------- | ------------ |
| 001         | 0_BL       | 0_AC        | 1            | 1                         | 0            |
| 001         | 0_BL       | 1_SC        | 1            | 2                         | 1            |

**After Merge (Resulting DataFrame)**

| CaregiverID | StudyPhase | SessionType | SessionCount | Merge_TotalSessionTrials | IOAmonitor1 | CONFmonitor1 |
| ----------- | ---------- | ----------- | ------------ | ------------------------- | ----------- | ------------ |
| 001         | 0_BL       | 0_AC        | 1            | 1                         | 0           | 0            |

```python
# Merging IOA and Confederate data based on the matching columns
# Merging IOA and Confederate rows on common identifiers to create matched pairs
merged_with_key = pd.merge(
    ioa_data,
    confederate_data,
    on=['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials'],
    suffixes=('_IOA', '_Conf')
)
```

#### 5. Generate Key

This section creates a unique identifier for each row in the `merged_with_key` DataFrame by generating a new column called `'IOAxCONF_Key'`. The new column ensures that each row has a distinct reference, even when there are duplicate rows after merging.

```python
# Creating unique keys for each match
# Generating a unique identifier for each pair of matched rows

merged_with_key['IOAxCONF_Key'] = list(range(1, len(merged_with_key) + 1))
```

- **Column Assignment**: This code adds a new column named `'IOAxCONF_Key'` to the `merged_with_key` DataFrame. This column will store unique identifiers.

- **Unique Identifier Generation**: 
  - The function `range(1, len(merged_with_key) + 1)` generates a sequence of integers starting from 1 up to the total number of rows in the DataFrame. This ensures that each row is assigned a unique identifier, even if some rows contain duplicate values.
  
- **List Conversion**: 
  - The `list()` function converts the `range()` object into a list, which is a structure compatible with DataFrame columns. This allows the sequence of integers to be easily assigned as a new column in the DataFrame.

By using this approach, each row in the DataFrame is uniquely identified, which is crucial when handling merged datasets that may contain duplicate entries.

### 6. Merge Keys Back to Original Dataset

The unique keys generated from the matched pairs are added back into the original dataset through a left merge. This ensures each row retains its original information, along with the newly assigned key if a match is found.

The `how='left'` parameter in the `pd.merge()` function specifies the type of merge operation being performed. In this case, a "left merge" is used, meaning all rows from the left DataFrame (`updated_data`) will be retained, and corresponding matches from the right DataFrame (`merged_with_key`) will be added. If there is no match found in the right DataFrame, the left DataFrame's rows are kept, with NaN values used for the columns from the right DataFrame.

The `on=[...]` part specifies which columns to use as keys for the merging operation. In this case, the merge is performed based on `CaregiverID`, `StudyPhase`, `SessionType`, `SessionCount`, and `Merge_TotalSessionTrials`. These columns must have matching values in both DataFrames for the merge to happen.

```python
# Merging the new keys back into the original dataset to ensure every row stays the same but with the new key
# Adding the unique keys back into the original dataset, ensuring all rows are retained
final_data_with_keys = pd.merge(
    updated_data, 
    merged_with_key[['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'IOAxCONF_Key']],
    how='left',
    on=['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials']
)
```

#### 7. Export the Final Dataset

The final dataset, now containing unique keys for each matched pair of IOA and Confederate rows, is saved to a new CSV file.

```python
# Save the updated dataframe to a new CSV file
# Saving the final dataset with the new keys to a CSV file
final_data_with_keys.to_csv(output_file_path, index=False)

print(f"Data with unique keys saved to {output_file_path}")
```

## Script Documentation: **IOAxCONFxCARE Kappa Data Prep**

###### - TechPT - 2024.10.17 - Script - IOAxCONFxCARE Kappa Prep

### Purpose

Expand the user interface of TechPT - 2024.10.17 - Script - IOAxCONF - Kappa Prep.py

This script processes a CSV dataset to match different combinations of respondents: IOA (Interobserver Agreement), Confederate, and Caregiver responses. It allows the user to choose which pair or set of respondents to compare, generating unique keys for each matched pair. The primary goal is to prepare the data for kappa analysis, with visualization as a secondary outcome.

### Key Features and Changes from Original Script

- **User Selection for Comparison**: The script now prompts the user to select which respondents to compare: IOA and CONF, IOA and CARE, CONF and CARE, or all three (IOA, CONF, and CARE).
- **Flexible Matching**: Depending on the user input, the script will perform a merge for the selected respondents and generate corresponding keys.
- **Output Naming**: The output file is named based on the selected comparison to clearly indicate which respondents were compared (e.g., `_IOAxCARE_keyed.csv`).
- **Separation of Data**: The dataset is separated into subsets for IOA, Confederate, and Caregiver based on the 'Respondent' column, and only the relevant subsets are merged as per the user's selection.
- **Unique Key Generation**: For each merged pair, a unique key is generated to identify matched rows. The generated key is then merged back into the original dataset.

### User Interaction

- **Respondent Selection**: The user is prompted via a dialog box to select the respondents to compare.
- **File Dialogs for Input and Output**: The user selects the input CSV file and output directory using file dialogs.

### Key Steps

1. **Loading the Dataset**: The script loads the dataset using `pandas` and prompts the user to specify the input file and output directory.
2. **Selecting Respondents**: The user selects which respondents to compare via a dialog box.
3. **Separating Data**: The script separates the dataset into IOA, Confederate, and Caregiver subsets based on the 'Respondent' column.
4. **Merging Data**: Based on the user's selection, the relevant subsets are merged using common identifiers (`CaregiverID`, `StudyPhase`, `SessionType`, `SessionCount`, `Merge_TotalSessionTrials`).
5. **Generating Unique Keys**: A unique key is generated for each matched row and merged back into the original dataset.
6. **Exporting Final Dataset**: The final dataset, now containing unique keys for each matched pair, is saved to a new CSV file.



## Script Documentation: **IOAxCONFxCARE Fully Keyed Data Prep**

###### - TechPT - 2024.10.18 - Combine Keyed Tables based on Instance.py

### Purpose

This script processes a CSV dataset to fully key and merge multiple observations from different respondents (IOA, Confederate, and Caregiver) into a single, unified dataset for further kappa analysis. The goal is to ensure all relevant keys are aligned for paired observations while maintaining duplicate records to reflect paired or multiple interactions. The final dataset is saved with all columns aligned for consistency and further analysis.


### CSV Dataset

The input CSV dataset contains observation data related to the IOA, Confederate, and Caregiver responses. It includes columns such as:

This was manually created by copy and pasting each of the previous keyed tables into a single Excel sheet.

- **InstanceID**: A unique identifier for each observation.
- **Respondent**: Specifies the type of respondent (IOA, Confederate, or Caregiver).
- **CaregiverID, StudyPhase, SessionType, SessionCount, Merge_TotalSessionTrials**: Various metadata about the trial or observation, such as session and phase identifiers.
- **Key Columns**: (`IOAxCARE_Key`, `CONFxCARE_Key`, `IOAxCONF_Key`, `CONFxCARExIOA_Key`) represent unique keys assigned to matched observations across different respondents.
- **Monitoring Columns**: Includes multiple columns (`ConfMonitoring1`, `ConfMonitoring2`, `IOAMonitoring1`, etc.) used to capture specific observation details.


### Key Steps

#### 1. Loading and Preparing the Dataset

- The script begins by importing necessary libraries (`pandas`, `os`, `tkinter`).
- It prompts the user to select the input CSV file containing the previously merged and keyed observation data.
- The CSV file is loaded into a pandas DataFrame.
- The script ensures that all columns are consistent and in the correct order, adding missing columns if needed.

```python
# Import necessary libraries
import pandas as pd
import os
from tkinter import filedialog, Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input CSV file
print("Please select the CSV file to merge.")
input_file_path = filedialog.askopenfilename(title="Select CSV File to Merge", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if not input_file_path:
    print("No file selected. Exiting script.")
    exit()

# Load the selected CSV file into a DataFrame
combined_df = pd.read_csv(input_file_path)
```

#### 2. Ensuring Column Consistency

- The script defines a list of columns to ensure the DataFrame structure is standardized for merging.
- It iterates over the defined columns to add any missing columns to the loaded DataFrame, ensuring all columns are present and ordered.

```python
# Ensure all columns are in the same order
output_columns = [
    'InstanceID', 'EventNote', 'DateTimeStamp:', 'ResponseIDx', 'Respondent', 'CaregiverID', 'StudyPhase',
    'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', 'TrialDirection', 'CareDirStart',
    'CareDirEnd', 'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4', 'SelfMonitoring5',
    'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3', 'ConfResponse',
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6',
    'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3', 'ConfChildResponse', 'ConfederateInteraction',
    'ConfTrialNote', 'ConfSessionNote', 'IOAVideoName', 'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3',
    'IOAMonitoring4', 'IOAMonitoring5', 'IOAMonitoring6', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3',
    'IOAChildResponse', 'IOAConfederateInteraction', 'IOATrialNote', 'IOASessionNote', 'IOAxCARE_Key',
    'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key'
]

# Ensure all output columns are present, adding missing columns if necessary
for col in output_columns:
    if col not in combined_df.columns:
        combined_df[col] = pd.NA

# Reorder columns
combined_df = combined_df[output_columns]
```

#### 3. Iterative Key Resolution

- The script iterates through the DataFrame row by row, searching for duplicate `InstanceID` values.
- For each unique `InstanceID`, it collects all duplicates and combines the key values into the first occurrence.
- After processing each `InstanceID`, the fully resolved row is appended to a new DataFrame (`resolved_df`).

```python
# Create a new DataFrame to store the resolved rows
resolved_df = pd.DataFrame(columns=combined_df.columns)

# Iterate through each row to handle duplicate InstanceIDs
while not combined_df.empty:
    # Take the first row and create a copy
    current_row = combined_df.iloc[0].copy()
    instance_id = current_row['InstanceID']

    # Find all rows with the same InstanceID
    duplicate_rows = combined_df[combined_df['InstanceID'] == instance_id]

    # Combine key values from duplicates into the first occurrence
    for _, duplicate_row in duplicate_rows.iterrows():
        for key_col in ['IOAxCARE_Key', 'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key']:
            if pd.isna(current_row[key_col]) and not pd.isna(duplicate_row[key_col]):
                current_row[key_col] = duplicate_row[key_col]

    # Append the resolved row to the new DataFrame
    resolved_df = pd.concat([resolved_df, current_row.to_frame().T], ignore_index=True)

    # Drop the processed rows from the combined DataFrame
    combined_df = combined_df[combined_df['InstanceID'] != instance_id]
```

#### 4. Exporting the Final Dataset

- After resolving all duplicates and keys, the final DataFrame (`resolved_df`) is saved to a new CSV file.
- The output filename is specified as `resolved_merged_keyed_data.csv`, and the user is prompted to select an output directory.

```python
# Open a file dialog to specify the output directory
print("Please select the output directory.")
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate output file name
output_file_name = 'resolved_merged_keyed_data.csv'
output_file_path = os.path.join(output_dir, output_file_name)

# Save the resolved DataFrame to a new CSV file
resolved_df.to_csv(output_file_path, index=False)

print(f"Resolved merged data saved to {output_file_path}")
```

### Summary

The script successfully combines multiple keyed datasets into a unified dataset by fully keying paired observations from different respondents. It uses a row-by-row approach to iteratively match `InstanceID` values and fill missing keys in the first occurrence of each duplicate. The final dataset is output with all rows aligned, maintaining all necessary keys for kappa analysis and further processing.


## Script Documentation **Flattening Process Documentation for IOA and Confederate Data**

- TechPT - 2024.10.18 - Script - IOAxCONF - flatten Kappa prep.py

This document explains the flattening process of merging and collapsing rows from the IOA (Independent Observer Agreement) and Confederate datasets into a single combined dataset, termed 'IOAxCONF'. The goal of this script is to create a more manageable format by combining multiple datasets while preserving key information.

### Overview

The flattening process involves the following key steps:

1. **Loading Data**: The script starts by allowing the user to select an input CSV file containing both IOA and Confederate data using a file dialog. Once selected, the data is loaded into a pandas DataFrame for further manipulation.

2. **Ensuring Data Consistency**: The columns that are used for merging purposes (‘CaregiverID’, ‘StudyPhase’, ‘SessionType’, ‘SessionCount’, ‘Merge_TotalSessionTrials’, ‘SessionBlockCount’, and ‘IOAxCONF_Key’) are converted to strings to ensure consistency. This step helps prevent data type mismatches during the merging process.

3. **Splitting the Dataset**: The script separates rows into two different datasets based on the 'Respondent' column value:
   - **IOA Data**: Contains rows where the respondent is the independent observer (labeled as '2_IOA').
   - **Confederate Data**: Contains rows where the respondent is the confederate (labeled as '1_CONF').

4. **Merging IOA and Confederate Data**: The IOA and Confederate datasets are merged on the 'IOAxCONF_Key' column, which serves as a unique identifier for the corresponding pairs. The result is a new DataFrame that contains rows from both datasets, paired according to matching keys.

5. **Collapsing Data**: For each merged row, a new collapsed row is created to combine relevant data from both the IOA and Confederate rows. Specific fields are prioritized as follows:
   - **Key Metadata**: The collapsed row retains information such as the 'InstanceID', 'CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', and 'DateTimeStamp' from the Confederate data.
   - **Respondent Label**: The 'Respondent' field is set to '3_IOAxCONF', indicating that the row is a combination of IOA and Confederate data.
   - **Monitoring Columns**: The monitoring data from both IOA and Confederate respondents are retained. Columns from each source are clearly labeled (e.g., 'Monitoring1_Conf' for Confederate data and 'Monitoring1_IOA' for IOA data).
   - **DateTimeStamp**: The timestamp from the Confederate entry ('DateTimeStamp_Conf') is preserved in the final collapsed dataset to retain chronological information.

6. **Saving the Collapsed Data**: Finally, the script saves the collapsed dataset into a new CSV file, appending the filename with '_collapsed_IOAxCONF'.

### Input File

- **Input Filename**: `TechPT - 2024.10.18 - Data - IOAxCONFxCARE Fully Keyed and cleaned for Kappa v2.csv`
- Processed by `TechPT - 2024.10.18 - Combine Keyed Tables based on Instance.py`

### Output
- `TechPT - 2024.10.18 - Data - IOAxCONF_Keyed_flat.csv`
The final output is a CSV file that combines the relevant rows from both datasets into a single, more concise dataset that includes key information from both the IOA and Confederate observers. The output CSV includes:
- Key identifiers for each trial or session.
- Monitoring details from both IOA and Confederate perspectives.
- Preserved key metadata and timestamps to ensure data traceability.

### Script Details

```python
import pandas as pd
import os
from tkinter import filedialog, Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input file
print("Please select the input CSV file.")
input_file_path = filedialog.askopenfilename(title="Select Input CSV File")
# Check if a file was selected
if not input_file_path:
    print("No file selected. Exiting script.")
    exit()

# Generate output file name based on the input file name
input_file_name = os.path.basename(input_file_path)
output_file_name = os.path.splitext(input_file_name)[0] + '_collapsed_IOAxCONF.csv'

# Load the selected CSV file into a DataFrame
loadedCSV_data = pd.read_csv(input_file_path)

# Ensure the relevant columns are strings for merging and manipulation purposes
for col in ['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', 'IOAxCONF_Key']:
    loadedCSV_data[col] = loadedCSV_data[col].astype(str)

# Separate the IOA and Confederate rows based on 'Respondent'
ioa_data = loadedCSV_data[loadedCSV_data['Respondent'] == '2_IOA']
confederate_data = loadedCSV_data[loadedCSV_data['Respondent'] == '1_CONF']

# Merging IOA and Confederate data based on the matching key 'IOAxCONF_Key'
merged_data = pd.merge(
    ioa_data,
    confederate_data,
    on='IOAxCONF_Key',
    suffixes=('_IOA', '_Conf')
)

# Creating the final collapsed dataset
collapsed_data = []

# Iterating over the merged rows to collapse data
for _, row in merged_data.iterrows():
    collapsed_row = {}

    # Use relevant fields from the 1_CONF row
    collapsed_row['InstanceID'] = row['InstanceID_Conf']
    collapsed_row['CaregiverID'] = row['CaregiverID_Conf']
    collapsed_row['StudyPhase'] = row['StudyPhase_Conf']
    collapsed_row['SessionType'] = row['SessionType_Conf']
    collapsed_row['SessionCount'] = row['SessionCount_Conf']
    collapsed_row['Merge_TotalSessionTrials'] = row['Merge_TotalSessionTrials_Conf']
    collapsed_row['SessionBlockCount'] = row['SessionBlockCount_Conf']
    collapsed_row['DateTimeStamp'] = row['DateTimeStamp_Conf']

    # Set Respondent to 3_IOAxCONF for the merged row
    collapsed_row['Respondent'] = '3_IOAxCONF'

    # Keep both sets of monitoring columns (Confederate and IOA)
    for prefix, suffix in [('Conf', '_Conf'), ('IOA', '_IOA')]:
        for col in [
            'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
            'SelfMonitoring5', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3',
            'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
            'ConfMonitoring5', 'ConfMonitoring6', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3',
            'ConfConfederateInteraction', 'ConfTrialNote',
            'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4',
            'IOAMonitoring5', 'IOAMonitoring6', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3',
            'IOAConfederateInteraction', 'IOATrialNote'
        ]:
            column_name = f"{col}{suffix}"
            if column_name in row:
                collapsed_row[column_name] = row[column_name]

    # Keep the IOAxCONF_Key
    collapsed_row['IOAxCONF_Key'] = row['IOAxCONF_Key']

    # Append the collapsed row to the final data list
    collapsed_data.append(collapsed_row)

# Convert collapsed data to a DataFrame
collapsed_data_df = pd.DataFrame(collapsed_data)
    
# Save the collapsed dataset to a CSV file
collapsed_data_df.to_csv(output_file_name, index=False)

print(f"Collapsed IOAxCONF dataset saved to {output_file_name}")
```

### Purpose and Benefits

This flattening process allows for a cleaner and more integrated dataset, making it easier to perform further analysis, such as calculating agreement between the IOA and Confederate observers. By combining the rows and clearly labeling the data from each source, it simplifies the interpretation of monitoring and observational data, making the final dataset more accessible for statistical analysis and comparison.

### Notes
- Each row in the final dataset represents a combined observation from the Confederate and IOA for a given key.
- The script prioritizes using Confederate data for metadata fields, ensuring consistency in identifying key sessions.
- All original monitoring fields are preserved under distinct labels to ensure there is no loss of information.

## Script documentation **IOAxCONF Kappa Prep Script Documentation**

- TechPT - 2024.10.18 - Script - IOAxCONF Kappa Calculator V2.py

### Overview
This script processes and compares data collected during observations by multiple observers: the Confederate (CONF) observer and the Inter-Observer Agreement (IOA) observer. The main goal is to determine the level of agreement between the observers and compute metrics that indicate the reliability of their observations. This is achieved using a confusion matrix and calculating the observed agreement (P_o).

### Confusion Matrix Breakdown
The confusion matrix is used to categorize the comparisons between the Confederate observer and the IOA observer into four categories:

- **`A` (True Positive Agreement)**: Both the Confederate (CONF) and the IOA observers agree that the behavior or event occurred (`1`).
  - Example: If `ConfMonitoring1` is `1` and `IOAMonitoring1` is also `1`, we count this as an agreement (`A`).
  
- **`D` (True Negative Agreement)**: Both observers agree that the behavior or event **did not occur** (`0`).
  - Example: If `ConfMonitoring1` is `0` and `IOAMonitoring1` is also `0`, we count this as a negative agreement (`D`).

- **`B` (False Positive)**: The Confederate observer recorded a behavior occurrence (`1`), but the IOA observer did **not** (`0`).
  - Example: If `ConfMonitoring1` is `1` and `IOAMonitoring1` is `0`, this is considered a false positive, leading to disagreement (`B`).
  
- **`C` (False Negative)**: The Confederate observer did **not** record the behavior (`0`), but the IOA observer recorded it as occurring (`1`).
  - Example: If `ConfMonitoring1` is `0` and `IOAMonitoring1` is `1`, this is considered a false negative, leading to disagreement (`C`).

### Confusion Matrix Summary
|                | IOA = 1 (Event Occurred) | IOA = 0 (Event Did Not Occur) |
|----------------|--------------------------|-------------------------------|
| **CONF = 1**   | **A** (True Positive)     | **B** (False Positive)        |
| **CONF = 0**   | **C** (False Negative)    | **D** (True Negative)         |

#### Matrix Calculations
1. **Matrix_A (True Positive Count)**:
   - This counts the number of times both the Confederate and IOA marked a behavior as occurring (`1`).
  
2. **Matrix_B (False Positive Count)**:
   - This counts the number of times the Confederate marked a behavior as occurring (`1`), but the IOA did not (`0`).

3. **Matrix_C (False Negative Count)**:
   - This counts the number of times the Confederate marked a behavior as not occurring (`0`), but the IOA marked it as occurring (`1`).

4. **Matrix_D (True Negative Count)**:
   - This counts the number of times both observers marked a behavior as not occurring (`0`).

#### Overall Metrics
- **`AD_Count`**: The total count of `A` and `D` (agreements) in the dataset.
  - `AD_Count = Matrix_A + Matrix_D`
  
- **`ABCD_Count`**: The total count of all possible outcomes (`A`, `B`, `C`, `D`).
  - `ABCD_Count = Matrix_A + Matrix_B + Matrix_C + Matrix_D`
  
- **`P_o` (Observed Agreement)**: The proportion of times that the Confederate and IOA agreed, either positively (`A`) or negatively (`D`).
  - `P_o = AD_Count / ABCD_Count` if `ABCD_Count > 0`

### Example with Data
In the data processed by the script:
- `Matrix_A = 3` means there were 3 cases of `True Positive Agreement` (`A`).
- `Matrix_B = 1` means there was 1 `False Positive` (`B`).
- `Matrix_C = 0` means there were no `False Negatives` (`C`).
- `Matrix_D = 4` means there were 4 `True Negative Agreements` (`D`).
- `AD_Count = 3 + 4 = 7`
- `ABCD_Count = 3 + 1 + 0 + 4 = 8`
- `P_o = 7 / 8 = 0.875` (which means an 87.5% agreement rate between observers for that particular row).

### Purpose of Confusion Matrix in Kappa Calculation
The confusion matrix values (`A`, `B`, `C`, `D`) help in calculating Cohen's Kappa, which corrects for the possibility of agreement happening by chance. 

Cohen's Kappa formula is:

\[
Kappa = \frac{P_o - P_e}{1 - P_e}
\]

Where:
- `P_o` is the observed agreement.
- `P_e` is the expected agreement by chance, calculated based on marginal probabilities.

Having a detailed confusion matrix helps to clearly differentiate between types of agreement (`A`, `D`) and disagreement (`B`, `C`) and thus derive meaningful insights on the reliability of the Confederate's ratings compared to the IOA observer.

### How the Script Processes Data
The script reads in a CSV file containing data collected by the Confederate and IOA observers. The key steps include:
1. **Data Loading and Cleaning**: Load the data into a DataFrame, reorder columns, and convert to appropriate data types.
2. **Comparison of Observer Ratings**: Loop through each row of the data, compare the monitoring values from the Confederate and IOA observers, and classify them into `A`, `B`, `C`, or `D`.
3. **Generating Comparison Results**: Store the comparison results into a new DataFrame, including metrics such as `Matrix_A`, `Matrix_B`, `Matrix_C`, `Matrix_D`, `AD_Count`, `ABCD_Count`, and `P_o`.
4. **Save Results**: Save the resulting comparison data to a new CSV file for further analysis.

This approach provides a structured and systematic way to evaluate observer reliability and highlight discrepancies in recorded behavior.

## Script Documentation **Documentation for TechPT - 2024.10.18 - Script - IOAxCONF Kappa Calculator V2.py**

### **Overview**
This script processes observational data from different respondents to prepare the data for subsequent analysis. Specifically, it assesses interobserver agreement using Cohen's Kappa by merging and comparing observational variables between respondents, such as IOA (Interobserver Agreement), CONF (Confederate), and CARE. The script generates a CSV output to store comparison results in a structured format, divided into smaller sections for clarity:

- **Purpose**: Assess interobserver agreement using Cohen's Kappa.
- **Data Sources**: Observational data from respondents such as IOA, CONF, and CARE.
  - `TechPT - 2024.10.18 - Data - IOAxCONF_Keyed_flat.csv`
  - `Processed by TechPT - 2024.10.18 - Script - IOAxCONF - flatten Kappa prep.py`
- **Output**: A CSV file with detailed observer agreement metrics for further analysis.

### **Key Features**

**1. Import Libraries**
The necessary Python libraries are imported:

- `pandas` for data manipulation.
- `os` to handle file paths effectively.
- `tkinter` to provide a user-friendly file selection dialog.

**2. File Path Configuration**
The script uses a user-selected file path, enabling the selection of CSV data via a graphical user interface (GUI). This approach makes the script more user-friendly by allowing users to easily select the input CSV file containing data with observations made by different respondents:

```python
from tkinter import Tk, filedialog

# Open a file dialog for the user to select the input CSV file
root = Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select the input CSV file", filetypes=[("CSV files", "*.csv")])
```

**3. Respondent Choice**
The script prompts the user to select which type of respondent comparison they want to perform. The available choices are as follows:

- `1` for IOA and CONF comparison (`IOAxCONF_Key`)
- `2` for IOA and CARE comparison (`IOAxCARE_Key`)
- `3` for CONF and CARE comparison (`CONFxCARE_Key`)
- `4` for all three respondents comparison (`CONFxCARExIOA_Key`)

The choice will determine which observations to compare within the script:

```python
respondent_choice = input("Select respondent choice:\n1. IOA vs CONF\n2. IOA vs CARE\n3. CONF vs CARE\n4. IOA, CONF, and CARE\nEnter choice (1-4): ")
comparison_label = ''
if respondent_choice == '1':
    comparison_label = 'IOAxCONF_Key'
elif respondent_choice == '2':
    comparison_label = 'IOAxCARE_Key'
elif respondent_choice == '3':
    comparison_label = 'CONFxCARE_Key'
elif respondent_choice == '4':
    comparison_label = 'CONFxCARExIOA_Key'
else:
    raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
```

**4. Output File Generation**
The output file name is generated based on the input file name and respondent choice, allowing traceability of the processing performed:

```python
input_file_name = os.path.basename(input_file_path)
output_file_name = os.path.splitext(input_file_name)[0] + '_' + comparison_label + '_RawAgreement.csv'
output_file_path = os.path.join(os.path.dirname(input_file_path), output_file_name)
```

This ensures that every processed file is easily identifiable and linked to the specific analysis performed.

**5. Load CSV Data**
The selected input CSV file is read into a pandas DataFrame:

```python
loadedCSV_data = pd.read_csv(input_file_path)
```

To ensure that the data loads correctly, the script prints the first two rows of the loaded data for verification.

**6. Ensure Column Order and Presence**
The script enforces a specific column order, ensuring consistency throughout the dataset. If any expected column is missing, it adds it with missing values (`pd.NA`). This step ensures that the loaded dataset has all necessary columns for further analysis:

```python
output_columns = [
    'InstanceID', 'DateTimeStamp', 'Respondent', 'CaregiverID', 'StudyPhase',
    'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', 'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4', 'SelfMonitoring5',
    'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3',
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4', 'ConfMonitoring5',
    'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3', 'ConfConfederateInteraction', 'ConfTrialNote',
    'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4', 'IOAMonitoring5', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3',
    'IOAConfederateInteraction', 'IOATrialNote', 'IOAxCARE_Key', 'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key'
]
```

**7. Ensure Consistent Data Types**
The script enforces consistent data types across columns for accurate calculations and analyses:

- Columns like `'InstanceID'`, `'Respondent'`, `'CaregiverID'`, `'StudyPhase'`, `'SessionType'`, `'ConfTrialNote'`, and `'IOATrialNote'` are set as strings (`str`), given that they contain non-numeric information.
- The remaining columns are set to floating-point values (`float64`), which allows for performing arithmetic and statistical operations when needed.

**9. Comparison Results DataFrame**
A new DataFrame (`comparison_results`) is prepared to store the outcome of the observation comparisons. This DataFrame will ultimately be saved as an output CSV file for subsequent analysis.

**10. Comparison Logic**
The script iterates through each row of the loaded data and performs a detailed comparison of the monitoring columns (`SelfMonitoring`, `ConfMonitoring`, and `IOAMonitoring`). For each row, the script follows these steps:

- **Columns Compared**: The columns being compared include `SelfMonitoring1`, `SelfMonitoring2`, `SelfMonitoring3`, `SelfMonitoring4`, `SelfMonitoring5`, `SelfMonitoring6a_1`, `SelfMonitoring6a_2`, and `SelfMonitoring6a_3`.
- **Comparison Process**:
  - For each monitoring column, the script identifies the corresponding `ConfMonitoring` and `IOAMonitoring` columns.
  - It compares the values between the `ConfMonitoring` and `IOAMonitoring` columns for each monitoring pair.
  - Depending on whether the values agree or disagree, the following outcomes are recorded:
    - **Positive Agreement (A)**: Both `ConfMonitoring` and `IOAMonitoring` values are `1`.
    - **Negative Agreement (D)**: Both `ConfMonitoring` and `IOAMonitoring` values are `0`.
    - **False Positive (B)**: `ConfMonitoring` is `1` and `IOAMonitoring` is `0`.
    - **False Negative (C)**: `ConfMonitoring` is `0` and `IOAMonitoring` is `1`.
  - If either value is missing (`NaN`), the comparison result is recorded as missing (`pd.NA`).
- **Appending Results**: The results of these comparisons are then appended to the current row, creating new columns (e.g., `Monitoring1`, `Monitoring2`, etc.) that store the outcomes (`A`, `B`, `C`, `D`, or `NaN`).
- The modified row is then added to the `comparison_results` list, which will be used to create the final results DataFrame.

**11. Save Comparison Results**
Finally, the comparison results DataFrame is saved as a CSV file:

```python
comparison_results_df.to_csv(output_file_path, index=False)
```

This allows for easy re-use and further analysis of the comparison outcomes, particularly for statistical measures like Cohen's Kappa.

**Next Steps**
The script currently includes the preliminary steps for loading, preparing, and structuring the data. The next steps involve refining the comparison logic between IOA and CONF observations to produce meaningful comparison metrics, such as agreement levels, which will then be used to calculate interobserver agreement indices such as Cohen's Kappa. Using Excel or Python... BOTH! 



## Script Documentation: **IOAxCONF - asklearn Kappa**

- **TechPT - 2024.10.19 - Script - IOAxCONF - sklearn Kappa.py**

### **Overview**

This script processes and compares observational data between the Confederate (CONF) observer and the Inter-Observer Agreement (IOA) observer, now with added functionality to calculate Cohen’s Kappa using the `scikit-learn` library. The purpose is to assess interobserver agreement and generate metrics (Cohen’s Kappa and percentage agreement) to evaluate the reliability of observations. The results are saved to a CSV file for further analysis.

### **Key Changes from Previous Version**

1. **Cohen's Kappa Calculation**:
   The core update in this version is the calculation of Cohen’s Kappa using `scikit-learn`'s `cohen_kappa_score` method. Unlike the previous version, which required manual construction of a confusion matrix, this version leverages the sklearn function for direct calculation. Cohen’s Kappa adjusts for chance agreement, giving a more robust reliability estimate compared to simple percentage agreement.

2. **Handling Missing Values**:
   This version includes improvements for handling missing data by automatically filtering out NaN values during the comparison of Confederate and IOA observations. This ensures accurate calculations and prevents errors due to incomplete data.

3. **Calculation for Different Subsets**:
   The script now calculates Kappa not only for the entire dataset but also for each subset of data (e.g., specific `CaregiverID` or `StudyPhase`), providing more detailed insights into interobserver agreement across different study phases and participants.

### **Key Features**

**1. Import Libraries**
```python
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from tkinter import filedialog
from tkinter import Tk
import numpy as np
```
- The `cohen_kappa_score` function from `scikit-learn` is used for calculating Cohen's Kappa, streamlining the analysis compared to manually managing confusion matrices.

**2. File Path Configuration**
The script prompts the user to select the input CSV file through a graphical file dialog:
```python
Tk().withdraw()  # Hide the main Tkinter window
file_path = filedialog.askopenfilename(title="Select CSV File")
df = pd.read_csv(file_path)
```

**3. Data Preparation**
The script casts relevant columns to `float64` and drops rows with missing values in the key monitoring columns:
```python
df = df.astype({...})
df.dropna(subset=[...], inplace=True)
df = df[df['CaregiverID'] != 'Case4']  # Exclude specific case
```

**4. Observations Comparison and Flattening**
Data from Confederate and IOA columns are flattened into arrays for comparison:
```python
rater1_all = df[['ConfMonitoring1', ...]].to_numpy().flatten()
rater2_all = df[['IOAMonitoring1', ...]].to_numpy().flatten()

# Remove NaN values
mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
rater1_all = rater1_all[mask]
rater2_all = rater2_all[mask]
```

**5. Cohen's Kappa Calculation for Entire Dataset**
Using `cohen_kappa_score`, the script computes Cohen’s Kappa for all observations:
```python
kappa = cohen_kappa_score(rater1_all, rater2_all)
percent_agreement = np.mean(rater1_all == rater2_all)
num_observations = len(rater1_all)
results.append(["Entire Set", kappa, percent_agreement * 100, num_observations])
```

**6. Per-Column Cohen's Kappa**
In this version, Cohen’s Kappa and percentage agreement are computed for each individual Confederate and IOA column pair:
```python
for conf_col, ioa_col in zip(conf_rater_columns, ioa_rater_columns):
    rater1 = df[conf_col]
    rater2 = df[ioa_col]
    kappa = cohen_kappa_score(rater1, rater2)
    percent_agreement = np.mean(rater1 == rater2)
    num_observations = len(rater1.dropna())
    results.append([f"{conf_col} vs {ioa_col}", kappa, percent_agreement * 100, num_observations])
```

**7. Subset-Based Cohen's Kappa**
The dataset is split by `CaregiverID` and `StudyPhase` to calculate Cohen’s Kappa for specific subgroups:
```python
for (caregiver_id, study_phase), group in df.groupby(['CaregiverID', 'StudyPhase']):
    rater1_all = group[conf_rater_columns].to_numpy().flatten()
    rater2_all = group[ioa_rater_columns].to_numpy().flatten()
    
    mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
    rater1_all = rater1_all[mask]
    rater2_all = rater2_all[mask]

    kappa = cohen_kappa_score(rater1_all, rater2_all)
    percent_agreement = np.mean(rater1_all == rater2_all)
    num_observations = len(rater1_all)
    results.append([f"CaregiverID {caregiver_id}, StudyPhase {study_phase}", kappa, percent_agreement * 100, num_observations])
```

**8. Save Results**
The comparison results are saved to a CSV file using a file dialog:
```python
results_df = pd.DataFrame(results, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations"])
output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
if output_file_path:
    results_df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")
```

### **Example Output**
1. **Cohen's Kappa for Entire Dataset**:
   - Prints Cohen's Kappa and the percentage agreement for the entire set of observations:
   ```plaintext
   Cohen's Kappa for the entire set: 0.83
   Percentage Agreement for the entire set: 87.50%
   Number of observations for the entire set: 1072
   ```

2. **Per-Column Cohen's Kappa**:
   - Example output for column pair comparisons:
   ```plaintext
   Cohen's Kappa between ConfMonitoring1 and IOAMonitoring1: 0.79
   Percentage Agreement between ConfMonitoring1 and IOAMonitoring1: 85.00%
   Number of observations: 134
   ```

3. **Subset-Based Kappa**:
   - Example output for CaregiverID and StudyPhase subset:
   ```plaintext
   Cohen's Kappa for CaregiverID A, StudyPhase 1: 0.76
   Percentage Agreement for CaregiverID A, StudyPhase 1: 84.23%
   Number of observations: 100
   ```

### **New Advantages**
- **Simplified Kappa Calculation**: Using `scikit-learn` removes the need for manual confusion matrix calculations, simplifying and speeding up the analysis.
- **Robust Handling of NaN Values**: The script automatically filters out missing values from the dataset, ensuring clean comparisons.
- **Granular Analysis**: By splitting the dataset into subsets, the script provides detailed insights into specific groups, helping assess agreement in various study phases.

### **Output File**
The script saves the results as a CSV file, containing the following columns:
- **Section**: Description of the comparison (e.g., "Entire Set", "ConfMonitoring1 vs IOAMonitoring1").
- **Cohen's Kappa**: The Kappa value for that comparison.
- **Percentage Agreement (%)**: The percentage of exact matches between raters.
- **Number of Observations**: The total number of observations included in the comparison.



## Script Documentation: Self-Monitoring Data Analysis


**Initial Dataset Title:** TechPT - 2024.10.18 - Data - IOAxCONFxCARE Fully Keyed and cleaned for Kappa v2

**Current Dataset Title:** TechPT - 2024.10.20 - Data - CARExCONF - SelfMonitoring V1.xlsx

**Note:** Only training phases are included. No self-monitoring data from Baseline (BL) or Return to Baseline (RTB) phases.

### Task Overview

This document provides a summary of the entire workflow for analyzing the IOA (Interobserver Agreement) between **CONF** (Confederate) and **CARE** (Caregiver) for self-monitoring. The focus is on calculating Cohen's Kappa statistic to assess interobserver reliability during the training phases. Each step lists the data preparation process, merging of key tables, data cleaning, and corresponding calculations.

### Step-by-Step Workflow

#### **Step 1: Initial Data Extraction and Cleaning**

- The dataset was manually arranged in Excel to ensure proper formatting and inclusion of only relevant observations from CONF and CARE during the self-monitoring training phases. Entries from Baseline (BL) and Return to Baseline (RTB) phases were excluded.
- A missing entry was identified and captured from the Master Table. The missing entry (InstanceID: `1phcqur8wf`, CaregiverID: `Case1`, StudyPhase: `3_T3`, etc.) was included to ensure the completeness of the dataset for analysis.

#### **Step 2: InstanceID Splitting and Sorting**

- A new column was added to split the **InstanceID** into `InstanceID_CONF` and `InstanceID_CARE` to facilitate merging. The formula used for splitting was: `=IF(D2="0_CARE", A2)`. This ensured clear distinction between CONF and CARE observations.
- A custom sort was applied by ascending **CONFxCare_Key** and then by ascending **Respondent** to alternate the data for simple merging. Cells in **A1** and **U1** were deleted to create an alternating pattern, streamlining the merging process.
- The **Respondent** value for all entries was updated to `7_CONFxCARE` to reflect combined observations of CONF and CARE during the self-monitoring phase.
- The dataset was further sorted by **InstanceID_CONF**, and all leftover metadata was manually deleted to ensure only relevant observation data remained for analysis.

#### **Step 3: Dataset Cleanup and Metadata Handling**

- Ensured there are no empty cells in the following columns: **InstanceID_CONF, InstanceID_CARE, DateTimeStamp, Respondent, CONFxCARE_Key, CaregiverID, StudyPhase, SessionType, SessionCount, Merge_TotalSessionTrials, ConfMonitoring1, ConfMonitoring2, ConfMonitoring3, ConfMonitoring4, ConfMonitoring5, ConfMonitoring6, ConfMonitoring6a_1, ConfMonitoring6a_2, ConfMonitoring6a_3**.
- During **Study Phase 1_T1**, the columns **SelfMonitoring3, SelfMonitoring4, SelfMonitoring5** were left empty, as no data was available for these variables in this phase.
- During **Study Phase 2_T2**, the columns **SelfMonitoring1, SelfMonitoring2, SelfMonitoring6, SelfMonitoring6a_1, SelfMonitoring6a_2, SelfMonitoring6a_3** were left empty, as no data was available for these variables in this phase.

#### **Step 4: Kappa Calculation and Analysis**

- Python was used to perform Cohen's Kappa calculations. The script filtered the dataset by study phase, dropping columns where no data was available.
  - **Filtered Datasets**: Specific columns were dropped for different study phases to align with available data:
    - **Study Phase 1_T1**: Dropped columns `SelfMonitoring3`, `SelfMonitoring4`, `SelfMonitoring5`, `ConfMonitoring3`, `ConfMonitoring4`, `ConfMonitoring5`.
    - **Study Phase 2_T2**: Dropped columns `SelfMonitoring1`, `SelfMonitoring2`, `SelfMonitoring6`, `SelfMonitoring6a_1`, `SelfMonitoring6a_2`, `SelfMonitoring6a_3`, `ConfMonitoring1`, `ConfMonitoring2`, `ConfMonitoring6`, `ConfMonitoring6a_1`, `ConfMonitoring6a_2`, `ConfMonitoring6a_3`.
    - **Study Phase 3_T3**: No columns were dropped.

- **Cohen's Kappa Calculation**: The analysis was conducted to measure the agreement between the CONF and CARE observers during the self-monitoring training phases. Cohen's Kappa values were calculated for each phase and for each monitoring item to assess the reliability of observations. The process involved the following key steps:
  - **Data Type Conversion**: Before calculations, the relevant columns were converted to float to ensure numerical operations could be performed without errors.
  - **Pairwise Analysis**: For each pair of columns (e.g., `ConfMonitoring1` vs. `SelfMonitoring1`), Cohen's Kappa was calculated to determine the level of agreement between the CONF and CARE observers.
  - **Handling Missing Values**: The script removed NaN values from both columns before performing calculations. This ensured that the analysis was based only on valid, complete observations.
  - **Metrics Calculation**: In addition to Cohen's Kappa, the following metrics were calculated for each pair of columns:
    - **Percentage Agreement**: The proportion of observations where both CONF and CARE raters agreed, either positively or negatively.
    - **True Positives (TP)**: The number of instances where both raters marked the behavior as present (`1`).
    - **True Negatives (TN)**: The number of instances where both raters marked the behavior as absent (`0`).
    - **False Positives (FP)**: The number of instances where the CARE rater marked the behavior as present (`1`) but the CONF rater did not (`0`).
    - **False Negatives (FN)**: The number of instances where the CONF rater marked the behavior as present (`1`) but the CARE rater did not (`0`).
    - **Expected Agreement**: The expected level of agreement by chance, calculated based on the marginal probabilities of each rater's responses.
    - **Kappa Interpretation**: The Kappa values were interpreted based on established guidelines:
      - **< 0**: No agreement
      - **0.01 - 0.20**: Slight agreement
      - **0.21 - 0.40**: Fair agreement
      - **0.41 - 0.60**: Moderate agreement
      - **0.61 - 0.80**: Substantial agreement
      - **0.81 - 1.00**: Almost perfect agreement

- **Omnibus Analysis**: In addition to the phase-specific analysis, an omnibus analysis was performed across the entire dataset to evaluate overall agreement, combining all study phases. This provided a holistic view of inter-rater reliability between CONF and CARE observers for self-monitoring.
  - **With and Without Monitoring6 Data**: The omnibus analysis was conducted twice—once including `Monitoring6` data and once excluding it. This allowed the assessment of how the inclusion of later-introduced monitoring items affected overall agreement.
  - **Results Summary**: The omnibus analysis provided insight into general trends, identifying whether certain phases or monitoring items consistently showed higher or lower levels of agreement.

Here is the integration of the *SelfMonitoring - Omnibus.py* script documentation into markdown, suitable for use in documentation or technical manuals.

```markdown
# SelfMonitoring - Omnibus.py Script Documentation

## Overview

This script, titled **SelfMonitoring - Omnibus.py**, performs a detailed analysis of self-monitoring data by calculating **Cohen's Kappa** and other inter-rater agreement metrics. The script is designed to evaluate the level of agreement between two raters—**the Confederate** and the **Self-Monitoring observer**—across multiple monitoring variables.

## Purpose

The primary goal of the script is to assess the **reliability** between Confederate Monitoring (ConfMonitoring) and Self Monitoring (SelfMonitoring) data by calculating **Cohen's Kappa**, **percentage agreement**, and other related metrics. The analysis is performed for each monitoring variable independently, as well as for the entire dataset (pooled data). This script provides further analysis based on these calculations.

## Steps of Analysis

### 1. Data Loading
The script uses the `tkinter` library to open a file dialog, allowing the user to select a CSV file containing the dataset. The selected CSV is loaded into a `pandas` DataFrame for analysis:

```python
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
from tkinter import filedialog
from tkinter import Tk

# Hide the root window
Tk().withdraw()

# Load the dataset
file_path = filedialog.askopenfilename(title="Select CSV File")
df = pd.read_csv(file_path)
```

### 2. Defining Columns for Comparison

The script defines two lists of monitoring variables, which represent columns in the dataset for comparison:

- **conf_monitoring_columns**: Columns corresponding to Confederate monitoring.
- **self_monitoring_columns**: Columns corresponding to Self-monitoring.

```python
conf_monitoring_columns = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
]
self_monitoring_columns = [
    'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
    'SelfMonitoring5', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3'
]
```

### 3. Metric Calculation Function

The function `calculate_metrics()` is used to calculate the following metrics between pairs of columns representing ratings from two different raters:

- **Cohen's Kappa**: A measure of agreement beyond chance.
- **Percentage Agreement**: Percentage of instances where both raters agreed.
- **True Positive, False Positive, False Negative, True Negative**: Counts for specific agreement types.
- **Expected Agreement** and other intermediate reliability calculations.

```python
def calculate_metrics(rater1, rater2):
    if np.all(rater1 == rater2):
        kappa = 1.0
        percent_agreement = 100.0
    else:
        kappa = cohen_kappa_score(rater1, rater2)
        percent_agreement = np.mean(rater1 == rater2) * 100

    # Additional calculations for true/false positive/negative
    true_positive = np.sum((rater1 == 1) & (rater2 == 1))
    false_positive = np.sum((rater1 == 0) & (rater2 == 1))
    false_negative = np.sum((rater1 == 1) & (rater2 == 0))
    true_negative = np.sum((rater1 == 0) & (rater2 == 0))

    # Further calculations for Cohen's Kappa
    expected_agreement = (
        ((true_positive + false_negative) / len(rater1)) * ((true_positive + false_positive) / len(rater1))
        + ((false_positive + true_negative) / len(rater1)) * ((false_negative + true_negative) / len(rater1))
    )
    po_minus_pe = percent_agreement / 100 - expected_agreement
    one_minus_pe = 1 - expected_agreement
    k = po_minus_pe / one_minus_pe if one_minus_pe != 0 else np.nan

    return [kappa, percent_agreement, len(rater1), true_positive, false_positive, false_negative, true_negative, 
            expected_agreement, po_minus_pe, one_minus_pe, k]
```

### 4. Iterative Calculation for Monitoring Pairs

The script iterates over each pair of Confederate and Self-Monitoring columns, calculating the metrics and storing the results.

```python
# Initialize results list
results = []

# Calculate metrics for each pair
for conf_col, self_col in zip(conf_monitoring_columns, self_monitoring_columns):
    rater1 = df[conf_col].to_numpy()
    rater2 = df[self_col].to_numpy()

    # Handle NaN values
    mask = ~np.isnan(rater1) & ~np.isnan(rater2)
    rater1, rater2 = rater1[mask], rater2[mask]

    if len(rater1) > 0 and len(rater2) > 0:
        metrics = calculate_metrics(rater1, rater2)
        results.append([f"{conf_col} vs {self_col}"] + metrics)
```

### 5. Pooled Data Analysis

In addition to pairwise comparisons, the script performs an omnibus analysis by pooling all Confederate and Self-Monitoring columns into two arrays, calculating overall metrics.

```python
# Pooled analysis
rater1_all = df[conf_monitoring_columns].to_numpy().flatten()
rater2_all = df[self_monitoring_columns].to_numpy().flatten()

# Handle NaN values
mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
rater1_all, rater2_all = rater1_all[mask], rater2_all[mask]

# Calculate pooled metrics
if len(rater1_all) > 0 and len(rater2_all) > 0:
    metrics = calculate_metrics(rater1_all, rater2_all)
    results.append(["Entire Set"] + metrics)
```

### 6. Saving Results to CSV

Once all metrics are calculated, the script saves the results into a CSV file using a file dialog.

```python
# Define headers and export results to CSV
headers = [
    "Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations",
    "True Positive", "False Positive", "False Negative", "True Negative", 
    "Expected Agreement", "P_o - P_e", "1 - P_e", "k"
]

# Save results
results_df = pd.DataFrame(results, columns=headers)
output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
if output_file_path:
    results_df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")
else:
    print("No results to save.")
```

## Metrics Calculated

The script calculates the following metrics:

- **Cohen's Kappa**: Inter-rater reliability beyond chance.
- **Percentage Agreement**: Proportion of times both raters agreed.
- **True Positive, False Positive, False Negative, True Negative**: Specific agreement counts.
- **Expected Agreement** (*P_e*): Probability of chance agreement used in Cohen's Kappa calculation.

## Example Use Case

1. **Select CSV File**: The user selects the dataset file using the file dialog.
2. **Comparison and Analysis**: The script performs pairwise and pooled dataset comparison for Confederate and Self-Monitoring columns.
3. **Save Results**: The script allows the user to save the results into a CSV file for further analysis.

## Summary

This script is a powerful tool for assessing the reliability of observational data between Confederate and Self-Monitoring raters. By calculating Cohen's Kappa and other metrics, it provides insights into inter-rater agreement

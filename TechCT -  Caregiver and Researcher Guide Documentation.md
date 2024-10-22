# TechCT - Caregiver and Researcher Guide Documentation
2024.10.21


## Table of Contents

- [Introduction](#introduction)
- [JavaScript Integration in Qualtrics](#javascript-integration-in-qualtrics)
  - [Overview](#overview)
  - [Implementation](#implementation)
    - [Hosting the Script](#hosting-the-script)
      - [Requirements of Hosting](#requirements-of-hosting)
      - [Hosting Troubleshooting](#hosting-troubleshooting)
    - [Integration in Survey](#integration-in-survey)
    - [Usage](#usage)
    - [Maintenance & Updates](#maintenance--updates)
- [Survey Link Formatting](#survey-link-formatting)
- [Variables](#variables)
  - [Embedded Data Configuration in Qualtrics Surveys](#embedded-data-configuration-in-qualtrics-surveys)
  - [Initialization](#initialization)
  - [Referencing](#referencing)
  - [Embedded Data Fields](#embedded-data-fields)
    - [Instance Code](#instance-code)
- [Survey Flow Logic and Block Naming Convention](#survey-flow-logic-and-block-naming-convention)
  - [Block Naming Convention](#block-naming-convention)
  - [Logic for Directing Respondents](#logic-for-directing-respondents)
  - [Trial Looping Logic](#trial-looping-logic)
    - [Overview](#overview-1)
    - [Key Components](#key-components)
  - [Setting Caregiver Direction Timestamps](#setting-caregiver-direction-timestamps)
    - [Implementation](#implementation)
    - [Usage](#usage-1)
    - [Integration](#integration-1)
    - [Flow Description](#flow-description)
    - [Considerations](#considerations)
  - [Incrementing Trial Count Variables](#incrementing-trial-count-variables)
    - [Implementation](#implementation-1)
    - [Usage](#usage-2)
    - [Functionality](#functionality)
    - [Integration](#integration-2)
  - [Testing Survey Logic and Managing Browser Sessions](#testing-survey-logic-and-managing-browser-sessions)
- [Function Descriptions](#function-descriptions)
  - [Current Date and Time Function in Qualtrics Survey](#current-date-and-time-function-in-qualtrics-survey)
    - [Function Overview](#function-overview)
    - [How It Works](#how-it-works)
    - [Usage](#usage-3)
    - [Customization](#customization)
- [Data Management](#data-management)
  - [Qualtrics Survey Data Structure and Organization](#qualtrics-survey-data-structure-and-organization)
    - [Response Data Table Column Details](#response-data-table-column-details)
  - [Exporting Data](#exporting-data)
    - [Export Options](#export-options)
  - [Qualtrics View Response Collection](#qualtrics-view-response-collection)
  - [Converting JSON Data to CSV](#converting-json-data-to-csv)
  - [Record Event Data Function in Qualtrics Survey](#record-event-data-function-in-qualtrics-survey)
    - [Function Overview](#function-overview-1)
    - [Embedded Data Field Limitations](#embedded-data-field-limitations)
    - [How It Works](#how-it-works-1)
    - [Sample JavaScript Implementation](#sample-javascript-implementation)
    - [Event Triggers](#event-triggers)
  - [Monitoring Question Response Data Entry](#monitoring-question-response-data-entry)
    - [JavaScript Code](#javascript-code)
      - [Code Explanation](#code-explanation)
  - [Mastery and Intervention Monitoring](#mastery-and-intervention-monitoring)
    - [Overview](#overview-2)
    - [Function Explanation](#function-explanation)
    - [Array Structure](#array-structure)
    - [Example Structure](#example-structure)
    - [Function Code](#function-code)
    - [Key Points](#key-points)
  - [Documentation for `evaluateAndProvideFeedback` Function](#documentation-for-evaluateandprovidefeedback-function)
    - [Overview](#overview-3)
    - [Function Explanation](#function-explanation-1)
    - [Function Code](#function-code-1)
    - [Key Points](#key-points-1)
    - [Mastery Criteria Update Documentation](#mastery-criteria-update-documentation)
- [Defined Direction Pool for Each Caregiver](#defined-direction-pool-for-each-caregiver)
  - [Object: `caregiverDirectionPool`](#object-caregiverdirectionpool)
- [Caregiver Direction Selection](#caregiver-direction-selection)
- [Confederate Response Selection](#confederate-response-selection)
- [Session and Trial Data Entry Synchronization Measures Using Embedded Data](#session-and-trial-data-entry-synchronization-measures-using-embedded-data)
  - [Implementation Strategies](#implementation-strategies)
- [Data Export](#data-export)
  - [Solution A: Reviewing Individual Response Entries on HTML](#solution-a-reviewing-individual-response-entries-on-html)
  - [Solution B: Tab Separated Values (.tsv)](#solution-b-tab-separated-values-tsv)
  - [Solution C: Manual Extraction and Transform](#solution-c-manual-extraction-and-transform)
    - [Converting JSON Data to CSV](#converting-json-data-to-csv)
    - [Solution C Data Transform Python Script](#solution-c-data-transform-python-script)
    - [Solution C JSON to CSV](#solution-c-json-to-csv)
- [Bugs and Issues](#bugs-and-issues)
- [Deprecated Features](#deprecated-features)
  - [Link Variables (Deprecated)](#link-variables-deprecated)
  - [Footer Update Function in Qualtrics Survey](#footer-update-function-in-qualtrics-survey)
    - [Footer Function Overview](#footer-function-overview)
    - [Footer HTML Housed in Qualtrics Look and Feel](#footer-html-housed-in-qualtrics-look-and-feel)
  - [Utilization of Supplemental Array to Manage Trial-by-Trial Observations](#utilization-of-supplemental-array-to-manage-trial-by-trial-observations)
  - [Mastery and Supplemental Instruction](#mastery-and-supplemental-instruction)




## Introduction

This documentation delineates the design and variable framework employed within the Qualtrics Survey platform for the technology-assisted caregiver training program (TechPT). The survey is crafted to support caregivers of children with behavioral challenges, utilizing a multi-tiered training approach. The primary research objective is to evaluate the impact of the training program on caregiver performance.

The study design incorporates a combination of multiple baseline across behaviors and a replicated AB design, facilitating within and between subject analysis. The survey framework, including block naming conventions and logic sequences, is tailored to seamlessly integrate with the study's multi-phase approach, centrally capturing data from both caregivers and confederates across various study phases and session types.

Core to the study's methodology is the use of digital guides facilitated through Qualtrics, ensuring standardized and efficient data collection. Two distinct session types are employed: simulated child and actual child. In both scenarios, caregivers are tasked with delivering directions. The actual child trial blocks serve as generalization probes, whereas in simulated blocks, caregivers practice with a confederate.

For seamless execution, caregivers are equipped with a session guide (personalized Qualtrics link with embedded data) delivered via text at the commencement of each session. This Qualtrics-based guide offers step-by-step directions to uniformly and systematically guide caregivers through the procedure.

Concurrently, confederates utilize a separate digital guide, also hosted on Qualtrics, during the simulated child trial blocks. This guide not only ensures adherence to the randomized behavior script but also provides a platform for monitoring caregiver interactions and evaluating their performance. The same guide is instrumental during actual child trial blocks, enabling confederates to systematically record both caregiver and child behaviors.

## JavaScript Integration in Qualtrics

### Overview

To enhance the flexibility and maintainability of the TechPT Qualtrics survey, a JavaScript library will be hosted. This library contains functions such as 'generateRandomString(length)' and objects such as the `caregiverDirectionPool`, which are used throughout the survey. By hosting a library, the code can me mananaged and updated without having to modify the javascript associated with individual questions or blocks within Qualtrics.

Qualtrics provides a built in javascript editor which is directly associated withi individual questions and blocks. Explanation of this functionality is described here: https://www.qualtrics.com/support/survey-platform/survey-module/question-options/add-javascript/ For the TechPT Survey, functions will be initiated by individual question blocks using the Qualtrics UI JavaScript Editor and called from the hosted javascript library.  The javascript within these blocks is reloaded each time a question is loaded. 

The Qualtrics 'add-javascript' documentation provides a reference for expanding the javascript functionality: "If you want to import JavaScript libraries, you can include a reference to them in the survey header within <'script> tags. Remember that even once you have referenced the library in your header, you must apply Javascript directly to applicable questions for that code to be pulled into the survey."

The Qualtrics does not provide JS jQuery Source but does offer a series of API references as a means to identify the Qualtrics.SurveyEngine functions and use cases : https://api.qualtrics.com/0f8fac59d1995-api-reference

### Implementation

#### Hosting the Script

##### Requirements of hosting

- Correct MIME Type: The server should serve the JavaScript library with the correct MIME type, which is application/javascript. This ensures that the browser recognizes the file as a JavaScript file and executes it accordingly.

- File Extension: The file should have a .js extension.

- Accessible URL: The URL where the JavaScript library is hosted should be publically accessible from any browser. Ensure that there are no server-side restrictions preventing the file from being accessed. Optimally the library would be hosted within the Qualtrics enviroment, secondaraly on a CMU managed server, and lastly on a public platform like GitHub. 

- CORS Headers: Currently have not had a need for this functionality, but may need to consider if any difficulties with security. If the JavaScript file is being accessed from a domain different from the one it's hosted on, you'll need to ensure that the server sends the appropriate CORS (Cross-Origin Resource Sharing) headers. This is to allow the browser to fetch and execute the script across domains. The header typically looks like this: Access-Control-Allow-Origin: *. The * allows any domain to access the resource, but for security reasons, you might want to replace * with the specific domain that will be accessing the script.

##### Hosting Troubleshooting

Initially the javascript library was hosted as a .txt file due to the Qualtrics UI blocking the upload of .js files. This resulted in a MIME type error as the Qualtrics UI was hosting the file as a  MIME type ('text/plain') which is not executable by a browser. A workaround was identfied to change the Qualtrics hosted file name to .js following the upload of a text, unfourtuatly this resulted in a MIME type error as well.

- The initial JavaScript library is hosted on Qualtrics at the following URL: https://PRIVATE
- The upload as .txt and change filename to .js  is hosted on Qualtrics at the following URL: https://PRIVATE
- As a temporary solution the javascript library is housed on a private server at: https://PRIVATE
  - There have been no functionality diffiuclties related to library hosting with this solution.

#### Integration in Survey

1. The script is added to the header of the survey. This ensures that it's loaded and available globally throughout the survey.
2. The script is referenced under `Look & Feel` section of the survey, click on the `General` tab.

```html
<script src="https://PRIVATE"></script>

//test changing file extension name in qualtrics
<script src="https://PRIVATE"></script>

//Temporarily housed  
<script src="https://PRIVATE"></script>
```

#### Usage

- With the script loaded, any functions can be called upon in subsequent JavaScript code within the survey.
- For instance, if you need to randomly select a direction for a caregiver, you can call the appropriate function directly.

#### Maintenance & Updates

- One of the primary advantages of this approach is centralized management. If updates or changes are required, modify the external script. These changes will automatically reflect wherever the script is linked in the survey.

## Survey Link formatting

To embed specific data into a Qualtrics survey through the link,  both the variable name and its associated value are appended to the core link URL. The general structure follows this format:

\[ Base Survey Link \]?\[ Embedded Variable Name \]=\[ Value \]

For incorporating multiple embedded variables, concatenate them using the "&" symbol.

Example link:

```
https://cmich.co1.qualtrics.com/jfe/form/SV_PRIVATE?CaregiverID=YOUR_VALUE&Respondent=YOUR_VALUE&StudyPhase=YOUR_VALUE&SessionType=YOUR_VALUE
```

For instance, for a confederate session guide (`1_CONF`) for caregiver ID `CG123`,during the baseline phase (`0_BL`), and the session type being actual child (`0_AC`), the resultant link appears as:

```
https://PRIVATE/jfe/form/SV_PRIVATE?CaregiverID=CG123&Respondent=1_CONF&StudyPhase=0_BL&SessionType=0_AC
```

The file, Session Link Generator.xlsx, offers an automated tool for specific link generation. 

The embedded Excel formula generating the link from individual columns is: 
```
="https://PRIVATE/jfe/form/SV_PRIVATE?CaregiverID=" & A2 & "&Respondent=" & B2 & "&StudyPhase=" & C2 & "&SessionType=" & D2 & "&SessionCount=" & E2
```

## Variables

This section provides an overview of the variables used in the Qualtrics survey and data analysis. These variables are essential for capturing, categorizing, and analyzing the data from the survey responses. They serve multiple purposes, such as identifying respondents, tracking survey progress, and storing specific data points.

Variables can be classified into two main categories:

Defined Variables: These are the primary variables that are explicitly defined in the survey to capture specific data points. They are typically set up as embedded data fields within the survey flow and can be populated from various sources, such as survey link parameters or respondent answers. Examples of defined variables include CaregiverID, StudyPhase, Respondent, SessionType, and SessionCount.

Defined variables are initialized through three different mechanisms:

1. Pre-Defined: 
   These are established variables within the Qualtrics survey structure.

2. Survey Link Initialized Embedded Fields:
   This branch of embedded data is populated by including the data as parameters in the survey link URL.
   The data is passed to the survey when a respondent clicks on the link or when the link is programmatically accessed.
   The embedded data fields are automatically populated with the values provided in the URL parameters.
   This approach is utilized to provide specific links to participants and configure the session to match study requirements.
   Examples of embedded data initialized via survey link include CaregiverID, StudyPhase, Respondent, SessionType, and SessionCount.

3. Survey Flow Initialized Embedded Fields:
   This branch of embedded data is defined and initialized within the survey flow using the "Embedded Data" element.
   The values for these embedded data fields are set directly within the survey flow, either as constants or derived from other survey elements or logic.
   This approach is useful when you need to set or modify embedded data values based on respondent answers, survey logic, or calculations performed within the survey.

Derived Variables: These variables are not explicitly defined in the survey but are calculated or derived based on other variables or survey responses. They are often used for data analysis or reporting purposes. Examples of derived variables could include total scores, percentages, or categorizations based on specific criteria.

The variables used in the survey play a crucial role in capturing relevant data points, enabling personalization and customization of the survey experience, and facilitating accurate data analysis. By leveraging embedded data fields and JavaScript, the survey can dynamically adapt to each respondent's specific context and track their progress throughout the study.

### Embedded Data Configuration in Qualtrics Surveys

Embedded data fields are a powerful feature in Qualtrics surveys that allow for dynamic storage and manipulation of information throughout the survey. They are crucial for initializing default values, populating data from survey link parameters, and making adjustments based on respondent answers. Embedded data fields provide a flexible and efficient way to personalize the survey experience and capture relevant data points.

A block titled **"Welcome - Survey Configuration - Embedded Data"** is created at the beginning of the survey flow. This initial block plays a pivotal role in setting up the foundation for data handling within the survey.

### Initialization

Within this initial block, essential embedded data fields are established. This step is critical for the declaration and initialization of each variable. It's important to note that these embedded data fields must first be initialized within Qualtrics "Survey Flow" before the header script can assign data to them. Once initialized, these fields remain active and accessible throughout the survey, allowing for their reference and modification in subsequent blocks, questions, and JavaScript.

### Referencing

When referencing embedded data fields in  survey questions, logic, or piped text, Qualtrics treats all branches of embedded data similarly. You can use the syntax `${e://Field/EmbeddedFieldName}` to access the values within the Qualtrics block design and `Qualtrics.SurveyEngine.getEmbeddedData('EmbeddedFieldName')` within JavaScript.

For example, to display the value of the `CaregiverID` embedded data field in a question text, use:
```
Your Caregiver ID is: ${e://Field/CaregiverID}
```

Similarly, to access the `StudyPhase` embedded data field in JavaScript, use:
```javascript
var studyPhase = Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase');
```

When referencing embedded data fields in survey logic or piped text, it's important to consider the following:

1. Case Sensitivity: Always start with a capital letter. Embedded data field names are case-sensitive. Make sure to use the exact name of the embedded data field when referencing it.

2. Proper Syntax: Use the correct syntax for referencing embedded data fields. In piped text or survey logic, use `${e://Field/EmbeddedFieldName}`, and in JavaScript, use `Qualtrics.SurveyEngine.getEmbeddedData('EmbeddedFieldName')`.

3. Default Values: If an embedded data field is not set or has an empty value, Qualtrics will treat it as an empty string (`""`) when referenced in piped text or survey logic. In JavaScript, you can use a default value or perform a null check to handle cases where the embedded data field may be undefined.

4. Encoding and Special Characters: If the value of an embedded data field contains special characters or HTML entities, they will be displayed as-is in piped text. If you need to display the actual value, you may need to use JavaScript to decode or escape the value before using it.

5. Embedded data fields in Qualtrics are always stored and retrieved as strings. When using them in JavaScript, convert numeric values using Number() or + and compare them as strings to ensure accurate results.



### Embedded Data Fields

InstanceID
- **Description**: A unique identifier for each survey response or entry.
- **Type**: Auto-generated alphanumeric string.
- **Values**: A randomly selected variable of the desired length, generated by the `generateRandomString` function.

#### Instance Code

The `generateRandomString` function is designed to dynamically generate a unique `InstanceID` for each call. Below is the JavaScript code utilized for this purpose located within the header:

```javascript
function generateRandomString(length) {
    var chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var result = '';
    for (var i = length; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];
    return result;
}
```

// Example to generate a 10-character random string:
var instanceID = generateRandomString(10);

// Store the generated ID in an embedded data field. This must occur after the Embedded Data field is created in Qualtrics.
Qualtrics.SurveyEngine.setEmbeddedData('Instance', instanceID);

The generaterandomString function is added to the first question within the "Welcome - Survey Configuration - Embedded Data" block to ensure the InstanceID is stored as soon as the respondent starts the survey.

```javascript
Qualtrics.SurveyEngine.addOnload(function()
{
	/*Place your JavaScript here to run when the page loads*/

	var instanceID = generateRandomString(10);
	Qualtrics.SurveyEngine.setEmbeddedData('Instance', instanceID);
	//Troubleshoot javascript variable
   //console.log("onLoad - javascript variable instanceID:",instanceID);
	
	//Troubleshooting to determine EmbeddedData is set  
   //var embeddedInstance = Qualtrics.SurveyEngine.getEmbeddedData('Instance');
	//console.log("onLoad InstanceField:", embeddedInstance);
	
});
```

ResponseID
   - **Description**: A system-generated reserved embeded data field identifier that Qualtrics assigns to each survey response. This ID ensures the uniqueness of every response and aids in data management, especially when analyzing or exporting data.
   - **Type**: Auto-generated number.
   - **Values**: Sequential integers.
   - **Note**: Field is labeled "Q_R"

CaregiverID
   - **Description**: Identifier specific to each caregiver.
   - **Type**: Embedded alphanumeric.
   - **Values**: Specific codes pre-assigned to each caregiver.

Respondent
   - **Description**: Specifies the role of the respondent in the trial.
   - **Type**: Embedded text.
   - **Possible Values**: 0_CARE, 1_CONF.

StudyPhase
   - **Description**: Phase of the study during which the trial took place.
   - **Type**: Embedded text.
   - **Possible Values**: 0_BL, 1_T1, 2_T2, 3_T3, 4_T4, 5_RTB.

SessionType
 - **Description**: Distinguishes between actual child or simulated sessions 
   -**Type**:Embedded text.
   -**Possible Values**: 0_AC, 1_SC

SessionData
   - **Description**: Various metrics to track the progress of each session.
   - **Sub-variables**:
      - **SessionCount**: Progressive count of sessions. Part of the embeded data from the link.
      - **SessionTimestamp**: Duration from the start of the guide.
      - **ActualTimestamp**: System time when the action was submitted. Retrieves the current UTC timestamp using the WorldTimeAPI. Webservice within survey flow.
      - **SessionBlockCount**: Progressive count of trial blocks within a session. Increments by .5 every trial as trialblocks are made of two trials.
      - **TotalSessionTrials**: Total count of trials within a session.

LoopManagement
   - **Description**: Variables and fields used to manage and control the looping behavior within the survey.
   - **Sub-variables**:
      - **LoopSwitch**: A Survey Flow Initialized Embedded Field set to 1, used to control the loop execution.
      - **LoopSetCount**: A Survey Flow Initialized Embedded Field, used to define the maximum number of loops.
         - Usage: A hidden question is held within the Welcome and Survey configuration-embedded Data with a text response set to `${e://Field/LoopSetCount}`.
      - **BreakSwitch**: Survey Flow Embedded Field set to `"0"`. This is switched to `"1"` when both check boxes are selected on the Wait Question Page (question: CARE-BL-SC-TB-BreakA)

SessionDirectionsTemplate
   - **Description**: Stores the complete list of directions for a specific caregiver and study phase.
   - **Type**: Embedded JSON string.
   - **Initial Value**: '0' (indicates empty template).
   - **Updated Value**: JSON string representation of the array of directions.

SessionDirectionPool
   - **Description**: Stores the remaining directions available for selection during a session.
   - **Type**: Embedded JSON string.
   - **Initial Value**: Empty JSON string.
   - **Updated Value**: JSON string representation of the array of remaining directions.
     
DirectionResponseData
   - **Description**: Details about the caregiver's direction and the confederate's response.
   - **Sub-variables**:
      - **TrialDirection**: Randomly selected from CaregiverDirectionPool based upon phase, including the phase code prefix. 'BL0_Have your child sit at the table', 'TR1_Have your child touch their nose'.
      - **CaregiverTrialDirection**: String text of prompted direction given to the caregiver. 'Have your child sit at the table', 'Have your child touch their nose'.
      - **CareDirStart**: The timestamp of when the direction stimuli is presented to the caregiver
      - **CareDirEnd**: The timestamp of when the caregiver reported coompleting the trial.
      - **ConfederateResponse**: One of two responses provided to the caregiver based on the study design. Sequence randomly generated by survey. (0_Comply, 1_NoComply).

SelfMonitoringObservations
- **Description**: Caregiver's self-monitoring responses. Dichotomous responses (0_No, 1_Yes) to specific self-monitoring questions. Reset to "" following each trial.
      - **SelfMonitoring1**: I moved close enough to touch the Researcher.
      - **SelfMonitoring2**: I said my child's name.
      - **SelfMonitoring3**: I stated the direction assertively.
      - **SelfMonitoring4**: I stated the direction clearly and concisely.
      - **SelfMonitoring5**: I stated the direction in a neutral tone.
      - **SelfMonitoring6**: The researcher completed the direction in a timely manner without additional support.
      - **SelfMonitoring6a_1**: If Yes (to SelfMonitoring6): I provided task-specific verbal feedback.
      - **SelfMonitoring6a_2**: If Yes (to SelfMonitoring6): I immediately gave verbal feedback.
      - **SelfMonitoring6a_3**: If Yes (to SelfMonitoring6): I immediately gave the reward.
      - **SelfMonitoring6b_1**: *DEPRECIATED* If No (to SelfMonitoring6): I withheld verbal feedback.
      - **SelfMonitoring6b_2**: *DEPRECITATED* If No (to SelfMonitoring6): I withheld the reward.
      
ConfEdcObservations
   
   - **Description**: Confederate's monitoring responses of EDC items. Dichotomous responses (0_No, 1_Yes) to specific monitoring questions. Reset to "" following each trial.
      - **ConfMonitoring1**: Caregiver moved close enough to touch the Researcher.
      - **ConfMonitoring2**: Caregiver said child's name.
      - **ConfMonitoring3**: Caregiver stated the direction assertively.
      - **ConfMonitoring4**: Caregiver stated the direction clearly and concisely.
      - **ConfMonitoring5**: Caregiver stated the direction in a neutral tone.
      - **ConfMonitoring6**: The subject completed the direction in a timely manner without additional support.
      - **ConfMonitoring6a_1**: If Yes (to ConfMonitoring6): Caregiver provided task-specific verbal feedback or witheld.
      - **ConfMonitoring6a_2**: If Yes (to ConfMonitoring6): Caregiver immediately gave verbal feedback or witheld.
      - **ConfMonitoring6a_3**: If Yes (to ConfMonitoring6): Caregiver immediately gave reward or witheld.
      - **ConfMonitoring6b_1**: *DEPRECIATED* If No (to ConfMonitoring6): Caregiver withheld verbal feedback.
      - **ConfMonitoring6b_2**: *DEPRECIATED* If No (to ConfMonitoring6): Caregiver withheld reward.

      Additional confederate observations
      
      - **ConfChildResponse**: Confederate Classification of child behavior during actual child trial blocks (0_Compliance, 1_ProblemsOfOmission, 2_ProblemsOfCommission).
      - **ConfInteraction**:  Alphanumerical confederate text input by confederate when a prompt is provided within trial. Reset to "" following each trial. if ConfederateInteraction = not "" then            Interaction = True. SumInteractions(Countif ConfederateInteraction = not "")
      - **ConfTrialNote**: Alphanumerical confederate text input by confederate to make a note on the current trial before moveing on.
      - **ConfSessionNote**: Alphanumerical confederate text input by confederate at the conclusion of the session. 

DataLogging

- **Description**: Variables and fields used to manage and control the event data logging process within the survey.
- **Sub-variables**:
    - **AggregatedData**: JSON-structured fields used in conjunction with the `recordEventData` function to export all survey events. Multiple AggregatedData fields (e.g., AggregatedData1, AggregatedData2, etc.) are used to store event data in a distributed manner, with each field containing up to 10 event records. See section "Record Event Data Function in Qualtrics Survey" for more information.
    - **RecorderCounter**: A Survey Flow Initialized Embedded Field used to keep track of the number of `recordEventData` calls within each AggregatedData field. It is incremented with each event recording and resets to 1 when it reaches 10, indicating a move to the next AggregatedData field.
    - **RecorderIndex**: A Survey Flow Initialized Embedded Field used to determine which AggregatedData field the event data should be stored in. It is incremented whenever the `RecorderCounter` reaches 10, signifying a shift to the next AggregatedData field in the sequence.



## Survey Flow Logic and Block Naming Convention

In the study's Qualtrics survey, a specific flow logic has been implemented to ensure that respondents (either caregivers or confederates) are directed to the appropriate survey blocks. These blocks vary based on their role in the study, the session type (Actual Child or Simulated Child), and the study phase (such as Baseline, Training, etc.). This section outlines the survey flow logic and the block naming convention used to facilitate this process.

### Block Naming Convention

The block names in the survey are constructed using a combination of abbreviations representing the respondent type, study phase, and session type. These abbreviations correspond with the Embedded Variables.

- **Respondent Type**:
   - `0_CARE`: Caregiver
   - `1_CONF`: Confederate

- **Study Phase**:
   - `0_BL`: Baseline
   - `1_T1`: Training Phase 1
   - `2_T2`: Training Phase 2
   - `3_T3`: Training Phase 3
   - `4_T4`: Training Phase 4
   - `5_RTB`: Reversal To Baseline

- **Session Type**:
   - `AC`: Actual Child Session
   - `SC`: Simulated Child Session

- **Trial Block**
   -`TB`: Trial Block

Naming Examples:

1. **Caregiver during the Baseline phase for an Actual Child session**:
   - `CARE-BL-AC`

2. **Confederate during Training phase 1 for a Simulated Child session**:
   - `CONF-T1-SC`

3. **Caregiver during ReversalToBaseline phase for a Simulated Child session**:
   - `CARE-BL-SC`
... and so on for each combination.

BlockNames:

CARE-BL-SC
CARE-T1-SC
CARE-T2-SC
CARE-T3-SC
CARE-T4-SC
CARE-TX-AC
CARE-BL-AC

CONF-TX-SC
CONF-T1-SC
CONF-T2-SC
CONF-T3-SC
CONF-T4-SC
CONF-TR-AC
CONF-BL-AC

### Logic for Directing Respondents

Caregiver Logic:

First Level (Respondent Type):
	If the respondent is a caregiver (0_CARE), proceed to the second level.

Second Level (Session Type):
	If the session type is Actual Child (0_AC), proceed to the third level for Actual Child sessions.
	If the session type is Simulated Child (1_SC), proceed to the third level for Simulated Child sessions.

Third Level for Actual Child Sessions (0_AC):
	If the study phase contains 'B' (indicating Baseline), display the CARE-BL-AC block.
	If the study phase does not contain 'B' (indicating one of the Training phases), display the CARE-TX-AC block.
	
Third Level for Simulated Child Sessions (1_SC): Direct to the corresponding CARE-XX-SC block, where XX represents the specific study phase (BL, T1, T2, T3, T4, RTB).
	For Baseline (0_BL), display CARE-BL-SC.
	For Training 1 (1_T1), display CARE-T1-SC.
	For Training 2 (2_T2), display CARE-T2-SC.
	For Training 3 (3_T3), display CARE-T3-SC.
	For Reversal To Baseline (5_RTB), display CARE-RTB-SC.
	
Confederate Logic:

First Level (Respondent Type):

	If the respondent is a confederate (1_CONF), proceed to the second level.

Second Level (Session Type):
	If the session type is Actual Child (0_AC), proceed to the third level for Actual Child sessions.
	If the session type is Simulated Child (1_SC), proceed to the third level for Simulated Child sessions.

Third Level for Actual Child Sessions (0_AC):
	If the study phase contains 'B' (indicating Baseline), display the CONF-BL-AC block.
	If the study phase does not contain 'B' (indicating one of the Training phases), display the CONF-TX-AC block.

Third Level for Simulated Child Sessions (1_SC): Direct to the corresponding CONF-XX-SC block, where XX represents the specific study phase (BL, T1, T2, T3, T4, RTB).
	For Baseline (0_BL), display CONF-BL-SC.
	For Training 1 (1_T1), display CONF-T1-SC.
	For Training 2 (2_T2), display CONF-T2-SC.
	For Training 3 (3_T3), display CONF-T3-SC.
	For Reversal To Baseline (5_RTB), display CONF-RTB-SC.

### Trial Looping Logic

#### Overview
The Trial Looping logic is a critical component of the survey design, enabling the execution of multiple trials within a single survey session. It allows for the controlled presentation of trial prompts, data collection, and loop termination based on specific conditions.

#### Key Components
1. **LoopSwitch**:
   - A Survey Flow Initialized Embedded Field, set to `1` to signify active loop execution.

2. **LoopSetCount**:
   - A Survey Flow Initialized Embedded Field, set to `100`, defining the maximum loop iterations. Future use could set it to the required number of trials.
   - Referenced in the 'Welcome and Survey Configuration - Embedded Data' Block with a text entry question (`LoopSetCount-Quest`) set to ${e://Field/LoopSetCount} using the Qualtrics default choices question behavior.
    - A separate timing question, on the same page as  `LoopSetCount-Quest` is used to auto-advance after 0.01 seconds.
    - Javascript is also added to the to the question  `LoopSetCount-Quest` to hide the contents of the question.
        - Question Javascript: 
        ```javascript 
            Qualtrics.SurveyEngine.addOnload(function()
            {
            // Hide the question text
             jQuery('.QuestionText').css('display', 'none');

            // Hide the input box
            jQuery('.InputText').css('visibility', 'hidden');
            });

            Qualtrics.SurveyEngine.addOnReady(function()
            {
                // Hide the "Next" button
                jQuery("#NextButton").css("visibility","hidden");
            });

   - The value of 100 is chosen to provide an excessive number of iterations, ensuring that the loop continues until the user manually breaks it using Question 2 (e.g., CARE-BL-SC-TB-LoopBr).
   - Setting LoopSetCount to a high value allows for flexibility in the number of trials completed by the user, as the loop will continue until either the maximum iterations are reached or the user chooses to exit using Question 2.

3. **BreakSwitch**
   - A Survey Flow Initialized Embedded Field, set to `0`. Utilized for participant to break the loop.

4. **Intro Block**:
   - The starting block for each participant type and session (e.g., CARE-BL-SC), determined by Survey Link Initialized Embedded Fields (caregiverID, etc.).

5. **Loop and Merge Block**:
   - Responsible for trial execution (e.g., `CARE-BL-SC-TB`), set to iterate based on `LoopSetCount` with a defined number of loops. It includes:

     - **Question 1** (e.g., `CARE-BL-SC-TB-Wait1`): Instructs users to wait and advance post agreement between caregiver and confederate. The `selectDirection()` function is called using the `Qualtrics.SurveyEngine.addOnReady` function to randomly select a direction for the trial.
       - Display Logic: If LoopSwitch Is Equal to 1

     - **Question 2** (e.g., `CARE-BL-SC-TB-BreakA`): Uses JavaScript to evaluate if both checkboxes are selected; if true, `BreakSwitch` is set to 1, and `LoopSwitch` is set to 0.
       - Display Logic: If LoopSwitch Is Equal to 1
       - Question JavaScript:
         ```javascript
         Qualtrics.SurveyEngine.addOnUnload(function()
         {
             var selectedChoices = this.getSelectedChoices();
             if (selectedChoices.length === 2) {
                 Qualtrics.SurveyEngine.setEmbeddedData("BreakSwitch", 1);
                 Qualtrics.SurveyEngine.setEmbeddedData("LoopSwitch", 0);
             }
         });
         ```

     - **Question 3** (e.g., `CARE-BL-SC-TB-HideA1`): Hidden question to allow variables to set onunload for CARE-BL-SC-TB-BreakA.
       - Display Logic: If LoopSwitch Is Equal to 1
       - Question JavaScript: Matches `LoopSetCount-Quest` to hide question. 
         
     - **Question 4** (e.g., `CARE-BL-SC-TB-HideA2`): Timing question to auto advance. Not displayed to the participant.
       - Display Logic: If LoopSwitch Is Equal to 1

     - **Question 5** (e.g., `CARE-BL-SC-TB-BreakB`): User input to verify the Break. Selecting "No" sets `LoopSwitch` to 1 and `BreakSwitch` to 1, re-presenting Instruction to caregiver to wait and advance post agreement between caregiver and confederate. without re-running `selectDirection()`. Selecting "Yes" sets `LoopSwitch` to 0 and `BreakSwitch` to 0, effectively ending the survey.
       - Display Logic: BreakSwitch Is Equal to 1 And LoopSwitch Is Equal to 0
       - Question JavaScript:
         ```javascript
         Qualtrics.SurveyEngine.addOnUnload(function()
         {
             var selectedChoicesarray = this.getSelectedChoices('QID37');
             var selectedChoicesnumber = selectedChoicesarray[0];
             if (selectedChoicesnumber === "4") {
                 Qualtrics.SurveyEngine.setEmbeddedData("LoopSwitch", "1");
                 Qualtrics.SurveyEngine.setEmbeddedData("BreakSwitch", "1");
             } else {
                 Qualtrics.SurveyEngine.setEmbeddedData("LoopSwitch", "0");
                 Qualtrics.SurveyEngine.setEmbeddedData("BreakSwitch", "0");
             }
         });
         ```

     - **Question 6** (e.g., `CARE-BL-SC-TB-HideB1`): Hidden question to allow variables to set onunload for CARE-BL-SC-TB-BreakB.
       - Display Logic: If LoopSwitch Is Equal to 0 And BreakSwitch Is Equal to 1
       - Question JavaScript: Matches `LoopSetCount-Quest` to hide question. 

     - **Question 7** (e.g., `CARE-BL-SC-TB-HideB2`): Timing question to auto advance. Not displayed to the participant.
       - Display Logic: If LoopSwitch Is Equal to 0 And BreakSwitch Is Equal to 1

     - **Question 8** (e.g., `CARE-BL-SC-TB-Wait2`): Instructs users to wait and advance post agreement between caregiver and confederate.
       - Display Logic: If BreakSwitch Is Equal to 1 And LoopSwitch Is Equal to 1

     - **Question 9** (e.g., `CARE-BL-SC-TB-T`): Displays the 'TrialDirection' text prompt to the user.
       - Display Logic: If LoopSwitch Is Equal to 1
       - This holds the CareDirStart and CareDirStop function call

    - **Further Questions**: The confederate guide has observational questions throughout all conditions. The caregiver guide has self-monitoring questions during the simulated training phases.

5. **JavaScript Functions**:
   - **selectDirection**: Randomly assigns 'TrialDirection' from `CaregiverDirectionPool` without replacement. Called using the `Qualtrics.SurveyEngine.addOnReady` function in the "CARE-BL-SC-TB-Wait1" question.
   - **Header Script**: Updates 'AggregatedData' whenever a new page within the loop is loaded, notably after displaying Question 1 and advancing from Question 9 or monitoring questions. See 'AggregatedData' under variables for more information.

  

### Setting Caregiver Direction Timestamps

The survey captures two timestamps related to the caregiver's direction:
- `CareDirStart`: Represents the timestamp when the direction stimulus is presented to the caregiver.
- `CareDirEnd`: Represents the timestamp when the caregiver reports completing the trial.

#### Implementation
Two JavaScript functions, `setCareDirStart()` and `setCareDirEnd()`, are defined in the survey's header script to set the respective timestamps:

```javascript
function setCareDirStart() {
    var careDirStart = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('CareDirStart', careDirStart);
}

function setCareDirEnd() {
    var careDirEnd = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('CareDirEnd', careDirEnd);
}
```

These functions utilize the `getCurrentDateTime()` function to retrieve the current timestamp and store it in the corresponding embedded data field using `Qualtrics.SurveyEngine.setEmbeddedData()`.

#### Usage
To set the `CareDirStart` timestamp, the `setCareDirStart()` function is called when the direction stimulus is presented to the caregiver. This can be achieved by adding the following code to the question's JavaScript:

```javascript
Qualtrics.SurveyEngine.addOnload(function() {
    setCareDirStart();
});
```

To set the `CareDirEnd` timestamp, the `setCareDirEnd()` function is called when the caregiver reports completing the trial. This can be done by adding the following code to the question's JavaScript:

```javascript
Qualtrics.SurveyEngine.addOnUnload(function() {
    setCareDirEnd();
});
```

#### Integration
The `CareDirStart` and `CareDirEnd` timestamps are captured and stored in the respective embedded data fields. These fields are  included in the `eventData` object within the `recordEventData` function for tracking and analysis purposes.



#### Flow Description
1. The survey begins with the Intro Block (e.g., CARE-BL-SC), which is determined by the Survey Link Initialized Embedded Fields (Respondent, etc.). The LoopSetCount question, not displayed to users, is within the Intro block and establishes the LoopSetCount for the Loop and Merge Block to configure.

2. After the Intro Block, the survey proceeds to the Loop and Merge Block (e.g., CARE-BL-SC-TB).

3. Within the Loop and Merge Block:
   - **Question 1** (e.g., CARE-BL-SC-TB-Wait1) prompts the user to wait and advance until agreement between caregiver and confederate. The `selectDirection()` function is called to randomly select a direction for the trial.
   - **Question 2** (e.g., CARE-BL-SC-TB-BreakA) allows the user to break the loop by selecting both checkboxes. When both checkboxes are selected, the `BreakSwitch` is set to 1, and `LoopSwitch` is set to 0.
   - **Question 3** (e.g., 040) is a hidden question that allows variables to set onunload for CARE-BL-SC-TB-BreakA.
   - **Question 4** (e.g., Q41) is a timing question to record and manage how long a participant spends on the page. It is not displayed to the participant.
   - **Question 5** (e.g., CARE-BL-SC-TB-BreakB) is a user input question to verify the Break. Selecting "No" sets `LoopSwitch` to 1 and `BreakSwitch` to 1, re-presenting Question 1 without re-running `selectDirection()`. Selecting "Yes" sets `LoopSwitch` to 0 and `BreakSwitch` to 0, effectively ending the survey.
   - **Question 6** (e.g., Q42) is a hidden question that allows variables to set onunload for CARE-BL-SC-TB-BreakB.
   - **Question 7** (e.g., Q43) is a timing question to record and manage how long a participant spends on the page. It is not displayed to the participant.
   - **Question 8** (e.g., CARE-BL-SC-TB-Wait2) prompts the user to wait and advance until agreement between caregiver and confederate.
   - **Question 9** (e.g., CARE-BL-SC-TB-T) provides the textual prompt ('TrialDirection') to the user.
   - Additional questions for self-monitoring during training phases and confederate monitoring questions during all phases.

4. Display logic for questions within the Loop and Merge Block checks `LoopSwitch` and `BreakSwitch` values to determine which questions are displayed and when the loop should be terminated.

5. The JavaScript function `selectDirection` sets 'TrialDirection' to a randomized text value from `CaregiverDirectionPool` without replacement.

6. The Header Script appends data to 'AggregatedData' every time a new page is loaded within the loop, which occurs when Question 1 is loaded and when advancing from Question 9 or monitoring questions.

7. The loop continues until either the maximum number of loops (defined by LoopSetCount) is reached or the user chooses to exit using Question 2 and confirms the exit in Question 5.

#### Considerations
- It's important to note that the first time Question 1 is displayed, there may be null variables set by subsequent questions/scripts.
- The looping behavior depends on the values of `LoopSwitch` and `BreakSwitch`, which are determined by the user's responses to Question 2 and Question 5.
- Variables set during Qualtrics.SurveyEngine.addOnUnload(function()) will need a buffer to set properly. A question in-between is utilized.

### Incrementing Trial Count Variables


The survey utilizes two variables to track the progress of trials and trial blocks within a session:
- `TotalSessionTrials`: Represents the total count of trials completed within the session.
- `SessionBlockCount`: Indicates the progression of trial blocks within the session.

#### Implementation
A JavaScript function, `incrementSessionVariables()`, is defined in the survey's header script to increment the session variables:

```javascript
function incrementSessionVariables() {
    var totalSessionTrials = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('TotalSessionTrials'));
    totalSessionTrials++;
    Qualtrics.SurveyEngine.setEmbeddedData('TotalSessionTrials', totalSessionTrials);

    var sessionBlockCount = parseFloat(Qualtrics.SurveyEngine.getEmbeddedData('SessionBlockCount'));
    sessionBlockCount += 0.5;
    Qualtrics.SurveyEngine.setEmbeddedData('SessionBlockCount', sessionBlockCount);
}
```

This function retrieves the current values of `TotalSessionTrials` and `SessionBlockCount` from the embedded data, increments them accordingly, and updates the embedded data fields using `Qualtrics.SurveyEngine.setEmbeddedData()`.

#### Usage
To increment the session variables, the `incrementSessionVariables()` function is called at the point where a trial is considered complete. This can be done by adding the following code to the question's JavaScript:

```javascript
Qualtrics.SurveyEngine.addOnUnload(function() {
    incrementSessionVariables();
});
```

By placing this function call in the question-specific JavaScript, you can control when the session variables are incremented based on the specific survey flow and question logic.



#### Functionality
- `TotalSessionTrials` is incremented by 1 after each trial, keeping track of the total count of trials completed within the session.
- `SessionBlockCount` is incremented by 0.5 after each trial, indicating the progression of trial blocks within the session.
  - Whole numbers (e.g., 1, 2, 3) represent the completion of a trial block.
  - Fractional numbers (e.g., 0.5, 1.5, 2.5) represent the completion of a single trial within a block.

#### Integration
The `incrementSessionVariables()` function is called at the appropriate location in the survey flow or question logic where a trial is considered complete. The updated values of `TotalSessionTrials` and `SessionBlockCount` are then captured in the `eventData` object within the `recordEventData` function for tracking and analysis purposes.

The function is currently called from the following questions:

    - CARE-BL-SC-TB-T
    - CARE-AC-TB-T
    - CARE-T1-SC-TB-T
    - CARE-T2-SC-TB-T
    - CONF-TX-SC-TB-T



### Testing Survey Logic and Managing Browser Sessions

During the development and testing phase of our Qualtrics survey, an issue was encountered related to how the survey handles sessions and respondent tracking. This issue is particularly relevant for surveys employing complex logic and embedded data.

- Survey Resumption Behavior

Qualtrics has a feature that saves a respondent's progress, allowing them to continue where they left off. While beneficial for longer surveys, this can present challenges during testing when different conditions need to be assessed from the start.

ResponseID and Browser Caching:

Each survey attempt is typically associated with a unique ResponseID, stored in the browser's cache. Re-entering the survey from the same browser could be recognized as a continuation of a previous attempt, leading to inconsistent testing results.

Recommended Solutions:

-Testing-
Clearing Browser Cache: To start a new survey session without previous data, clear your browser's cache.
Incognito/Private Browsing Mode: Use an incognito or private window for each test attempt. These sessions do not share cookies or cache with others, ensuring a fresh start each time.
Preview Mode: use the qualtrics preview mode refresh the browser.

Production: Ensure a new browser session is initated whenever opening a new link.
Production Update: right click on reload button within chrome, then select "clear cache and hard reset"


## Function Descriptions

### Current Date and Time Function in Qualtrics Survey

The "Current Date and Time Function" is a custom JavaScript function designed to retrieve the current date and time in a specific format within a Qualtrics survey. This function enables accurate timestamping of survey responses and events, which is crucial for data analysis and tracking.

#### Function Overview

- **Function Name**: `getCurrentDateTime`
- **Purpose**: To retrieve the current date and time in the format "YYYY-MM-DDTHH:mm:ss±HH:mm", where:
  - YYYY represents the year
  - MM represents the month (01-12)
  - DD represents the day of the month (01-31)
  - HH represents the hours (00-23)
  - mm represents the minutes (00-59)
  - ss represents the seconds (00-59)
  - ±HH:mm represents the timezone offset from UTC
- **Location in Survey**: This JavaScript function can be placed in the survey's header script or within a specific question's JavaScript editor, depending on the desired scope and usage.

#### How It Works

1. The function creates a new `Date` object representing the current date and time.

2. It extracts the individual components of the date and time (year, month, day, hours, minutes, seconds) using the respective methods of the `Date` object.

3. The function calculates the timezone offset in minutes using the `getTimezoneOffset()` method, which returns the difference between UTC and the local time zone.

4. It determines the sign of the timezone offset ('+' for positive offset, '-' for negative offset) and formats the offset hours and minutes as a string in the format "±HH:mm".

5. Finally, the function constructs the formatted date and time string by combining the extracted components and the timezone offset using template literals.

6. The resulting string is returned in the format "YYYY-MM-DDTHH:mm:ss±HH:mm".

#### Usage

To use the `getCurrentDateTime` function in your Qualtrics survey, follow these steps:

1. Copy the function code and paste it into the JavaScript editor of the desired question or the survey's header script.

2. Call the function whenever to retrieve the current date and time. For example:

```javascript
const currentDateTime = getCurrentDateTime();
console.log(currentDateTime);
```

3. The function will return the current date and time in the specified format, which can be used for timestamping, data analysis, or any other desired purpose. 

#### Customization

If you require a different format for the date and time or need to modify the behavior of the function, you can adjust the code accordingly. The function can be easily customized to include additional components, change the formatting, or adapt to specific timezone requirements.

By incorporating the `getCurrentDateTime` function into your Qualtrics survey, you can accurately capture and record the current date and time, enabling precise timestamping and facilitating data analysis based on temporal information.



## Data Management

This section outlines a method for capturing detailed user experience data within Qualtrics surveys using custom JavaScript for data aggregation and a post-collection transformation process to structure the data in a row-wise format. The main objectives of this approach are:

1. Address the limitation of Qualtrics, which only records data points at the completion of the survey.
2. Enable more granular and frequent data capture to sufficiently record events.
3. Facilitate data analysis by structuring the data in a row-wise format.

The loop and merge function was initially evaluated as a potential solution but was found to be inadequate due to insufficient recording fields and frequency. After further evaluation, the selected approach involves utilizing a JSON-formatted variable, defined as an embedded variable, which is updated with each event. This method allows for capturing detailed user experience data throughout the survey.

### Record Event Data Function in Qualtrics Survey

The "Record Event Data Function" is designed to systematically collect and log a comprehensive array of survey variables at every significant event within the Qualtrics environment. This function aims to generate a "master" dataset capturing intricate details of each session, trial, and participant interaction.

#### Function Overview

- **Function Name**: `recordEventData`
- **Purpose**: To systematically capture a wide range of variables at designated events within the survey to construct a detailed master dataset.
- **Location in Survey**: This JavaScript function is incorporated into the survey's header script, ensuring universal execution at every load of a page and any additional predetermined survey events.

#### Embedded Data Field Limitations

When using embedded data fields to store event data in Qualtrics, it's important to be aware of the following limitations:

1. Character Limit: Embedded data field titles have a maximum character limit of 500 characters. 

2. Value Size Limit: Each value of an embedded data field should never exceed 20KB (20,000 bytes). The number of bytes per character varies depending on the character set and encoding used. English characters typically use 1 byte per character, while languages like Chinese or Hebrew can use multiple bytes per character.


To mitigate these limitations, the "Record Event Data Function" employs a rotation logic that distributes event data across multiple AggregatedData fields, ensuring that each field contains a maximum of 10 event records before moving to the next field.

#### How It Works

1. **Qualtrics Preparation**:
   - Multiple embedded data fields named `AggregatedData1`, `AggregatedData2`, etc., are included in the initializing block within the survey flow. These fields will store the aggregated event data in JSON format, with each field containing up to 10 event records.

2. **Variable Collection and Rotation Logic**:
   - The `recordEventData` function aggregates values from a variety of sources, including embedded data fields and JavaScript variables, that represent key survey elements (e.g., `InstanceID`, `ResponseID`, `CaregiverID`, etc.).
   - A `RecordCounter` variable keeps track of the number of `recordEventData` calls, and an `RecordIndex` variable determines which AggregatedData field the event data should be stored in.
   - When the `counter` reaches 10, it is reset to 1, and the `Index` is incremented to move to the next AggregatedData field.

3. **Event Triggering**:
   - Predetermined survey events (such as opening the guide, completing a task, entering an observation, or initiating a new trial) trigger the `recordEventData` function. This ensures that data is captured at critical moments, reflecting the survey's dynamic progression.

4. **Data Logging**:
   - Upon activation, `recordEventData` logs the collected variables into a structured JSON format and appends the event data to the appropriate AggregatedData field based on the current `RecorderIndex`.
   - The function retrieves any existing data from the current AggregatedData field, parses it from JSON (if available), and appends the current event data to the existing data array.
   - The updated aggregated data is then stringified and stored back into the corresponding AggregatedData field.

5. **Implementation Details**:
   - Custom JavaScript is utilized to define the `recordEventData` function's logic, including data collection, rotation logic, and data logging mechanisms.
   - The function is designed to be compatible with Qualtrics' platform and optimized for performance to avoid disrupting the respondent's experience.

#### Sample JavaScript Implementation

```javascript
function recordEventData() {
    // Get the current RecorderCounter and RecorderIndex from embedded data
    var counter = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('RecorderCounter'));
    var index = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('RecorderIndex'));

    // Increment counter
    counter++;

    // If counter reaches 10, reset it and increment index
    if (counter > 10) {
        counter = 1;
        index++;
    }

    // Update the RecorderCounter and RecorderIndex in embedded data
    Qualtrics.SurveyEngine.setEmbeddedData('RecorderCounter', counter);
    Qualtrics.SurveyEngine.setEmbeddedData('RecorderIndex', index);

    // Collect embedded data and dynamic variables
    var eventData = {
        'InstanceID': Qualtrics.SurveyEngine.getEmbeddedData('InstanceID'),
        'ResponseID': Qualtrics.SurveyEngine.getEmbeddedData('ResponseID'),
        'CaregiverID': Qualtrics.SurveyEngine.getEmbeddedData('CaregiverID'),
        // Add other variables following the same pattern
    };

    // Log or transmit the eventData as required
    console.log(eventData); // Placeholder for actual logging mechanism

    // Save eventData to the appropriate AggregatedData field
    var fieldName = 'AggregatedData' + index;
    var existingData = Qualtrics.SurveyEngine.getEmbeddedData(fieldName);
    var aggregatedData = existingData ? JSON.parse(existingData) : [];
    aggregatedData.push(eventData);
    Qualtrics.SurveyEngine.setEmbeddedData(fieldName, JSON.stringify(aggregatedData));
}

// Trigger on page load
Qualtrics.SurveyEngine.addOnload(function() {
    recordEventData(); // Call function to record event data
});
```

In this implementation, the `recordEventData` function collects relevant variables from embedded data fields and JavaScript variables, and appends the event data to the appropriate AggregatedData field based on the rotation logic. The function is triggered on each page load using the `Qualtrics.SurveyEngine.addOnload` event.

By distributing event data across multiple AggregatedData fields and limiting each field to a maximum of 10 event records, this approach helps mitigate the limitations of Qualtrics' embedded data fields while ensuring reliable data capture and storage within the Qualtrics environment.

#### Event Triggers

recordEventData( )

| Block           | Question        | Javascript | EventNote                       |
|-----------------|-----------------|------------|---------------------------------|
| Welcome         | Welcome         | OnLoad     | "0_SurveyStart"                 |
| CARE-BL-SC      | EDC             | Onload     | "1.0_BL_EDC-Start"              |
| CARE-BL-SC      | EDC             | OnUnload   | "1.1_BL_EDC-End"                |
| CARE-BL-SC-TB   | CARE-BL-SC-TB-T | Onload     | "2.0_Care_BL_Direction-Start"   |
| CARE-BL-SC-TB   | BL-EventData    | OnUnload   | "3.0_Care_BL__SC_TrialComplete" |
| CARE-T1-SC-TB   | T1-EventData    | OnUnload   | "3.0_Care_T1_SC_TrialComplete"  | 
| CARE-T2-SC-TB   | T2-EventData    | OnUnload   | "3.0_Care_T2_SC_TrialComplete"  |


### Monitoring Question Response Data Entry

The Qualtrics Survey Engine JavaScript API enables the capturing of question responses and storing them in corresponding embedded data fields. This functionality allows for the tracking and utilization of respondents' answers for data analysis and survey logic. The JavaScript code is added to each question where capturing and storing the response in an embedded data field is required. While this requires each question to have JavaScript, it simplifies the `eventdata` function by managing the item responses to a standardized field.

##### JavaScript Code

The following JavaScript code is added to each question to capture the selected response and store it in the corresponding embedded data field:

```javascript
Qualtrics.SurveyEngine.addOnUnload(function() {
    var selectedChoices = this.getSelectedChoices();
    var recordedValue = '';

    if (selectedChoices.length > 0) {
        var selectedChoice = selectedChoices[0];

        // Map the selected choice to the desired recorded value
        if (selectedChoice === '1') {
            recordedValue = '0';  // Choice '1' maps to '0'
        } else if (selectedChoice === '2') {
            recordedValue = '1';  // Choice '2' maps to '1'
        }
    }

    Qualtrics.SurveyEngine.setEmbeddedData('EmbeddedField', recordedValue);
});
```

###### Code Explanation

- `this.getSelectedChoices()` retrieves an array of the selected choices for the current question.
- The code assumes that only one choice will be selected. If multiple choices are allowed, the logic needs to be modified accordingly.
- The selected choice is mapped to the desired recorded value using conditional statements.
- `Qualtrics.SurveyEngine.setEmbeddedData('EmbeddedField', recordedValue)` saves the recorded value to the specified embedded data field.

In order to customize for each question:
- `'EmbeddedField'` is replaced with the actual name of the embedded data field.
- The conditional statements are modified to map the selected choices to the appropriate recorded values based on the question's choice options.
- The recoding is completed so that a response of "Yes" is equal to '1' and a response of "No" is equal to '0'.

Consider:
- Embedded data fields must be properly defined in the survey flow before being used in the JavaScript code.
- Data type and format are considered when storing recorded values, and the code is adjusted if numeric or other data types are needed.

The captured question responses, stored in the predefined survey flow embedded data fields, can be utilized in the `recordEventData` function or other survey logic as required.


### Mastery and Intervention Monitoring

#### Overview

The `updateConfMonitoringArrays` function is designed to manage and update the scores of multiple `ConfMonitoring` fields across trial blocks in a Qualtrics survey. This function captures the scores of individual trials within each trial block and stores them in a structured 2D array format. The function ensures that only the last three trial blocks are kept for evaluation purposes, providing a streamlined approach to track and assess caregiver performance.

#### Function Explanation

The `updateConfMonitoringArrays` function performs the following tasks:

1. **Initialization**:
   - Defines an array of `ConfMonitoring` fields that need to be tracked.
   - Retrieves the existing scores from the embedded data field `ConfMonitoringScores`.

2. **Updating Scores**:
   - For each `ConfMonitoring` field, the function retrieves the current score for the trial.
   - The score is appended to the current trial block (the last sub-array in the 2D array).

3. **Managing Trial Blocks**:
   - When a trial block (two trials) is complete, a new empty sub-array is created to start the next trial block.
   - The function ensures that only the last three completed trial blocks (a maximum of four sub-arrays, including the current block) are retained in the array.

4. **Saving Updated Data**:
   - The updated 2D array structure is saved back into the embedded data field `ConfMonitoringScores`.

#### Array Structure

The `ConfMonitoringScores` field is a JSON-encoded dictionary where each key represents a `ConfMonitoring` field, and the value is a 2D array that holds the trial scores.

- **Key**: The name of the `ConfMonitoring` field (e.g., `ConfMonitoring1`).
- **Value**: A 2D array where each sub-array represents a trial block, and each element within the sub-array represents a trial score (0 or 1).

#### Example Structure

After several trials, the `ConfMonitoringScores` might look like this:

```json
{
  "ConfMonitoring1": [
    [1, 1],      // Trial Block 1: Two trials with scores 1 and 1
    [1, 0],      // Trial Block 2: Two trials with scores 1 and 0
    [1, 1],      // Trial Block 3: Two trials with scores 1 and 1
    [1]          // Current Trial Block: One trial with score 1 (not yet complete)
  ],
  "ConfMonitoring2": [
    [1, 1],      // Trial Block 1
    [0, 0],      // Trial Block 2
    [1, 1],      // Trial Block 3
    [1]          // Current Trial Block
  ],
  "ConfMonitoring3": [
    [0, 1],      // Trial Block 1
    [1, 1],      // Trial Block 2
    [1, 0],      // Trial Block 3
    [0]          // Current Trial Block
  ]
}
```

#### Function Code

Below is the implementation of the `updateConfMonitoringArrays` function:

```javascript
function updateConfMonitoringArrays() {
    var confMonitoringFields = [
        'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 
        'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6a_1', 
        'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
    ];
    var confMonitoringScores = JSON.parse(Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoringScores')) || {};

    confMonitoringFields.forEach(function(field) {
        if (!confMonitoringScores[field]) {
            confMonitoringScores[field] = [[]];
        }

        var score = Number(Qualtrics.SurveyEngine.getEmbeddedData(field)) === 1 ? 1 : 0;
        var currentBlock = confMonitoringScores[field].length - 1;

        confMonitoringScores[field][currentBlock].push(score);

        if (confMonitoringScores[field][currentBlock].length === 2) {
            // If current trial block is complete, start a new trial block
            confMonitoringScores[field].push([]);
        }

        // Limit to the last 3 trial blocks (6 trials)
        if (confMonitoringScores[field].length > 4) {
            confMonitoringScores[field].shift();
        }
    });

    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoringScores', JSON.stringify(confMonitoringScores));
}
```

#### Key Points

- The function ensures that only the most recent three trial blocks are kept in memory, aligning with mastery criteria requirements.
- Each `ConfMonitoring` field's scores are stored in a structured 2D array, which simplifies the process of calculating trial block scores and determining mastery.























### Documentation for `evaluateAndProvideFeedback` Function

#### Overview

The `evaluateAndProvideFeedback` function is designed to evaluate caregiver performance based on the scores stored in `ConfMonitoringScores` and provide necessary feedback or interventions. It checks if mastery is achieved, and if so, updates the embedded data fields to reflect this status.

#### Function Explanation

The `evaluateAndProvideFeedback` function performs the following tasks:

1. **Session Type Check**:
   - Exits the function if the session type is not appropriate for evaluation (e.g., "0_AC").

2. **Session Block Count Check**:
   - Ensures that at least three session blocks have been completed.
   - Exits if `sessionBlockCount` is not a whole number.

3. **Evaluate Mastery**:
   - Checks if all `ConfMonitoring` items in the last three completed trial blocks have perfect scores.
   - If mastery is achieved, updates the embedded data fields to indicate mastery and exits the survey loop.

4. **Check for Recent Errors**:
   - Evaluates the most recent trial block for any errors.
   - Provides feedback only if there are errors in the most recent trial block.

5. **Provide Feedback or Verbal Prompts**:
   - If feedback is needed, provides written feedback for up to two instances.
   - If feedback count exceeds two, provides verbal prompts.

#### Function Code

Below is the implementation of the `evaluateAndProvideFeedback` function:

**Note this code was updated due to error of mastery criteria items. See documentation below**

```javascript
// *** START Evaluate Mastery and Provide Feedback Code ***

function evaluateAndProvideFeedback() {
    // Exit function if session is not an AC
    var SessionType = Qualtrics.SurveyEngine.getEmbeddedData('SessionType');
    if (SessionType === "0_AC") {
        return;
    }

    // Exit function if sessionBlockCount is less than 3. This ensures that at least 3 trial blocks have been completed to check for mastery
    var sessionBlockCount = parseFloat(Qualtrics.SurveyEngine.getEmbeddedData('SessionBlockCount')) || 0;
    console.log("Session Block Count: ", sessionBlockCount);
    console.log("Total Session Trials: ", Qualtrics.SurveyEngine.getEmbeddedData('TotalSessionTrials'));
    if (sessionBlockCount < 3) {
        return;
    }

    // Check if sessionBlockCount is a whole number (i.e., a complete trial block)
    if (sessionBlockCount % 1 !== 0) {
        console.log("SessionBlockCount is not a whole number. Exiting function.");
        return;
    }

    var confMonitoringFields = [
        'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 
        'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6a_1', 
        'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
    ];
    var confMonitoringScores = JSON.parse(Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoringScores')) || {};

    console.log("ConfMonitoringScores: ", JSON.stringify(confMonitoringScores));

    // Mastery: Check if all confMonitoring items in the last three completed trial blocks are correct
    var allCorrect = confMonitoringFields.every(function(field) {
        var scores = confMonitoringScores[field] || [[]];
        var lastThreeBlocks = scores.slice(-4, -1); // Get the last three completed trial blocks accounting for the carrier field added by updateConfMonitoringArrays

        return lastThreeBlocks.every(function(block, index) {
            var blockScore = block.reduce((a, b) => a + b, 0);
            console.log(`Field: ${field}, Block ${index + 1} score:`, blockScore);
            return blockScore === 2;
        });
    });

    if (allCorrect) {
        console.log("Mastery achieved!");
        Qualtrics.SurveyEngine.setEmbeddedData('LoopSwitch', '0');
        Qualtrics.SurveyEngine.setEmbeddedData('BreakSwitch', '1');
        Qualtrics.SurveyEngine.setEmbeddedData('MasteryAchieved', '1');
        return;
    } else {
        if (sessionBlockCount < 6) {
            return;
        }

        var feedbackCount = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('FeedbackCount')) || 0;
        console.log("Current feedback count:", feedbackCount);

        var recentErrors = confMonitoringFields.some(function(field) {
            var scores = confMonitoringScores[field] || [[]];
            var lastBlock = scores[scores.length - 2] || [];  // Get the last completed trial block

            var blockScore = lastBlock.reduce((a, b) => a + b, 0);
            return blockScore < 2;
        });

        if (!recentErrors) {
            console.log("No recent errors, no feedback needed.");
            return;
        }

        if (feedbackCount < 2) {
            feedbackCount++;
            Qualtrics

.SurveyEngine.setEmbeddedData('FeedbackSwitch', '1');
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackCount', feedbackCount);
            console.log("Providing written feedback. Updated feedback count:", feedbackCount);
            provideWrittenFeedback(confMonitoringScores, confMonitoringFields); 
        } else {
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackSwitch', '2');
            console.log("Providing verbal prompt.");
            provideVerbalPrompt(confMonitoringScores, confMonitoringFields); 
        }
    }
}

// Function to provide written feedback
function provideWrittenFeedback(confMonitoringScores, confMonitoringFields) {
    var feedbackMessages = {
        'ConfMonitoring1': "Before saying your focus child's name, get within arm's reach.",
        'ConfMonitoring2': "Say your focus child's name.",
        'ConfMonitoring3': "State the direction assertively.",
        'ConfMonitoring4': "State the direction clearly and concisely.",
        'ConfMonitoring5': "State the direction in a neutral tone.",
        'ConfMonitoring6a_1': "Provide task-specific praise if your focus child completes the direction or withhold praise.",
        'ConfMonitoring6a_2': "Immediately provide verbal feedback to your focus child after they complete the direction or withhold feedback.",
        'ConfMonitoring6a_3': "Immediately provide a reward to your focus child after they complete the direction or withhold the reward."
    };

    var allFeedbackMessages = '<ul>';  // Start an unordered list

    confMonitoringFields.forEach(function(field) {
        var scores = confMonitoringScores[field] || [[]];
        var lastBlock = scores[scores.length - 2] || [];  // Get the last completed trial block

        var blockScore = lastBlock.reduce((a, b) => a + b, 0);
        if (blockScore < 2) {
            var feedbackMessage = feedbackMessages[field];
            console.log(`Providing feedback for ${field}: ${feedbackMessage}`);
            allFeedbackMessages += '<li>' + feedbackMessage + '</li>';  // Add each message as a list item
        } 
    });

    allFeedbackMessages += '</ul>';  // End the unordered list

    // Store the accumulated feedback messages in a single embedded data field
    Qualtrics.SurveyEngine.setEmbeddedData('AllFeedbackMessages', allFeedbackMessages);
}

// Function to provide verbal prompt
function provideVerbalPrompt(confMonitoringScores, confMonitoringFields) {
    console.log("Verbal prompt provided.");

    var verbalFeedbackMessages = {
        'ConfMonitoring1': "Arms reach.",
        'ConfMonitoring2': "Say Name.",
        'ConfMonitoring3': "Assertively.",
        'ConfMonitoring4': "Clearly and concisely.",
        'ConfMonitoring5': "Neutral tone.",
        'ConfMonitoring6a_1': "Task-specific praise or withhold praise.",
        'ConfMonitoring6a_2': "Immediately provide verbal feedback or withhold feedback.",
        'ConfMonitoring6a_3': "Immediately provide reward or withhold the reward."
    };

    var allFeedbackMessages = '<ul>';  // Start an unordered list

    confMonitoringFields.forEach(function(field) {
        var scores = confMonitoringScores[field] || [[]];
        var lastBlock = scores[scores.length - 2] || [];  // Get the last completed trial block

        var blockScore = lastBlock.reduce((a, b) => a + b, 0);
        if (blockScore < 2) {
            var feedbackMessage = verbalFeedbackMessages[field];
            console.log(`Providing feedback for ${field}: ${feedbackMessage}`);
            allFeedbackMessages += '<li>' + feedbackMessage + '</li>';  // Add each message as a list item
        } 
    });

    allFeedbackMessages += '</ul>';  // End the unordered list

    // Store the accumulated feedback messages in a single embedded data field
    Qualtrics.SurveyEngine.setEmbeddedData('AllFeedbackMessages', allFeedbackMessages);
}

// *** END Evaluate and Provide Feedback Code ***
```

#### Key Points

- The function ensures the session type and block count criteria are met before evaluating mastery.
- It checks if all relevant fields have perfect scores in the last three trial blocks to determine mastery.
- If mastery is achieved, it updates the necessary embedded data fields to reflect the status and exits the survey loop.
- If mastery is not achieved, it evaluates the most recent trial block for errors and provides feedback or verbal prompts accordingly.
- Embedded data fields are utilized within Qualtrics Survey Flow to end the Loopblock based upon conditional question display.

#### **Documentation of Mastery Criteria Update**

##### **Date:** 2024.08.07

###### **Issue Identified:**
During the training session for **Case 3**, I identified that the mastery criteria were incorrectly programmed. The same criteria were applied across all study phases, rather than tailoring them to the specific items to be monitored in each phase. I allowed the session to continue without making immediate changes but later corrected the issue for future participants.

- **Research Note:**  
  "Mastery criteria was wrong. Didn’t realize till part way through the session. Continued the session with no changes. Mastery criteria was met with all of the items. Went home and adjusted criteria for remaining participants. Will reflect change in documentation."

###### **Original Mastery Criteria Code:**
The original code applied the following monitoring items to all phases (`1_T1`, `2_T2`, `3_T3`), without distinction:

```javascript
var confMonitoringFields = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 
    'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6a_1', 
    'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
];
```

###### **Updated Mastery Criteria Code:**
The corrected code now assigns different monitoring items to each phase, based on the specific training requirements for that phase:

```javascript
//Mastery Items per phase
var studyPhase = Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase');
if (studyPhase === "1_T1") {
    var confMonitoringFields = [
        'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring6a_1', 
        'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
    ];
} else if (studyPhase === "2_T2") {
    var confMonitoringFields = [
        'ConfMonitoring3', 'ConfMonitoring4', 'ConfMonitoring5'
    ];
} else if (studyPhase === "3_T3") {
    var confMonitoringFields = [
        'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 
        'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6a_1', 
        'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
    ];
}
```

###### **Explanation of the Change:**
- **Original Code Issue:** The original code treated all study phases the same, applying all eight **ConfMonitoring** items (`ConfMonitoring1` to `ConfMonitoring6a_3`) universally, which was only appropriate for **StudyPhase 3_T3**. This resulted in incorrect mastery criteria for the earlier phases of training.
- **Updated Code Correction:**
    - **StudyPhase 1_T1** now evaluates **ConfMonitoring1**, **ConfMonitoring2**, and the **ConfMonitoring6** subitems, focusing on attention and feedback.
    - **StudyPhase 2_T2** expands to include **ConfMonitoring1**, **ConfMonitoring2**, **ConfMonitoring3**, reflecting more direction delivery.
    - **StudyPhase 3_T3** retains the full set of monitoring items, as it represents the most comprehensive evaluation stage.
- **Case 3**: The error was identified during the first training session with **Case 3**, but the criteria had been met using the original configuration. Future participants will be evaluated based on the updated, phase-specific criteria.
  
- **Observation:** This adjustment ensures that each phase is evaluated according to its specific mastery criteria.


## Defined direction pool for each caregiver

### Object: `caregiverDirectionPool`

***Location***
home.js - referenced script loaded on the header.

**Purpose:**  
The `caregiverDirectionPool` is a JavaScript object that stores a structured set of directions for caregivers. Each caregiver is identified by a unique ID, and for each caregiver, there are two sets of directions: `baseline` and `training`.

**Structure:**  
- **Key**: Caregiver's unique identifier (e.g., `"CaregiverID"`).
- **Value**: An object containing three properties: `baseline`, `training`, and `generalization`. Each of these properties is an array of string directions.

**Properties:**  
- **baseline**: An array of directions specific to the baseline phase. Each direction is prefixed with a code (e.g., `"0_BL"`) followed by the actual direction text.
- **training**: An array of directions specific to the training phase. Each direction is prefixed with a code (e.g., `"0_TR"`) followed by the actual direction text.
- **generalization**: An array of directions specific to the actual child generalization probes. Each direction is prefixed with a code (e.g., `"0_GP"`) followed by actual direction text.

**Usage:**  
The `caregiverDirectionPool` object provides a centralized location to store and manage the directions for each caregiver. By referencing a caregiver's unique ID, a script can easily retrieve the appropriate set of directions for the current phase of the study.

**Example:**  
To access the baseline directions for `"CaregiverID"`, you would use the following syntax:  
`caregiverDirectionPool["CaregiverID"].baseline`

Similarly, to access the training directions for the same caregiver:  
`caregiverDirectionPool["CaregiverID"].training`

**Extensibility:**  
To add more caregivers or modify existing directions, simply extend or modify the `caregiverDirectionPool` object structure. Each caregiver should have a unique ID and associated sets of directions for both the baseline and training phases.

```javascript
// *** START CaregiverDirectionPool Code ***

{
    "CaregiverID": {
        baseline: [
            "BL0_Have your child sit at the table",
            "BL1_Have your child pick up the toy",
            // ... additional baseline directions
        ],
        training: [
            "TR0_Have your child put their shoes on",
            "TR1_Have your child touch their nose",
            // ... additional training directions
        ]
    },
    // ... other caregivers can be added as needed
}

// *** END CaregiverDirectionPool Code ***
```

## Caregiver Direction Selection

**Purpose**:
To dynamically select and present a direction to the caregiver based on the current study phase and specific caregiver.

**Implementation**:
JavaScript is employed within Qualtrics to facilitate this logic. The `selectDirection` function is called when the survey page is fully displayed using the `Qualtrics.SurveyEngine.addOnReady` function.

The `selectDirection` function performs the following steps:

1. Retrieves the values of `SessionDirectionsTemplate`, `SessionDirectionPool`, `StudyPhase`, `CaregiverID`, and `SessionType` embedded data variables.

2. Checks if the `SessionDirectionsTemplate` is empty. If it is, the function determines the correct list of directions to pull from (either baseline, training, or actual child) based on the current study phase and session type:
   - If `SessionType` is `0_AC`, the function selects the `actualChild` directions.
   - If `SessionType` is not `0_AC`, the function selects:
     - `baseline` directions for `0_BL` or `5_RTB` study phases.
     - `training` directions for other study phases.

3. The selected list of directions is stored in the `SessionDirectionsTemplate` variable and updated in the embedded data.

4. If the `SessionDirectionsTemplate` is not empty, the function parses the `SessionDirectionsTemplate` and `SessionDirectionPool` from their JSON string representation.

5. The `getSpecificDirection` function is defined within the `selectDirection` function. It retrieves a specific direction from the `SessionDirectionsTemplate` based on a given index.

6. The `getRandomDirection` function is defined within the `selectDirection` function. It checks if the `SessionDirectionPool` is empty. If it is, the function replenishes it with the directions from the `SessionDirectionsTemplate`. It then randomly selects a direction from the `SessionDirectionPool`, removes the selected direction from the pool, and returns it.

7. The function decides which direction to select based on the study phase and session type:
   - If `studyPhase` is `0_BL` and `sessionType` is `0_AC`, the function uses the `SpecificBaselineDirectionIndex` embedded data field to select a specific direction.
   - Otherwise, the function selects a random direction.

8. The selected direction is stored in the `selectedDirection` variable.

9. The selected direction is set as the `TrialDirection` embedded data variable for tracking purposes.

10. The first four characters of the selected direction are removed, and the resulting direction text is set as the `CaregiverTrialDirection` embedded data variable for displaying to the caregiver.

11. The updated `SessionDirectionPool` is stored back into the embedded data.

**Additional Information**:
The `selectDirection` function is called using the `Qualtrics.SurveyEngine.addOnReady` function, on **Question 1** (e.g., `CARE-BL-SC-TB-Wait`) of the Loop and Merge Block.

The `SessionDirectionsTemplate` serves as a master list of directions for each caregiver and study phase, while the `SessionDirectionPool` is a working copy of the directions that gets depleted as directions are randomly selected. When the `SessionDirectionPool` becomes empty, it is replenished with the directions from the `SessionDirectionsTemplate`.

The `getSpecificDirection` function is responsible for retrieving a specific direction from the `SessionDirectionsTemplate` based on a given index. This is used during the baseline actual child phase to ensure specific directions are presented.

The `getRandomDirection` function is responsible for randomly selecting a direction from the `SessionDirectionPool`, removing the selected direction from the pool, and returning it. This ensures that each direction is presented only once until all the directions in the pool have been exhausted.

The selected direction is stored in the `TrialDirection` embedded data variable for tracking purposes and also cleaned up by removing the first four characters before being stored in the `CaregiverTrialDirection` embedded data variable for displaying to the caregiver.

### Updated `selectDirection` Function

```javascript
function selectDirection() {
    
    var SessionDirectionsTemplate = Qualtrics.SurveyEngine.getEmbeddedData('SessionDirectionsTemplate');
    var SessionDirectionPool = Qualtrics.SurveyEngine.getEmbeddedData('SessionDirectionPool');
    
    var selectedDirection;

    // Check if template is empty. Get the list of directions for the specified caregiver and phase. Place it in the template.
    if (SessionDirectionsTemplate === "0") {
        // Retrieve the values of the StudyPhase, CaregiverID, and SessionType embedded variables
        var studyPhase = Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase');
        var caregiverID = Qualtrics.SurveyEngine.getEmbeddedData('CaregiverID');
        var sessionType = Qualtrics.SurveyEngine.getEmbeddedData('SessionType');
        
        // Determine the correct list to pull directions from for baseline, training, or actual child
        if (sessionType === "0_AC") {
            SessionDirectionsTemplate = JSON.stringify(caregiverDirectionPool[caregiverID]["actualChild"]);
        } else {
            if (studyPhase === "0_BL" || studyPhase === "5_RTB") {
                SessionDirectionsTemplate = JSON.stringify(caregiverDirectionPool[caregiverID]["baseline"]);
            } else {
                SessionDirectionsTemplate = JSON.stringify(caregiverDirectionPool[caregiverID]["training"]);
            }
        }

        // Store the JSON formatted SessionDirectionsTemplate in embedded data then update JavaScript SessionDirectionsTemplate with parsed value
        Qualtrics.SurveyEngine.setEmbeddedData('SessionDirectionsTemplate', SessionDirectionsTemplate);
        SessionDirectionsTemplate = JSON.parse(SessionDirectionsTemplate);

        // Initialize the SessionDirectionPool with the SessionDirectionsTemplate
        SessionDirectionPool = JSON.stringify(SessionDirectionsTemplate);
        Qualtrics.SurveyEngine.setEmbeddedData('SessionDirectionPool', SessionDirectionPool);
        SessionDirectionPool = Array.from(JSON.parse(SessionDirectionPool));
    } else {
        // Parse the SessionDirectionsTemplate and SessionDirectionPool from JSON string
        SessionDirectionsTemplate = JSON.parse(SessionDirectionsTemplate);
        SessionDirectionPool = Array.from(JSON.parse(SessionDirectionPool));
    }

    function getSpecificDirection(index) {
        // Retrieve the specific direction from the SessionDirectionsTemplate based on the index
        return SessionDirectionsTemplate[index];
    }

    function getRandomDirection() {
        // Check if SessionDirectionPool is empty
        if (SessionDirectionPool.length === 0) {
            // If empty, replenish it from the SessionDirectionsTemplate
            SessionDirectionPool = [...SessionDirectionsTemplate];
        }

        // Randomly select a direction from the list
        var randomIndex = Math.floor(Math.random() * SessionDirectionPool.length);
        var selectedDirection = SessionDirectionPool[randomIndex];
        SessionDirectionPool.splice(randomIndex, 1);
        return selectedDirection;
    }

    // Retrieve the values of the StudyPhase and SessionType embedded variables
    var studyPhase = Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase');
    var sessionType = Qualtrics.SurveyEngine.getEmbeddedData('SessionType');

    // Execute function based on StudyPhase and SessionType
    if (studyPhase === "0_BL" && sessionType === "0_AC") {
        // Use a specific direction based on the survey link initialized embedded field
        var specificDirectionIndex = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('SpecificBaselineDirectionIndex'));
        selectedDirection = getSpecificDirection(specificDirectionIndex);
    } else {
        // Use random direction selection for other phases
        selectedDirection = getRandomDirection();
    }

    // Set the selected direction as an embedded variable for tracking with AggregateData
    Qualtrics.SurveyEngine.setEmbeddedData('TrialDirection', selectedDirection);
    
    // Clean selected direction by removing first four characters for the caregiver piped question text
    selectedDirection = selectedDirection.substring(4);
    Qualtrics.SurveyEngine.setEmbeddedData('CaregiverTrialDirection', selectedDirection);
    
    // Store the updated SessionDirectionPool in embedded data
    Qualtrics.SurveyEngine.setEmbeddedData('SessionDirectionPool', JSON.stringify(SessionDirectionPool));
}
```

## Confederate Response Selection 

**Purpose**:
To randomly select a response for the confederate within each trial block, ensuring a balanced distribution of "Comply" and "No Comply" responses.

**Implementation**:
JavaScript is employed within Qualtrics to facilitate this logic. The `selectConfResponse()` function is called at the appropriate point in the survey flow or question logic to randomly assign a response to the confederate.

The `selectConfResponse()` function performs the following steps:

1. Retrieves the value of the `ConfResponseBlock` embedded data field using `Qualtrics.SurveyEngine.getEmbeddedData('ConfResponseBlock')`. This field stores the state of the response block array across trials.

2. Checks if the `ConfResponseBlock` is empty. If it is, the function initializes it with the initial state `['0_Comply', '1_NoComply']`. If it's not empty, the function parses the JSON string to convert it back to an array.

3. Checks if the `ConfResponseBlock` array is empty. If it is, the function resets it to the initial state `['0_Comply', '1_NoComply']`, as both responses have been used in the current block.

4. Generates a random index within the range of the current `ConfResponseBlock` array using `Math.floor(Math.random() * confResponseBlock.length)`.

5. Retrieves the selected response from the `ConfResponseBlock` array using the random index.

6. Removes the selected response from the `ConfResponseBlock` array using `confResponseBlock.splice(randomIndex, 1)` to ensure it is not repeated within the same block.

7. Sets the selected response as the value of the `ConfResponse` embedded data field using `Qualtrics.SurveyEngine.setEmbeddedData('ConfResponse', selectedResponse)`.

8. Updates the `ConfResponseBlock` embedded data field with the modified `confResponseBlock` array by converting it back to a JSON string using `JSON.stringify(confResponseBlock)`.

9. it will not only set the `ConfResponse` and `ConfResponseBlock` embedded data fields but also set the SelfMonitoring6 embedded data field based on the selected response.

If the selected response is '0_Comply', `SelfMonitoring6` will be set to '1'.
If the selected response is '1_NoComply', `SelfMonitoring6` will be set to '0'.

**JavaScript Code**:
```javascript
function selectConfResponse() {
    var confResponseBlock = Qualtrics.SurveyEngine.getEmbeddedData('ConfResponseBlock');

    if (confResponseBlock === '') {
        confResponseBlock = ['0_Comply', '1_NoComply'];
    } else {
        confResponseBlock = JSON.parse(confResponseBlock);
    }

    if (confResponseBlock.length === 0) {
        confResponseBlock = ['0_Comply', '1_NoComply'];
    }

    var randomIndex = Math.floor(Math.random() * confResponseBlock.length);
    var selectedResponse = confResponseBlock[randomIndex];
    confResponseBlock.splice(randomIndex, 1);

    Qualtrics.SurveyEngine.setEmbeddedData('ConfResponse', selectedResponse);
    Qualtrics.SurveyEngine.setEmbeddedData('ConfResponseBlock', JSON.stringify(confResponseBlock));

    // Set SelfMonitoring6 based on the selected response
    if (selectedResponse === '0_Comply') {
        Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6', '1');
    } else {
        Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6', '0');
    }
}
```

**Embedded Data Fields**:
- `ConfResponse`: Stores the selected response for the confederate (either "0_Comply" or "1_NoComply").
- `ConfResponseBlock`: Stores the state of the response block array across trials. It is initialized with an empty value in the survey flow.

**Usage**:
The `selectConfResponse()` function should be called at the appropriate point in the survey flow or question logic to randomly assign a response to the confederate. It can be called within the `Qualtrics.SurveyEngine.addOnload()` block or any other suitable location.

The selected response stored in the `ConfResponse` embedded data field can be used to display the confederate's response or to determine the confederate's behavior based on the assigned response.

**Example**:
```javascript
Qualtrics.SurveyEngine.addOnload(function() {
    /*Place your JavaScript here to run when the page loads*/
    selectConfResponse();
});
```

By using this approach, the confederate's responses will be randomized within each trial block, ensuring a balanced distribution of "Comply" and "No Comply" responses, while allowing for the possibility of consecutive "No Comply" or "Comply" responses across trial blocks.

## Session and Trial Data Entry Synchronization Measures Using Embedded Data

This section outlines the procedures and configurations implemented in a Qualtrics survey to synchronize session and trial data entries by caregivers and confederates. The synchronization is critical for ensuring accurate data matching and analysis, particularly for inter-rater agreement assessments.

### Implementation Strategies

1. **CaregiverID and Session Count Synchronization**:
   - **Objective**: Link data across different sessions to the respective caregiver.
   - **Implementation**: 
   - Unique survey URLs are generated for each session, incorporating `CaregiverID` and `SessionCount` as query parameters, using an Excel sheet formula (Session Link Generator.xlsx).
   - Within Qualtrics, an "Embedded Data" element in the survey flow captures these parameters at the start of the survey.

2. **Timestamps for Trial Entries**:
   - **Objective**: Record the timing of each entry to establish the sequence of events.
   - **Implementation**: Utilize Qualtrics' built-in timestamp ('ActualTimestamp' and 'SessionTimestamp') feature to capture the start and end times of each trial entry. This can be achieved by enabling the "Capture Timing" option in the survey options or through embedded data fields that capture timestamps at critical points.

3. **Trial Entry Cycle Control**:
   - **Objective**: Prevent the commencement of the next trial entry cycle until both parties are ready.
   - **Implementation**: Introduce a "Wait Block" at the end of each trial, where progression to the next trial requires explicit action from both participants, ensuring readiness.

4. **Proximity and Coordination**:
   - **Objective**: Facilitate immediate communication and coordination between the caregiver and confederate.
   - **Implementation**: Conduct sessions in the same physical space, allowing for direct interaction and synchronization of activities.

5. **Explicit Signal for Advancement**:
   - **Objective**: Ensure simultaneous progression to the next trial by both parties.
   - **Implementation**: Establish a standardized signal (verbal or within the survey) to indicate readiness to advance, further aligning the timestamps of entries.

6. **Continuous Monitoring and Adjustment**:
   - **Objective**: Maintain effective synchronization throughout the study.
   - **Implementation**: Regularly review the synchronization measures for effectiveness and make adjustments based on observed performance and feedback.

7. **Addressing Limitations**:
   - **Objective**: Minimize manual tasks required for data synchronization.
   - **Implementation**: Acknowledge the potential need for manual adjustments in data alignment and strive to limit these through careful design
  



---

### Data Export

Qualtrics offers options for exporting response data. Initially, the solution was to use the Qualtrics Survey website to manually copy and paste the text, but this was labor-intensive, albeit useful for verifying individual responses. The alternative solution is downloading the entire response table from Qualtrics.

- **Solution A: Reviewing Individual Response Entries on HTML**: This process is used to quickly verify the output of a specific session and can be further extracted.
- **Solution B: Tab Separated Values (.tsv)**: This format, recommended for use with Microsoft Excel, separates each response value with a tab and each response with a newline. Qualtrics TSV exports use UTF-16 encoding to handle special characters.
- **Solution C: Copy and Paste Method for Manual Extraction:** This method is an alternative approach when automated exports within Qualtrics fail to retrieve the required data (e.g., AggregatedData). It involves using the Qualtrics web interface to manually copy and paste responses into a text file, which can then be transformed into a structured format.

#### Qualtrics Survey Data Structure and Organization

Responses in Qualtrics are stored in the "response data table," accessible via the "Data & Analysis" tab on the dashboard.

#### Response Data Table Column Details

- **Response Data Order**: The order of questions in the exported table typically matches their order in the survey, subject to any randomization or survey logic.
- **Question Identification**:
  - **QID (Question ID)**: A system-generated unique identifier for each question, used internally.
  - **User-Generated Question Title**: A descriptive name assigned by the survey creator for internal reference; not visible to respondents.
- **Question Content**:
  - **Question Text**: The actual wording of the question as seen by survey participants.
- **Metadata Fields in Data Table**:
  - Includes system-generated fields such as `startDate`, `endDate`, `progress`, `duration`, and `finished`, which are fixed and cannot be modified within Qualtrics.

#### Solution A Data Extraction Procedure

##### Qualtrics View Response Collection

Use this solution to obtain a result from a specific Qualtrics survey response.

1. Open the TechPT Session Guide project.
2. Click **Data and Analysis**.
3. Select the three dots next to the response you want to collect.
4. Click **View Response** and wait for it to load.
5. Scroll down to the aggregate data text and copy it.
6. Paste the text into a plain text editor, such as Notepad or Notepad++.
7. Organize and clean the data by deleting extraneous labels (e.g., "aggregate data x", "respondent data x") so that each aggregate data entry is aligned.
8. Assign a name using the format `Date (YYYY.MM.DD) - CaregiverID - Respondent - StudyPhase - SessionType - SessionCount - [A,B,C for multiple entries during the same session].txt`. Example: `2024.07.02 - CG3255 - 1_CARE - 1_T1 - 1_SC - 1.txt`.
9. Follow the steps to convert JSON data to CSV.
10. Open the exported dataset.

##### Converting JSON Data to CSV

To utilize the exported data table from Qualtrics:

1. Open the tab-delimited file in Excel.
2. Copy all cells of `AggregatedData[x]` for the relevant survey row.
3. Paste into a new text file.
4. Label the file using the format `Date (YYYY.MM.DD) - CaregiverID - Respondent - StudyPhase - SessionType - SessionCount - [A,B,C for multiple entries during the same session].txt`.
5. Run the Python script `json_to_csv.py`.


- A file dialog will open, prompting you to select the input JSON file.
- The script will automatically clean up the JSON data by removing any delimiter patterns (such as `] [`) and replacing them with commas.
- Another dialog will ask you to specify the location and name for the output CSV file. Choose a location, enter a name, and click "Save".
- The script will parse the JSON data, extract field names from the first object, and write the data to the CSV file.
- Upon completion, you'll see a success message indicating that the data has been exported to the CSV file.

##### Python Code for JSON to CSV Conversion

```python
import json
import csv
import tkinter as tk
from tkinter import filedialog
import re
import os

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input JSON file
json_file = filedialog.askopenfilename(title="Select JSON File", filetypes=[("Text Files", "*.txt")])

# Read the JSON data from the file
with open(json_file, "r") as file:
    json_data = file.read()

# Clean up the JSON data by removing the delimiter pattern
cleaned_json_data = re.sub(r'\]\s*\[', ',', json_data)

# Parse the cleaned JSON data
parsed_json_data = json.loads(cleaned_json_data)

# Extract the field names from the first object
field_names = list(parsed_json_data[0].keys())

# Get the base name of the input file
input_file_name = os.path.basename(json_file)

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate the output file path
output_file = os.path.join(output_dir, input_file_name)
output_file = os.path.splitext(output_file)[0] + ".csv"

# Open the output file in write mode
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for obj in parsed_json_data:
        writer.writerow(obj)

print(f"Data exported to {output_file} successfully.")
```

#### Solution B Data Extraction Procedure

This procedure extracts the entire response table from Qualtrics and creates a structured Excel sheet from `AggregatedData`.

1. Browse to your survey in Qualtrics.
2. Select **Data & Analysis**.
3. Click **Export & Import**.
4. Select **Export Data**.
5. Choose the TSV format.
6. Follow the download export options.
7. Follow the procedure for converting the TSV to a master Excel sheet.

##### Download Export Options

Selected options are marked with an [X].

- [X] **Download All Fields**: Includes all data fields in the export.
- [X] **Use Numeric Values**: Exports the numerical response identifier.
- **Use Choice Text**: Exports the text of the selected choices.
- **Compress Data as .zip File**: Compresses the export to save space.
- **Use Commas for Decimals**: Uses commas as decimal separators.
- **Remove Line Breaks**: Prevents formatting issues.
- [X] **Recode Seen but Unanswered Questions as -99**.
- [X] **Recode Seen but Unanswered Multi-Value Fields as 0**.
- **Export Viewing Order Data for Randomized Surveys**.
- **Split Multi-Value Fields into Columns**.
- [X] **Use Internal IDs in Header**.
- **Exclude Survey Response Edits**.
- **Include Download Links for User-Uploaded Files**.

##### Convert Raw Qualtrics TSV to Master

Execute the Python script `Qualtrics_to_Excel.py`. This script will load the TSV, extract relevant data, and export it into an Excel workbook.

#### Solution C Data Extraction Procedure

When final data collection was completed, the export function within Qualtrics was not extracting `AggregatedData`. An alternative solution was devised:

1. Add AggregateData embedded fields using the Qualtrics Field Editor tool.
2. Select 100 responses per page.
3. Use Ctrl-A then Ctrl-C to copy all responses.
4. Paste into a new text file.
5. Repeat for remaining responses.
6. Save the file as `TechPT - 2024.09.13 - Solution C RAW Data Export.txt`.
7. Use the `Solution C Data Transform.py` script.
8. Use the `Solution C JSON to CSV.py` script.

##### Solution C Data Transform Python Script

This script removes extraneous text and isolates JSON data from the embedded `AggregateData`.

```python
import re
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input text file
txt_file = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])

# Read the raw data
with open(txt_file, "r") as file:
    raw_data = file.read()

# Use a regular expression to extract JSON blocks
json_blocks = re.findall(r'\[.*?\]', raw_data, re.DOTALL)
cleaned_json_data = ' '.join(json_blocks)

# Write the cleaned JSON data to a new file
output_dir = filedialog.askdirectory(title="Select Output Directory")
output_file = f"{output_dir}/cleaned_json_output.txt"

with open(output_file, "w") as file:
    file.write(cleaned_json_data)

print(f"Cleaned JSON data exported to {output_file}")
```

##### Solution C JSON to CSV

Updated Solution A's script to accommodate additional JSON dictionary items (IOA fields).

```python
import json
import csv
import tkinter as tk
from tkinter import filedialog
import re
import os

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input JSON file
json_file = filedialog.askopenfilename(title="Select JSON File", filetypes=[("Text Files", "*.txt")])

# Read and clean up the JSON data
with open(json_file, "r") as file:
    json_data = file.read()
cleaned_json_data = re.sub(r'\]\s*\[', ',', json_data)

# Parse the cleaned JSON data
parsed_json_data = json.loads(cleaned_json_data)

# Define the desired header order, including IOA fields
desired_field_order = [
    "InstanceID", "EventNote", "DateTimeStamp:", "ResponseIDx", "CaregiverID", "Respondent", "StudyPhase",
    "SessionType", "SessionCount", "TotalSessionTrials", "SessionBlockCount", "TrialDirection", "CareDirStart",
    "CareDirEnd", "SelfMonitoring1", "SelfMonitoring2", "SelfMonitoring3", "SelfMonitoring4", "SelfMonitoring5",
    "SelfMonitoring6", "SelfMonitoring6a_1", "SelfMonitoring6a_2", "SelfMonitoring6a_3", "ConfResponse",
    "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", "ConfMonitoring6",
    "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3", "ConfChildResponse", "ConfederateInteraction",
    "ConfTrialNote", "ConfSessionNote",
    # IOA-specific fields
    "IOAVideoName", "IOADirStart", "IOADirEnd", "IOAMonitoring1", "IOAMonitoring2", "IOAMonitoring3",
    "IOAMonitoring4", "IOAMonitoring5", "IOAMonitoring6", "IOAMonitoring6a_1", "IOAMonitoring6a_2",
    "IOAMonitoring6a_3", "IOAResponse", "IOAChildResponse", "IOAConfederateInteraction", "IOATrialNote", 
    "IOASessionNote"
]

# Get the base name of the input file with the extension
input_file_name = os.path.basename(json_file)

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate the output file path using the input file name
output_file = os.path.join(output_dir, input_file_name)

# Change the file extension of the output file to .csv
output_file = os.path.splitext(output_file)[0] + ".csv"

# Open the output file in write mode
with open(output_file, "w", newline="") as file:
    # Create a CSV writer object using the desired header order
    writer = csv.DictWriter(file, fieldnames=desired_field_order)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for obj in parsed_json_data:
        # Write each row; missing fields will automatically be handled as empty
        writer.writerow({field: obj.get(field, '') for field in desired_field_order})

print(f"Data exported to {output_file} successfully.")

```
## Bugs and Issues

Training trial directon recording.
Message prompt for confederate end of trial says SC regardless of sessiontype.
Display of feedback and verbal prompting is not recorded.
Loop and merge 100 loops, likely creating an issue with the expansive rows in the qualtrics data table.
2024.09.26 - Name changes between qualtrics and data processing. CaregiverID gets changed due to privacy. Sometimes CaseAssignment is used, sometimes CaregiverID is replaced with the caseassignment value. This inconsistency can cause issues with data processing and analysis. A similar issue occurs with SessionCount and the data anayliss of session number. It slipped into the code at some point when developing queries and trying to figure out how to exctract trial block data based on session count and phase. Also, some of the computed values ALL_ get mixed in. The master table also had a ':' in the header, which caused issues with the data processing. The header was changed to remove the ':' and the data processing was updated to reflect this change. This is the only documentation. 


## Depreciated Features

### Link Variables (Deprecated)

This methodology was removed as it is redundant. The Qualtrics Backend automatically defines the survey link data as an embedded data field. Left in the header script for legacy operations. Moving forward, all functions should call upon the 'Embeddedfield' name. Currently left in header for legacy operation.

```javascript
// *** START GET LINK VARIABLES ***
function getURLParameters() {
    var params = window.location.search.substring(1).split('&');
    var paramObject = {};
    for (var i = 0; i < params.length; i++) {
        var param = params[i].split('=');
        paramObject[param[0]] = decodeURIComponent(param[1]);
    }
    return paramObject;
}

var urlParams = getURLParameters();

// *** END GET LINK VARIABLES


// *** START SET LINK EMBEDDED VARIABLES ***

var caregiverID = urlParams.CaregiverID;
var studyPhase = urlParams.StudyPhase;
var respondent = urlParams.Respondent;
var sessionType = urlParams.SessionType;
var sessionCount = urlParams.SessionCount;

// ... and so on for the other parameters

// *** END SET LINK EMBEDDED VARIABLES ***
```


### Footer Update Function in Qualtrics Survey
**Retired-Not fully functional (cache issues) and was for troubleshooting purposes. Commented out Footer Script, and removed Element from footer in look and feel.**

The "Footer Update Function" is designed to dynamically display specific survey metadata in the footer of a Qualtrics survey page. This metadata includes the respondent type, study phase, and session type. The function works by retrieving these details from predefined variables and updating a designated HTML element within the survey's footer.


#### Footer Function Overview

- **Function Name**: `updateFooterWithEmbeddedData`
- **Purpose**: To display survey metadata (Respondent, Study Phase, Session Type) in the survey footer.
- **Location in Survey**: This JavaScript function should be placed in the survey's header script or within a JavaScript block that executes on each page of the survey.

#### How It Works

1. **Constructing the Information String**:
   - The function constructs a string that combines the values of `respondent`, `studyPhase`, and `sessionType`. These variables are previously  defined and hold the current survey's metadata.

2. **Updating the Footer Element**:
   - The function identifies the HTML element with the ID `EmbeddedInfo`. This element is defined in Qualtrics Look and Feel footer HTML structure.
   - <div style="text-align: center; margin-top: 20px;">        <span id="EmbeddedInfo">[Block Name]</span> </div>
   - Once identified, the function updates the `innerText` of this element with the constructed information string.

3. **Automatic Execution**:
   - The function call `updateFooterWithEmbeddedData()` at the end of the script block ensures that this update occurs automatically when the page loads.

####  Footer HTML housed in Qualtrics look and Feel

```html
<div style="text-align: center; margin-top: 20px;">
       <span id="EmbeddedInfo">[Block Name]</span>
</div>
```

```javascript
// *** START Footer Update Function ***

function updateFooterWithEmbeddedData() {
    // Construct the information string
    var embeddedInfo = respondent + ", " + studyPhase + ", " + sessionType;

    // Update the footer element with this information
    var footerElement = document.getElementById('EmbeddedInfo');
    if (footerElement) {
        footerElement.innerText = embeddedInfo;
		} else {
        console.log("Footer element not found.");
    }
}
updateFooterWithEmbeddedData();

// *** END Footer Update Function ***
```	

### Utilization of supplemental array to manage Trial by trial observations

Upon returning to developing this function, the process had been modified slightly by experimental procedures. The solution was intially combursome, but near functional. However, with new information and distance from project, a solution to further utilize the recordeventdata function was selected, therby abandoning the array.  Additional rationale:

Using the existing recordEventData function to store and manage your data could indeed simplify your process and reduce redundancy. By leveraging the embedded data already captured, you can streamline the process of updating and calculating necessary values.

Updated Approach
Leverage Embedded Data: Use the recordEventData function to capture and store data points.
Real-time Calculation: Calculate necessary values such as trial block scores and overall percentages directly from the embedded data.
Minimize Redundancy: Avoid creating and maintaining a separate array for the same data.


### Mastery and Supplemental Instruction 

The structure of each object in the `confMonitoringArray` looks like this:

```javascript
{
  "question": "ConfMonitor1",
  "trialBlockScore": ["", "", "", ""]
}
```

- `trialBlockScore[0]`: Represents the score for TB_A (Trial Block A).
- `trialBlockScore[1]`: Represents the score for TB_B (Trial Block B).
- `trialBlockScore[2]`: Represents the score for TB_C (Trial Block C).
- `trialBlockScore[3]`: Represents the score for TB_Cache (Trial Block Cache).


````javascript
function updateConfMonitoringArray() {
   var confMonitoringArray = JSON.parse('${e://Field/ConfMonitoringArray}');
   var sessionBlockCount = parseFloat('${e://Field/SessionBlockCount}');

   if (Number.isInteger(sessionBlockCount)) {
      // Move TB_B to TB_A
      confMonitoringArray.forEach(function(item) {
         item.trialBlockScore[0] = item.trialBlockScore[1];
      });

      // Move TB_C to TB_B
      confMonitoringArray.forEach(function(item) {
         item.trialBlockScore[1] = item.trialBlockScore[2];
      });

      // Calculate TB_C score using TB_Cache and Current Trial
      confMonitoringArray.forEach(function(item) {
         var tbCacheValue = parseInt(item.trialBlockScore[3]);
         if (isNaN(tbCacheValue)) {
            // handle error
            console.error('Invalid tbCacheValue');
            return;
         }
         var currentTrialValue = parseInt('${e://Field/ConfMonitorX}');
         if (isNaN(currentTrialValue)) {
            //handle error
            console.error('Invalid currentTrialValue'):
         }
         item.trialBlockScore[2] = calculateTrialBlockScore(tbCacheValue, currentTrialValue);
      });

      // Null TB_Cache
      confMonitoringArray.forEach(function(item) {
         item.trialBlockScore[3] = "";
      });

      // Calculate the overall percentage for the last 3 trial blocks
      var overallPercentage = calculateOverallPercentage(confMonitoringArray);

      // Update the embedded data field with the overall percentage
      Qualtrics.SurveyEngine.setEmbeddedData('OverallPercentage', overallPercentage);
   } else {
      // Move current trial to TB_Cache
      confMonitoringArray.forEach(function(item) {
         item.trialBlockScore[3] = '${e://Field/ConfMonitorX}';
      });
   }

   // Update the embedded data field with the modified array
   Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoringArray', JSON.stringify(confMonitoringArray));
}
````

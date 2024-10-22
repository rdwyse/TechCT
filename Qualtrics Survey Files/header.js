//console.log("Start Header Script!!");

// *** START First Run ***

if (Qualtrics.SurveyEngine.getEmbeddedData('FirstRunSwitch') === "0") {
    // Set the FirstRunSwitch to 1 to indicate the script has run once
    Qualtrics.SurveyEngine.setEmbeddedData('FirstRunSwitch', "1");

    var sessiontime = Qualtrics.SurveyEngine.getEmbeddedData('DateTimeStamp');
    Qualtrics.SurveyEngine.setEmbeddedData('SessionStartTime', sessiontime);

}
// *** END DEFINE ADDITIONAL EMBEDDED Variables ***


// *** START CaregiverDirectionPool Code ***


// *** Start currentDateTime stamp ***

function getCurrentDateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
  
    const timezoneOffset = -now.getTimezoneOffset();
    const sign = timezoneOffset >= 0 ? '+' : '-';
    const offsetHours = String(Math.abs(Math.floor(timezoneOffset / 60))).padStart(2, '0');
    const offsetMinutes = String(Math.abs(timezoneOffset % 60)).padStart(2, '0');
  
    return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}${sign}${offsetHours}:${offsetMinutes}`;
  }
// *** END currentDateTime stamp ***


var caregiverDirectionPool = {
    "CG3325": {
        baseline: [
            "BL0_Have your child sit at the table",
            "BL1_Have your child pick up the toy",
            "BL2_Have your child put the toy in the box",
            // ... additional baseline directions
        ],
        training: [
            "TR0_Have your child put their shoes on",
            "TR1_Have your child touch their nose",
            // ... additional training directions
        ]
    }
    // ... other caregivers can be added as needed
};
// *** End CaregiverDirectionPool Code ***


// *** START Instance Code ***
  
   function generateRandomString(length) {
    var chars = '0123456789abcdefghijklmnopqrstuvwxyz';
    var result = '';
    for (var i = length; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];
    return result;
   }
   
// ***END Instance Code***


// *** START Direction Selection Function Code ***

function selectDirection() {
    
    var SessionDirectionsTemplate = Qualtrics.SurveyEngine.getEmbeddedData('SessionDirectionsTemplate');
    var SessionDirectionPool = Qualtrics.SurveyEngine.getEmbeddedData('SessionDirectionPool');
    
    var selectedDirection;

    // Check if template is empty. Get the list of directions for the specified caregiver and phase. Place it in the template.
    if (SessionDirectionsTemplate === "0") {
        // Retrieve the values of the StudyPhase and CaregiverID embedded variables
        var studyPhase = Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase');
        var caregiverID = Qualtrics.SurveyEngine.getEmbeddedData('CaregiverID');
        
        // Determine the correct list to pull directions from for baseline or training
        if (studyPhase === "0_BL" || studyPhase === "5_RTB") {
            SessionDirectionsTemplate = JSON.stringify(caregiverDirectionPool[caregiverID]["baseline"]);
        } else {
            SessionDirectionsTemplate = JSON.stringify(caregiverDirectionPool[caregiverID]["training"]);
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

    // Execute function
    selectedDirection = getRandomDirection();

    // Set the selected direction as an embedded variable for tracking with AggregateData
    Qualtrics.SurveyEngine.setEmbeddedData('TrialDirection', selectedDirection);
    
    // Clean selected direction by removing first four characters for the caregiver piped question text
    selectedDirection = selectedDirection.substring(4);
    Qualtrics.SurveyEngine.setEmbeddedData('CaregiverTrialDirection', selectedDirection);
    
    // Store the updated SessionDirectionPool in embedded data
    Qualtrics.SurveyEngine.setEmbeddedData('SessionDirectionPool', JSON.stringify(SessionDirectionPool));
    
}
// *** END Direction Selection Function Code ***


// *** START ConfederateDirectionPool Code ***

function selectConfResponse() {
    
    if (Qualtrics.SurveyEngine.getEmbeddedData('SessionType') === "0_AC") {
        return; // Exit the function
    }
    
    var confResponseBlock = Qualtrics.SurveyEngine.getEmbeddedData('ConfResponseBlock');

    
    if (confResponseBlock === '' || confResponseBlock === undefined || confResponseBlock === null) {
        confResponseBlock = ['0_Comply', '1_NoComply'];
        // console.log("ConfResponseBlock is Null. Resetting to default values.");
    } else {
        confResponseBlock = JSON.parse(confResponseBlock);
        // console.log("ConfResponseBlock is not empty. Parsing values.");
    }

    if (confResponseBlock.length === 0) {
        confResponseBlock = ['0_Comply', '1_NoComply'];
        // console.log("ConfResponseBlock is ===0. Resetting to default values.");
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
// *** END ConfederateDirectionPool Code ***


// *** START Caregiver - Confederate Direction Timestamp Function Code ***

function setCareDirStart() {
    var careDirStart = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('CareDirStart', careDirStart);
}

function setCareDirEnd() {
    var careDirEnd = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('CareDirEnd', careDirEnd);
}

function setConfDirStart() {
    var confDirStart = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('ConfDirStart', confDirStart);
}

function setConfDirEnd() {
    var confDirEnd = getCurrentDateTime();
    Qualtrics.SurveyEngine.setEmbeddedData('ConfDirEnd', confDirEnd);
}
// *** END Caregiver - Confederate Direction Timestamp Function Code ***

// *** START Increment Session Variables Function Code ***

function incrementSessionVariables() {
    var totalSessionTrials = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('TotalSessionTrials'));
    totalSessionTrials++;
    Qualtrics.SurveyEngine.setEmbeddedData('TotalSessionTrials', totalSessionTrials);

    var sessionBlockCount = parseFloat(Qualtrics.SurveyEngine.getEmbeddedData('SessionBlockCount'));
    sessionBlockCount += 0.5;
    Qualtrics.SurveyEngine.setEmbeddedData('SessionBlockCount', sessionBlockCount);
}
// *** END Increment Session Variables Function Code ***


// *** START Record Event Data Function Code ***

function recordEventData(eventNote) {
    // Example of collecting embedded data and dynamic variables

        // Get the current RecorderCounter and RecorderIndex from embedded data
        var counter = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('RecorderCounter'));
        var index = parseInt(Qualtrics.SurveyEngine.getEmbeddedData('RecorderIndex'));
        // console.log("counter: " + counter);
        // console.log("index: " + index);

    
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

    var eventData = {
        'InstanceID': generateRandomString(10),
        'EventNote': eventNote,
        'DateTimeStamp:': getCurrentDateTime(),
        'ResponseIDx': Qualtrics.SurveyEngine.getEmbeddedData('ResponseIDx'),
        'CaregiverID': Qualtrics.SurveyEngine.getEmbeddedData('CaregiverID'),
        'Respondent': Qualtrics.SurveyEngine.getEmbeddedData('Respondent'),
        'StudyPhase': Qualtrics.SurveyEngine.getEmbeddedData('StudyPhase'),
        'SessionType': Qualtrics.SurveyEngine.getEmbeddedData('SessionType'),
        'SessionCount': Qualtrics.SurveyEngine.getEmbeddedData('SessionCount'),
        'TotalSessionTrials': Qualtrics.SurveyEngine.getEmbeddedData('TotalSessionTrials'),
        'SessionBlockCount': Qualtrics.SurveyEngine.getEmbeddedData('SessionBlockCount'),

        
        //CaregiverItems
        'TrialDirection': Qualtrics.SurveyEngine.getEmbeddedData('TrialDirection'),
        'CareDirStart': Qualtrics.SurveyEngine.getEmbeddedData('CareDirStart'),
        'CareDirEnd': Qualtrics.SurveyEngine.getEmbeddedData('CareDirEnd'),       
        'SelfMonitoring1': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring1'),
        'SelfMonitoring2': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring2'),
        'SelfMonitoring3': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring3'),
        'SelfMonitoring4': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring4'),
        'SelfMonitoring5': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring5'),
        'SelfMonitoring6': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring6'),
        'SelfMonitoring6a_1': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring6a_1'),
        'SelfMonitoring6a_2': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring6a_2'),
        'SelfMonitoring6a_3': Qualtrics.SurveyEngine.getEmbeddedData('SelfMonitoring6a_3'),

        

        //confederateItems
        'ConfResponse': Qualtrics.SurveyEngine.getEmbeddedData('ConfResponse'),
        'ConfMonitoring1': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring1'),
        'ConfMonitoring2': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring2'),
        'ConfMonitoring3': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring3'),
        'ConfMonitoring4': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring4'),
        'ConfMonitoring5': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring5'),
        'ConfMonitoring6': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring6'),
        'ConfMonitoring6a_1': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring6a_1'),
        'ConfMonitoring6a_2': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring6a_2'),
        'ConfMonitoring6a_3': Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoring6a_3'),
        'ConfChildResponse': Qualtrics.SurveyEngine.getEmbeddedData('ConfChildResponse'),
        'ConfederateInteraction': Qualtrics.SurveyEngine.getEmbeddedData('ConfederateInteraction'),
        'ConfTrialNote': Qualtrics.SurveyEngine.getEmbeddedData('ConfTrialNote'),
        'ConfSessionNote': Qualtrics.SurveyEngine.getEmbeddedData('ConfSessionNote') 
        
    };
    //console.log(eventData); 

    // Save eventData to the appropriate AggregateData field

    var fieldName = 'AggregateData' + index;
    //console.log("AggregateDate + Index: " + fieldName);

    var existingData = Qualtrics.SurveyEngine.getEmbeddedData(fieldName);
    //console.log("Existing Data: " + existingData);
   
    var aggregatedData = existingData ? JSON.parse(existingData) : [];
    //console.log("Aggregate Data: " + aggregatedData);
    aggregatedData.push(eventData);
    //console.log("Aggregate Data Pushed: " + aggregatedData);
    //Qualtrics.SurveyEngine.setEmbeddedData(fieldName, JSON.stringify(aggregatedData));
    //console.log("stringified JSON: " + JSON.stringify(aggregatedData))
   
    Qualtrics.SurveyEngine.setEmbeddedData(fieldName, JSON.stringify(aggregatedData));
    //console.log("AggregatedData1: " + Qualtrics.SurveyEngine.getEmbeddedData('AggregateData1'));

};
// *** END Record Event Data Function Code ***


// *** START clearEmbeddedData Function Code ***

    function clearEmbeddedTrialData() {
    // Null out the monitoring embedded data variables

    // CaregiverItems
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring1', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring2', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring3', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring4', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring5', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6a_1', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6a_2', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6a_3', '');
    Qualtrics.SurveyEngine.setEmbeddedData('SelfMonitoring6b_1', '');
    Qualtrics.SurveyEngine.setEmbeddedData('CareDirEnd', '');
    Qualtrics.SurveyEngine.setEmbeddedData('TrialDirection', '');

    // ConfederateItems
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring1', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring2', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring3', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring4', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring5', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring6', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring6a_1', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring6a_2', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfMonitoring6a_3', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfChildResponse', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfResponse', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfederateInteraction', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfTrialNote', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfDirStart', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfDirEnd', '');
    Qualtrics.SurveyEngine.setEmbeddedData('TrialDirection', '');
    Qualtrics.SurveyEngine.setEmbeddedData('ConfResponse', '');
   
    // Additional Nulling of variables occurs on the EventData javascript block within each caregiver and confederate trial block to clean up for the end of the session.
};
// *** END clearEmbeddedData Function Code ***


// *** START Update ConfMonitoring Array Code ***

function updateConfMonitoringArrays() {
    var confMonitoringFields = ['ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'];
    var confMonitoringScores = JSON.parse(Qualtrics.SurveyEngine.getEmbeddedData('ConfMonitoringScores')) || {};

    confMonitoringFields.forEach(function(field) {
        if (!confMonitoringScores[field]) {
            confMonitoringScores[field] = [[]];
        }

        var rawScore = Qualtrics.SurveyEngine.getEmbeddedData(field);
    
        var score = Number(rawScore) === 1 ? 1 : 0;  // Ensure numeric comparison
        

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
// *** END Update ConfMonitoring Array Code ***


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
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackSwitch', '1');
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackCount', feedbackCount);
            console.log("Providing written feedback. Updated feedback count:", feedbackCount);
            provideWrittenFeedback(confMonitoringScores, confMonitoringFields); 
        } else {
            feedbackCount++;
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackSwitch', '2');
            Qualtrics.SurveyEngine.setEmbeddedData('FeedbackCount', feedbackCount);
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

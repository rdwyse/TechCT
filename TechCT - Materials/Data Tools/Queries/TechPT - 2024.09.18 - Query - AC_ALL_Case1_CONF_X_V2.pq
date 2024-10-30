let
	// Define parameters
	CaregiverID = "Case1",        // Parameter: Case1, Case2, Case3, Case4
	Respondent = "1_CONF",        // Parameter: 1_CONF, 2_IOA, CARE (Confederate, IOA, Caregiver)
	SessionType = "0_AC",         // Parameter: 0_AC (Actual Child), 1_SC (Simulated Child)
	EventNote = "3.0_Conf_TX_SC_TrialComplete",  // Parameter: 3.0_Conf_TX_SC_TrialComplete, 2.0_Conf_TX_BL_Start, etc.


    // Source data from Excel table
    Source = Excel.CurrentWorkbook(){[Name="Table2"]}[Content],

    // Change data types for consistency
    #"Changed Type" = Table.TransformColumnTypes(Source, {
        {"InstanceID", type text}, {"EventNote", type text}, {"DateTimeStamp", type datetimezone}, 
        {"ResponseIDx", type text}, {"CaregiverID", type text}, {"Respondent", type text}, 
        {"StudyPhase", type text}, {"SessionType", type text}, {"SessionCount", Int64.Type}, 
        {"TotalSessionTrials", Int64.Type}, {"SessionBlockCount", type number}, {"TrialDirection", type text}, 
        {"CareDirStart", type datetimezone}, {"CareDirEnd", type datetimezone}, 
        {"SelfMonitoring1", Int64.Type}, {"SelfMonitoring2", Int64.Type}, {"SelfMonitoring3", Int64.Type}, 
        {"SelfMonitoring4", Int64.Type}, {"SelfMonitoring5", Int64.Type}, {"SelfMonitoring6", Int64.Type}, 
        {"SelfMonitoring6a_1", Int64.Type}, {"SelfMonitoring6a_2", Int64.Type}, {"SelfMonitoring6a_3", Int64.Type}, 
        {"ConfResponse", type text}, {"ConfMonitoring1", Int64.Type}, {"ConfMonitoring2", Int64.Type}, 
        {"ConfMonitoring3", Int64.Type}, {"ConfMonitoring4", Int64.Type}, {"ConfMonitoring5", Int64.Type}, 
        {"ConfMonitoring6", Int64.Type}, {"ConfMonitoring6a_1", Int64.Type}, {"ConfMonitoring6a_2", Int64.Type}, 
        {"ConfMonitoring6a_3", Int64.Type}, {"ConfChildResponse", type text}, {"ConfederateInteraction", Int64.Type}, 
        {"ConfTrialNote", type text}, {"ConfSessionNote", type text}, {"IOAVideoName", type any}, 
        {"IOADirStart", type any}, {"IOADirEnd", type any}, {"IOAMonitoring1", type any}, 
        {"IOAMonitoring2", type any}, {"IOAMonitoring3", type any}, {"IOAMonitoring4", type any}, 
        {"IOAMonitoring5", type any}, {"IOAMonitoring6", type any}, {"IOAMonitoring6a_1", type any}, 
        {"IOAMonitoring6a_2", type any}, {"IOAMonitoring6a_3", type any}, {"IOAResponse", type any}, 
        {"IOAChildResponse", type any}, {"IOAConfederateInteraction", type any}, {"IOATrialNote", type any}, 
        {"IOASessionNote", type any}}),

    // Apply filtering for CaregiverID, Respondent, SessionType, and EventNote using parameters
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each 
        ([CaregiverID] = CaregiverID) and 
        ([Respondent] = Respondent) and 
        ([SessionType] = SessionType) and 
        ([EventNote] = EventNote)
    ),

    // Remove unnecessary columns, keeping only relevant ones
    #"Removed Other Columns" = Table.SelectColumns(#"Filtered Rows", {
        "InstanceID", "EventNote", "DateTimeStamp", "ResponseIDx", "CaregiverID", "Respondent", 
        "StudyPhase", "SessionType", "SessionCount", "TotalSessionTrials", "SessionBlockCount", 
        "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", 
        "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3", "ConfChildResponse", 
        "ConfederateInteraction", "ConfTrialNote"
    }),

    // Add a custom column for T1 average (ConfMonitoring1, 2, 6a_1, 6a_2, 6a_3)
    #"Added Custom" = Table.AddColumn(#"Removed Other Columns", "T1_Average", each 
        ([ConfMonitoring1] + [ConfMonitoring2] + [ConfMonitoring6a_1] + [ConfMonitoring6a_2] + [ConfMonitoring6a_3]) / 5
    ),

    // Add a custom column for T2 average (ConfMonitoring3, 4, 5)
    #"Added Custom1" = Table.AddColumn(#"Added Custom", "T2_Average", each 
        ([ConfMonitoring3] + [ConfMonitoring4] + [ConfMonitoring5]) / 3
    ),

    // Add a custom column for AllConfMonitoring average (all ConfMonitoring columns)
    #"Added Custom2" = Table.AddColumn(#"Added Custom1", "AllConfMonitoring_Average", each 
        ([ConfMonitoring1] + [ConfMonitoring2] + [ConfMonitoring3] + [ConfMonitoring4] + [ConfMonitoring5] + 
        [ConfMonitoring6a_1] + [ConfMonitoring6a_2] + [ConfMonitoring6a_3]) / 8
    )

in
    #"Added Custom2"
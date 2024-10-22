//ALL_ALL_Case1_CONF_TrialBlockScoring_v1
// 2024.09.18

let
    // Define parameters
    CaregiverID = "Case1",  // Select the relevant participant ID
    Respondent = "1_CONF",  // Parameter: 1_CONF, 2_IOA, CARE (Confederate, IOA, Caregiver)
    SessionType = "1_SC",   // Set session type
    EventNote = "3.0_Conf_TX_SC_TrialComplete",  // Parameter: 3.0_Conf_TX_SC_TrialComplete, 2.0_Conf_TX_BL_Start, etc.

    // Load the data
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

    // Filter by CaregiverID, Respondent, EventNote, and SessionType
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each 
        ([CaregiverID] = CaregiverID) and 
        ([Respondent] = Respondent) and
        ([EventNote] = EventNote) and
        ([SessionType] = SessionType)
    ),

    // Sort the table by DateTimeStamp to ensure the rows are in chronological order
    #"Sorted Rows" = Table.Sort(#"Filtered Rows",{{"DateTimeStamp", Order.Ascending}}),

    // Add an index column starting from 1
    #"Added Index" = Table.AddIndexColumn(#"Sorted Rows", "Index", 1, 1, Int64.Type),

    // Create TrialBlockGroup column by dividing the Index by 2 and adding 1 (pairs of two trials per group)
    #"Added TrialBlockGroup" = Table.AddColumn(#"Added Index", "TrialBlockGroup", each Number.IntegerDivide([Index] - 1, 2) + 1),

    // Group by TrialBlockGroup (which uniquely identifies each block of two trials)
    #"GroupedTBRows" = Table.Group(#"Added TrialBlockGroup", {"TrialBlockGroup"}, {
        {"ComputedTrialBlockSubTable", each _, Int64.Type}
    }),


    // Compute the trial block scores for each ConfMonitoring variable and extract additional fields from Trial 2
    #"Added Custom" = Table.AddColumn(#"GroupedTBRows", "TrialBlockScore", each
        let 
            TrialRows = [ComputedTrialBlockSubTable],  //  set to the sub-table of trials (ComputedTrialBlockSubTable) within each trial block.
            Trial1 = if Table.RowCount(TrialRows) > 0 then TrialRows{0} else null, // First trial in the block
            Trial2 = if Table.RowCount(TrialRows) > 1 then TrialRows{1} else null, // Second trial in the block
            
            // Extract additional fields from Trial2 (if it exists)
            SessionNumber = if Trial2 <> null then Trial2[SessionCount] else null,
            StudyPhase = if Trial2 <> null then Trial2[StudyPhase] else null,
            CaregiverID = if Trial2 <> null then Trial2[CaregiverID] else null,
            DateTimeStamp = if Trial2 <> null then Trial2[DateTimeStamp] else null,

            // Compute score for ConfMonitoring1
            TB_ConfMonitoring1 = if (Trial1[ConfMonitoring1] = 1 and Trial2[ConfMonitoring1] = 1) then 1 else 0,

            // Compute score for ConfMonitoring2
            TB_ConfMonitoring2 = if (Trial1[ConfMonitoring2] = 1 and Trial2[ConfMonitoring2] = 1) then 1 else 0,

            // Compute score for ConfMonitoring3
            TB_ConfMonitoring3 = if (Trial1[ConfMonitoring3] = 1 and Trial2[ConfMonitoring3] = 1) then 1 else 0,

            // Compute score for ConfMonitoring4
            TB_ConfMonitoring4 = if (Trial1[ConfMonitoring4] = 1 and Trial2[ConfMonitoring4] = 1) then 1 else 0,

            // Compute score for ConfMonitoring5
            TB_ConfMonitoring5 = if (Trial1[ConfMonitoring5] = 1 and Trial2[ConfMonitoring5] = 1) then 1 else 0,

            // Compute score for ConfMonitoring6a_1
            TB_ConfMonitoring6a_1 = if (Trial1[ConfMonitoring6a_1] = 1 and Trial2[ConfMonitoring6a_1] = 1) then 1 else 0,

            // Compute score for ConfMonitoring6a_2
            TB_ConfMonitoring6a_2 = if (Trial1[ConfMonitoring6a_2] = 1 and Trial2[ConfMonitoring6a_2] = 1) then 1 else 0,

            // Compute score for ConfMonitoring6a_3
            TB_ConfMonitoring6a_3 = if (Trial1[ConfMonitoring6a_3] = 1 and Trial2[ConfMonitoring6a_3] = 1) then 1 else 0

            // Create a record with all the scores and additional Trial 2 fields
            in
            [
                SessionNumber = SessionNumber,
                StudyPhase = StudyPhase,
                CaregiverID = CaregiverID,
                DateTimeStamp = DateTimeStamp,
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

    // Expand the TrialBlockScore record into separate columns
    #"Expanded TrialBlockScore" = Table.ExpandRecordColumn(#"Added Custom", "TrialBlockScore", 
        {"SessionNumber", "StudyPhase", "CaregiverID", "DateTimeStamp", 
        "TB_ConfMonitoring1", "TB_ConfMonitoring2", "TB_ConfMonitoring3", "TB_ConfMonitoring4", 
        "TB_ConfMonitoring5", "TB_ConfMonitoring6a_1", "TB_ConfMonitoring6a_2", "TB_ConfMonitoring6a_3"}),

    // Remove ComputedTrialBlockSubTable
    #"Removed Columns" = Table.RemoveColumns(#"Expanded TrialBlockScore", {"ComputedTrialBlockSubTable"}),

    // Add a custom column for T1 Count (TB_ConfMonitoring1, 2, 6a_1, 6a_2, 6a_3)
    #"Added T1_Count" = Table.AddColumn(#"Removed Columns", "T1_Count", each 
        ([TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3])
    ),

    // Add a custom column for T2 Count (TB_ConfMonitoring3, 4, 5)
    #"Added T2_Count" = Table.AddColumn(#"Added T1_Count", "T2_Count", each 
        ([TB_ConfMonitoring3] + [TB_ConfMonitoring4] + [TB_ConfMonitoring5])
    ),

    // Add a custom column for AllConfMonitoring Count (all TB_ConfMonitoring columns)
    #"Added AllConfMonitoring_Count" = Table.AddColumn(#"Added T2_Count", "AllConfMonitoring_Count", each 
        ([TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring3] + [TB_ConfMonitoring4] + [TB_ConfMonitoring5] + 
        [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3])
    ),

    // Add a custom column for T1 Average
    #"Added T1_Average" = Table.AddColumn(#"Added AllConfMonitoring_Count", "T1_Average", each 
        ([TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3]) / 5
    ),

    // Add a custom column for T2 Average
    #"Added T2_Average" = Table.AddColumn(#"Added T1_Average", "T2_Average", each 
        ([TB_ConfMonitoring3] + [TB_ConfMonitoring4] + [TB_ConfMonitoring5]) / 3
    ),

    // Add a custom column for AllConfMonitoring Average
    #"Added AllConfMonitoring_Average" = Table.AddColumn(#"Added T2_Average", "AllConfMonitoring_Average", each 
        ([TB_ConfMonitoring1] + [TB_ConfMonitoring2] + [TB_ConfMonitoring3] + [TB_ConfMonitoring4] + [TB_ConfMonitoring5] + 
        [TB_ConfMonitoring6a_1] + [TB_ConfMonitoring6a_2] + [TB_ConfMonitoring6a_3]) / 8
    ),

    // Reorder the columns as required
    #"Reordered Columns" = Table.ReorderColumns(#"Added AllConfMonitoring_Average", 
        {"DateTimeStamp", "CaregiverID", "SessionNumber", "TrialBlockGroup", "StudyPhase", 
        "TB_ConfMonitoring1", "TB_ConfMonitoring2", "TB_ConfMonitoring3", "TB_ConfMonitoring4", 
        "TB_ConfMonitoring5", "TB_ConfMonitoring6a_1", "TB_ConfMonitoring6a_2", "TB_ConfMonitoring6a_3", 
        "T1_Average", "T2_Average", "AllConfMonitoring_Average", "T1_Count", "T2_Count", "AllConfMonitoring_Count"}
    )

in
    #"Reordered Columns"

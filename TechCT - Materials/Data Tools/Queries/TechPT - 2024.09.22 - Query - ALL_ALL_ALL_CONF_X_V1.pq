let
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

    // Helper function to process each CaregiverID (SC and AC sessions)
    ProcessCaregiver = (CaregiverID as text) =>
    let
        Respondent = "1_CONF",  // Parameter: 1_CONF, 2_IOA, CARE (Confederate, IOA, Caregiver)
        EventNote_Prefix = "3.0_Conf",  // Match the first 8 characters of EventNote
        SessionType_SC = "1_SC",   // Set session type for Simulated Child
        SessionType_AC = "0_AC",   // Set session type for Actual Child

        // Filter SC sessions for this Caregiver
        #"Filtered Rows_SC" = Table.SelectRows(#"Changed Type", each 
            ([CaregiverID] = CaregiverID) and 
            ([Respondent] = Respondent) and
            (Text.Start([EventNote], 8) = EventNote_Prefix) and  
            ([SessionType] = SessionType_SC)
        ),

        // Sort the SC sessions by DateTimeStamp to ensure the rows are in chronological order
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
        
        // Add SC_SessionType for SC trials
        #"Added SC_SessionType" = Table.AddColumn(#"Added SC_AllConfMonitoring_Average", "SC_SessionType", each "1_SC"),

        // Filter AC sessions for this Caregiver
        #"Filtered Rows_AC" = Table.SelectRows(#"Changed Type", each 
            ([CaregiverID] = CaregiverID) and 
            ([Respondent] = Respondent) and
            (Text.Start([EventNote], 8) = EventNote_Prefix) and  
            ([SessionType] = SessionType_AC)
        ),

        // Select necessary columns and rename SessionCount to SessionNumber for AC trials
        #"Selected Columns_AC" = Table.SelectColumns(#"Filtered Rows_AC", {"DateTimeStamp", "CaregiverID", "SessionCount", "StudyPhase", 
            "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", 
            "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3", "SessionType"}),

        #"Renamed Columns_AC" = Table.RenameColumns(#"Selected Columns_AC", {{"SessionCount", "SessionNumber"}}),

        // Add TrialBlockGroup column for AC (you can set it to null if you don't need it)
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

        // Add AC_SessionType for AC trials
        #"Added AC_SessionType" = Table.AddColumn(#"Added AC_AllConfMonitoring_Average", "AC_SessionType", each "0_AC"),

        // Combine SC and AC for this CaregiverID
        #"Combined_SC_AC" = Table.Combine({#"Added SC_SessionType", #"Added AC_SessionType"})

    in
        #"Combined_SC_AC",  // This is where SC and AC are combined for each caregiver
    
    // Get the unique CaregiverIDs
    CaregiverIDs = List.Distinct(#"Changed Type"[CaregiverID]),

    // Apply the ProcessCaregiver function to each CaregiverID
    AllResults = List.Transform(CaregiverIDs, each ProcessCaregiver(_)),

    // Combine the results for all CaregiverIDs into one table
    FinalResult = Table.Combine(AllResults),

        // Define the list of columns before adding ALL columns
        AllColumnsWithoutALL = {
            "DateTimeStamp", "CaregiverID", "SessionNumber", "TrialBlockGroup", "StudyPhase", "SC_SessionType", "AC_SessionType",
            "TB_ConfMonitoring1", "TB_ConfMonitoring2", "TB_ConfMonitoring3", "TB_ConfMonitoring4",
            "TB_ConfMonitoring5", "TB_ConfMonitoring6a_1", "TB_ConfMonitoring6a_2", "TB_ConfMonitoring6a_3",
            "SC_T1_Average", "SC_T2_Average", "SC_AllConfMonitoring_Average", "SC_T1_Count", "SC_T2_Count", "SC_AllConfMonitoring_Count",
            "AC_T1_Average", "AC_T2_Average", "AC_AllConfMonitoring_Average", "AC_T1_Count", "AC_T2_Count", "AC_AllConfMonitoring_Count"
        },

    // Reorder the columns as needed
    #"Reordered Columns" = Table.ReorderColumns(FinalResult, AllColumnsWithoutALL),

    // Add combined ALL columns by adding columns individually
    #"Added ALL_T1_Count" = Table.AddColumn(#"Reordered Columns", "ALL_T1_Count", each 
        if [SC_T1_Count] <> null then [SC_T1_Count] else [AC_T1_Count], type number),
    #"Added ALL_T2_Count" = Table.AddColumn(#"Added ALL_T1_Count", "ALL_T2_Count", each 
        if [SC_T2_Count] <> null then [SC_T2_Count] else [AC_T2_Count], type number),
    #"Added ALL_AllConfMonitoring_Count" = Table.AddColumn(#"Added ALL_T2_Count", "ALL_AllConfMonitoring_Count", each 
        if [SC_AllConfMonitoring_Count] <> null then [SC_AllConfMonitoring_Count] else [AC_AllConfMonitoring_Count], type number),
    #"Added ALL_T1_Average" = Table.AddColumn(#"Added ALL_AllConfMonitoring_Count", "ALL_T1_Average", each 
        if [SC_T1_Average] <> null then [SC_T1_Average] else [AC_T1_Average], type number),
    #"Added ALL_T2_Average" = Table.AddColumn(#"Added ALL_T1_Average", "ALL_T2_Average", each 
        if [SC_T2_Average] <> null then [SC_T2_Average] else [AC_T2_Average], type number),
    #"Added ALL_AllConfMonitoring_Average" = Table.AddColumn(#"Added ALL_T2_Average", "ALL_AllConfMonitoring_Average", each 
        if [SC_AllConfMonitoring_Average] <> null then [SC_AllConfMonitoring_Average] else [AC_AllConfMonitoring_Average], type number),

    // Add ALL_SessionType column
    #"Added ALL_SessionType" = Table.AddColumn(#"Added ALL_AllConfMonitoring_Average", "ALL_SessionType", each 
        if [SC_SessionType] <> null then [SC_SessionType] else [AC_SessionType]),

    // Define the final AllColumns list including the ALL columns
    AllColumnsFinal = {
        "ALL_T1_Average", "ALL_T2_Average", "ALL_AllConfMonitoring_Average", "ALL_T1_Count", "ALL_T2_Count", "ALL_AllConfMonitoring_Count", "ALL_SessionType"
    },

    // Reorder columns to include new ALL columns
    #"Reordered Columns Final" = Table.ReorderColumns(#"Added ALL_SessionType", AllColumnsFinal),

    // Sort rows by DateTimeStamp in ascending order
    #"Sorted AllColumnsFinal" = Table.Sort(#"Reordered Columns Final", {{"DateTimeStamp", Order.Ascending}}),

    //select only interested columns

    #"Removed Other Columns" = Table.SelectColumns(#"Sorted AllColumnsFinal",{"DateTimeStamp", "CaregiverID", "SessionNumber", "TrialBlockGroup", "StudyPhase", "ALL_T1_Average", "ALL_T2_Average", "ALL_AllConfMonitoring_Average", "ALL_T1_Count", "ALL_T2_Count", "ALL_AllConfMonitoring_Count", "ALL_SessionType"}),
    #"Reordered Columns1" = Table.ReorderColumns(#"Removed Other Columns",{"DateTimeStamp", "CaregiverID", "ALL_SessionType", "SessionNumber", "TrialBlockGroup", "StudyPhase", "ALL_T1_Average", "ALL_T2_Average", "ALL_AllConfMonitoring_Average", "ALL_T1_Count", "ALL_T2_Count", "ALL_AllConfMonitoring_Count"})


in
    #"Reordered Columns1"